package com.esco.qrscanreceiver;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;

import org.apache.cordova.CallbackContext;
import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.LOG;
import org.apache.cordova.PluginResult;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by yl on 2018/10/9.
 */

public class QRScanReceiver extends CordovaPlugin {

    //扫描条码服务广播
    //Scanning barcode service broadcast.
    public static final String SCN_CUST_ACTION_SCODE = "com.android.server.scannerservice.broadcast";
    //条码扫描数据广播
    //Barcode scanning data broadcast.
    public static final String SCN_CUST_EX_SCODE = "scannerdata";

    /*6.0 以下系统采用的开始，停止扫描广播*/
    /*6.0 the following system adopts the beginning, stop scanning broadcast.*/
    public static final String SCN_CUST_ACTION_START = "android.intent.action.SCANNER_BUTTON_DOWN";
    public static final String SCN_CUST_ACTION_CANCEL = "android.intent.action.SCANNER_BUTTON_UP";

    /*这是扫描头触发控制节点，一般控制连扫模式需要用到*/
    /*This is the scan head trigger control node, which is used to control the scan mode.*/
    private static final String SCANNER_CTRL_FILE = "/sys/devices/platform/scan_se955/se955_state";

    //使能扫描开关，控制扫描头上下电
    //Enable scanning switch to control scanning overhead.
    public static final String SCANNER_POWER = "com.android.server.scannerservice.onoff";

    public static final String SCANNER_OUTPUT_MODE = "SCANNER_OUTPUT_MODE";

    private String LOG_TAG = "QRScanReceiver";



    BroadcastReceiver receiver;

    private CallbackContext qrCallbackContext;

    @Override
    public boolean execute(String action, JSONArray args, CallbackContext callbackContext) throws JSONException {

        if (action.equals("start")) {
            if(this.qrCallbackContext!=null){
                removeListener();
            }
            this.qrCallbackContext = callbackContext;

            IntentFilter intentFilter = new IntentFilter(SCN_CUST_ACTION_SCODE);
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
            this.qrCallbackContext = null;
            callbackContext.success();
            return true;
        }


        return false;
    }

    private void scanDataHandle(Intent intent){
        sendUpdate(getQRData(intent),true);
    }

    private void sendUpdate(JSONObject info, boolean keepCallback) {
        if (this.qrCallbackContext != null) {
            PluginResult result = new PluginResult(PluginResult.Status.OK, info);
            result.setKeepCallback(keepCallback);
            this.qrCallbackContext.sendPluginResult(result);
        }
    }

    private JSONObject getQRData(Intent intent) {
        JSONObject obj = new JSONObject();
        try {
            obj.put("data",intent.getStringExtra(SCN_CUST_EX_SCODE).toString());
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
