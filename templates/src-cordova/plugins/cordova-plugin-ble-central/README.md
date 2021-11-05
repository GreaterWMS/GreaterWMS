# Bluetooth Low Energy (BLE) Central Plugin for Apache Cordova

This plugin enables communication between a phone and Bluetooth Low Energy (BLE) peripherals.

The plugin provides a simple [JavaScript API](#api) for iOS and Android.

 * Scan for peripherals
 * Connect to a peripheral
 * Read the value of a characteristic
 * Write new value to a characteristic
 * Get notified when characteristic's value changes

Advertising information is returned when scanning for peripherals.
Service, characteristic, and property info is returned when connecting to a peripheral.
All access is via service and characteristic UUIDs. The plugin manages handles internally.

Simultaneous connections to multiple peripherals are supported.

_This plugin isn't intended for scanning beacons._ Try [cordova-plugin-ibeacon](https://github.com/petermetz/cordova-plugin-ibeacon) for iBeacons.<br/>
If you want to create Bluetooth devices, try [cordova-plugin-ble-peripheral](https://github.com/don/cordova-plugin-ble-peripheral).

See the [examples](https://github.com/don/cordova-plugin-ble-central/tree/master/examples) for ideas on how this plugin can be used.

## Supported Platforms

* iOS
* Android (4.3 or greater)

# Installing

### Cordova

    $ cordova plugin add cordova-plugin-ble-central

### PhoneGap

    $ phonegap plugin add cordova-plugin-ble-central

### PhoneGap Build

Edit config.xml to install the plugin for [PhoneGap Build](http://build.phonegap.com).

    <gap:plugin name="cordova-plugin-ble-central" source="npm" />
    <preference name="phonegap-version" value="cli-6.1.0" />

### PhoneGap Developer App

This plugin is included in iOS and Android versions of the [PhoneGap Developer App](http://app.phonegap.com/).

Note that this plugin's id changed from `com.megster.cordova.ble` to `cordova-plugin-ble-central` as part of the migration from the [Cordova plugin repo](http://plugins.cordova.io/) to [npm](https://www.npmjs.com/).

### iOS

For iOS, apps will crash unless they include usage description keys for the types of data they access. Applications targeting iOS 13 and later, define [NSBluetoothAlwaysUsageDescription](https://developer.apple.com/documentation/bundleresources/information_property_list/nsbluetoothalwaysusagedescription?language=objc) to tell the user why the application needs Bluetooth. For apps with a deployment target earlier than iOS 13, add [NSBluetoothPeripheralUsageDescription](https://developer.apple.com/documentation/bundleresources/information_property_list/nsbluetoothperipheralusagedescription?language=objc). Both of these keys can be set when installing the plugin by passing the BLUETOOTH_USAGE_DESCRIPTION variable.

    $ cordova plugin add cordova-plugin-ble-central --variable BLUETOOTH_USAGE_DESCRIPTION="Your description here"

See Apple's documentation about [Protected Resources](https://developer.apple.com/documentation/bundleresources/information_property_list/protected_resources) for more details. If your app needs other permissions like location, try the [cordova-custom-config plugin](https://github.com/don/cordova-plugin-ble-central/issues/700#issuecomment-538312656).

It is possible to delay the initialization of the plugin on iOS. Normally the Bluetooth permission dialog is shown when the app loads for the first time. Delaying the initialization of the plugin shows the permission dialog the first time the Bluetooth API is called. Set `IOS_INIT_ON_LOAD` to false when installing.

    --variable IOS_INIT_ON_LOAD=false

# API

## Methods

- [ble.scan](#scan)
- [ble.startScan](#startscan)
- [ble.startScanWithOptions](#startscanwithoptions)
- [ble.stopScan](#stopscan)
- [ble.setPin](#setpin)
- [ble.connect](#connect)
- [ble.autoConnect](#autoconnect)
- [ble.disconnect](#disconnect)
- [ble.requestMtu](#requestmtu)
- [ble.requestConnectionPriority](#requestconnectionpriority)
- [ble.read](#read)
- [ble.write](#write)
- [ble.writeWithoutResponse](#writewithoutresponse)
- [ble.startNotification](#startnotification)
- [ble.stopNotification](#stopnotification)
- [ble.isEnabled](#isenabled)
- [ble.isLocationEnabled](#islocationenabled)
- [ble.isConnected](#isconnected)
- [ble.startStateNotifications](#startstatenotifications)
- [ble.stopStateNotifications](#stopstatenotifications)
- [ble.showBluetoothSettings](#showbluetoothsettings)
- [ble.enable](#enable)
- [ble.readRSSI](#readrssi)
- [ble.connectedPeripheralsWithServices](#connectedperipheralswithservices)
- [ble.peripheralsWithIdentifiers](#peripheralswithidentifiers)
- [ble.bondedDevices](#bondeddevices)

## scan

Scan and discover BLE peripherals.

    ble.scan(services, seconds, success, failure);

### Description

Function `scan` scans for BLE devices.  The success callback is called each time a peripheral is discovered. Scanning automatically stops after the specified number of seconds.

    {
        "name": "TI SensorTag",
        "id": "BD922605-1B07-4D55-8D09-B66653E51BBA",
        "rssi": -79,
        "advertising": /* ArrayBuffer or map */
    }

Advertising information format varies depending on your platform. See [Advertising Data](#advertising-data) for more information.

### Location Permission Notes
With Android SDK >= 23 (6.0), additional permissions are required for Bluetooth low energy scanning. The location permission [ACCESS_COARSE_LOCATION](https://developer.android.com/reference/android/Manifest.permission.html#ACCESS_COARSE_LOCATION) is required because Bluetooth beacons can be used to determine a user's location. If necessary, the plugin will prompt the user to allow the app to access to device's location. If the user denies permission, the scan failure callback will receive the error "Location permission not granted".

Location Services must be enabled for Bluetooth scanning. If location services are disabled, the failure callback will receive the error "Location services are disabled". If you want to manage location permission and screens, try the [cordova-diagonostic-plugin](https://github.com/dpa99c/cordova-diagnostic-plugin) or the Ionic Native [Diagnostic plugin](https://ionicframework.com/docs/native/diagnostic/).

### Parameters

- __services__: List of services to discover, or [] to find all devices
- __seconds__: Number of seconds to run discovery
- __success__: Success callback function that is invoked which each discovered device.
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.scan([], 5, function(device) {
        console.log(JSON.stringify(device));
    }, failure);

## startScan

Scan and discover BLE peripherals.

    ble.startScan(services, success, failure);

### Description

Function `startScan` scans for BLE devices.  The success callback is called each time a peripheral is discovered. Scanning will continue until `stopScan` is called.

    {
        "name": "TI SensorTag",
        "id": "BD922605-1B07-4D55-8D09-B66653E51BBA",
        "rssi": -79,
        "advertising": /* ArrayBuffer or map */
    }

Advertising information format varies depending on your platform. See [Advertising Data](#advertising-data) for more information.

See the [location permission notes](#location-permission-notes) above for information about Location Services in Android SDK >= 23.

### Parameters

- __services__: List of services to discover, or [] to find all devices
- __success__: Success callback function that is invoked which each discovered device.
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.startScan([], function(device) {
        console.log(JSON.stringify(device));
    }, failure);

    setTimeout(ble.stopScan,
        5000,
        function() { console.log("Scan complete"); },
        function() { console.log("stopScan failed"); }
    );

## startScanWithOptions

Scan and discover BLE peripherals, specifying scan options.

    ble.startScanWithOptions(services, options, success, failure);

### Description

Function `startScanWithOptions` scans for BLE devices. It operates similarly to the `startScan` function, but allows you to specify extra options (like allowing duplicate device reports).  The success callback is called each time a peripheral is discovered. Scanning will continue until `stopScan` is called.

    {
        "name": "TI SensorTag",
        "id": "BD922605-1B07-4D55-8D09-B66653E51BBA",
        "rssi": -79,
        "advertising": /* ArrayBuffer or map */
    }

Advertising information format varies depending on your platform. See [Advertising Data](#advertising-data) for more information.

See the [location permission notes](#location-permission-notes) above for information about Location Services in Android SDK >= 23.

### Parameters

- __services__: List of services to discover, or [] to find all devices
- __options__: an object specifying a set of name-value pairs. The currently acceptable options are:
- _reportDuplicates_: true if duplicate devices should be reported, false (default) if devices should only be reported once. [optional]
- __success__: Success callback function that is invoked which each discovered device.
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.startScanWithOptions([],
        { reportDuplicates: true }
        function(device) {
            console.log(JSON.stringify(device));
        },
        failure);

    setTimeout(ble.stopScan,
        5000,
        function() { console.log("Scan complete"); },
        function() { console.log("stopScan failed"); }
    );


## stopScan

Stop scanning for BLE peripherals.

    ble.stopScan(success, failure);

### Description

Function `stopScan` stops scanning for BLE devices.

### Parameters

- __success__: Success callback function, invoked when scanning is stopped. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.startScan([], function(device) {
        console.log(JSON.stringify(device));
    }, failure);

    setTimeout(ble.stopScan,
        5000,
        function() { console.log("Scan complete"); },
        function() { console.log("stopScan failed"); }
    );

    /* Alternate syntax
    setTimeout(function() {
        ble.stopScan(
            function() { console.log("Scan complete"); },
            function() { console.log("stopScan failed"); }
        );
    }, 5000);
    */

## setPin

Set device pin

    ble.setPin(pin, [success], [failure]);

### Description

Function `setPin` sets the pin when device requires it.

### Parameters

- __pin__: Pin of the device as a string
- __success__: Success callback function that is invoked when the function is invoked. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

## connect

Connect to a peripheral.

    ble.connect(device_id, connectCallback, disconnectCallback);

### Description

Function `connect` connects to a BLE peripheral. The callback is long running. The connect callback will be called when the connection is successful. Service and characteristic info will be passed to the connect callback in the [peripheral object](#peripheral-data). 

The disconnect callback is called if the connection fails, or later if the peripheral disconnects. When possible, a peripheral object is passed to the failure callback. The disconnect callback is only called when the peripheral initates the disconnection. The disconnect callback is not called when the application calls [ble.disconnect](#disconnect). The disconnect callback is how your app knows the peripheral inintiated a disconnect.

### Scanning before connecting

Android can connect to peripherals using MAC address without scanning. If the MAC address is not found the connection will time out.

For iOS, the plugin needs to know about any device UUID before calling connect. You can do this by calling [ble.scan](#scan), [ble.startScan](#startscan), [ble.connectedPeripheralsWithServices](#connectedperipheralswithservices), or [ble.peripheralsWithIdentifiers](#peripheralswithidentifiers) so the plugin has a list of available peripherals.

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __connectCallback__: Connect callback function that is invoked when the connection is successful.
- __disconnectCallback__: Disconnect callback function, invoked when the peripheral disconnects or an error occurs.

## autoConnect

Establish an automatic connection to a peripheral.

    ble.autoConnect(device_id, connectCallback, disconnectCallback);

### Description

Automatically connect to a device when it is in range of the phone. When the device connects, the connect callback is called with a [peripheral object](#peripheral-data). The call to autoConnect will not time out. It will wait forever until the device is in range. When the peripheral disconnects, the disconnect callback is called with a peripheral object.

Calling [ble.disconnect](#disconnect) will stop the automatic reconnection.

Both the connect and disconnect callbacks can be called many times as the device connects and disconnects. Do not wrap this function in a Promise or Observable. 

On iOS, [background notifications on ios](#background-notifications-on-ios) must be enabled if you want to run in the background. On Android, this relies on the autoConnect argument of `BluetoothDevice.connectGatt()`. Not all Android devices implement this feature correctly.

See notes about [scanning before connecting](#scanning-before-connecting)

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __connectCallback__: Connect callback function that is invoked when the connection is successful.
- __disconnectCallback__: Disconnect callback function, invoked when the peripheral disconnects or an error occurs.

## disconnect

Disconnect.

    ble.disconnect(device_id, [success], [failure]);

### Description

Function `disconnect` disconnects the selected device.

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __success__: Success callback function that is invoked when the connection is successful. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

## requestMtu

requestMtu

    ble.requestMtu(device_id, mtu, [success], [failure]);

### Description

This function may be used to request (on Android) a larger MTU size to be able to send more data at once.
This can be useful when performing a write request operation (write without response), the data sent is truncated to the MTU size.
The resulting MTU size is sent to the success callback. The requested and resulting MTU sizes are not necessarily equal.

### Supported Platforms

 * Android

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __mtu__: MTU size
- __success__: Success callback function that is invoked when the MTU size request is successful. The resulting MTU size is passed as an integer.
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.requestMtu(device_id, new_mtu,
        function(mtu){
            alert("MTU set to: " + mtu);
        },
        function(failure){
            alert("Failed to request MTU.");
        }
    );

## requestConnectionPriority

requestConnectionPriority

    ble.requestConnectionPriority(device_id, priority, [success], [failure]);

### Description

When Connecting to a peripheral android can request for the connection priority for better communication.

### Supported Platforms

 * Android

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __priority__: high or balanced or low
- __success__: Success callback function that is invoked when the connection is successful. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

## refreshDeviceCache

refreshDeviceCache

    ble.refreshDeviceCache(deviceId, timeoutMillis,  [success], [failure]);

### Description

Some poorly behaved devices show old cached services and characteristics info. (Usually because they
don't implement Service Changed 0x2a05 on Generic Attribute Service 0x1801 and the central doesn't know 
the data needs to be refreshed.) This method might help.

*NOTE* Since this uses an undocumented API it's not guaranteed to work.

### Supported Platforms

 * Android

### Parameters

- __deviceId__: UUID or MAC address of the peripheral
- __timeoutMillis__: timeout in milliseconds after refresh before discovering services  
- __success__: Success callback function invoked with the refreshed peripheral. [optional]
- __failure__: Error callback function, invoked when an error occurs. [optional]

## read

Reads the value of a characteristic.

    ble.read(device_id, service_uuid, characteristic_uuid, success, failure);

### Description

Function `read` reads the value of the characteristic.

Raw data is passed from native code to the callback as an [ArrayBuffer](#typed-arrays).

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __service_uuid__: UUID of the BLE service
- __characteristic_uuid__: UUID of the BLE characteristic
- __success__: Success callback function that is invoked when the connection is successful. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

Retrieves an [ArrayBuffer](#typed-arrays) when reading data.

    // read data from a characteristic, do something with output data
    ble.read(device_id, service_uuid, characteristic_uuid,
        function(data){
            console.log("Hooray we have data"+JSON.stringify(data));
            alert("Successfully read data from device."+JSON.stringify(data));
        },
        function(failure){
            alert("Failed to read characteristic from device.");
        }
    );

## write

Writes data to a characteristic.

    ble.write(device_id, service_uuid, characteristic_uuid, data, success, failure);

### Description

Function `write` writes data to a characteristic.

### Parameters
- __device_id__: UUID or MAC address of the peripheral
- __service_uuid__: UUID of the BLE service
- __characteristic_uuid__: UUID of the BLE characteristic
- __data__: binary data, use an [ArrayBuffer](#typed-arrays)
- __success__: Success callback function that is invoked when the connection is successful. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

Use an [ArrayBuffer](#typed-arrays) when writing data.

    // send 1 byte to switch a light on
    var data = new Uint8Array(1);
    data[0] = 1;
    ble.write(device_id, "FF10", "FF11", data.buffer, success, failure);

    // send a 3 byte value with RGB color
    var data = new Uint8Array(3);
    data[0] = 0xFF; // red
    data[1] = 0x00; // green
    data[2] = 0xFF; // blue
    ble.write(device_id, "ccc0", "ccc1", data.buffer, success, failure);

    // send a 32 bit integer
    var data = new Uint32Array(1);
    data[0] = counterInput.value;
    ble.write(device_id, SERVICE, CHARACTERISTIC, data.buffer, success, failure);

## writeWithoutResponse

Writes data to a characteristic without confirmation from the peripheral.

    ble.writeWithoutResponse(device_id, service_uuid, characteristic_uuid, data, success, failure);

### Description

Function `writeWithoutResponse` writes data to a characteristic without a response from the peripheral. You are not notified if the write fails in the BLE stack. The success callback is be called when the characteristic is written.

### Parameters
- __device_id__: UUID or MAC address of the peripheral
- __service_uuid__: UUID of the BLE service
- __characteristic_uuid__: UUID of the BLE characteristic
- __data__: binary data, use an [ArrayBuffer](#typed-arrays)
- __success__: Success callback function that is invoked when the connection is successful. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

## startNotification

Register to be notified when the value of a characteristic changes.

    ble.startNotification(device_id, service_uuid, characteristic_uuid, success, failure);

### Description

Function `startNotification` registers a callback that is called *every time* the value of a characteristic changes. This method handles both `notifications` and `indications`. The success callback is called multiple times.

Raw data is passed from native code to the success callback as an [ArrayBuffer](#typed-arrays).

See [Background Notifications on iOS](#background-notifications-on-ios)

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __service_uuid__: UUID of the BLE service
- __characteristic_uuid__: UUID of the BLE characteristic
- __success__: Success callback function invoked every time a notification occurs
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    var onData = function(buffer) {
        // Decode the ArrayBuffer into a typed Array based on the data you expect
        var data = new Uint8Array(buffer);
        alert("Button state changed to " + data[0]);
    }

    ble.startNotification(device_id, "FFE0", "FFE1", onData, failure);

## stopNotification

Stop being notified when the value of a characteristic changes.

    ble.stopNotification(device_id, service_uuid, characteristic_uuid, success, failure);

### Description

Function `stopNotification` stops a previously registered notification callback.

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __service_uuid__: UUID of the BLE service
- __characteristic_uuid__: UUID of the BLE characteristic
- __success__: Success callback function that is invoked when the notification is removed. [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

## isConnected

Reports the connection status.

    ble.isConnected(device_id, success, failure);

### Description

Function `isConnected` calls the success callback when the peripheral is connected and the failure callback when *not* connected.

NOTE that for many apps isConnected is unncessary. The app can track the connected state. Ater calling [connect](#connect) the app is connected when the success callback function is called. If the device disconnects at any point in the future, the failure callback of connect will be called.

### Parameters

- __device_id__: UUID or MAC address of the peripheral
- __success__: Success callback function that is invoked with a boolean for connected status.
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.isConnected(
        'FFCA0B09-CB1D-4DC0-A1EF-31AFD3EDFB53',
        function() {
            console.log("Peripheral is connected");
        },
        function() {
            console.log("Peripheral is *not* connected");
        }
    );

## isEnabled

Reports if bluetooth is enabled.

    ble.isEnabled(success, failure);

### Description

Function `isEnabled` calls the success callback when Bluetooth is enabled and the failure callback when Bluetooth is *not* enabled.

### Parameters

- __success__: Success callback function, invoked when Bluetooth is enabled.
- __failure__: Error callback function, invoked when Bluetooth is disabled.

### Quick Example

    ble.isEnabled(
        function() {
            console.log("Bluetooth is enabled");
        },
        function() {
            console.log("Bluetooth is *not* enabled");
        }
    );


## isLocationEnabled

Reports if location services are enabled.

    ble.isLocationEnabled(success, failure);

### Description

Function `isLocationEnabled` calls the success callback when location services are enabled and the failure callback when location services are *not* enabled. On some devices, location services must be enabled in order to scan for peripherals.

### Supported Platforms

 * Android

### Parameters

- __success__: Success callback function, invoked when location services are enabled.
- __failure__: Error callback function, invoked when location services are disabled.

### Quick Example

    ble.isEnabled(
        function() {
            console.log("location services are enabled");
        },
        function() {
            console.log("location services are *not* enabled");
        }
    );

## startStateNotifications

Registers to be notified when Bluetooth state changes on the device.

    ble.startStateNotifications(success, failure);

### Description

Function `startStateNotifications` calls the success callback when the Bluetooth is enabled or disabled on the device.

__States__

- "on"
- "off"
- "turningOn" (Android Only)
- "turningOff" (Android Only)
- "unknown" (iOS Only)
- "resetting" (iOS Only)
- "unsupported" (iOS Only)
- "unauthorized" (iOS Only)

### Parameters

- __success__: Success callback function that is invoked with a string for the Bluetooth state.
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.startStateNotifications(
        function(state) {
            console.log("Bluetooth is " + state);
        }
    );

## stopStateNotifications

Stops state notifications.

    ble.stopStateNotifications(success, failure);

### Description

Function `stopStateNotifications` calls the success callback when Bluetooth state notifications have been stopped.

## showBluetoothSettings

Show the Bluetooth settings on the device.

    ble.showBluetoothSettings(success, failure);

### Description

Function `showBluetoothSettings` opens the Bluetooth settings for the operating systems.

`showBluetoothSettings` is not available on iOS. Plugins like [cordova-diagonostic-plugin](https://github.com/dpa99c/cordova-diagnostic-plugin) and the Ionic Native [Diagnostic plugin](https://ionicframework.com/docs/native/diagnostic/) have APIs to open Bluetooth and other settings, but will often get apps rejected by Apple.

### Supported Platforms

 * Android

### Parameters

- __success__: Success callback function [optional]
- __failure__: Error callback function, invoked when error occurs. [optional]

### Quick Example

    ble.showBluetoothSettings();

## enable

Enable Bluetooth on the device.

    ble.enable(success, failure);

### Description

Function `enable` prompts the user to enable Bluetooth.

#### Android

`enable` is only supported on Android and does not work on iOS.

If `enable` is called when Bluetooth is already enabled, the user will not prompted and the success callback will be invoked.

### Parameters

- __success__: Success callback function, invoked if the user enabled Bluetooth.
- __failure__: Error callback function, invoked if the user does not enabled Bluetooth.

### Quick Example

    ble.enable(
        function() {
            console.log("Bluetooth is enabled");
        },
        function() {
            console.log("The user did *not* enable Bluetooth");
        }
    );

## readRSSI

Read the RSSI value on the device connection.

    ble.readRSSI(device_id, success, failure);

### Description

Samples the RSSI value (a measure of signal strength) on the connection to a bluetooth device. Requires that you have established a connection before invoking (otherwise an error will be raised).

### Parameters

- __device_id__: device identifier
- __success__: Success callback function, invoked with the RSSI value (as an integer)
- __failure__: Error callback function, invoked if there is no current connection or if there is an error reading the RSSI.

### Quick Example
    var rssiSample;
    ble.connect(device_id,
        function(device) {
            rssiSample = setInterval(function() {
                    ble.readRSSI(device_id, function(rssi) {
                            console.log('read RSSI',rssi,'with device', device_id);
                        }, function(err) {
                            console.error('unable to read RSSI',err);
                            clearInterval(rssiSample);
                            })
                }, 5000);
        },
        function(err) { console.error('error connecting to device')}
        );

## connectedPeripheralsWithServices

Find the connected peripherals offering the listed service UUIDs.

    ble.connectedPeripheralsWithServices([service], success, failure);

### Description

Retreives a list of the peripherals (containing any of the specified services) currently connected to the system. The peripheral list is sent to the success callback. This function wraps [CBCentralManager.retrieveConnectedPeripheralsWithServices:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518924-retrieveconnectedperipheralswith?language=objc)

### Parameters

- __services__: List of services to discover
- __success__: Success callback function, invoked with a list of peripheral objects
- __failure__: Error callback function

### Supported Platforms

 * iOS

## peripheralsWithIdentifiers

Find the connected peripherals offering the listed service UUIDs.

    ble.peripheralsWithIdentifiers([uuids], success, failure);

### Description

Sends a list of known peripherals by their identifiers to the success callback. This function wraps [CBCentralManager.retrievePeripheralsWithIdentifiers:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519127-retrieveperipheralswithidentifie?language=objc)

### Parameters

- __identifiers__: List of peripheral UUIDs
- __success__: Success callback function, invoked with a list of peripheral objects
- __failure__: Error callback function

### Supported Platforms

 * iOS

## bondedDevices

Find the bonded devices.

    ble.bondedDevices(success, failure);

### Description

Sends a list of bonded low energy peripherals to the success callback.

### Parameters

- __success__: Success callback function, invoked with a list of peripheral objects
- __failure__: Error callback function

### Supported Platforms

 * Android


# Peripheral Data

Peripheral Data is passed to the success callback when scanning and connecting. Limited data is passed when scanning.

    {
        "name": "Battery Demo",
        "id": "20:FF:D0:FF:D1:C0",
        "advertising": [2,1,6,3,3,15,24,8,9,66,97,116,116,101,114,121],
        "rssi": -55
    }

After connecting, the peripheral object also includes service, characteristic and descriptor information.

    {
        "name": "Battery Demo",
        "id": "20:FF:D0:FF:D1:C0",
        "advertising": [2,1,6,3,3,15,24,8,9,66,97,116,116,101,114,121],
        "rssi": -55,
        "services": [
            "1800",
            "1801",
            "180f"
        ],
        "characteristics": [
            {
                "service": "1800",
                "characteristic": "2a00",
                "properties": [
                    "Read"
                ]
            },
            {
                "service": "1800",
                "characteristic": "2a01",
                "properties": [
                    "Read"
                ]
            },
            {
                "service": "1801",
                "characteristic": "2a05",
                "properties": [
                    "Read"
                ]
            },
            {
                "service": "180f",
                "characteristic": "2a19",
                "properties": [
                    "Read"
                ],
                "descriptors": [
                    {
                        "uuid": "2901"
                    },
                    {
                        "uuid": "2904"
                    }
                ]
            }
        ]
    }


# Advertising Data

Bluetooth advertising data is returned in when scanning for devices. The format varies depending on your platform. On Android advertising data will be the raw advertising bytes. iOS does not allow access to raw advertising data, so a dictionary of data is returned.

The advertising information for both Android and iOS appears to be a combination of advertising data and scan response data.

Ideally a common format (map or array) would be returned for both platforms in future versions. If you have ideas, please contact me.

## Android

    {
        "name": "demo",
        "id": "00:1A:7D:DA:71:13",
        "advertising": ArrayBuffer,
        "rssi": -37
    }

Convert the advertising info to a Uint8Array for processing. `var adData = new Uint8Array(peripheral.advertising)`. You application is responsible for parsing all the information out of the advertising ArrayBuffer using the [GAP type constants](https://www.bluetooth.com/specifications/assigned-numbers/generic-access-profile). For example to get the service data from the advertising info, I [parse the advertising info into a map](https://github.com/don/ITP-BluetoothLE/blob/887511c375b1ab2fbef3afe210d6a6b7db44cee9/phonegap/thermometer_v2/www/js/index.js#L18-L39) and then get the service data to retrieve a [characteristic value that is being broadcast](https://github.com/don/ITP-BluetoothLE/blob/887511c375b1ab2fbef3afe210d6a6b7db44cee9/phonegap/thermometer_v2/www/js/index.js#L93-L103).

## iOS

Note that iOS uses the string value of the constants for the [Advertisement Data Retrieval Keys](https://developer.apple.com/library/ios/documentation/CoreBluetooth/Reference/CBCentralManagerDelegate_Protocol/index.html#//apple_ref/doc/constant_group/Advertisement_Data_Retrieval_Keys). This will likely change in the future.

    {
        "name": "demo"
        "id": "15B4F1C5-C9C0-4441-BD9F-1A7ED8F7A365",
        "advertising": {
            "kCBAdvDataLocalName": "demo",
            "kCBAdvDataManufacturerData": {}, // arraybuffer data not shown
            "kCBAdvDataServiceUUIDs": [
                "721b"
            ],  
            "kCBAdvDataIsConnectable": true,
            "kCBAdvDataServiceData": {
                "BBB0": {}   // arraybuffer data not shown
            },
        },
        "rssi": -61
    }

Some of the values such as kCBAdvDataManufacturerData are ArrayBuffers. The data won't print out, but you can convert it to bytes using `new Uint8Array(peripheral.advertisting.kCBAdvDataManufacturerData)`. Your application is responsible for parsing and decoding any binary data such as kCBAdvDataManufacturerData or kCBAdvDataServiceData.

    function onDiscoverDevice(device) {
        // log the device as JSON
        console.log('Found Device', JSON.stringify(device, null, 2));

        // on iOS, print the manufacturer data if it exists
        if (device.advertising && device.advertising.kCBAdvDataManufacturerData) {
            const mfgData = new Uint8Array(device.advertising.kCBAdvDataManufacturerData);
            console.log('Manufacturer Data is', mfgData);
        }

    }

    ble.scan([], 5, onDiscoverDevice, onError);

# Typed Arrays

This plugin uses typed Arrays or ArrayBuffers for sending and receiving data.

This means that you need convert your data to ArrayBuffers before sending and from ArrayBuffers when receiving.

    // ASCII only
    function stringToBytes(string) {
       var array = new Uint8Array(string.length);
       for (var i = 0, l = string.length; i < l; i++) {
           array[i] = string.charCodeAt(i);
        }
        return array.buffer;
    }

    // ASCII only
    function bytesToString(buffer) {
        return String.fromCharCode.apply(null, new Uint8Array(buffer));
    }

You can read more about typed arrays in these articles on [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays) and [HTML5 Rocks](http://www.html5rocks.com/en/tutorials/webgl/typed_arrays/).

# UUIDs

UUIDs are always strings and not numbers. Some 16-bit UUIDs, such as '2220' look like integers, but they're not. (The integer 2220 is 0x8AC in hex.) This isn't a problem with 128 bit UUIDs since they look like strings 82b9e6e1-593a-456f-be9b-9215160ebcac. All 16-bit UUIDs should also be passed to methods as strings.

<a name="background-notifications-on-ios">

# Background Scanning and Notifications on iOS

Android applications will continue to receive notification while the application is in the background.

iOS applications need additional configuration to allow Bluetooth to run in the background.

Install the [cordova-custom-config](https://www.npmjs.com/package/cordova-custom-config) plugin.

    cordova plugin add cordova-custom-config

Add a new section to config.xml

    <platform name="ios">
        <config-file parent="UIBackgroundModes" target="*-Info.plist">
            <array>
                <string>bluetooth-central</string>
            </array>
        </config-file>
    </platform>

See [ble-background](https://github.com/don/ble-background) example project for more details.

# Testing the Plugin

Tests require the [Cordova Plugin Test Framework](https://github.com/apache/cordova-plugin-test-framework)

Create a new project

    git clone https://github.com/don/cordova-plugin-ble-central
    cordova create ble-test com.example.ble.test BLETest
    cd ble-test
    cordova platform add android
    cordova plugin add ../cordova-plugin-ble-central
    cordova plugin add ../cordova-plugin-ble-central/tests
    cordova plugin add cordova-plugin-test-framework

Change the start page in `config.xml`

    <content src="cdvtests/index.html" />

Run the app on your phone

    cordova run android --device

# Nordic DFU

If you need Nordic DFU capability, Tomáš Bedřich has a [fork](https://github.com/fxe-gear/cordova-plugin-ble-central) of this plugin that adds an `updateFirmware()` method that allows users to upgrade nRF5x based chips over the air. https://github.com/fxe-gear/cordova-plugin-ble-central

# License

Apache 2.0

# Feedback

Try the code. If you find an problem or missing feature, file an issue or create a pull request.

# Other Bluetooth Plugins

 * [cordova-plugin-ble-peripheral](https://github.com/don/cordova-plugin-ble-peripheral) - Create and publish Bluetooth LE services on iOS and Android using Javascript.
 * [BluetoothSerial](https://github.com/don/BluetoothSerial) - Connect to Arduino and other devices. Bluetooth Classic on Android, BLE on iOS.
 * [RFduino](https://github.com/don/cordova-plugin-rfduino) - RFduino specific plugin for iOS and Android.
 * [BluetoothLE](https://github.com/randdusing/BluetoothLE) - Rand Dusing's BLE plugin for Cordova
 * [PhoneGap Bluetooth Plugin](https://github.com/tanelih/phonegap-bluetooth-plugin) - Bluetooth classic pairing and connecting for Android
