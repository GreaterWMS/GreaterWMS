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

// Platform: browser
window.navigator.notification = window.navigator.notification || {};

module.exports.alert = window.navigator.notification.alert = function (message, callback) {
    // `notification.alert` executes asynchronously
    setTimeout(function () {
        window.alert(message);
        if (callback) {
            callback();
        }
    }, 0);
};

module.exports.confirm = window.navigator.notification.confirm = function (message, callback) {
    // `notification.confirm` executes asynchronously
    /* eslint-disable standard/no-callback-literal */
    setTimeout(function () {
        var result = window.confirm(message);
        if (callback) {
            if (result) {
                callback(1); // OK
            } else {
                callback(2); // Cancel
            }
        }
    }, 0);
};

module.exports.prompt = window.navigator.notification.prompt = function (message, callback, title, buttonLabels, defaultText) {
    // `notification.prompt` executes asynchronously
    setTimeout(function () {
        var result = window.prompt(message, defaultText || '');
        if (callback) {
            if (result === null) {
                callback({ buttonIndex: 2, input1: '' }); // Cancel
            } else {
                callback({ buttonIndex: 1, input1: result }); // OK
            }
        }
    }, 0);
};
/* eslint-enable standard/no-callback-literal */
var audioContext = (function () {
    // Determine if the Audio API is supported by this browser
    var AudioApi = window.AudioContext;
    if (!AudioApi) {
        AudioApi = window.webkitAudioContext;
    }

    if (AudioApi) {
        // The Audio API is supported, so create a singleton instance of the AudioContext
        return new AudioApi();
    }

    return undefined;
}());

module.exports.beep = window.navigator.notification.beep = function (times) {
    if (times > 0) {
        var BEEP_DURATION = 700;
        var BEEP_INTERVAL = 300;

        if (audioContext) {
            // Start a beep, using the Audio API
            var osc = audioContext.createOscillator();
            osc.type = 0; // sounds like a "beep"
            osc.connect(audioContext.destination);
            osc.start(0);

            setTimeout(function () {
                // Stop the beep after the BEEP_DURATION
                osc.stop(0);

                if (--times > 0) {
                    // Beep again, after a pause
                    setTimeout(function () {
                        navigator.notification.beep(times);
                    }, BEEP_INTERVAL);
                }

            }, BEEP_DURATION);
        } else if (typeof (console) !== 'undefined' && typeof (console.log) === 'function') {
            // Audio API isn't supported, so just write `beep` to the console
            for (var i = 0; i < times; i++) {
                console.log('Beep!');
            }
        }
    }
};
