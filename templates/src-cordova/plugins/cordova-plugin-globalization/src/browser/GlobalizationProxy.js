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
var moment = require('cordova-plugin-globalization.moment');

function getCrossPlatformLocale () {
    // userLanguage is for IE, which corresponds to selected regional format
    return navigator.userLanguage || navigator.language;
}

function stdTimezoneOffset (date) {
    var jan = new Date(date.getFullYear(), 0, 20);
    var jul = new Date(date.getFullYear(), 6, 20);
    return Math.max(jan.getTimezoneOffset(), jul.getTimezoneOffset());
}

function dst (date) {
    return date.getTimezoneOffset() < stdTimezoneOffset(date);
}

function dstOffsetAbs (date) {
    var janOffset = new Date(date.getFullYear(), 0, 20).getTimezoneOffset();
    var julOffset = new Date(date.getFullYear(), 6, 20).getTimezoneOffset();
    if (janOffset < 0) { janOffset = -janOffset; }
    if (julOffset < 0) { julOffset = -julOffset; }
    var offset = janOffset - julOffset;
    if (offset < 0) { offset = -offset; }
    return offset;
}

function getWeekDayNames (locale, options) {
    var result = [];
    var date;
    for (var i = 0; i < 7; i++) {
        date = new Date(2014, 5, i + 1, 0, 0, 0, 0);
        result[i] = date.toLocaleDateString(locale, options);
    }
    return result;
}

function convertToIntlNumberFormatOptions (options) {
    switch (options.type) {
    case 'decimal':
        return { style: 'decimal' };
    case 'currency':
        throw '\'currency\' number type is not supported';
    case 'percent':
        return { style: 'percent' };
    default:
        throw 'The options.type can be \'decimal\', \'percent\' or \'currency\'';
    }
}

function convertToMomentLocalizedFormat (options) {
    var selectorError = 'The options.selector can be \'date\', \'time\' or \'date and time\'';
    var formatLengthError = 'The options.formatLength can be \'short\', \'medium\', \'long\', or \'full\'';
    /* eslint-disable no-unreachable */
    switch (options.formatLength) {
    case 'short':
        switch (options.selector) {
        case 'date and time': return 'lll';
        case 'date': return 'l';
        case 'time': return 'LT';
        default:
            throw selectorError;
        }
        break;
    case 'medium':
        switch (options.selector) {
        case 'date and time': return 'LLL';
        case 'date': return 'L';
        case 'time':
            throw '\'time\' selector does not support \'medium\' formatLength';
        default:
            throw selectorError;
        }
        break;
    case 'long':
        switch (options.selector) {
        case 'date and time': return 'llll';
        case 'date': return 'll';
        case 'time':
            throw '\'time\' selector does not support \'long\' formatLength';
        default:
            throw selectorError;
        }
        break;
    case 'full':
        switch (options.selector) {
        case 'date and time': return 'LLLL';
        case 'date': return 'LL';
        case 'time': return 'LTS';
        default:
            throw selectorError;
        }
        break;
    default:
        throw formatLengthError;
    }
}
/* eslint-enable no-unreachable */
function prepareAndGetDateOptions (options) {
    options = options || {formatLength: 'short', selector: 'date and time'};
    options.formatLength = options.formatLength || 'short';
    options.selector = options.selector || 'date and time';

    return convertToMomentLocalizedFormat(options);
}

var globalization = {
    getLocaleName: function (win, fail) {
        try {
            win({ value: getCrossPlatformLocale() });
        } catch (e) {
            fail({ code: 0, message: e.hasOwnProperty('message') ? e.message : e });
        }
    },

    numberToString: function (win, fail, args) {
        try {
            var options = args[0].options || { type: 'decimal' };
            options.type = options.type || 'decimal';

            options = convertToIntlNumberFormatOptions(options);

            var formatter = new Intl.NumberFormat(getCrossPlatformLocale(), options);
            win({ value: formatter.format(args[0].number) });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.FORMATTING_ERROR,
                e.hasOwnProperty('message') ? e.message : e));
        }
    },

    isDayLightSavingsTime: function (win, fail, args) {
        try {
            var date = new Date(args[0].date);
            win({ dst: dst(date) });
        } catch (e) {
            fail({ code: 0, message: e.hasOwnProperty('message') ? e.message : e });
        }
    },

    getFirstDayOfWeek: function (win, fail) {
        try {
            var locale = getCrossPlatformLocale();
            moment.locale(locale);
            // Converting ISO format (Monday = 1, Sunday = 7) to what Cordova expects (Sunday = 1, Monday = 2, Saturday = 7)
            var shiftDay = moment().weekday(0).isoWeekday() + 1;
            win({ value: shiftDay % 8 + Math.floor(shiftDay / 8) });
        } catch (e) {
            fail({ code: 0, message: e.hasOwnProperty('message') ? e.message : e });
        }
    },

    getDateNames: function (win, fail, args) {
        try {
            var options = args[0].options || { type: 'wide', item: 'months' };
            var type = options.type || 'wide';
            var item = options.item || 'item';

            var locale = getCrossPlatformLocale();

            if (item === 'months' && type === 'wide') {
                options = { month: 'long' };
            } else if (item === 'months' && type === 'narrow') {
                options = { month: 'short' };
            } else if (item === 'days' && type === 'wide') {
                options = { weekday: 'long' };
            } else if (item === 'days' && type === 'narrow') {
                options = { weekday: 'short' };
            } else {
                throw 'Incorrect type or item';
            }

            var result = [];
            if (item === 'months') {
                for (var i = 0; i < 12; i++) {
                    var date = new Date(2014, i, 20, 0, 0, 0, 0);
                    result[i] = date.toLocaleDateString(locale, options);
                }
            } else {
                result = getWeekDayNames(locale, options);
            }

            win({ value: result });
        } catch (e) {
            fail({ code: 0, message: e.hasOwnProperty('message') ? e.message : e });
        }
    },

    getDatePattern: function (win, fail) {
        try {
            var formatter = new Intl.DateTimeFormat(getCrossPlatformLocale());
            var timezone = formatter.hasOwnProperty('resolved') ? formatter.resolved.timeZone : '';
            var dstOffset = dstOffsetAbs(new Date());

            win({
                utc_offset: new Date().getTimezoneOffset() * (-60),
                dst_offset: dstOffset * 60,
                timezone: timezone,
                pattern: ''
            });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.PATTERN_ERROR,
                e.hasOwnProperty('message') ? e.message : e));
        }
    },

    getNumberPattern: function (win, fail, args) {
        try {
            var options = args[0].options || { type: 'decimal' };
            options.type = options.type || 'decimal';

            options = convertToIntlNumberFormatOptions(options);

            var formatter = new Intl.NumberFormat(getCrossPlatformLocale(), options);

            if (!formatter.hasOwnProperty('resolved')) {
                fail('Not supported');
                return;
            }
            var pattern = formatter.resolved.pattern;
            win({
                pattern: pattern,
                symbol: '',
                fraction: 0,
                rounding: 0,
                positive: '',
                negative: '',
                decimal: '',
                grouping: ''
            });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.PATTERN_ERROR,
                e.hasOwnProperty('message') ? e.message : e));
        }
    },

    getPreferredLanguage: function (win, fail, args) {
        // Falling back on locale
        globalization.getLocaleName(win, fail);
    },

    getCurrencyPattern: function (win, fail, args) {
        fail('Not supported');
    },

    stringToDate: function (win, fail, args) {
        try {
            var options = prepareAndGetDateOptions(args[0].options);
            moment.locale(getCrossPlatformLocale());

            var date = moment(args[0].dateString, options).toDate();

            win({
                year: date.getFullYear(),
                month: date.getMonth(),
                day: date.getDate(),
                hour: date.getHours(),
                minute: date.getMinutes(),
                second: date.getSeconds(),
                millisecond: date.getMilliseconds()
            });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.PARSING_ERROR,
                e.hasOwnProperty('message') ? e.message : e));
        }
    },

    stringToNumber: function (win, fail, args) {
        fail('Not supported');
    },

    dateToString: function (win, fail, args) {
        try {
            var date = new Date(args[0].date);
            var options = prepareAndGetDateOptions(args[0].options);
            moment.locale(getCrossPlatformLocale());

            win({ value: moment(date).format(options) });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.FORMATTING_ERROR,
                e.hasOwnProperty('message') ? e.message : e));
        }
    }
};

module.exports = globalization;

require('cordova/exec/proxy').add('Globalization', module.exports);
