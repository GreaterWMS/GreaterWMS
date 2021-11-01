*Please be aware that this application / sample is provided as-is for demonstration purposes without any guarantee of support*
=========================================================

[![npm version](http://img.shields.io/npm/v/com-darryncampbell-cordova-plugin-intent.svg?style=flat-square)](https://npmjs.org/package/com-darryncampbell-cordova-plugin-intent "View this project on npm")
[![npm downloads](http://img.shields.io/npm/dm/com-darryncampbell-cordova-plugin-intent.svg?style=flat-square)](https://npmjs.org/package/com-darryncampbell-cordova-plugin-intent "View this project on npm")
[![npm downloads](http://img.shields.io/npm/dt/com-darryncampbell-cordova-plugin-intent.svg?style=flat-square)](https://npmjs.org/package/com-darryncampbell-cordova-plugin-intent "View this project on npm")
[![npm licence](http://img.shields.io/npm/l/com-darryncampbell-cordova-plugin-intent.svg?style=flat-square)](https://npmjs.org/package/com-darryncampbell-cordova-plugin-intent "View this project on npm")

Note: this is the current underlying implementation for https://www.npmjs.com/package/@ionic-native/web-intent and https://ionicframework.com/docs/native/web-intent/

# Android X support
- For Android X Support please use version >= [2.x.x](https://www.npmjs.com/package/com-darryncampbell-cordova-plugin-intent/v/2.0.0) 
- For Android Support Library please use version [1.3.x](https://www.npmjs.com/package/com-darryncampbell-cordova-plugin-intent/v/1.3.0)

# Interaction with Camera Plugin
If you are installing this plugin along with cordova-plugin-camera you **MUST install cordova-plugin-camera first.**

# Overview
This Cordova plugin provides a general purpose shim layer for the Android intent mechanism, exposing various ways to handle sending and receiving intents.

## Credits
This project uses code released under the following MIT projects:
- https://github.com/napolitano/cordova-plugin-intent (marked as no longer maintained)
- https://github.com/Initsogar/cordova-webintent.git (no longer available on github but the project is forked here: https://github.com/darryncampbell/cordova-webintent)
This project is also released under MIT.  Credit is given in the code where appropriate

## IntentShim
This plugin defines a `window.plugins.intentShim` object which provides an API for interacting with the Android intent mechanism on any Android device.

## Testing / Example
An example application is available at https://github.com/darryncampbell/plugin-intent-api-exerciser to demonstrate the API and can be used to test the functionality.

## Installation

### Cordova Version < 7
    cordova plugin add https://github.com/darryncampbell/darryncampbell-cordova-plugin-intent.git

### Cordova Version >= 7
    cordova plugin add com-darryncampbell-cordova-plugin-intent

## Use with PhoneGap

Please use the latest PhoneGap cli when including this plugin, please refer to [Issue 63](https://github.com/darryncampbell/darryncampbell-cordova-plugin-intent/issues/63) for context. 

## Supported Platforms
- Android

## intentShim.registerBroadcastReceiver

Registers a broadcast receiver for the specified filters

    window.plugins.intentShim.registerBroadcastReceiver(filters, callback);

### Description

The `intentShim.registerBroadcastReceiver` function registers a dynamic broadcast receiver for the specified list of filters and invokes the specified callback when any of those filters are received

### Example

Register a broadcast receiver for two filters:

    window.plugins.intentShim.registerBroadcastReceiver({
        filterActions: [
            'com.darryncampbell.cordova.plugin.broadcastIntent.ACTION',
            'com.darryncampbell.cordova.plugin.broadcastIntent.ACTION_2'
            ]
        },
        function(intent) {
            console.log('Received broadcast intent: ' + JSON.stringify(intent.extras));
        }
    );


## intentShim.unregisterBroadcastReceiver

Unregisters any BroadcastRecivers

    window.plugins.intentShim.unregisterBroadcastReceiver();

### Description

The `intentShim.unregisterBroadcastReceiver` function unregisters all broadcast receivers registered with `intentShim.registerBroadcastReceiver(filters, callback);`.  No further broadcasts will be received for any registered filter after this call.

### Android Quirks

The developer is responsible for calling unregister / register when their application goes into the background or comes back to the foreground, if desired.

### Example

Unregister the broadcast receiver when the application receives an onPause event:

    bindEvents: function() {
        document.addEventListener('pause', this.onPause, false);
    },
    onPause: function()
    {
        window.plugins.intentShim.unregisterBroadcastReceiver();
    }

## intentShim.sendBroadcast

Sends a broadcast intent

    window.plugins.intentShim.sendBroadcast(action, extras, successCallback, failureCallback);

### Description

The `intentShim.sendBroadcast` function sends an Android broadcast intent with a specified action

### Example

Send a broadcast intent to a specified action that contains a random number in the extras

    window.plugins.intentShim.startActivity(
        {
            action: "com.darryncampbell.cordova.plugin.intent.ACTION",
            extras: {
                    'random.number': Math.floor((Math.random() * 1000) + 1)
            }
        },
        function() {},
        function() {alert('Failed to open URL via Android Intent')}
    );


## intentShim.onIntent

Returns the content of the intent used whenever the application activity is launched

    window.plugins.intentShim.onIntent(callback);

### Description

The `intentShim.onIntent` function returns the intent which launched the Activity and maps to the Android Activity's onNewIntent() method, https://developer.android.com/reference/android/app/Activity.html#onNewIntent(android.content.Intent).  The registered callback is invoked whenever the activity is launched

### Android Quirks

By default the android application will be created with launch mode set to 'SingleTop'.  If you wish to change this to 'SingleTask' you can do so by modifying `config.xml` as follows:

    <platform name="android">
        ...
        <preference name="AndroidLaunchMode" value="singleTask"/>
    </platform>
See https://www.mobomo.com/2011/06/android-understanding-activity-launchmode/ for more information on the differences between the two.

### Example

Registers a callback to be invoked

    window.plugins.intentShim.onIntent(function (intent) {
        console.log('Received Intent: ' + JSON.stringify(intent.extras));
    });

## intentShim.startActivity

Starts a new activity using an intent built from action, url, type, extras or some subset of those parameters

    window.plugins.intentShim.startActivity(params, successCallback, failureCallback);

### Description

The `intentShim.startActivity` function maps to Android's activity method startActivity, https://developer.android.com/reference/android/app/Activity.html#startActivity(android.content.Intent) to launch a new activity.

### Android Quirks

Some common actions are defined as constants in the plugin, see below.

### Examples

Launch the maps activity

    window.plugins.intentShim.startActivity(
    {
        action: window.plugins.intentShim.ACTION_VIEW,
        url: 'geo:0,0?q=London'
    },
    function() {},
    function() {alert('Failed to open URL via Android Intent')}
    );

Launch the web browser

    window.plugins.intentShim.startActivity(
    {
        action: window.plugins.intentShim.ACTION_VIEW,
        url: 'http://www.google.co.uk'
    },
    function() {},
    function() {alert('Failed to open URL via Android Intent')}
    );

## intentShim.getIntent

Retrieves the intent that launched the activity

    window.plugins.intentShim.getIntent(resultCallback, failureCallback);

### Description

The `intentShim.getIntent` function maps to Android's activity method getIntent, https://developer.android.com/reference/android/app/Activity.html#getIntent() to return the intent that started this activity.

### Example

    window.plugins.intentShim.getIntent(
        function(intent)
        {
            console.log('Action' + JSON.stringify(intent.action));
            var intentExtras = intent.extras;
            if (intentExtras == null)
                intentExtras = "No extras in intent";
            console.log('Launch Intent Extras: ' + JSON.stringify(intentExtras));
        },
        function()
        {
            console.log('Error getting launch intent');
        });


## intentShim.startActivityForResult

Starts a new activity and return the result to the application

    window.plugins.intentShim.startActivityForResult(params, resultCallback, failureCallback);

### Description

The `intentShim.startActivityForResult` function maps to Android's activity method startActivityForResult, https://developer.android.com/reference/android/app/Activity.html#startActivityForResult(android.content.Intent, int) to launch a new activity and the resulting data is returned via the resultCallback.

### Android Quirks

Some common actions are defined as constants in the plugin, see below.

### Example

Pick an Android contact

    window.plugins.intentShim.startActivityForResult(
    {
        action: window.plugins.intentShim.ACTION_PICK,
        url: "content://com.android.contacts/contacts",
        requestCode: 1
    },
    function(intent)
    {
        if (intent.extras.requestCode == 1)
        {
            console.log('Picked contact: ' + intent.data);
        }
    },
    function()
    {
        console.log("StartActivityForResult failure");
    });

## intentShim.sendResult

Assuming this application was started with `intentShim.startActivityForResult`, send a result back

    window.plugins.intentShim.sendResult(args, callback);

### Description

The `intentShim.sendResult` function returns an `Activity.RESULT_OK` Intent to the activity that started this application, along with any extras that you want to send along (as `args.extras` object), and a `callback` function. It then calls Android Activity's finish() method, https://developer.android.com/reference/android/app/Activity.html#finish().

### Android Quirks

Both `args` and `callback` arguments have to be provided. If you do not need the functionality, send an empty object and an empty function

    window.plugins.intentShim.sendResult({}, function() {});

### Example

    window.plugins.intentShim.sendResult(
        {
            extras: {
                'Test Intent': 'Successfully sent',
                'Test Intent int': 42,
                'Test Intent bool': true,
                'Test Intent double': parseFloat("142.12")
            }
        },
        function() {
        
        }
    );

## Predefined Constants

The following constants are defined in the plugin for use in JavaScript
- window.plugins.intentShim.ACTION_SEND
- window.plugins.intentShim.ACTION_VIEW
- window.plugins.intentShim.EXTRA_TEXT
- window.plugins.intentShim.EXTRA_SUBJECT
- window.plugins.intentShim.EXTRA_STREAM
- window.plugins.intentShim.EXTRA_EMAIL
- window.plugins.intentShim.ACTION_CALL
- window.plugins.intentShim.ACTION_SENDTO
- window.plugins.intentShim.ACTION_GET_CONTENT
- window.plugins.intentShim.ACTION_PICK

## Tested Versions

Tested with Cordova version 6.5.0 and Cordova Android version 6.2.1



