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

var CompassHeading = require('cordova-plugin-device-orientation.CompassHeading'),
    CompassError = require('cordova-plugin-device-orientation.CompassError');

var compassCallback = null,
    compassReady = false;


module.exports = {
    getHeading: function (successCallback, errorCallback) {
        if (window.DeviceOrientationEvent !== undefined) {
            compassCallback = function (orientation) {
                var heading = 360 - orientation.alpha;

                if (compassReady) {
                    if (successCallback)
                        successCallback( new CompassHeading (heading, heading, 0, 0));
                    window.removeEventListener("deviceorientation", compassCallback, true);
                }
                compassReady = true;
            };
            compassReady = false; // workaround invalid first event value returned by WRT
            window.addEventListener("deviceorientation", compassCallback, true);
        }
        else {
            if (errorCallback)
                errorCallback(CompassError.COMPASS_NOT_SUPPORTED);
        }
    },

    stopHeading: function (successCallback, errorCallback) {
        console.log("Compass stopHeading: not implemented yet.");
    }
};

require("cordova/tizen/commandProxy").add("Compass", module.exports);
