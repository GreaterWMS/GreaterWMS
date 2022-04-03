/*
       Licensed to the Apache Software Foundation (ASF) under one
       or more contributor license agreements.  See the NOTICE file
       distributed with this work for additional information
       regarding copyright ownership.  The ASF licenses this file
       to you under the Apache License, Version 2.0 (the
       "License"); you may not use this file except in compliance
       with the License.  You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

       Unless required by applicable law or agreed to in writing,
       software distributed under the License is distributed on an
       "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
       KIND, either express or implied.  See the License for the
       specific language governing permissions and limitations
       under the License.
*/
package com.ubx.cordova.plugin;

import java.util.TimeZone;

import org.apache.cordova.CordovaWebView;
import org.apache.cordova.CallbackContext;
import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CordovaInterface;
import org.apache.cordova.PluginResult;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import android.provider.Settings;
import org.apache.cordova.CallbackContext;
import org.apache.cordova.CordovaPlugin;
import org.json.JSONArray;
import org.json.JSONException;
import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.text.TextUtils;
import android.util.Log;
import android.device.DeviceManager;

public class Uplugin extends CordovaPlugin {
    public static final String TAG = "Uplugin";
    private BroadcastReceiver mScanReceiver;
    private Activity activity;
    public final static String SCAN_ACTION = "android.intent.ACTION_DECODE_DATA";// default

    /**
     * Constructor.
     */
    public Uplugin() {
    }

    /**
     * Executes the request and returns PluginResult.
     *
     * @param action            The action to execute.
     * @param args              JSONArry of arguments for the plugin.
     * @param callbackContext   The callback id used when calling back into JavaScript.
     * @return                  True if the action was valid, false if not.
     */
    public boolean execute(String action, JSONArray args, CallbackContext callbackContext) throws JSONException {
        if ("getDeviceID".equals(action)) {
            String r = this.getSerialNumber();

            callbackContext.success(r);
        } else if (action.equals("getBarcode")) {
            String message = args.getString(0);
            if (TextUtils.isEmpty(message)) {
                callbackContext.error("faild,args cannot be empty");
                return true;
            }
            if ("start".equals(message)) {
                startScan(callbackContext);
            } else if ("stop".equals(message)) {
                stopScan(callbackContext);
            } else {
                callbackContext.error("failed,Operation does not exist");
            }

        } else {
            return false;
        }
        return true;
    }




    public String getSerialNumber() {
        String serial =  new DeviceManager().getDeviceId();
        return serial;
    }





    /**
     * open scanner
     *
     * @param message
     * @param callbackContext
     */
    private void startScan(final CallbackContext callbackContext)
    {

        IntentFilter filter = new IntentFilter();

        filter.addAction(SCAN_ACTION);

        activity = this.cordova.getActivity();
        if (activity != null)
        {
            mScanReceiver = new BroadcastReceiver()
            {
                @Override
                public void onReceive(Context context, Intent intent)
                {
                    // TODO Auto-generated method stub
                    byte[] barcode = intent.getByteArrayExtra("barcode");
                    int barcodelen = intent.getIntExtra("length", 0);
                    byte temp = intent.getByteExtra("barcodeType", (byte) 0);
                    String barcodeStr = new String(barcode, 0, barcodelen);
                    coolMethod(barcodeStr, callbackContext);
                }
            };
            activity.registerReceiver(mScanReceiver, filter);
    ;
        }
    }

    /**
     * stop scanner
     */
    private void stopScan(final CallbackContext callbackContext)
    {
        // TODO Auto-generated method stub

        if (activity != null)
        {
            activity.unregisterReceiver(mScanReceiver);
            if (callbackContext != null)
            {
                coolMethod("> stop success", callbackContext);
            }
        }
    }

    private void coolMethod(String message, CallbackContext callbackContext)
    {
        if (!TextUtils.isEmpty(message))
        {

            PluginResult pluginResult=new PluginResult(PluginResult.Status.OK,message);
            pluginResult.setKeepCallback(true);
            callbackContext.sendPluginResult(pluginResult);
        } else
        {
            callbackContext.error("> scan error.");
        }
    //    stopScan(null);
    }

    @Override
    public void onDestroy()
    {
        // TODO Auto-generated method stub
        super.onDestroy();
        try
        {
            stopScan(null);
        } catch (Exception e)
        {
            // TODO: handle exception
        }
    }



}
