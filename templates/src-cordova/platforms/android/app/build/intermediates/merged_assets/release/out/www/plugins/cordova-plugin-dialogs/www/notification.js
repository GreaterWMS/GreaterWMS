cordova.define("cordova-plugin-dialogs.notification", function(require, exports, module) {
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

var exec = require('cordova/exec');
var platform = require('cordova/platform');

/**
 * Provides access to notifications on the device.
 */

module.exports = {

    /**
     * Open a native alert dialog, with a customizable title and button text.
     *
     * @param {String} message              Message to print in the body of the alert
     * @param {Function} completeCallback   The callback that is called when user clicks on a button.
     * @param {String} title                Title of the alert dialog (default: Alert)
     * @param {String} buttonLabel          Label of the close button (default: OK)
     */
    alert: function (message, completeCallback, title, buttonLabel) {
        var _message = (typeof message === 'string' ? message : JSON.stringify(message));
        var _title = (typeof title === 'string' ? title : 'Alert');
        var _buttonLabel = (buttonLabel && typeof buttonLabel === 'string' ? buttonLabel : 'OK');
        exec(completeCallback, null, 'Notification', 'alert', [_message, _title, _buttonLabel]);
    },

    /**
     * Open a native confirm dialog, with a customizable title and button text.
     * The result that the user selects is returned to the result callback.
     *
     * @param {String} message              Message to print in the body of the alert
     * @param {Function} resultCallback     The callback that is called when user clicks on a button.
     * @param {String} title                Title of the alert dialog (default: Confirm)
     * @param {Array} buttonLabels          Array of the labels of the buttons (default: ['OK', 'Cancel'])
     */
    confirm: function (message, resultCallback, title, buttonLabels) {
        var _message = (typeof message === 'string' ? message : JSON.stringify(message));
        var _title = (typeof title === 'string' ? title : 'Confirm');
        var _buttonLabels = (buttonLabels || ['OK', 'Cancel']);

        // Strings are deprecated!
        if (typeof _buttonLabels === 'string') {
            console.log('Notification.confirm(string, function, string, string) is deprecated.  Use Notification.confirm(string, function, string, array).');
        }

        _buttonLabels = convertButtonLabels(_buttonLabels);

        exec(resultCallback, null, 'Notification', 'confirm', [_message, _title, _buttonLabels]);
    },

    /**
     * Open a native prompt dialog, with a customizable title and button text.
     * The following results are returned to the result callback:
     *  buttonIndex     Index number of the button selected.
     *  input1          The text entered in the prompt dialog box.
     *
     * @param {String} message              Dialog message to display (default: "Prompt message")
     * @param {Function} resultCallback     The callback that is called when user clicks on a button.
     * @param {String} title                Title of the dialog (default: "Prompt")
     * @param {Array} buttonLabels          Array of strings for the button labels (default: ["OK","Cancel"])
     * @param {String} defaultText          Textbox input value (default: empty string)
     */
    prompt: function (message, resultCallback, title, buttonLabels, defaultText) {
        var _message = (typeof message === 'string' ? message : JSON.stringify(message));
        var _title = (typeof title === 'string' ? title : 'Prompt');
        var _buttonLabels = (buttonLabels || ['OK', 'Cancel']);

        // Strings are deprecated!
        if (typeof _buttonLabels === 'string') {
            console.log('Notification.prompt(string, function, string, string) is deprecated.  Use Notification.confirm(string, function, string, array).');
        }

        _buttonLabels = convertButtonLabels(_buttonLabels);

        var _defaultText = (defaultText || '');
        exec(resultCallback, null, 'Notification', 'prompt', [_message, _title, _buttonLabels, _defaultText]);
    },

    /**
     * Causes the device to beep.
     * On Android, the default notification ringtone is played "count" times.
     *
     * @param {Integer} count       The number of beeps.
     */
    beep: function (count) {
        var defaultedCount = count || 1;
        exec(null, null, 'Notification', 'beep', [ defaultedCount ]);
    }
};

function convertButtonLabels (buttonLabels) {

    // Some platforms take an array of button label names.
    // Other platforms take a comma separated list.
    // For compatibility, we convert to the desired type based on the platform.
    if (platform.id === 'amazon-fireos' || platform.id === 'android' || platform.id === 'ios' ||
        platform.id === 'windowsphone' || platform.id === 'firefoxos' || platform.id === 'ubuntu' ||
        platform.id === 'windows8' || platform.id === 'windows') {

        if (typeof buttonLabels === 'string') {
            buttonLabels = buttonLabels.split(','); // not crazy about changing the var type here
        }
    } else {
        if (Array.isArray(buttonLabels)) {
            var buttonLabelArray = buttonLabels;
            buttonLabels = buttonLabelArray.toString();
        }
    }

    return buttonLabels;
}

});
