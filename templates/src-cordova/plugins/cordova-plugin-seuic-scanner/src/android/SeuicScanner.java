package com.seuic.scanner;

import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CallbackContext;
import org.apache.cordova.LOG;
import org.apache.cordova.PluginResult;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;

/**
 * This class echoes a string called from JavaScript.
 */

public class SeuicScanner extends CordovaPlugin {

   private static final String LOG_TAG = "ScannerManager";
	private static final String SCANACTION = "com.android.server.scannerservice.scan";

    private BroadcastReceiver receiver;
    private CallbackContext scannerCallbackContext = null;


    @Override
    public boolean execute(String action, JSONArray args, CallbackContext callbackContext) throws JSONException {

        if (action.equals("start")) {
            if(this.scannerCallbackContext!=null){
                removeListener();
            }
            this.scannerCallbackContext = callbackContext;

            IntentFilter intentFilter = new IntentFilter(SCANACTION);
            if (this.receiver == null) {
                this.receiver = new BroadcastReceiver() {
                    @Override
                    public void onReceive(Context context, Intent intent) {
                        scanDataHandle(intent);
                    }
                };
                webView.getContext().registerReceiver(this.receiver, intentFilter);
            }

            PluginResult pluginResult = new PluginResult(PluginResult.Status.NO_RESULT);
            pluginResult.setKeepCallback(true);
            callbackContext.sendPluginResult(pluginResult);
            return true;
        }else if (action.equals("stop")) {
            removeListener();
            this.sendUpdate(new JSONObject(), false); // release status callback in JS side
            this.scannerCallbackContext = null;
            callbackContext.success();
            return true;
        }


        return false;
    }

    private void scanDataHandle(Intent intent){
        sendUpdate(getCodeData(intent),true);
    }

    private void sendUpdate(JSONObject info, boolean keepCallback) {
        if (this.scannerCallbackContext != null) {
            PluginResult result = new PluginResult(PluginResult.Status.OK, info);
            result.setKeepCallback(keepCallback);
            this.scannerCallbackContext.sendPluginResult(result);
        }
    }

    private JSONObject getCodeData(Intent intent) {
        JSONObject obj = new JSONObject();
        try {
            obj.put("data",intent.getStringExtra("scannerdata").toString());
        } catch (JSONException e) {
            LOG.e(LOG_TAG, e.getMessage(), e);
        }
        return obj;
    }


    private void removeListener(){
        if(this.receiver!=null){
            webView.getContext().unregisterReceiver(this.receiver);
            this.receiver=null;
        }
    }




}

