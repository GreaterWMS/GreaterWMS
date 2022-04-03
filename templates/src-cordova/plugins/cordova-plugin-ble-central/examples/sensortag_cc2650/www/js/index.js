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

//http://processors.wiki.ti.com/index.php/CC2650_SensorTag_User%27s_Guide
var accelerometer = {
    service: "F000AA80-0451-4000-B000-000000000000",
    data: "F000AA81-0451-4000-B000-000000000000", // read/notify 3 bytes X : Y : Z
    notification:"F0002902-0451-4000-B000-000000000000",
    configuration: "F000AA82-0451-4000-B000-000000000000", // read/write 1 byte
    period: "F000AA83-0451-4000-B000-000000000000" // read/write 1 byte Period = [Input*10]ms
};

var barometer = {
    service: "F000AA40-0451-4000-B000-000000000000",
    data: "F000AA41-0451-4000-B000-000000000000",
    notification: "F0002902-0451-4000-B000-000000000000",
    configuration: "F000AA42-0451-4000-B000-000000000000",
    period: "F000AA43-0451-4000-B000-000000000000"

};

// button bitmask
var LEFT_BUTTON = 1;  // 0001
var RIGHT_BUTTON = 2; // 0010
var REED_SWITCH = 4;  // 0100

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
        // scan for CC2560 SensorTags
        ble.scan(['AA80'], 5, app.onDiscoverDevice, app.onError);
    },
    onDiscoverDevice: function(device) {
        var listItem = document.createElement('li'),
            html = '<b>' + device.name + '</b><br/>' +
                'RSSI: ' + device.rssi + '&nbsp;|&nbsp;' +
                device.id;

        listItem.dataset.deviceId = device.id;  // TODO
        listItem.innerHTML = html;
        deviceList.appendChild(listItem);
    },
    connect: function(e) {
        var deviceId = e.target.dataset.deviceId,
            onConnect = function() {

                //Subscribe to button service
                ble.startNotification(deviceId, button.service, button.data, app.onButtonData, app.onError);
                //Subscribe to accelerometer service
                ble.startNotification(deviceId, accelerometer.service, accelerometer.data, app.onAccelerometerData, app.onError);
                //Subscribe to barometer service
                ble.startNotification(deviceId, barometer.service, barometer.data, app.onBarometerData, app.onError);


                // turn accelerometer on
                var configData = new Uint16Array(1);
                //Turn on gyro, accel, and mag, 2G range, Disable wake on motion
                configData[0] = 0x007F;
                ble.write(deviceId, accelerometer.service, accelerometer.configuration, configData.buffer,
                    function() { console.log("Started accelerometer."); },app.onError);

                var periodData = new Uint8Array(1);
                periodData[0] = 0x0A;
                ble.write(deviceId, accelerometer.service, accelerometer.period, periodData.buffer,
                    function() { console.log("Configured accelerometer period."); },app.onError);

                //Turn on barometer
                var barometerConfig = new Uint8Array(1);
                barometerConfig[0] = 0x01;
                ble.write(deviceId, barometer.service, barometer.configuration, barometerConfig.buffer,
                    function() { console.log("Started barometer."); },app.onError);

                //Associate the deviceID with the disconnect button
                disconnectButton.dataset.deviceId = deviceId;
                app.showDetailPage();
            };

        ble.connect(deviceId, onConnect, app.onError);
    },
    onButtonData: function(data) {
        console.log(data);
        var state = new Uint8Array(data);
        var message = '';

        if (state === 0) {
            message = 'No buttons are pressed.';
        }

        if (state & LEFT_BUTTON) {
            message += 'Left button is pressed.<br/>';
        }

        if (state & RIGHT_BUTTON) {
            message += 'Right button is pressed.<br/>';
        }

        if (state & REED_SWITCH) {
            message += 'Reed switch is activated.<br/>';
        }

        buttonState.innerHTML = message;
    },

    sensorMpu9250GyroConvert: function(data){
        return data / (65536/500);
    },

    sensorMpu9250AccConvert: function(data){
        // Change  /2 to match accel range...i.e. 16 g would be /16
        return data / (32768 / 2);
    },

    onAccelerometerData: function(data) {
        console.log(data);
        var message;
        var a = new Int16Array(data);

        //0 gyro x
        //1 gyro y
        //2 gyro z
        //3 accel x
        //4 accel y
        //5 accel z
        //6 mag x
        //7 mag y
        //8 mag z

        // TODO get a template to line this up
        // TODO round or format numbers for better display
        message = "Gyro <br/>"+
                  "X: " + app.sensorMpu9250GyroConvert(a[0]) + "<br/>" +
                  "Y: " + app.sensorMpu9250GyroConvert(a[1]) + "<br/>" +
                  "Z: " + app.sensorMpu9250GyroConvert(a[2]) + "<br/>" +
                  "Accel <br/>"+
                  "X: " + app.sensorMpu9250AccConvert(a[3]) + "<br/>" +
                  "Y: " + app.sensorMpu9250AccConvert(a[4]) + "<br/>" +
                  "Z: " + app.sensorMpu9250AccConvert(a[5]) + "<br/>" +
                  "Mag <br/>"+
                  "X: " + a[6] + "<br/>" +
                  "Y: " + a[7] + "<br/>" +
                  "Z: " + a[8] + "<br/>" ;

        accelerometerData.innerHTML = message;
    },
    sensorBarometerConvert: function(data){
        return (data / 100);

    },
    onBarometerData: function(data) {
         console.log(data);
         var message;
         var a = new Uint8Array(data);

         //0-2 Temp
         //3-5 Pressure
         message =  "Temperature <br/>" +
                    app.sensorBarometerConvert( a[0] | (a[1] << 8) | (a[2] << 16)) + "°C <br/>" +
                    "Pressure <br/>" +
                    app.sensorBarometerConvert( a[3] | (a[4] << 8) | (a[5] << 16)) + "hPa <br/>" ;


        barometerData.innerHTML = message;

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
