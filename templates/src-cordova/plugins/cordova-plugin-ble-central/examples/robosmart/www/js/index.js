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
/* global detailPage, lightSwitch, dimmer, disconnectButton */
/* global cordova, ble  */
/* jshint browser: true , devel: true*/
'use strict';

var arrayBufferToInt = function (ab) {
    var a = new Uint8Array(ab);
    return a[0];
};

var robosmart = {
    service: 'FF10',
    lightSwitch: 'FF11',
    brightness: 'FF12',
    powerConsumed: 'FF16',
    name: 'FF17',
    description: 'FF18',
    room: 'FF19',
    locationName: 'FF1b',
    locationGps: 'FF1d',
    disconnect: 'FF1a',
};

var app = {
    initialize: function() {
        this.bindEvents();
        detailPage.hidden = true;
    },
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
        refreshButton.addEventListener('touchstart', this.refreshDeviceList, false);
        lightSwitch.addEventListener('change', this.setOnOff, false);
        dimmer.addEventListener('change', this.setBrightness, false);
        disconnectButton.addEventListener('touchstart', this.disconnect, false);
        deviceList.addEventListener('touchstart', this.connect, false); // assume not scrolling
    },
    onDeviceReady: function() {
        app.refreshDeviceList();
    },
    refreshDeviceList: function() {
        deviceList.innerHTML = ''; // empties the list

        if (cordova.platformId === 'android') {
            // Bug: Android can't find RoboSmart when scanning for service
            ble.scan([], 5, app.onDiscoverDevice, app.onError);
        } else {
            ble.scan([robosmart.service], 5, app.onDiscoverDevice, app.onError);
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
        var deviceId = e.target.dataset.deviceId,
            onConnect = function() {
                // subscribe for power consumption notifications
                disconnectButton.dataset.deviceId = deviceId;
                lightSwitch.dataset.deviceId = deviceId;
                dimmer.dataset.deviceId = deviceId;
                app.showDetailPage();
                app.syncUI(deviceId);
            };

        ble.connect(deviceId, onConnect, app.onError);
    },
    setOnOff: function(event) { // send data to robosmart

        var success = function() {
            console.log("success");
        };

        var failure = function() {
            alert("Failed writing data to the robosmart");
        };

        var data = new Uint8Array(1);
        data[0] = event.target.checked ? 0x1 : 0x0;
        var deviceId = event.target.dataset.deviceId;

        ble.write(deviceId, robosmart.service, robosmart.lightSwitch, data.buffer, success, failure);
    },
    setBrightness: function(event) { // send data to robosmart

        var success = function() {
            // if the light was off and brightness is adjusted, the light will turn on
            lightSwitch.checked = true;
            console.log("success");
        };

        var failure = function() {
            alert("Failed writing data to the robosmart");
        };

        var deviceId = event.target.dataset.deviceId;

        // pass the brightness from the slider to the light
        var brightness = new Uint8Array(1);
        brightness[0] = event.target.value;

        ble.write(deviceId, robosmart.service, robosmart.brightness, brightness.buffer, success, failure);
    },
    syncUI: function(deviceId) {

        var switchCallback = function(data) {
            lightSwitch.checked = arrayBufferToInt(data) === 0x1;
        };

        var dimmerCallback = function(data) {
            dimmer.value = arrayBufferToInt(data);
        };

        var failure = function(reason) {
            console.log("Error syncing UI with the current state " + reason);
        };

        ble.read(deviceId, robosmart.service, robosmart.lightSwitch, switchCallback, failure);
        ble.read(deviceId, robosmart.service, robosmart.brightness, dimmerCallback, failure);

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
