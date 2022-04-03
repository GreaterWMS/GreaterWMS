package com.chariotsolutions.nfc.plugin;

import net.rim.device.api.i18n.MessageFormat;
import net.rim.device.api.io.nfc.NFCException;
import net.rim.device.api.io.nfc.emulation.VirtualNDEFTag;
import net.rim.device.api.io.nfc.ndef.NDEFMessage;
import net.rim.device.api.io.nfc.ndef.NDEFMessageListener;
import net.rim.device.api.io.nfc.ndef.NDEFRecord;
import net.rim.device.api.io.nfc.ndef.NDEFTagConnection;
import net.rim.device.api.io.nfc.readerwriter.*;
import net.rim.device.api.system.ControlledAccessException;
import org.apache.cordova.api.Plugin;
import org.apache.cordova.api.PluginResult;
import org.apache.cordova.api.PluginResult.Status;
import org.apache.cordova.json4j.JSONObject;
import org.apache.cordova.json4j.JSONArray;
import org.apache.cordova.json4j.JSONException;
import org.apache.cordova.util.Logger;

import javax.microedition.io.Connector;
import java.io.IOException;
import java.util.Hashtable;

// http://docs.blackberry.com/en/developers/deliverables/34480/Near_Field_Communication_1631111_11.jsp

// Bug with ControlledAccessException addDetectionListener
// http://supportforums.blackberry.com/t5/Java-Development/Listener-belongs-to-another-application-module/m-p/1333559#M176142

// TODO allow error detection listeners
// TODO should add new JS API to specify just the types we want
// nfc.addDetectionListener(ndefListener, new int[]{...});
// Target.NDEF_TAG, Target.ISO_14443_4 and Target.ISO_14443_3.

// TODO allow TAG LISTENER TO WRITE
public class NfcPlugin extends Plugin {

    private static final String TAG = "NfcPlugin: ";
    
    // supported actions
    private static final String REGISTER_MIME_TYPE = "registerMimeType";
    private static final String REGISTER_NDEF = "registerNdef";
    // private static final String REGISTER_NDEF_FORMATABLE = "registerNdefFormatable";
    private static final String REGISTER_DEFAULT_TAG = "registerTag";

    private static final String WRITE_TAG = "writeTag";
    private static final String ERASE_TAG = "eraseTag";

    private static final String SHARE_TAG = "shareTag";
    private static final String UNSHARE_TAG = "unshareTag";
    private static final String INIT = "init";
    
    private static final String REMOVE_MIME_TYPE = "removeMimeType";
    private static final String REMOVE_NDEF = "removeNdef";
    private static final String REMOVE_DEFAULT_TAG = "removeTag";

    // event types
    private static final String NDEF = "ndef";
    private static final String NDEF_MIME = "ndef-mime";
    // private static final String NDEF_FORMATABLE = "ndef-formatable";
    private static final String TAG_DEFAULT = "tag";

    private TagWritingListener ndefListener;
    private DetectionListener tagListener;
    private VirtualNDEFTag virtualTag;

    private int WAIT_FOR_WRITE_MILLIS = 3000;

    /**
     * Executes the request and returns PluginResult.
     *
     * @param action
     *            The action to execute.
     * @param args
     *            JSONArray of arguments for the plugin.
     * @param callbackId
     *            The callback id used when calling back into JavaScript.
     * @return A PluginResult object with a status and message.
     */
    public PluginResult execute(String action, JSONArray args, String callbackId) {
        Logger.debug(action + " " + args.toString());
        PluginResult result;

        try {
        if(INIT.equals(action)) {
            Logger.debug(TAG + " Enabling plugin");

            if (args.length() > 0) {
                WAIT_FOR_WRITE_MILLIS = args.getInt(0);
            }

            return new PluginResult(Status.OK);

        } else if (REGISTER_MIME_TYPE.equals(action)) {
            result = registerMimeListener(args);

        } else if (REMOVE_MIME_TYPE.equals(action)) {
            result = removeMimeListener(args);

        } else if (REGISTER_NDEF.equals(action)) {
            result = registerNdefListener();

        } else if (REMOVE_NDEF.equals(action)) {
            result = removeNdefListener();

        } else if (REGISTER_DEFAULT_TAG.equals(action)) {
            result = registerTagListener();

        } else if (REMOVE_DEFAULT_TAG.equals(action)) {
            result = removeTagListener();

        } else if (WRITE_TAG.equals(action)) {
            result = writeTag(args);

        } else if (ERASE_TAG.equals(action)) {
            result = eraseTag();

        } else if (SHARE_TAG.equals(action)) {
            result = shareTag(args);

        } else if (UNSHARE_TAG.equals(action)) {
            result = unshareTag();

        } else {
            result = new PluginResult(Status.INVALID_ACTION, TAG + "Invalid action: " + action);
        }
        } catch(NFCException e) {
            Logger.err(e.toString(), e);
            return new PluginResult(Status.ERROR, e.toString() + " action=" + action);

        } catch(JSONException e) {
            Logger.err(e.toString(), e);
            return new PluginResult(Status.ERROR, e.toString() + " action=" + action);

        } catch(ControlledAccessException e) {
            // User didn't allow NFC
            Logger.err(e.toString(), e);
            return new PluginResult(Status.ERROR, e.toString() + " action=" + action);
        } catch(SecurityException e) {
            // IT policy doesn't allow NFC
            Logger.err(e.toString(), e);
            return new PluginResult(Status.ERROR, e.toString() + " action=" + action);
        }

        return result;
    }

    private PluginResult registerMimeListener(JSONArray args) throws NFCException, JSONException {
        ReaderWriterManager nfc = ReaderWriterManager.getInstance();
        String mimeType = args.getString(0);

        NDEFMessageListener listener = new NDEFMessageListener() {
            public void onNDEFMessageDetected(final NDEFMessage msg)
            {
                NfcPlugin.this.fireNdefEvent(NDEF_MIME, msg, null);
            }
        };

        nfc.addNDEFMessageListener(listener, NDEFRecord.TNF_MEDIA, mimeType, true);
        return new PluginResult(Status.OK);
    }

    private PluginResult removeMimeListener(JSONArray args) throws NFCException, JSONException {
        ReaderWriterManager nfc = ReaderWriterManager.getInstance();
        String mimeType = args.getString(0);
        nfc.removeNDEFMessageListener(NDEFRecord.TNF_MEDIA, mimeType);
        return new PluginResult(Status.OK);
    }

    private PluginResult registerNdefListener() throws NFCException, JSONException {
        ReaderWriterManager nfc = ReaderWriterManager.getInstance();
        ndefListener  = new TagWritingListener();
        nfc.addDetectionListener(ndefListener, new int[]{Target.NDEF_TAG});
        return new PluginResult(Status.OK);
    }

    private PluginResult removeNdefListener() throws NFCException, JSONException {
        ReaderWriterManager nfc = ReaderWriterManager.getInstance();
        nfc.removeDetectionListener(ndefListener);
        return new PluginResult(Status.OK);
    }

    private PluginResult registerTagListener() throws NFCException, JSONException {
        ReaderWriterManager nfc = ReaderWriterManager.getInstance();

        tagListener  = new DetectionListener() {

            public void onTargetDetected(Target target) {

                Hashtable props = Util.getTagProperties(target);

                NDEFMessage message = null;
                try {
                    NDEFTagConnection tagConnection = (NDEFTagConnection) Connector.open(target.getUri(Target.NDEF_TAG));
                    message = tagConnection.read();  // might want to handle NFCException different
                } catch (IOException e) {
                    Logger.error("Failed reading tag " + e.toString());
                }

                fireNdefEvent(TAG_DEFAULT, message, props);

            }
        };
        nfc.addDetectionListener(tagListener);
        return new PluginResult(Status.OK);
    }

    private PluginResult removeTagListener() throws NFCException, JSONException {
        ReaderWriterManager nfc = ReaderWriterManager.getInstance();
        nfc.removeDetectionListener(tagListener);
        return new PluginResult(Status.OK);
    }

    private PluginResult writeTag(JSONArray args) throws NFCException, JSONException {

        NDEFMessage message = Util.jsonToNdefMessage(args.getString(0));

        try {
            if (ndefListener != null) {
                ndefListener.write(message);
            } else {
                return new PluginResult(Status.IO_EXCEPTION, "Tag Write Failed (Lost Tag)");
            }
        } catch (TagLockedException e) {
            Logger.debug("Tag is locked");
            return new PluginResult(Status.ERROR, e.getMessage());
        } catch (NotEnoughSpaceException e) {
            Logger.debug("Tag capacity exceeded");
            return new PluginResult(Status.ERROR, e.getMessage());
        } catch (NFCException e) {
            Logger.debug("Error writing tag");
            return new PluginResult(Status.ERROR, e.getMessage());
        } catch (IOException e) {
            Logger.debug("Error connecting to tag");
            return new PluginResult(Status.ERROR, e.getMessage());
        }
        return new PluginResult(Status.OK);
    }

    private PluginResult eraseTag() throws NFCException {

        try {
            if (ndefListener != null) {
                ndefListener.erase();
            } else {
                return new PluginResult(Status.IO_EXCEPTION, "Erase Failed (Lost Tag)");
            }
        } catch (TagLockedException e) {
            Logger.debug("Tag is locked");
            return new PluginResult(Status.ERROR, e.getMessage());
        } catch (NFCException e) {
            Logger.debug("Error writing tag");
            return new PluginResult(Status.ERROR, e.getMessage());
        }
        return new PluginResult(Status.OK);
    }

    private PluginResult shareTag(JSONArray args) throws NFCException, JSONException {

        NDEFMessage message = Util.jsonToNdefMessage(args.getString(0));
        virtualTag = new VirtualNDEFTag(message);
        virtualTag.startEmulation();
        return new PluginResult(Status.OK);
    }

    private PluginResult unshareTag() throws NFCException {
        virtualTag.stopEmulation();
        return new PluginResult(Status.OK);
    }

    //private void fireNdefEvent(String type, Ndef ndef, Parcelable[] messages) {
    private void fireNdefEvent(String type, NDEFMessage message, Hashtable props) {

        String javascriptTemplate =
            "var e = document.createEvent(''Events'');\n" +
                    "e.initEvent(''{0}'');\n" +
                    "e.tag = {1};\n" +
                    "document.dispatchEvent(e);";

        JSONObject jsonObject = Util.ndefToJSON(message, props);
        String tag = jsonObject.toString();

        Object[] args = { type, tag };

        String command = MessageFormat.format(javascriptTemplate, args);
        Logger.debug(command);
        this.invokeScript(command);
    }

    // The Android code calls nfc.write() after receiving an nfcEvent
    // Blackberry wants tags to be written inside the DetectionListener event handler
    // http://www.blackberry.com/developers/docs/7.0.0api/net/rim/device/api/io/nfc/readerwriter/DetectionListener.html
    //
    // WARNING Huge hack: sleep the listener thread so the Plugin can call Javascript and then Javascript can call
    // nfc.write before onTargetDetected completes and target is invalid.
    //
    // Javascript has no idea when reads fail with errors.  Need to look into registering error listeners.
    class TagWritingListener implements DetectionListener {

        NDEFTagConnection tagConnection;
        Target target;
        Thread t;

        public void onTargetDetected(Target target) {
            this.target = target;

            try {
                tagConnection = (NDEFTagConnection) Connector.open(target.getUri(Target.NDEF_TAG));
                NDEFMessage message = tagConnection.read();
                fireNdefEvent(NDEF, message, Util.getTagProperties(target));

                t = Thread.currentThread();
                try {
                    Thread.sleep(WAIT_FOR_WRITE_MILLIS);
                } catch (InterruptedException e) {
                    Logger.debug("Detection Listener sleep interrupted.");
                }
            } catch (NFCException e) {
                Logger.error("Failed to read NDEF tag" + e.toString());
            } catch (IOException e) {
                Logger.error("Failed to connect to NDEF tag" + e.toString());
            }

        }

        public void write(NDEFMessage message) throws IOException {

            tagConnection.write(message);
            t.interrupt();

        }

        public void erase() throws NFCException {

            tagConnection.erase();
            t.interrupt();

        }

    }

}