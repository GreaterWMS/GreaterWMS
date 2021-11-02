/*
 *
 * Copyright 2013 Canonical Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
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

/* global Cordova */

var exec = require('cordova/exec');
var argscheck = require('cordova/argscheck');
var GlobalizationError = require('./GlobalizationError');

function convertStringToDateOptions (override) {
    var options = { formatLength: 'short', selector: 'date and time' };

    if (override) {
        for (var key in options) {
            if (!options.hasOwnProperty(key)) { continue; }
            if (typeof (options[key]) !== typeof (override[key])) { continue; }
            options[key] = override[key];
        }
    }
    var formats = ['short', 'medium', 'long', 'full'];
    var selectors = ['date', 'time', 'date and time'];

    options.formatLength = formats.indexOf(options.formatLength);
    options.selector = selectors.indexOf(options.selector);
    // TODO: throw error
    if (options.formatLength === -1) { options.formatLength = 0; }
    if (options.selector === -1) { options.selector = 0; }

    return options;
}

function convertStringToNumberOptions (override) {
    var options = { type: 'decimal' };
    // TODO: make function
    if (override) {
        for (var key in options) {
            if (!options.hasOwnProperty(key)) { continue; }
            if (typeof (options[key]) !== typeof (override[key])) { continue; }
            options[key] = override[key];
        }
    }

    var types = [ 'decimal', 'percent', 'currency' ];
    options.type = types.indexOf(options.type);
    if (options.type === -1) { options.type = 0; }

    return options;
}

function isInt (n) {
    return n % 1 === 0;
}

module.exports = {
    isDayLightSavingsTime: function (date, successCB, failureCB) {
        argscheck.checkArgs('dfF', 'Globalization.isDayLightSavingsTime', arguments);

        exec(successCB, failureCB, 'Globalization', 'isDayLightSavingsTime', [ { time_t: date.getTime() } ]);
    },

    dateToString: function (date, successCB, failureCB, override) {
        argscheck.checkArgs('dfFO', 'Globalization.dateToString', arguments);

        var options = convertStringToDateOptions(override);
        exec(successCB, failureCB, 'Globalization', 'dateToString',
            [ { time_t: date.getTime(), formatLength: options.formatLength, selector: options.selector } ]);

    },

    stringToDate: function (dateString, successCB, failureCB, override) {
        argscheck.checkArgs('sfFO', 'Globalization.stringToDate', arguments);

        var options = convertStringToDateOptions(override);
        exec(successCB, failureCB, 'Globalization', 'stringToDate',
            [ { dateString: dateString, formatLength: options.formatLength, selector: options.selector } ]);
    },

    getDateNames: function (successCB, failureCB, override) {
        argscheck.checkArgs('fFO', 'Globalization.getDateNames', arguments);

        var options = { type: 'wide', item: 'months' };

        if (override) {
            for (var key in options) {
                if (!options.hasOwnProperty(key)) { continue; }
                if (typeof (options[key]) !== typeof (override[key])) { continue; }
                options[key] = override[key];
            }
        }

        var requests = ['days', 'months'];
        var formats = ['narrow', 'wide'];

        options.item = requests.indexOf(options.item);
        options.type = formats.indexOf(options.type);

        // TODO: throw error
        if (options.item === -1) { options.item = 0; }
        if (options.type === -1) { options.type = 0; }

        exec(successCB, failureCB, 'Globalization', 'getDateNames', [ options ]);
    },

    numberToString: function (number, successCB, failureCB, override) {
        argscheck.checkArgs('nfFO', 'Globalization.numberToString', arguments);

        var options = convertStringToNumberOptions(override);

        exec(successCB, failureCB, 'Globalization', 'numberToString',
            [ { type: options.type, isInt: isInt(number), number: number } ]);
    },

    stringToNumber: function (numberString, successCB, failureCB, override) {
        argscheck.checkArgs('sfFO', 'Globalization.stringToNumber', arguments);

        var options = convertStringToNumberOptions(override);
        exec(successCB, failureCB, 'Globalization', 'stringToNumber', [ options.type, numberString ]);
    },

    getDatePattern: function (successCB, failureCB, override) {
        argscheck.checkArgs('fFO', 'Globalization.getDatePattern', arguments);

        var options = convertStringToDateOptions(override);
        exec(successCB, failureCB, 'Globalization', 'getDatePattern', [ options.formatLength, options.selector ]);
    },

    getNumberPattern: function (successCB, failureCB, override) {
        argscheck.checkArgs('fFO', 'getNumberPattern', arguments);

        var options = convertStringToNumberOptions(override);
        Cordova.exec(successCB, failureCB, 'Globalization', 'getNumberPattern', [ options.type ]);
    },

    getCurrencyPattern: function (currencyCode, successCB, failureCB) {
        argscheck.checkArgs('sfF', 'Globalization.getCurrencyPattern', arguments);

        failureCB(new GlobalizationError(GlobalizationError.PATTERN_ERROR, 'unimplemented'));
        // exec(successCB, failureCB, "Globalization", "getCurrencyPattern", [{"currencyCode": currencyCode}]);
    }
};

require('cordova/exec/proxy').add('navigator.globalization', module.exports);
