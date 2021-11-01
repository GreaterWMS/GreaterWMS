cordova.define("cordova-plugin-battery-status.battery", function(require, exports, module) {
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

/**
 * This class contains information about the current battery status.
 * @constructor
 */
var cordova = require('cordova');
var exec = require('cordova/exec');

var STATUS_CRITICAL = 5;
var STATUS_LOW = 20;

var Battery = function () {
    this._level = null;
    this._isPlugged = null;
    // Create new event handlers on the window (returns a channel instance)
    this.channels = {
        batterystatus: cordova.addWindowEventHandler('batterystatus'),
        batterylow: cordova.addWindowEventHandler('batterylow'),
        batterycritical: cordova.addWindowEventHandler('batterycritical')
    };
    for (var key in this.channels) {
        this.channels[key].onHasSubscribersChange = Battery.onHasSubscribersChange;
    }
};

function handlers () {
    return battery.channels.batterystatus.numHandlers +
        battery.channels.batterylow.numHandlers +
        battery.channels.batterycritical.numHandlers;
}

/**
 * Event handlers for when callbacks get registered for the battery.
 * Keep track of how many handlers we have so we can start and stop the native battery listener
 * appropriately (and hopefully save on battery life!).
 */
Battery.onHasSubscribersChange = function () {
  // If we just registered the first handler, make sure native listener is started.
    if (this.numHandlers === 1 && handlers() === 1) {
        exec(battery._status, battery._error, 'Battery', 'start', []);
    } else if (handlers() === 0) {
        exec(null, null, 'Battery', 'stop', []);
    }
};

/**
 * Callback for battery status
 *
 * @param {Object} info            keys: level, isPlugged
 */
Battery.prototype._status = function (info) {

    if (info) {
        if (battery._level !== info.level || battery._isPlugged !== info.isPlugged) {

            if (info.level === null && battery._level !== null) {
                return; // special case where callback is called because we stopped listening to the native side.
            }

            // Something changed. Fire batterystatus event
            cordova.fireWindowEvent('batterystatus', info);

            if (!info.isPlugged) { // do not fire low/critical if we are charging. issue: CB-4520
                // note the following are NOT exact checks, as we want to catch a transition from
                // above the threshold to below. issue: CB-4519
                if (battery._level > STATUS_CRITICAL && info.level <= STATUS_CRITICAL) {
                    // Fire critical battery event
                    cordova.fireWindowEvent('batterycritical', info);
                } else if (battery._level > STATUS_LOW && info.level <= STATUS_LOW) {
                    // Fire low battery event
                    cordova.fireWindowEvent('batterylow', info);
                }
            }
            battery._level = info.level;
            battery._isPlugged = info.isPlugged;
        }
    }
};

/**
 * Error callback for battery start
 */
Battery.prototype._error = function (e) {
    console.log('Error initializing Battery: ' + e);
};

var battery = new Battery(); // jshint ignore:line

module.exports = battery;

});
