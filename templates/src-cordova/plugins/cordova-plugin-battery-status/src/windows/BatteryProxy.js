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

/* global Windows, WinJS, BatteryStatus */

var PowerManager = Windows && Windows.System &&
    Windows.System.Power && Windows.System.Power.PowerManager;

if (PowerManager) {
    var pluginCallback;
    var reportStatus = function () {
        if (!pluginCallback) {
            return;
        }

        pluginCallback({
            level: PowerManager.remainingChargePercent,
            isPlugged: PowerManager.powerSupplyStatus !== Windows.System.Power.PowerSupplyStatus.notPresent
        }, { keepCallback: true });
    };

    var BatteryWin10 = {
        start: function (win, fail) {
            pluginCallback = win;
            PowerManager.addEventListener('remainingchargepercentchanged', reportStatus);
            PowerManager.addEventListener('powersupplystatuschanged', reportStatus);

            reportStatus();
        },

        stop: function () {
            if (pluginCallback) {
                PowerManager.removeEventListener('remainingchargepercentchanged', reportStatus);
                PowerManager.removeEventListener('powersupplystatuschanged', reportStatus);
            }

            pluginCallback = null;
        }
    };

    require('cordova/exec/proxy').add('Battery', BatteryWin10);

} else {

    var stopped;

    var handleResponse = function (successCb, errorCb, jsonResponse) {
        var info = JSON.parse(jsonResponse);

        if (info.hasOwnProperty('exceptionMessage')) {
            errorCb(info.exceptionMessage);
            return;
        }

        successCb(info, { keepCallback: true });
    };

    var Battery = {
        start: function (win, fail, args, env) {
            function getBatteryStatus (success, error) {
                handleResponse(success, error, BatteryStatus.BatteryStatus.start());
            }

            function getBatteryStatusLevelChangeEvent (success, error) {
                return BatteryStatus.BatteryStatus.getBatteryStatusChangeEvent().done(function (result) {
                    if (stopped) {
                        return;
                    }

                    handleResponse(success, error, result);

                    setTimeout(function () { getBatteryStatusLevelChangeEvent(success, error); }, 0);
                }, function (err) {
                    fail(err);
                });
            }

            // Battery API supported on Phone devices only so in case of
            // desktop/tablet the only one choice is to fail with appropriate message.
            if (!WinJS.Utilities.isPhone) {
                fail('The operation is not supported on Windows Desktop devices.');
                return;
            }

            stopped = false;
            try {
                getBatteryStatus(win, fail);
                getBatteryStatusLevelChangeEvent(win, fail);
            } catch (e) {
                fail(e);
            }
        },

        stop: function () {
            // Battery API supported on Phone devices only so in case of
            // desktop/tablet device we don't need for any actions.
            if (!WinJS.Utilities.isPhone) {
                return;
            }

            stopped = true;
            BatteryStatus.BatteryStatus.stop();
        }
    };

    require('cordova/exec/proxy').add('Battery', Battery);
}
