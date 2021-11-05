package com.chariotsolutions.nfc.plugin;

import net.rim.device.api.io.nfc.NFCException;
import net.rim.device.api.io.nfc.ndef.NDEFMessage;
import net.rim.device.api.io.nfc.ndef.NDEFRecord;
import net.rim.device.api.io.nfc.readerwriter.Target;
import org.apache.cordova.json4j.JSONArray;
import org.apache.cordova.json4j.JSONException;
import org.apache.cordova.json4j.JSONObject;
import org.apache.cordova.util.Logger;

import java.util.*;

public class Util {

    static final String TAG = "NfcPluginUtil: ";

    static JSONObject ndefToJSON(NDEFMessage message, Hashtable props) {  // Blackberry doesn't have Ndef object

        JSONObject json = new JSONObject();
        if (props == null) { props = new Hashtable(); }

        try {
            // TODO consider renaming properties to match Android
            for (Enumeration keys = props.keys(); keys.hasMoreElements();) {
                String key = (String)keys.nextElement();
                String value = (String)props.get(key);

                if (key.equals("SerialNumber")) {
                    byte[] serialNumber = value.getBytes();
                    json.put(fixName(key), byteArrayToJSON(serialNumber));
                } else {
                    if (value.equals("TRUE")) {
                        json.put(fixName(key), true);
                    } else if (value.equals("FALSE")) {
                        json.put(fixName(key), false);
                    } else {
                        json.put(fixName(key), value);
                    }
                }
            }

            json.put("ndefMessage", messageToJSON(message));
        } catch (JSONException e) {
            Logger.error("Failed to convert ndef into json: " + message.toString());
        }
        return json;
    }

    static String fixName(String key) {
        return key.substring(0,1).toLowerCase() + key.substring(1);
    }

    static NDEFMessage jsonToNdefMessage(String ndefMessageAsJSON) throws JSONException, NFCException {
        NDEFMessage message = new NDEFMessage();
        NDEFRecord[] records = Util.jsonToNdefRecords(ndefMessageAsJSON);
        message.setRecords(records);
        return message;
    }

    static NDEFRecord[] jsonToNdefRecords(String ndefMessageAsJSON) throws JSONException, NFCException {
        Logger.log(ndefMessageAsJSON);
        JSONArray jsonRecords = new JSONArray(ndefMessageAsJSON);

        NDEFRecord[] records = new NDEFRecord[jsonRecords.length()];
        for (int i = 0; i < jsonRecords.length(); i++) {
            JSONObject record = jsonRecords.getJSONObject(i);
            byte tnf = (byte) record.getInt("tnf");
            byte[] type = jsonToByteArray(record.getJSONArray("type"));
            byte[] id = jsonToByteArray(record.getJSONArray("id"));
            byte[] payload = jsonToByteArray(record.getJSONArray("payload"));

            records[i] = new NDEFRecord();
            records[i].setId(new String(id));
            records[i].setType(tnf, new String(type));
            records[i].setPayload(payload);
        }
        return records;
    }

    static JSONArray byteArrayToJSON(byte[] bytes) {
        JSONArray json = new JSONArray();
        for (int i = 0; i < bytes.length; i++) {
            json.put(bytes[i]);
        }
        return json;
    }

    static byte[] jsonToByteArray(JSONArray json) throws JSONException {
        byte[] b = new byte[json.length()];
        for (int i = 0; i < json.length(); i++) {
            b[i] = (byte) json.getInt(i);
        }
        return b;
    }

    static JSONArray messageToJSON(NDEFMessage message) throws JSONException {
        if (message == null) {
            return null;
        }

        JSONArray jsonArray = new JSONArray();
        NDEFRecord[] records = message.getRecords();

        for (int i=0; i < records.length; i++) {
            jsonArray.put(recordToJSON(records[i]));
        }

        return jsonArray;
    }

    // Blackberry's API is a little nicer using String where Android uses byte[]
    // Translating stuff to byte[] so both work the same
    static JSONObject recordToJSON(NDEFRecord record) {
        JSONObject json = new JSONObject();
        try {
            json.put("tnf", record.getTypeNameFormat());
            json.put("type", byteArrayToJSON(record.getType().getBytes()));
            json.put("id", byteArrayToJSON(record.getId().getBytes()));
            json.put("payload", byteArrayToJSON(record.getPayload()));
        } catch (JSONException e) {
            //Not sure why this would happen, documentation is unclear.
            Logger.err(TAG + "Failed to convert ndef record into json: " + record.toString(), e);
        }
        return json;
    }

    static Hashtable getTagProperties(Target target) {
        Hashtable props = new Hashtable();
        Enumeration propertyNames = target.getProperties();
        while (propertyNames.hasMoreElements()) {
            String name = (String)propertyNames.nextElement();
            props.put(name, target.getProperty(name));
        }
        return props;
    }
}
