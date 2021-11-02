/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
*/

/*jslint sloppy:true */
/*global Windows:true, require, module, setTimeout */

var CompassHeading = require('cordova-plugin-device-orientation.CompassHeading'),
    CompassError = require('cordova-plugin-device-orientation.CompassError');


module.exports = {

    onReadingChanged: null,
    getHeading: function (win, lose) {
        var deviceCompass = Windows.Devices.Sensors.Compass.getDefault();
        if (!deviceCompass) {
            setTimeout(function () {
                lose(CompassError.COMPASS_NOT_SUPPORTED);
            }, 0);
        } else {
            var reading = deviceCompass.getCurrentReading(),
                heading = new CompassHeading(reading.headingMagneticNorth, reading.headingTrueNorth, null, reading.timestamp.getTime());
            setTimeout(function () {
                win(heading);
            }, 0);
        }
    },
    stopHeading: function (win, lose) {
        setTimeout(function () {
            win();
        }, 0);
    }
};

require("cordova/exec/proxy").add("Compass", module.exports);
