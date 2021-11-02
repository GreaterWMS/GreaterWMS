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

var w3cBattery;
var winCallBack;

function success () {
    winCallBack({ level: w3cBattery.level * 100, isPlugged: w3cBattery.charging });
}

var Battery = {
    start: function (win, fail, args, env) {
        try {
            var subscribe = function (battery) {
                w3cBattery = battery;
                winCallBack = win;

                success();

                if (typeof w3cBattery.addEventListener === 'function') {
                    w3cBattery.addEventListener('levelchange', success, false);
                    w3cBattery.addEventListener('chargingchange', success, false);
                } else {
                    w3cBattery.onlevelchange = success;
                    w3cBattery.onchargingchange = success;
                }
            };

            if (typeof navigator.getBattery === 'function') {
                navigator.getBattery().then(function (battery) {
                    subscribe(battery);
                });
            } else {
                var origBattery = cordova.require('cordova/modulemapper').getOriginalSymbol(window, 'navigator.battery'); // eslint-disable-line no-undef

                if (origBattery) {
                    subscribe(origBattery);
                } else {
                    fail('Not supported');
                }
            }
        } catch (e) {
            fail(e);
        }
    },

    stop: function () {
        try {
            if (typeof w3cBattery.removeEventListener === 'function') {
                w3cBattery.removeEventListener('levelchange', success, false);
                w3cBattery.removeEventListener('chargingchange', success, false);
            } else {
                w3cBattery.onlevelchange = null;
                w3cBattery.onchargingchange = null;
            }
        } catch (e) {
            console.warn('Error occured while trying to stop battery: ' + JSON.stringify(e));
        }
    }
};

require('cordova/exec/proxy').add('Battery', Battery);
