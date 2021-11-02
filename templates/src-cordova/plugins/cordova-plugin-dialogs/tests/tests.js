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

/* eslint-env jasmine */
/* global cordova */

exports.defineAutoTests = function () {
    describe('Notification (navigator.notification)', function () {
        it('should exist', function () {
            expect(navigator.notification).toBeDefined();
        });

        it('should contain a beep function', function () {
            expect(typeof navigator.notification.beep).toBeDefined();
            expect(typeof navigator.notification.beep).toBe('function');
        });

        it('should contain an alert function', function () {
            expect(typeof navigator.notification.alert).toBeDefined();
            expect(typeof navigator.notification.alert).toBe('function');
        });

        it('should contain a confirm function', function () {
            expect(typeof navigator.notification.confirm).toBeDefined();
            expect(typeof navigator.notification.confirm).toBe('function');
        });

        it('should contain a prompt function', function () {
            expect(typeof navigator.notification.prompt).toBeDefined();
            expect(typeof navigator.notification.prompt).toBe('function');
        });
    });
};

/******************************************************************************/
/******************************************************************************/
/******************************************************************************/

exports.defineManualTests = function (contentEl, createActionButton) {
    var logMessage = function (message) {
        var log = document.getElementById('info');
        var logLine = document.createElement('div');
        logLine.innerHTML = message;
        log.appendChild(logLine);
    };

    var clearLog = function () {
        var log = document.getElementById('info');
        log.innerHTML = '';
    };

    var beep = function () {
        console.log('beep()');
        navigator.notification.beep(3);
    };

    var alertDialog = function (message, title, button) {
        console.log('alertDialog()');
        navigator.notification.alert(message,
            function () {
                console.log('Alert dismissed.');
            },
            title, button);
        console.log('After alert');
    };

    var confirmDialogA = function (message, title, buttons) {
        clearLog();
        navigator.notification.confirm(message,
            function (r) {
                if (r === 0) {
                    logMessage('Dismissed dialog without making a selection.');
                    console.log('Dismissed dialog without making a selection.');
                } else {
                    console.log('You selected ' + r);
                    logMessage('You selected ' + (buttons.split(','))[r - 1]);
                }
            },
            title,
            buttons);
    };

    var confirmDialogB = function (message, title, buttons) {
        clearLog();
        navigator.notification.confirm(message,
            function (r) {
                if (r === 0) {
                    logMessage('Dismissed dialog without making a selection.');
                    console.log('Dismissed dialog without making a selection.');
                } else {
                    console.log('You selected ' + r);
                    logMessage('You selected ' + buttons[r - 1]);
                }
            },
            title,
            buttons);
    };

    var promptDialog = function (message, title, buttons, defaultText) {
        clearLog();
        navigator.notification.prompt(message,
            function (r) {
                if (r && r.buttonIndex === 0) {
                    var msg = 'Dismissed dialog';
                    if (r.input1) {
                        msg += ' with input: ' + r.input1;
                    }
                    logMessage(msg);
                    console.log(msg);
                } else {
                    console.log('You selected ' + r.buttonIndex + ' and entered: ' + r.input1);
                    logMessage('You selected ' + buttons[r.buttonIndex - 1] + ' and entered: ' + r.input1);
                }
            },
            title,
            buttons, defaultText);
    };

    /******************************************************************************/

    var dialogs_tests = '<div id="beep"></div>' +
        'Expected result: Device will beep (unless device is on silent). Nothing will get updated in status box.' +
        '<h2>Dialog Tests</h2>' +
        '<h3>Dialog boxes will pop up for each of the following tests</h3>' +
        '<p/> <div id="alert"></div>' +
        'Expected result: Dialog will say "You pressed alert". Press continue to close dialog. Nothing will get updated in status box.' +
        '<p/> <div id="confirm_deprecated"></div>' +
        'Expected result: Dialog will say "You pressed confirm". Press Yes, No, or Maybe to close dialog. Status box will tell you what option you selected.' +
        '<p/> <div id="confirm"></div>' +
        'Expected result: Dialog will say "You pressed confirm". Press Yes, No, or Maybe, Not Sure to close dialog. Status box will tell you what option you selected, and should use 1-based indexing.' +
        '<p/> <div id="prompt"></div>' +
        'Expected result: Dialog will say "You pressed prompt". Enter any message and press Yes, No, or Maybe, Not Sure to close dialog. Status box will tell you what option you selected and message you entered or if empty, it will display "Default Text", and should use 1-based indexing.' +
        '<p/> <div id="built_in_alert"></div>' +
        'Expected result: Dialog will have title "index.html" and say "You pressed alert" Press OK to close dialog. Nothing will get updated in status box.' +
        '<p/> <div id="built_in_confirm"></div>' +
        'Expected result: Dialog will have title "index.html" and say "You selected confirm". Press Cancel or OK to close dialog. Nothing will get updated in status box.' +
        '<p/> <div id="built_in_prompt"></div>' +
        'Expected result: Dialog will have title "index.html" and say "This is a prompt". "Default value" will be in text box. Press Cancel or OK to close dialog. Nothing will get updated in status box.' +
        '<p/> <h3>CB-8947 Tests</h3><div id="cb8947"></div>' +
        'Expected results: Dialogs will not crash iOS';

    contentEl.innerHTML = '<div id="info"></div>' +
        dialogs_tests;

    createActionButton('Beep', function () {
        beep();
    }, 'beep');

    createActionButton('Alert Dialog', function () {
        alertDialog('You pressed alert.', 'Alert Dialog', 'Continue');
    }, 'alert');

    // WP8.1 detection is necessary since it doesn't support confirm dialogs with more than 2 buttons
    var isRunningOnWP81 = cordova.platformId === 'windows' && navigator.userAgent.indexOf('Windows Phone') > -1;

    createActionButton('Confirm Dialog - Deprecated', function () {
        var buttons = isRunningOnWP81 ? 'Yes,No' : 'Yes,No,Maybe';
        confirmDialogA('You pressed confirm.', 'Confirm Dialog', buttons);
    }, 'confirm_deprecated');

    createActionButton('Confirm Dialog', function () {
        var buttons = isRunningOnWP81 ? ['Yes', 'Actually, No'] : ['Yes', 'No', 'Maybe, Not Sure'];
        confirmDialogB('You pressed confirm.', 'Confirm Dialog', buttons);
    }, 'confirm');

    createActionButton('Prompt Dialog', function () {
        promptDialog('You pressed prompt.', 'Prompt Dialog', ['Yes', 'No', 'Maybe, Not Sure'], 'Default Text');
    }, 'prompt');

    createActionButton('Prompt Dialog - no default', function () {
        promptDialog('You pressed prompt.', 'Prompt Dialog', ['Yes', 'No']);
    }, 'prompt');

    createActionButton('Built-in Alert Dialog', function () {
        if (typeof alert === 'function') {
            alert('You pressed alert'); // eslint-disable-line no-undef
        }
    }, 'built_in_alert');

    createActionButton('Built-in Confirm Dialog', function () {
        if (typeof confirm === 'function') {
            confirm('You selected confirm'); // eslint-disable-line no-undef
        }
    }, 'built_in_confirm');

    createActionButton('Built-in Prompt Dialog', function () {
        if (typeof prompt === 'function') {
            prompt('This is a prompt', 'Default value'); // eslint-disable-line no-undef
        }
    }, 'built_in_prompt');

    // CB-8947 - ensure number messages don't crash iOS
    createActionButton('Alert Dialog with Number', function () {
        var callback = function () { clearLog(); console.log('Test passed'); };
        navigator.notification.alert(17, callback);
    }, 'cb8947');

    // CB-8947 - ensure object messages don't crash iOS
    createActionButton('Alert Dialog with Object', function () {
        var object = { number: 42, message: "Make sure an object doesn't crash iOS", issue: 'CB-8947' };
        var callback = function () { clearLog(); console.log('Test passed'); };
        navigator.notification.alert(object, callback);
    }, 'cb8947');

    // CB-8947 - ensure object messages don't crash iOS
    createActionButton('Confirm Dialog with Object', function () {
        var object = { number: 42, message: "Make sure an object doesn't crash iOS", issue: 'CB-8947' };
        var callback = function () { clearLog(); console.log('Test passed'); };
        navigator.notification.confirm(object, callback);
    }, 'cb8947');

    // CB-8947 - ensure object messages don't crash iOS
    createActionButton('Prompt Dialog with Object', function () {
        var object = { number: 42, message: "Make sure an object doesn't crash iOS", issue: 'CB-8947' };
        var callback = function () { clearLog(); console.log('Test passed'); };
        navigator.notification.prompt(object, callback);
    }, 'cb8947');

};
