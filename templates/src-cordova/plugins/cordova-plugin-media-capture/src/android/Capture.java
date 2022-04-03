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
package org.apache.cordova.mediacapture;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Arrays;

import android.content.ActivityNotFoundException;
import android.os.Build;
import android.os.Bundle;

import org.apache.cordova.file.FileUtils;
import org.apache.cordova.file.LocalFilesystemURL;

import org.apache.cordova.CallbackContext;
import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.LOG;
import org.apache.cordova.PermissionHelper;
import org.apache.cordova.PluginManager;
import org.apache.cordova.mediacapture.PendingRequests.Request;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.Manifest;
import android.app.Activity;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.PackageManager.NameNotFoundException;
import android.database.Cursor;
import android.graphics.BitmapFactory;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Environment;
import android.provider.MediaStore;

public class Capture extends CordovaPlugin {

    private static final String VIDEO_3GPP = "video/3gpp";
    private static final String VIDEO_MP4 = "video/mp4";
    private static final String AUDIO_3GPP = "audio/3gpp";
    private static final String[] AUDIO_TYPES = new String[] {"audio/3gpp", "audio/aac", "audio/amr", "audio/wav"};
    private static final String IMAGE_JPEG = "image/jpeg";

    private static final int CAPTURE_AUDIO = 0;     // Constant for capture audio
    private static final int CAPTURE_IMAGE = 1;     // Constant for capture image
    private static final int CAPTURE_VIDEO = 2;     // Constant for capture video
    private static final String LOG_TAG = "Capture";

    private static final int CAPTURE_INTERNAL_ERR = 0;
//    private static final int CAPTURE_APPLICATION_BUSY = 1;
//    private static final int CAPTURE_INVALID_ARGUMENT = 2;
    private static final int CAPTURE_NO_MEDIA_FILES = 3;
    private static final int CAPTURE_PERMISSION_DENIED = 4;
    private static final int CAPTURE_NOT_SUPPORTED = 20;

    private boolean cameraPermissionInManifest;     // Whether or not the CAMERA permission is declared in AndroidManifest.xml

    private final PendingRequests pendingRequests = new PendingRequests();

    private int numPics;                            // Number of pictures before capture activity
    private Uri imageUri;

//    public void setContext(Context mCtx)
//    {
//        if (CordovaInterface.class.isInstance(mCtx))
//            cordova = (CordovaInterface) mCtx;
//        else
//            LOG.d(LOG_TAG, "ERROR: You must use the CordovaInterface for this to work correctly. Please implement it in your activity");
//    }

    @Override
    protected void pluginInitialize() {
        super.pluginInitialize();

        // CB-10670: The CAMERA permission does not need to be requested unless it is declared
        // in AndroidManifest.xml. This plugin does not declare it, but others may and so we must
        // check the package info to determine if the permission is present.

        cameraPermissionInManifest = false;
        try {
            PackageManager packageManager = this.cordova.getActivity().getPackageManager();
            String[] permissionsInPackage = packageManager.getPackageInfo(this.cordova.getActivity().getPackageName(), PackageManager.GET_PERMISSIONS).requestedPermissions;
            if (permissionsInPackage != null) {
                for (String permission : permissionsInPackage) {
                    if (permission.equals(Manifest.permission.CAMERA)) {
                        cameraPermissionInManifest = true;
                        break;
                    }
                }
            }
        } catch (NameNotFoundException e) {
            // We are requesting the info for our package, so this should
            // never be caught
            LOG.e(LOG_TAG, "Failed checking for CAMERA permission in manifest", e);
        }
    }

    @Override
    public boolean execute(String action, JSONArray args, CallbackContext callbackContext) throws JSONException {
        if (action.equals("getFormatData")) {
            JSONObject obj = getFormatData(args.getString(0), args.getString(1));
            callbackContext.success(obj);
            return true;
        }

        JSONObject options = args.optJSONObject(0);

        if (action.equals("captureAudio")) {
            this.captureAudio(pendingRequests.createRequest(CAPTURE_AUDIO, options, callbackContext));
        }
        else if (action.equals("captureImage")) {
            this.captureImage(pendingRequests.createRequest(CAPTURE_IMAGE, options, callbackContext));
        }
        else if (action.equals("captureVideo")) {
            this.captureVideo(pendingRequests.createRequest(CAPTURE_VIDEO, options, callbackContext));
        }
        else {
            return false;
        }

        return true;
    }

    /**
     * Provides the media data file data depending on it's mime type
     *
     * @param filePath path to the file
     * @param mimeType of the file
     * @return a MediaFileData object
     */
    private JSONObject getFormatData(String filePath, String mimeType) throws JSONException {
        Uri fileUrl = filePath.startsWith("file:") ? Uri.parse(filePath) : Uri.fromFile(new File(filePath));
        JSONObject obj = new JSONObject();
        // setup defaults
        obj.put("height", 0);
        obj.put("width", 0);
        obj.put("bitrate", 0);
        obj.put("duration", 0);
        obj.put("codecs", "");

        // If the mimeType isn't set the rest will fail
        // so let's see if we can determine it.
        if (mimeType == null || mimeType.equals("") || "null".equals(mimeType)) {
            mimeType = FileHelper.getMimeType(fileUrl, cordova);
        }
        LOG.d(LOG_TAG, "Mime type = " + mimeType);

        if (mimeType.equals(IMAGE_JPEG) || filePath.endsWith(".jpg")) {
            obj = getImageData(fileUrl, obj);
        }
        else if (Arrays.asList(AUDIO_TYPES).contains(mimeType)) {
            obj = getAudioVideoData(filePath, obj, false);
        }
        else if (mimeType.equals(VIDEO_3GPP) || mimeType.equals(VIDEO_MP4)) {
            obj = getAudioVideoData(filePath, obj, true);
        }
        return obj;
    }

    /**
     * Get the Image specific attributes
     *
     * @param filePath path to the file
     * @param obj represents the Media File Data
     * @return a JSONObject that represents the Media File Data
     * @throws JSONException
     */
    private JSONObject getImageData(Uri fileUrl, JSONObject obj) throws JSONException {
        BitmapFactory.Options options = new BitmapFactory.Options();
        options.inJustDecodeBounds = true;
        BitmapFactory.decodeFile(fileUrl.getPath(), options);
        obj.put("height", options.outHeight);
        obj.put("width", options.outWidth);
        return obj;
    }

    /**
     * Get the Image specific attributes
     *
     * @param filePath path to the file
     * @param obj represents the Media File Data
     * @param video if true get video attributes as well
     * @return a JSONObject that represents the Media File Data
     * @throws JSONException
     */
    private JSONObject getAudioVideoData(String filePath, JSONObject obj, boolean video) throws JSONException {
        MediaPlayer player = new MediaPlayer();
        try {
            player.setDataSource(filePath);
            player.prepare();
            obj.put("duration", player.getDuration() / 1000);
            if (video) {
                obj.put("height", player.getVideoHeight());
                obj.put("width", player.getVideoWidth());
            }
        } catch (IOException e) {
            LOG.d(LOG_TAG, "Error: loading video file");
        }
        return obj;
    }

    /**
     * Sets up an intent to capture audio.  Result handled by onActivityResult()
     */
    private void captureAudio(Request req) {
      if (!PermissionHelper.hasPermission(this, Manifest.permission.READ_EXTERNAL_STORAGE)) {
          PermissionHelper.requestPermission(this, req.requestCode, Manifest.permission.READ_EXTERNAL_STORAGE);
      } else {
          try {
              Intent intent = new Intent(android.provider.MediaStore.Audio.Media.RECORD_SOUND_ACTION);

              this.cordova.startActivityForResult((CordovaPlugin) this, intent, req.requestCode);
          } catch (ActivityNotFoundException ex) {
              pendingRequests.resolveWithFailure(req, createErrorObject(CAPTURE_NOT_SUPPORTED, "No Activity found to handle Audio Capture."));
          }
      }
    }

    private String getTempDirectoryPath() {
        File cache = null;

        // Use internal storage
        cache = cordova.getActivity().getCacheDir();

        // Create the cache directory if it doesn't exist
        cache.mkdirs();
        return cache.getAbsolutePath();
    }

    /**
     * Sets up an intent to capture images.  Result handled by onActivityResult()
     */
    private void captureImage(Request req) {
        boolean needExternalStoragePermission =
            !PermissionHelper.hasPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE);

        boolean needCameraPermission = cameraPermissionInManifest &&
            !PermissionHelper.hasPermission(this, Manifest.permission.CAMERA);

        if (needExternalStoragePermission || needCameraPermission) {
            if (needExternalStoragePermission && needCameraPermission) {
                PermissionHelper.requestPermissions(this, req.requestCode, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.CAMERA});
            } else if (needExternalStoragePermission) {
                PermissionHelper.requestPermission(this, req.requestCode, Manifest.permission.WRITE_EXTERNAL_STORAGE);
            } else {
                PermissionHelper.requestPermission(this, req.requestCode, Manifest.permission.CAMERA);
            }
        } else {
            // Save the number of images currently on disk for later
            this.numPics = queryImgDB(whichContentStore()).getCount();

            Intent intent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);

            ContentResolver contentResolver = this.cordova.getActivity().getContentResolver();
            ContentValues cv = new ContentValues();
            cv.put(MediaStore.Images.Media.MIME_TYPE, IMAGE_JPEG);
            imageUri = contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, cv);
            LOG.d(LOG_TAG, "Taking a picture and saving to: " + imageUri.toString());

            intent.putExtra(android.provider.MediaStore.EXTRA_OUTPUT, imageUri);

            this.cordova.startActivityForResult((CordovaPlugin) this, intent, req.requestCode);
        }
    }

    private static void createWritableFile(File file) throws IOException {
        file.createNewFile();
        file.setWritable(true, false);
    }

    /**
     * Sets up an intent to capture video.  Result handled by onActivityResult()
     */
    private void captureVideo(Request req) {
        if(cameraPermissionInManifest && !PermissionHelper.hasPermission(this, Manifest.permission.CAMERA)) {
            PermissionHelper.requestPermission(this, req.requestCode, Manifest.permission.CAMERA);
        } else {
            Intent intent = new Intent(android.provider.MediaStore.ACTION_VIDEO_CAPTURE);

            if(Build.VERSION.SDK_INT > 7){
                intent.putExtra("android.intent.extra.durationLimit", req.duration);
                intent.putExtra("android.intent.extra.videoQuality", req.quality);
            }
            this.cordova.startActivityForResult((CordovaPlugin) this, intent, req.requestCode);
        }
    }

    /**
     * Called when the video view exits.
     *
     * @param requestCode       The request code originally supplied to startActivityForResult(),
     *                          allowing you to identify who this result came from.
     * @param resultCode        The integer result code returned by the child activity through its setResult().
     * @param intent            An Intent, which can return result data to the caller (various data can be attached to Intent "extras").
     * @throws JSONException
     */
    public void onActivityResult(int requestCode, int resultCode, final Intent intent) {
        final Request req = pendingRequests.get(requestCode);

        // Result received okay
        if (resultCode == Activity.RESULT_OK) {
            Runnable processActivityResult = new Runnable() {
                @Override
                public void run() {
                    switch(req.action) {
                        case CAPTURE_AUDIO:
                            onAudioActivityResult(req, intent);
                            break;
                        case CAPTURE_IMAGE:
                            onImageActivityResult(req);
                            break;
                        case CAPTURE_VIDEO:
                            onVideoActivityResult(req, intent);
                            break;
                    }
                }
            };

            this.cordova.getThreadPool().execute(processActivityResult);
        }
        // If canceled
        else if (resultCode == Activity.RESULT_CANCELED) {
            // If we have partial results send them back to the user
            if (req.results.length() > 0) {
                pendingRequests.resolveWithSuccess(req);
            }
            // user canceled the action
            else {
                pendingRequests.resolveWithFailure(req, createErrorObject(CAPTURE_NO_MEDIA_FILES, "Canceled."));
            }
        }
        // If something else
        else {
            // If we have partial results send them back to the user
            if (req.results.length() > 0) {
                pendingRequests.resolveWithSuccess(req);
            }
            // something bad happened
            else {
                pendingRequests.resolveWithFailure(req, createErrorObject(CAPTURE_NO_MEDIA_FILES, "Did not complete!"));
            }
        }
    }


    public void onAudioActivityResult(Request req, Intent intent) {
        // Get the uri of the audio clip
        Uri data = intent.getData();
        // create a file object from the uri
        req.results.put(createMediaFile(data));

        if (req.results.length() >= req.limit) {
            // Send Uri back to JavaScript for listening to audio
            pendingRequests.resolveWithSuccess(req);
        } else {
            // still need to capture more audio clips
            captureAudio(req);
        }
    }

    public void onImageActivityResult(Request req) {
        // Add image to results
        req.results.put(createMediaFile(imageUri));

        checkForDuplicateImage();

        if (req.results.length() >= req.limit) {
            // Send Uri back to JavaScript for viewing image
            pendingRequests.resolveWithSuccess(req);
        } else {
            // still need to capture more images
            captureImage(req);
        }
    }

    public void onVideoActivityResult(Request req, Intent intent) {
        Uri data = null;

        if (intent != null){
            // Get the uri of the video clip
            data = intent.getData();
        }

        if( data == null){
            File movie = new File(getTempDirectoryPath(), "Capture.avi");
            data = Uri.fromFile(movie);
        }

        // create a file object from the uri
        if(data == null) {
            pendingRequests.resolveWithFailure(req, createErrorObject(CAPTURE_NO_MEDIA_FILES, "Error: data is null"));
        }
        else {
            req.results.put(createMediaFile(data));

            if (req.results.length() >= req.limit) {
                // Send Uri back to JavaScript for viewing video
                pendingRequests.resolveWithSuccess(req);
            } else {
                // still need to capture more video clips
                captureVideo(req);
            }
        }
    }

    /**
     * Creates a JSONObject that represents a File from the Uri
     *
     * @param data the Uri of the audio/image/video
     * @return a JSONObject that represents a File
     * @throws IOException
     */
    private JSONObject createMediaFile(Uri data) {
        File fp = webView.getResourceApi().mapUriToFile(data);
        JSONObject obj = new JSONObject();

        Class webViewClass = webView.getClass();
        PluginManager pm = null;
        try {
            Method gpm = webViewClass.getMethod("getPluginManager");
            pm = (PluginManager) gpm.invoke(webView);
        } catch (NoSuchMethodException e) {
        } catch (IllegalAccessException e) {
        } catch (InvocationTargetException e) {
        }
        if (pm == null) {
            try {
                Field pmf = webViewClass.getField("pluginManager");
                pm = (PluginManager)pmf.get(webView);
            } catch (NoSuchFieldException e) {
            } catch (IllegalAccessException e) {
            }
        }
        FileUtils filePlugin = (FileUtils) pm.getPlugin("File");
        LocalFilesystemURL url = filePlugin.filesystemURLforLocalPath(fp.getAbsolutePath());

        try {
            // File properties
            obj.put("name", fp.getName());
            obj.put("fullPath", Uri.fromFile(fp));
            if (url != null) {
                obj.put("localURL", url.toString());
            }
            // Because of an issue with MimeTypeMap.getMimeTypeFromExtension() all .3gpp files
            // are reported as video/3gpp. I'm doing this hacky check of the URI to see if it
            // is stored in the audio or video content store.
            if (fp.getAbsoluteFile().toString().endsWith(".3gp") || fp.getAbsoluteFile().toString().endsWith(".3gpp")) {
                if (data.toString().contains("/audio/")) {
                    obj.put("type", AUDIO_3GPP);
                } else {
                    obj.put("type", VIDEO_3GPP);
                }
            } else {
                obj.put("type", FileHelper.getMimeType(Uri.fromFile(fp), cordova));
            }

            obj.put("lastModifiedDate", fp.lastModified());
            obj.put("size", fp.length());
        } catch (JSONException e) {
            // this will never happen
            e.printStackTrace();
        }
        return obj;
    }

    private JSONObject createErrorObject(int code, String message) {
        JSONObject obj = new JSONObject();
        try {
            obj.put("code", code);
            obj.put("message", message);
        } catch (JSONException e) {
            // This will never happen
        }
        return obj;
    }

    /**
     * Creates a cursor that can be used to determine how many images we have.
     *
     * @return a cursor
     */
    private Cursor queryImgDB(Uri contentStore) {
        return this.cordova.getActivity().getContentResolver().query(
            contentStore,
            new String[] { MediaStore.Images.Media._ID },
            null,
            null,
            null);
    }

    /**
     * Used to find out if we are in a situation where the Camera Intent adds to images
     * to the content store.
     */
    private void checkForDuplicateImage() {
        Uri contentStore = whichContentStore();
        Cursor cursor = queryImgDB(contentStore);
        int currentNumOfImages = cursor.getCount();

        // delete the duplicate file if the difference is 2
        if ((currentNumOfImages - numPics) == 2) {
            cursor.moveToLast();
            int id = Integer.valueOf(cursor.getString(cursor.getColumnIndex(MediaStore.Images.Media._ID))) - 1;
            Uri uri = Uri.parse(contentStore + "/" + id);
            this.cordova.getActivity().getContentResolver().delete(uri, null, null);
        }
    }

    /**
     * Determine if we are storing the images in internal or external storage
     * @return Uri
     */
    private Uri whichContentStore() {
        if (Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
            return android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI;
        } else {
            return android.provider.MediaStore.Images.Media.INTERNAL_CONTENT_URI;
        }
    }

    private void executeRequest(Request req) {
        switch (req.action) {
            case CAPTURE_AUDIO:
                this.captureAudio(req);
                break;
            case CAPTURE_IMAGE:
                this.captureImage(req);
                break;
            case CAPTURE_VIDEO:
                this.captureVideo(req);
                break;
        }
    }

    public void onRequestPermissionResult(int requestCode, String[] permissions,
                                          int[] grantResults) throws JSONException {
        Request req = pendingRequests.get(requestCode);

        if (req != null) {
            boolean success = true;
            for(int r:grantResults) {
                if (r == PackageManager.PERMISSION_DENIED) {
                    success = false;
                    break;
                }
            }

            if (success) {
                executeRequest(req);
            } else {
                pendingRequests.resolveWithFailure(req, createErrorObject(CAPTURE_PERMISSION_DENIED, "Permission denied."));
            }
        }
    }

    public Bundle onSaveInstanceState() {
        return pendingRequests.toBundle();
    }

    public void onRestoreStateForActivityResult(Bundle state, CallbackContext callbackContext) {
        pendingRequests.setLastSavedState(state, callbackContext);
    }
}
