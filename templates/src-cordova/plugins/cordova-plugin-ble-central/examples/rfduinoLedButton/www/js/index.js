// (c) 2014-2015 Don Coleman
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/* global mainPage, deviceList, refreshButton */
/* global detailPage, buttonState, ledButton, disconnectButton */
/* global ble, cordova  */
/* jshint browser: true , devel: true*/
'use strict';

var arrayBufferToInt = function (ab) {
    var a = new Uint8Array(ab);
    return a[0];
};

var rfduino = {
    serviceUUID: "2220",
    receiveCharacteristic: "2221",
    sendCharacteristic: "2222",
    disconnectCharacteristic: "2223"
};

// returns advertising data as hashmap of byte arrays keyed by type
// advertising data is length, type, data
// https://www.bluetooth.org/en-us/specification/assigned-numbers/generic-access-profile
function parseAdvertisingData(bytes) {
    var length, type, data, i = 0, advertisementData = {};

    while (length !== 0) {

        length = bytes[i] & 0xFF;
        i++;

        type = bytes[i] & 0xFF;
        i++;

        data = bytes.slice(i, i + length - 1); // length includes type byte, but not length byte
        i += length - 2;  // move to end of data
        i++;

        advertisementData[type] = data;
    }

    return advertisementData;
}

// RFduino advertises the sketch its running in the Manufacturer field 0xFF
// RFduino provides a UART-like service so all sketchs look the same (0x2220)
// This RFduino "service" name is used to different functions on the boards
var getRFduinoService = function(scanRecord) {
    var mfgData;

    if (cordova.platformId === 'ios') {
        mfgData = arrayBufferToIntArray(scanRecord.kCBAdvDataManufacturerData);
    } else { // android
        var ad = parseAdvertisingData(arrayBufferToIntArray(scanRecord));
        mfgData = ad[0xFF];
    }

    if (mfgData) {
      // ignore 1st 2 bytes of mfg data
      return bytesToString(mfgData.slice(2));
    } else {
      return "";
    }
};

// Convert ArrayBuffer to int[] for easier processing.
// If Uint8Array.slice worked, this would be unnecessary
var arrayBufferToIntArray = function(buffer) {
    var result;

    if (buffer) {
        var typedArray = new Uint8Array(buffer);
        result = [];
        for (var i = 0; i < typedArray.length; i++) {
            result[i] = typedArray[i];
        }
    }

    return result;
};

var bytesToString = function (bytes) {
    var bytesAsString = "";
    for (var i = 0; i < bytes.length; i++) {
        bytesAsString += String.fromCharCode(bytes[i]);
    }
    return bytesAsString;
};

var app = {
    initialize: function() {
        this.bindEvents();
        detailPage.hidden = true;
    },
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
        refreshButton.addEventListener('touchstart', this.refreshDeviceList, false);
        ledButton.addEventListener('touchstart', this.sendData, false);
        ledButton.addEventListener('touchend', this.sendData, false);
        disconnectButton.addEventListener('touchstart', this.disconnect, false);
        deviceList.addEventListener('touchstart', this.connect, false); // assume not scrolling
    },
    onDeviceReady: function() {
        app.refreshDeviceList();
    },
    refreshDeviceList: function() {
        deviceList.innerHTML = ''; // empties the list
        ble.scan([rfduino.serviceUUID], 5, app.onDiscoverDevice, app.onError);
    },
    onDiscoverDevice: function(device) {
        var listItem = document.createElement('li'),
            html = '<b>' + device.name + '</b><br/>' +
                'RSSI: ' + device.rssi + '&nbsp;|&nbsp;' +
                'Advertising: ' + getRFduinoService(device.advertising) + '<br/>' +
                device.id;

        listItem.dataset.deviceId = device.id;
        listItem.innerHTML = html;
        deviceList.appendChild(listItem);
    },
    connect: function(e) {
        var deviceId = e.target.dataset.deviceId,
            onConnect = function() {
                // subscribe for incoming data
                ble.startNotification(deviceId, rfduino.serviceUUID, rfduino.receiveCharacteristic, app.onData, app.onError);
                disconnectButton.dataset.deviceId = deviceId;
                ledButton.dataset.deviceId = deviceId;
                app.showDetailPage();
            };

        ble.connect(deviceId, onConnect, app.onError);
    },
    onData: function(data) { // data received from rfduino
        console.log(data);
        var buttonValue = arrayBufferToInt(data);
        if (buttonValue === 1) {
            buttonState.innerHTML = "Button Pressed";
        } else {
            buttonState.innerHTML = "Button Released";
        }
    },
    sendData: function(event) { // send data to rfduino

        var success = function() {
            console.log("success");
        };

        var failure = function() {
            alert("Failed writing data to the rfduino");
        };

        var data = new Uint8Array(1);
        data[0] = event.type === 'touchstart' ? 0x1 : 0x0;
        var deviceId = event.target.dataset.deviceId;

        ble.writeWithoutResponse(deviceId, rfduino.serviceUUID, rfduino.sendCharacteristic, data.buffer, success, failure);

    },
    disconnect: function(event) {
        var deviceId = event.target.dataset.deviceId;
        ble.disconnect(deviceId, app.showMainPage, app.onError);
    },
    showMainPage: function() {
        mainPage.hidden = false;
        detailPage.hidden = true;
    },
    showDetailPage: function() {
        mainPage.hidden = true;
        detailPage.hidden = false;
    },
    onError: function(reason) {
        alert("ERROR: " + reason); // real apps should use notification.alert
    }
};
