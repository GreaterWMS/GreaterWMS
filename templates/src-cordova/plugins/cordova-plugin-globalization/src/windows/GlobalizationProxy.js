/*
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

/* global Windows, GlobalizationProxy */

var GlobalizationError = require('./GlobalizationError');
var locale = navigator.userLanguage || navigator.language;

var decimalFormatter;
var currencyFormatter;
var percentFormatter;

function createRoundingAlgorithm () {
    // This is undefined in case of Windows 8.0
    if (Windows.Globalization.NumberFormatting.IncrementNumberRounder) {
        var rounder = new Windows.Globalization.NumberFormatting.IncrementNumberRounder();
        rounder.roundingAlgorithm = Windows.Globalization.NumberFormatting.RoundingAlgorithm.roundHalfUp;
        rounder.increment = 0.01;

        return rounder;
    }

    return null;
}

function createDecimalFormatter (regionName) {
    decimalFormatter = new Windows.Globalization.NumberFormatting.DecimalFormatter([locale], regionName);

    decimalFormatter.numberRounder = createRoundingAlgorithm();
    decimalFormatter.isGrouped = false;

    return decimalFormatter;
}

function getDecimalFormatter (regionName) {
    return decimalFormatter || createDecimalFormatter(regionName);
}

function createCurrencyFormatter (regionName) {
    var regionObj = new Windows.Globalization.GeographicRegion(regionName);
    var currency = regionObj.currenciesInUse[0];

    currencyFormatter = new Windows.Globalization.NumberFormatting.CurrencyFormatter(currency, [locale], regionName);

    currencyFormatter.numberRounder = createRoundingAlgorithm();
    currencyFormatter.isGrouped = true;

    return currencyFormatter;
}

function getCurrencyFormatter (regionName) {
    return currencyFormatter || createCurrencyFormatter(regionName);
}

function createPercentFormatter (regionName) {
    percentFormatter = new Windows.Globalization.NumberFormatting.PercentFormatter([locale], regionName);

    percentFormatter.numberRounder = createRoundingAlgorithm();
    percentFormatter.fractionDigits = 0;
    percentFormatter.isGrouped = false;

    return percentFormatter;
}

function getPercentFormatter (regionName) {
    return percentFormatter || createPercentFormatter(regionName);
}

function getNumberFormatter (options) {
    options = options || { type: 'decimal' };
    options.type = options.type || 'decimal';

    var tags = locale.split('-');
    var regionName = tags[tags.length - 1];

    switch (options.type) {
    case 'decimal':
    {
        return getDecimalFormatter(regionName);
    }
    case 'currency':
    {
        return getCurrencyFormatter(regionName);
    }
    case 'percent':
    {
        return getPercentFormatter(regionName);
    }
    default:
        throw "The options.type can be 'decimal', 'percent', or 'currency' only";
    }
}

module.exports = {
    getPreferredLanguage: function (win, fail) {
        try {
            var language = Windows.System.UserProfile.GlobalizationPreferences.languages[0];

            win({ value: language });
        } catch (e) {
            fail(e);
        }
    },

    getLocaleName: function (win, fail) {
        // Corresponds to a user-selected regional format
        win({ value: locale });
    },

    dateToString: function (win, fail, args) {
        tryDoAction(GlobalizationProxy.GlobalizationProxy.dateToString,
            JSON.stringify({
                date: args[0].date,
                options: args[0].options || { formatLength: 'short', selector: 'date and time' }
            }), win, fail);
    },

    stringToDate: function (win, fail, args) {
        tryDoAction(GlobalizationProxy.GlobalizationProxy.stringToDate,
            JSON.stringify({
                dateString: args[0].dateString,
                options: args[0].options || { formatLength: 'short', selector: 'date and time' }
            }), win, fail);
    },

    getDateNames: function (win, fail, args) {
        try {
            var options = args[0].options || { type: 'wide', item: 'months' };
            var type = options.type || 'wide';
            var item = options.item || 'months';

            var monthFormat = Windows.Globalization.DateTimeFormatting.MonthFormat.none;
            var dayOfWeekFormat = Windows.Globalization.DateTimeFormatting.DayOfWeekFormat.none;

            if (item === 'months' && type === 'wide') {
                monthFormat = Windows.Globalization.DateTimeFormatting.MonthFormat.full;
            } else if (item === 'months' && type === 'narrow') {
                monthFormat = Windows.Globalization.DateTimeFormatting.MonthFormat.abbreviated;
            } else if (item === 'days' && type === 'wide') {
                dayOfWeekFormat = Windows.Globalization.DateTimeFormatting.DayOfWeekFormat.full;
            } else if (item === 'days' && type === 'narrow') {
                dayOfWeekFormat = Windows.Globalization.DateTimeFormatting.DayOfWeekFormat.abbreviated;
            } else {
                throw 'Incorrect item type';
            }

            var formatter = new Windows.Globalization.DateTimeFormatting.DateTimeFormatter(
                Windows.Globalization.DateTimeFormatting.YearFormat.none,
                monthFormat,
                Windows.Globalization.DateTimeFormatting.DayFormat.none,
                dayOfWeekFormat,
                Windows.Globalization.DateTimeFormatting.HourFormat.none,
                Windows.Globalization.DateTimeFormatting.MinuteFormat.none,
                Windows.Globalization.DateTimeFormatting.SecondFormat.none,
                [locale]);

            var result = [];
            var i;
            var date;
            if (item === 'months') {
                for (i = 0; i < 12; i++) {
                    date = new Date(2014, i, 20, 0, 0, 0, 0);
                    result[i] = formatter.format(date);
                }
            } else {
                for (i = 0; i < 7; i++) {
                    date = new Date(2014, 5, i + 1, 0, 0, 0, 0);
                    result[i] = formatter.format(date);
                }
            }

            win({ value: result });
        } catch (e) {
            fail(new GlobalizationError(0, e));
        }
    },

    isDayLightSavingsTime: function (win, fail, args) {
        tryDoAction(GlobalizationProxy.GlobalizationProxy.isDayLightSavingsTime,
            JSON.stringify({
                date: args[0].date
            }), win, fail);
    },

    getFirstDayOfWeek: function (win, fail) {
        win({ value: Windows.System.UserProfile.GlobalizationPreferences.weekStartsOn + 1 });
    },

    numberToString: function (win, fail, args) {
        try {
            var formatter = getNumberFormatter(args[0].options);
            var formattedNumber = formatter.format(args[0].number);
            if (!formattedNumber) {
                throw 'Unknown error';
            }

            win({ value: formattedNumber });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.FORMATTING_ERROR, e));
        }
    },

    stringToNumber: function (win, fail, args) {
        try {
            var formatter = getNumberFormatter(args[0].options);
            var number = formatter.parseDouble(args[0].numberString);
            if (!number) {
                throw 'Input string was in incorrect format';
            }

            win({ value: number });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.PARSING_ERROR, e));
        }
    },

    getDatePattern: function (win, fail, args) {
        tryDoAction(GlobalizationProxy.GlobalizationProxy.getDatePattern,
            JSON.stringify({
                options: args[0].options
            }), win, fail);
    },

    getNumberPattern: function (win, fail, args) {
        try {
            var result = GlobalizationProxy.GlobalizationProxy.getNumberPattern(JSON.stringify({
                options: args[0].options
            }));

            var obj = JSON.parse(result);
            checkForGlobalizationError(obj);

            var formatter = getNumberFormatter(args[0].options);
            obj.fraction = formatter.fractionDigits;

            win(obj);
        } catch (e) {
            fail(e);
        }
    },

    getCurrencyPattern: function (win, fail, args) {
        try {
            var tags = locale.split('-');
            var regionName = tags[tags.length - 1];
            var currency = args[0].currencyCode;
            var formatter = new Windows.Globalization.NumberFormatting.CurrencyFormatter(
                currency, [locale], regionName);

            win({
                fraction: formatter.fractionDigits,
                code: formatter.currency,

                // unsupported
                decimal: '',
                grouping: '',
                pattern: '',
                rounding: 0
            });
        } catch (e) {
            fail(new GlobalizationError(GlobalizationError.PATTERN_ERROR, e));
        }
    }
};

function tryDoAction (action, args, win, fail) {
    try {
        var result = action(args);
        var obj = JSON.parse(result);
        checkForGlobalizationError(obj);
        win(obj);
    } catch (e) {
        fail(e);
    }
}

function checkForGlobalizationError (obj) {
    if (obj && 'code' in obj && 'message' in obj) {
        throw new GlobalizationError(obj.code, obj.message);
    }
}

(function init () {
    GlobalizationProxy.GlobalizationProxy.setLocale(locale);
})();

require('cordova/exec/proxy').add('Globalization', module.exports);
