package zebra.d;

import android.util.Log;

import com.zebra.deviceidentifierswrapper.DIHelper;
import com.zebra.deviceidentifierswrapper.IDIResultCallbacks;

import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CallbackContext;

import org.json.JSONArray;
import org.json.JSONException;

/**
 * This class echoes a string called from JavaScript.
 */
public class ZebraD extends CordovaPlugin {

  @Override
  public boolean execute(String action, JSONArray args, CallbackContext callbackContext) throws JSONException {
    String[] permissions = {
      "com.zebra.provider.READ", "com.symbol.emdk.permission.EMDK"
    };
    cordova.requestPermissions(this, 500, permissions);
    if (action.equals("getSerialNumber")) {
      this.getSerialNumber(callbackContext);
      return true;
    }
    if (action.equals("getIMEINumber")) {
      this.getIMEINumber(callbackContext);
      return true;
    }
    return false;
  }

  private void getSerialNumber(CallbackContext callbackContext) {
    DIHelper.getSerialNumber(cordova.getContext(), new IDIResultCallbacks() {
      @Override
      public void onSuccess(String message) {
        // The message contains the serial number
//        Log.d("message", message);
        callbackContext.success(message);
      }

      @Override
      public void onError(String message) {
        // An error occurred
//        Log.d("message", message);
        callbackContext.success(message);
      }

      @Override
      public void onDebugStatus(String message) {
        // You can use this method to get verbose information
        // about what's happening behind the curtain
//        Log.d("message", message);
        callbackContext.success(message);
      }
    });
  }

  private void getIMEINumber(CallbackContext callbackContext) {
    DIHelper.getIMEINumber(cordova.getActivity(), new IDIResultCallbacks() {
      @Override
      public void onSuccess(String message) {
        // We've got an EMEI number
        Log.d("IMEI", message);
        callbackContext.success(message);
      }

      @Override
      public void onError(String message) {
        // An error occurred
        Log.d("IMEI", message);
        callbackContext.success(message);
      }

      @Override
      public void onDebugStatus(String message) {
        // You can use this method to get verbose information
        // about what's happening behind the curtain
        Log.d("IMEI", message);
        callbackContext.success(message);
      }
    });
  }
}
