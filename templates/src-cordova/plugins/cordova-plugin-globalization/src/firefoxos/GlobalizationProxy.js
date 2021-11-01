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

var GlobalizationError = require('./GlobalizationError');

var l10n_loaded = new Event('l10n_loaded'); // eslint-disable-line no-undef
var l10n_ready = new Event('l10n_ready'); // eslint-disable-line no-undef

var is_l10n_ready = false;

document.addEventListener('l10n_loaded', function () {
    console.log('DEBUG: L10n loaded');
    navigator.mozL10n.ready(function () {
        console.log('DEBUG: L10n ready');
        is_l10n_ready = true;
        document.dispatchEvent(l10n_ready);
    });
});

function callIfL10nReady (callback) {
    if (is_l10n_ready) {
        return callback();
    }
    document.addEventListener('l10n_ready', callback);
}

function loadFile (elementName, attributes, callback) {
    var e = document.createElement(elementName);
    for (var attrName in attributes) {
        if (attributes.hasOwnProperty(attrName)) {
            e.setAttribute(attrName, attributes[attrName]);
        }
    }
    e.onreadystatechange = e.onload = function () {
        var state = e.readyState;
        if (!callback.done && (!state || /loaded|complete/.test(state))) {
            callback.done = true;
            callback();
        }
    };
    document.head.appendChild(e);
}

function loadDependencies () {
// Adding globalization file to the HEAD section
// <link rel="resource" type="application/l10n" href="locales/date.ini" />

    loadFile('link', {
        'rel': 'resource',
        'type': 'application/l10n',
        'href': 'locales/date.ini'}, function () {});
    loadFile('script', {
        'type': 'text/javascript',
        'src': 'js/l10n.js'},
    function () {
        loadFile('script', {
            'type': 'text/javascript',
            'src': 'js/l10n_date.js'},
        function () {
            document.dispatchEvent(l10n_loaded);
        });
    });
}

loadDependencies();

function getPreferredLanguage (successCB, errorCB) {
    // WARNING: this isn't perfect - there is a difference between UI language
    // and preferred language, however it doesn't happen too often.
    callIfL10nReady(function () {
        successCB({value: navigator.mozL10n.language.code});
    });
}

function getLocaleName (successCB, errorCB) {
    callIfL10nReady(function () {
        successCB(navigator.mozL10n.language.code);
    });
}

function dateToString (successCB, errorCB, params) {
    var date = new Date(params[0].date);
    var options = params[0].options;

    callIfL10nReady(function () {
        var f = new navigator.mozL10n.DateTimeFormat();
        successCB({'value': _getStringFromDate(f, date, options)});
    });

    function _getStringFromDate (f, date, options) {
        var format = navigator.mozL10n.get('shortDateTimeFormat');
        if (options) {
            if (options.selector === 'date') {
                return f.localeDateString(date);
            }
            if (options.selector === 'time') {
                return f.localeTimeString(date);
            }
            if (options.formatLength !== 'short') {
                format = navigator.mozL10n.get('dateTimeFormat');
                return f.localeString(date, format);
            }
            if (options.selector === 'time') {
                return f.localeTimeString(date, format);
            }
        }
        var d = f.localeDateString(date);
        var t = f.localeTimeString(date);
        return d + ' ' + t;
    }
}

function stringToDate (successCB, errorCB, params) {
    var date;
    var dateString = params[0].dateString;
    var options = params[0].options;
    try {
        date = new Date(dateString);
    } catch (e) {
        console.log('Cordova, stringToDate, An error occurred ' + e.message);
        return errorCB(new GlobalizationError(
            GlobalizationError.PARSING_ERROR, e.message));
    }
    if (!date || date === 'Invalid Date') {
        console.log('Cordova, stringToDate, Invalid Date: ' + dateString);
        return errorCB(new GlobalizationError(
            GlobalizationError.PARSING_ERROR, 'Invalid Date (' + dateString + ')'));
    }

    var dateObj = {
        'year': date.getFullYear(),
        'month': date.getMonth(),
        'day': date.getDay()
    };
    var timeObj = {
        'hour': date.getHours(),
        'minute': date.getMinutes(),
        'second': date.getSeconds(),
        'millisecond': date.getMilliseconds()
    };
    if (options) {
        if (options.selector === 'date') {
            return successCB(dateObj);
        }
        if (options.selector === 'time') {
            return successCB(timeObj);
        }
    }
    for (var i in timeObj) {
        if (timeObj.hasOwnProperty(i)) {
            dateObj[i] = timeObj[i];
        }
    }
    successCB(dateObj);
}

function getDatePattern (successCB, failureCB, options) {
    failureCB(GlobalizationError.UNKNOWN_ERROR, 'unsupported');
}

function getDateNames (successCB, failureCB, params) {
    callIfL10nReady(function () {
        var version = 'long';
        var item = 'month';
        var options = params[0].options;
        if (options) {
            if (options.type === 'narrow') {
                version = 'short';
            } else if (options.type === 'genitive' && options.item === 'months') {
                version = options.type;
            }
            if (options.item === 'days') {
                item = 'weekday';
            }
        }
        var limit = (item === 'month') ? 11 : 6;

        var arr = [];
        for (var i = 0; i <= limit; i++) {
            arr.push(navigator.mozL10n.get(item + '-' + i + '-' + version));
        }
        successCB({'value': arr});
    });
}

Date.prototype.stdTimezoneOffset = function () { // eslint-disable-line no-extend-native
    // Return the standard timezone offset (usually 0 or -600)
    var jan = new Date(this.getFullYear(), 0, 1);
    var jul = new Date(this.getFullYear(), 6, 1);
    return Math.max(jan.getTimezoneOffset(), jul.getTimezoneOffset());
};

Date.prototype.isDayLightSavingsTime = function () { // eslint-disable-line no-extend-native
    return this.getTimezoneOffset() < this.stdTimezoneOffset();
};

function isDayLightSavingsTime (successCB, failureCB, params) {
    var date = new Date(params[0].date);
    successCB({'dst': date.isDayLightSavingsTime()});
}

function getFirstDayOfWeek (successCB, failureCB) {
    callIfL10nReady(function () {
        var firstDay = navigator.mozL10n.get('weekStartsOnMonday');
        // Sunday: 1
        // Monday: 2
        successCB({'value': 1 + parseInt(firstDay)});
    });
}

function numberToString (number, successCB, failureCB) {
    failureCB(GlobalizationError.UNKNOWN_ERROR, 'unsupported');
}

function stringToNumber (numberString, successCB, failureCB, options) {
    failureCB(GlobalizationError.UNKNOWN_ERROR, 'unsupported');
}

function getNumberPattern (successCB, failureCB, options) {
    failureCB(GlobalizationError.UNKNOWN_ERROR, 'unsupported');
}

function getCurrencyPattern (currencyCode, successCB, failureCB) {
    failureCB(GlobalizationError.UNKNOWN_ERROR, 'unsupported');
}

var Globalization = {
    getLocaleName: getLocaleName,
    getPreferredLanguage: getPreferredLanguage,
    dateToString: dateToString,
    stringToDate: stringToDate,
    getDatePattern: getDatePattern,
    getDateNames: getDateNames,
    isDayLightSavingsTime: isDayLightSavingsTime,
    getFirstDayOfWeek: getFirstDayOfWeek,
    numberToString: numberToString,
    stringToNumber: stringToNumber,
    getNumberPattern: getNumberPattern,
    getCurrencyPattern: getCurrencyPattern
};

require('cordova/exec/proxy').add('Globalization', Globalization);
