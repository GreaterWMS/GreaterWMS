package iDataScanner;

import android.content.Intent;

import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CallbackContext;
import org.apache.cordova.LOG;
import org.apache.cordova.PluginResult;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.app.Activity;
import android.content.Context;
import android.text.TextUtils;
import android.util.Log;

import android.content.IntentFilter;
import android.content.BroadcastReceiver;

/**
 * This class echoes a string called from JavaScript.
 */
public class iDataScanner extends CordovaPlugin {

    private static final String LOG_TAG = "iDataScanner";
    private static final String SCAN_ACTION = "android.intent.action.SCANRESULT";
    private static final String SCAN_OUTPUT = "android.intent.action.BARCODEOUTPUT";

    BroadcastReceiver receiver;

    private CallbackContext scannerCallbackContext = null;

    /**
     * Constructor.
     */
    public iDataScanner() {
        this.receiver = null;
    }

    /**
     * Executes the request.
     *
     * @param action        	The action to execute.
     * @param args          	JSONArry of arguments for the plugin.
     * @param callbackContext 	The callback context used when calling back into JavaScript.
     * @return              	True if the action was valid, false if not.
     */
    public boolean execute(String action, JSONArray args, CallbackContext callbackContext) {
        if (action.equals("start")) {
            if (this.scannerCallbackContext != null) {
                removeScannerListener();
            }
            this.scannerCallbackContext = callbackContext;

            Intent intent = new Intent(SCAN_OUTPUT);
            intent.putExtra(SCAN_OUTPUT,1);
            webView.getContext().sendBroadcast(intent);

            IntentFilter intentFilter = new IntentFilter();
            intentFilter.addAction(SCAN_ACTION);
            if (this.receiver == null) {
                this.receiver = new BroadcastReceiver() {
                    @Override
                    public void onReceive(Context context, Intent intent) {
                        updateCodeInfo(intent);
                    }
                };
                webView.getContext().registerReceiver(this.receiver, intentFilter);
            }

            // Don't return any result now, since status results will be sent when events come in from broadcast receiver
            PluginResult pluginResult = new PluginResult(PluginResult.Status.NO_RESULT);
            pluginResult.setKeepCallback(true);
            callbackContext.sendPluginResult(pluginResult);
            return true;
        }

        else if (action.equals("stop")) {
            removeScannerListener();
            this.sendUpdate(new JSONObject(), false); // release status callback in JS side
            this.scannerCallbackContext = null;
            callbackContext.success();
            Intent intent = new Intent(SCAN_OUTPUT);
            intent.putExtra(SCAN_OUTPUT,0);
            webView.getContext().sendBroadcast(intent);
            return true;
        }

        return false;
    }

    /**
     * Stop Scanner receiver.
     */
    public void onDestroy() {
        removeScannerListener();
    }

    /**
     * Stop Scanner receiver.
     */
    public void onReset() {
        removeScannerListener();
    }

    /**
     * Stop the Scanner receiver and set it to null.
     */
    private void removeScannerListener() {
        if (this.receiver != null) {
            try {
                webView.getContext().unregisterReceiver(this.receiver);
                this.receiver = null;
            } catch (Exception e) {
                LOG.e(LOG_TAG, "Error unregistering Scanner receiver: " + e.getMessage(), e);
            }
        }
    }

    /**
     * Creates a JSONObject with the current Scanner information
     *
     * @param
     * @return a JSONObject containing the code status information
     */
    private JSONObject getCodeInfo(Intent codeIntent) {
        JSONObject obj = new JSONObject();
        try {
            String code = codeIntent.getStringExtra("values").toString();
            if (code == null || TextUtils.isEmpty(code))
                return null;
            LOG.d(LOG_TAG, "values" + code);
            obj.put("data", code);
        } catch (JSONException e) {
            LOG.e(LOG_TAG, e.getMessage(), e);
        }
        return obj;
    }

    /**
     * Updates the JavaScript side whenever the code changes
     *
     * @param batteryIntent the current battery information
     * @return
     */
    private void updateCodeInfo(Intent codeIntent) {
        JSONObject jsonObject = getCodeInfo(codeIntent);
        if (jsonObject == null)
            return;
        sendUpdate(jsonObject, true);
    }

    /**
     * Create a new plugin result and send it back to JavaScript
     *
     * @param connection the network info to set as navigator.connection
     */
    private void sendUpdate(JSONObject info, boolean keepCallback) {
        if (this.scannerCallbackContext != null) {
            PluginResult result = new PluginResult(PluginResult.Status.OK, info);
            result.setKeepCallback(keepCallback);
            this.scannerCallbackContext.sendPluginResult(result);
        }
    }


}
