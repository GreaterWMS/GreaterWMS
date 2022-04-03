// (c) 2014 Don Coleman
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
/* global detailPage, resultDiv, pulseWidthInput, motorButton, buzzerButton, disconnectButton */
/* global ble, cordova */
/* jshint browser: true , devel: true*/
'use strict';

// this is MetaWear's UART service
var metawear = {
    serviceUUID: "326a9000-85cb-9195-d9dd-464cfbbae75a",
    txCharacteristic: "326a9001-85cb-9195-d9dd-464cfbbae75a", // transmit is from the phone's perspective
    rxCharacteristic: "326a9006-85cb-9195-d9dd-464cfbbae75a"  // receive is from the phone's perspective
};

var app = {
    deviceId: "",
    initialize: function() {
        this.bindEvents();
        detailPage.hidden = true;
    },
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
        refreshButton.addEventListener('touchstart', this.refreshDeviceList, false);
        motorButton.addEventListener('click', this.onMotorButton, false);
        buzzerButton.addEventListener('click', this.onBuzzerButton, false);
        disconnectButton.addEventListener('touchstart', this.disconnect, false);
        deviceList.addEventListener('touchstart', this.connect, false); // assume not scrolling
    },
    onDeviceReady: function() {
        app.refreshDeviceList();
    },
    refreshDeviceList: function() {
        deviceList.innerHTML = ''; // empties the list
        if (cordova.platformId === 'android') { // Android filtering is broken
            ble.scan([], 5, app.onDiscoverDevice, app.onError);
        } else {
            ble.scan([metawear.serviceUUID], 5, app.onDiscoverDevice, app.onError);
        }
    },
    onDiscoverDevice: function(device) {
        var listItem = document.createElement('li'),
            html = '<b>' + device.name + '</b><br/>' +
                'RSSI: ' + device.rssi + '&nbsp;|&nbsp;' +
                device.id;

        listItem.dataset.deviceId = device.id;
        listItem.innerHTML = html;
        deviceList.appendChild(listItem);
    },
    connect: function(e) {
        app.deviceId = e.target.dataset.deviceId;

        var onConnect = function() {
            app.enableButtonFeedback(app.subscribeForIncomingData, app.onError);
            app.showDetailPage();
        };

        ble.connect(app.deviceId, onConnect, app.onError);
    },
    onData: function(buffer) { // data received from MetaWear

        var data = new Uint8Array(buffer);
        var message = "";

        if (data[0] === 1 && data[1] === 1) { // module = 1, opscode = 1
            if (data[2] === 1) { // button state
                message = "Button pressed";
            } else {
                message = "Button released";
            }
        }

        resultDiv.innerHTML = resultDiv.innerHTML + message + "<br/>";
        resultDiv.scrollTop = resultDiv.scrollHeight;
    },
    writeData: function(buffer, success, failure) { // to to be sent to MetaWear

        if (!success) {
            success = function() {
                console.log("success");
                resultDiv.innerHTML = resultDiv.innerHTML + "Sent: " + JSON.stringify(new Uint8Array(buffer)) + "<br/>";
                resultDiv.scrollTop = resultDiv.scrollHeight;
            };
        }

        if (!failure) {
            failure = app.onError;
        }

        ble.writeCommand(app.deviceId, metawear.serviceUUID, metawear.txCharacteristic, buffer, success, failure);
    },
    subscribeForIncomingData: function() {
        ble.startNotification(app.deviceId, metawear.serviceUUID, metawear.rxCharacteristic, app.onData, app.onError);
    },
    enableButtonFeedback: function(success, failure) {
        var data = new Uint8Array(6);
        data[0] = 0x01; // mechanical switch
        data[1] = 0x01; // switch state ops code
        data[2] = 0x01; // enable

        app.writeData(data.buffer, success, failure);
    },
    onMotorButton: function(event) {
        var pulseWidth = pulseWidthInput.value;
        var data = new Uint8Array(6);
        data[0] = 0x07; // module
        data[1] = 0x01; // pulse ops code
        data[2] = 0x80; // Motor
        data[3] = pulseWidth & 0xFF; // Pulse Width
        data[4] = pulseWidth >> 8; // Pulse Width
        data[5] = 0x00; // Some magic bullshit

        app.writeData(data.buffer);
    },
    onBuzzerButton: function(event) {
        var pulseWidth = pulseWidthInput.value;
        var data = new Uint8Array(6);
        data[0] = 0x07; // module
        data[1] = 0x01; // pulse ops code
        data[2] = 0xF8; // Buzzer
        data[3] = pulseWidth & 0xFF; // Pulse Width
        data[4] = pulseWidth >> 8; // Pulse Width
        data[5] = 0x01; // Some magic?

        app.writeData(data.buffer);
    },
    disconnect: function(event) {
        ble.disconnect(app.deviceId, app.showMainPage, app.onError);
        app.deviceId = "";
    },
    showMainPage: function() {
        mainPage.hidden = false;
        detailPage.hidden = true;
    },
    showDetailPage: function() {
        mainPage.hidden = true;
        detailPage.hidden = false;
        resultDiv.innerHTML = "<i>Press the button on the MetaWear</i><br/>";
    },
    onError: function(reason) {
        alert("ERROR: " + reason); // real apps should use notification.alert
    }
};
