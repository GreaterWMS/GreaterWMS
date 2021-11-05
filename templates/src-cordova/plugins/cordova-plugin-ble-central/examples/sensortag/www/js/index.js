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
/* global detailPage, accelerometerData, buttonState, disconnectButton */
/* global ble  */
/* jshint browser: true , devel: true*/
'use strict';

// http://processors.wiki.ti.com/index.php/SensorTag_User_Guide#Simple_Key_Service
var button = {
    service: "FFE0",
    data: "FFE1", // Bit 2: side key, Bit 1- right key, Bit 0 –left key
};


// http://processors.wiki.ti.com/index.php/SensorTag_User_Guide#Accelerometer_2
var accelerometer = {
    service: "F000AA10-0451-4000-B000-000000000000",
    data: "F000AA11-0451-4000-B000-000000000000", // read/notify 3 bytes X : Y : Z
    configuration: "F000AA12-0451-4000-B000-000000000000", // read/write 1 byte
    period: "F000AA13-0451-4000-B000-000000000000" // read/write 1 byte Period = [Input*10]ms
};

var app = {
    initialize: function() {
        this.bindEvents();
        detailPage.hidden = true;
    },
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
        refreshButton.addEventListener('touchstart', this.refreshDeviceList, false);
        disconnectButton.addEventListener('touchstart', this.disconnect, false);
        deviceList.addEventListener('touchstart', this.connect, false); // assume not scrolling
    },
    onDeviceReady: function() {
        app.refreshDeviceList();
    },
    refreshDeviceList: function() {
        deviceList.innerHTML = ''; // empties the list
        // scan for all devices
        ble.scan([], 5, app.onDiscoverDevice, app.onError);
    },
    onDiscoverDevice: function(device) {

        // we're not limiting scanning by services, so filter
        // the list for devices with "Sensor" in the name
        if (device.name.match(/sensor/i)) {

            var listItem = document.createElement('li'),
                html = '<b>' + device.name + '</b><br/>' +
                    'RSSI: ' + device.rssi + '&nbsp;|&nbsp;' +
                    device.id;

            listItem.dataset.deviceId = device.id;  // TODO
            listItem.innerHTML = html;
            deviceList.appendChild(listItem);

        }
    },
    connect: function(e) {
        var deviceId = e.target.dataset.deviceId,
            onConnect = function() {

                ble.startNotification(deviceId, button.service, button.data, app.onButtonData, app.onError);
                // subscribing for incoming data
                ble.startNotification(deviceId, accelerometer.service, accelerometer.data, app.onAccelerometerData, app.onError);
                // turn accelerometer on
                var configData = new Uint8Array(1);
                configData[0] = 0xFF;
                ble.write(deviceId, accelerometer.service, accelerometer.configuration, configData.buffer, 
                    function() { console.log("Started accelerometer."); },app.onError);
                disconnectButton.dataset.deviceId = deviceId;
                app.showDetailPage();
            };

        ble.connect(deviceId, onConnect, app.onError);
    },
    onButtonData: function(data) {
        console.log(data);
        var message;
        var a = new Uint8Array(data);
        switch(a[0]) { // should really check the bits in case bit 3 is set too
        case 0:
            message = "No buttons are pressed";
            break;
        case 1:
            message = "Right button is pressed";
            break;
        case 2:
            message = "Left button is pressed";
            break;
        case 3:
            message = "Both buttons are pressed";
            break;
        default:
            message = "Error";
        }

        buttonState.innerHTML = message;
    },
    onAccelerometerData: function(data) {
        console.log(data);
        var message;
        var a = new Uint8Array(data);

        // TODO get a template to line this up
        // TODO round or format numbers for better display
        message = "X: " + a[0]/64 + "<br/>" +
                  "Y: " + a[1]/64 + "<br/>" +
                  "Z: " + a[2]/64 * -1;

        accelerometerData.innerHTML = message;
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
