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
/* global cordova, GlobalizationError */

exports.defineAutoTests = function () {
    var isWindowsPhone = cordova.platformId === 'windowsphone';
    var isWindows = (cordova.platformId === 'windows') || (cordova.platformId === 'windows8');
    var isBrowser = cordova.platformId === 'browser';

    var fail = function (done) {
        expect(true).toBe(false);
        done();
    };

    describe('Globalization (navigator.globalization)', function () {

        it('globalization.spec.1 should exist', function () {
            expect(navigator.globalization).toBeDefined();
        });

        describe('getPreferredLanguage', function () {
            var checkPreferredLanguage = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.value).toBeDefined();
                expect(typeof a.value).toBe('string');
                expect(a.value.length > 0).toBe(true);
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.getPreferredLanguage).toBeDefined();
                expect(typeof navigator.globalization.getPreferredLanguage === 'function').toBe(true);
            });
            it('globalization.spec.3 getPreferredLanguage success callback should be called with a Properties object', function (done) {
                navigator.globalization.getPreferredLanguage(function (a) {
                    checkPreferredLanguage(a);
                    done();
                },
                fail.bind(null, done));
            });
            it('globalization.spec.4 getPreferredLanguage return string should contain one or more language subtags separated by hyphen', function (done) {
                navigator.globalization.getPreferredLanguage(function (a) {
                    checkPreferredLanguage(a);
                    expect(a.value.indexOf('_')).toBe(-1);

                    // A language tag is composed from a sequence of one or more "subtags", separated by hyphen.
                    // https://tools.ietf.org/html/bcp47#section-2.1
                    expect(a.value.split('-').length).toBeGreaterThan(0);

                    done();
                }, fail.bind(null, done));
            });
        });

        describe('getLocaleName', function () {
            var checkLocaleName = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.value).toBeDefined();
                expect(typeof a.value).toBe('string');
                expect(a.value.length > 0).toBe(true);
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.getLocaleName).toBeDefined();
                expect(typeof navigator.globalization.getLocaleName === 'function').toBe(true);
            });
            it('globalization.spec.3 getLocaleName success callback should be called with a Properties object', function (done) {
                navigator.globalization.getLocaleName(function (a) {
                    checkLocaleName(a);
                    done();
                }, fail.bind(null, done));
            });
            it('globalization.spec.4 getLocaleName return string should have a hyphen', function (done) {
                navigator.globalization.getLocaleName(function (a) {
                    checkLocaleName(a);
                    expect(a.value.indexOf('_')).toBe(-1);
                    if (!isBrowser) {
                        // The browser implementation returns non-BCP 47 compatible
                        // value in Chrome so we need to skip this expectation. See
                        // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-1
                        expect(a.value.indexOf('-')).toBeGreaterThan(0);
                    }
                    done();
                }, fail.bind(null, done));
            });
        });

        describe('Globalization Constants (window.Globalization)', function () {
            it('globalization.spec.1 should exist', function () {
                expect(window.GlobalizationError).toBeDefined();
                expect(window.GlobalizationError.UNKNOWN_ERROR).toBe(0);
                expect(window.GlobalizationError.FORMATTING_ERROR).toBe(1);
                expect(window.GlobalizationError.PARSING_ERROR).toBe(2);
                expect(window.GlobalizationError.PATTERN_ERROR).toBe(3);
            });
        });

        describe('dateToString', function () {
            var checkDateToString = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.value).toBeDefined();
                expect(typeof a.value).toBe('string');
                expect(a.value.length > 0).toBe(true);
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.dateToString).toBeDefined();
                expect(typeof navigator.globalization.dateToString === 'function').toBe(true);
            });
            it('globalization.spec.5 dateToString using default options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.dateToString(new Date(), function (a) {
                    checkDateToString(a);
                    done();
                }, fail.bind(null, done));
            });
            it('globalization.spec.6 dateToString using formatLength=short and selector=date options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.dateToString(new Date(), function (a) {
                    checkDateToString(a);
                    done();
                }, fail.bind(null, done),
                { formatLength: 'short', selector: 'date' });
            });
            it('globalization.spec.7 dateToString using formatLength=full and selector=date options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.dateToString(new Date(), function (a) {
                    checkDateToString(a);
                    done();
                }, fail.bind(null, done),
                { formatLength: 'full', selector: 'date' });
            });
            it('globalization.spec.8 dateToString using formatLength=medium and selector=date and time(default) options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.dateToString(new Date(), function (a) {
                    checkDateToString(a);
                    done();
                }, fail.bind(null, done),
                { formatLength: 'medium' });
            });
            it('globalization.spec.9 dateToString using formatLength=long and selector=date and time(default) options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.dateToString(new Date(), function (a) {
                    checkDateToString(a);
                    done();
                }, fail.bind(null, done),
                { formatLength: 'long' });
            });
            it('globalization.spec.10 dateToString using formatLength=full and selector=date and time(default) options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.dateToString(new Date(), function (a) {
                    checkDateToString(a);
                    done();
                }, fail.bind(null, done),
                { formatLength: 'full' });
            });
        });

        describe('stringToDate', function () {
            var checkStringToDate = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.year).toBeDefined();
                expect(typeof a.year).toBe('number');
                expect(a.year >= 0 && a.year <= 9999).toBe(true);
                expect(a.month).toBeDefined();
                expect(typeof a.month).toBe('number');
                expect(a.month >= 0 && a.month <= 11).toBe(true);
                expect(a.day).toBeDefined();
                expect(typeof a.day).toBe('number');
                expect(a.day >= 1 && a.day <= 31).toBe(true);
                expect(a.hour).toBeDefined();
                expect(typeof a.hour).toBe('number');
                expect(a.hour >= 0 && a.hour <= 23).toBe(true);
                expect(a.minute).toBeDefined();
                expect(typeof a.minute).toBe('number');
                expect(a.minute >= 0 && a.minute <= 59).toBe(true);
                expect(a.second).toBeDefined();
                expect(typeof a.second).toBe('number');
                expect(a.second >= 0 && a.second <= 59).toBe(true);
                expect(a.millisecond).toBeDefined();
                expect(typeof a.millisecond).toBe('number');
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.stringToDate).toBeDefined();
                expect(typeof navigator.globalization.stringToDate === 'function').toBe(true);
            });
            it('globalization.spec.12 stringToDate using default options, success callback should be called with a Properties object', function (done) {
                var win = function (a) {
                    checkStringToDate(a);
                    done();
                };

                navigator.globalization.dateToString(new Date(), function (a) {
                    navigator.globalization.stringToDate(a.value, win, fail.bind(null, done));
                }, fail.bind(null, done));
            });
            it('globalization.spec.13 stringToDate using formatLength=short and selector=date options, success callback should be called with a Properties object', function (done) {
                var win = function (a) {
                    checkStringToDate(a);
                    done();
                };

                navigator.globalization.dateToString(new Date(), function (a) {
                    navigator.globalization.stringToDate(a.value, win, fail.bind(null, done), { formatLength: 'short', selector: 'date' });
                }, fail.bind(null, done), { formatLength: 'short', selector: 'date' });
            });
            it('globalization.spec.14 stringToDate using formatLength=full and selector=date options, success callback should be called with a Properties object', function (done) {
                var win = function (a) {
                    checkStringToDate(a);
                    done();
                };

                navigator.globalization.dateToString(new Date(), function (a) {
                    navigator.globalization.stringToDate(a.value, win, fail.bind(null, done), { formatLength: 'full', selector: 'date' });
                }, fail.bind(null, done), { formatLength: 'full', selector: 'date' });
            });
            it('globalization.spec.15 stringToDate using invalid date, error callback should be called with a GlobalizationError object', function (done) {
                navigator.globalization.stringToDate('notADate', fail.bind(null, done), function (a) {
                    expect(a).toBeDefined();
                    expect(typeof a).toBe('object');
                    expect(a.code).toBeDefined();
                    expect(typeof a.code).toBe('number');
                    expect(a.code === GlobalizationError.PARSING_ERROR).toBe(true);
                    expect(a.message).toBeDefined();
                    expect(typeof a.message).toBe('string');
                    expect(a.message !== '').toBe(true);
                    done();
                }, { selector: 'foobar' });
            });
        });

        describe('getDatePattern', function () {
            var checkDatePattern = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.pattern).toBeDefined();
                expect(typeof a.pattern).toBe('string');
                if (!isBrowser) {
                    // In browser the 'pattern' property is not supported and returns empty string.
                    // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-4
                    expect(a.pattern.length > 0).toBe(true);
                }
                expect(a.timezone).toBeDefined();
                expect(typeof a.timezone).toBe('string');
                if (!isBrowser) {
                    // The browser platform partially supports 'timezone'. Only Chrome returns 'timezone' property.
                    // Its format is "Part of the world/{City}". Other browsers return empty string.
                    // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-4
                    expect(a.timezone.length > 0).toBe(true);
                }
                if (!isBrowser && !isWindowsPhone) {
                    expect(a.iana_timezone).toBeDefined();
                    expect(typeof a.iana_timezone).toBe('string');
                    // Windows doesn't support IANA timezone and always returns an empty string instead
                    if (!isWindows) {
                        expect(a.iana_timezone.length > 0).toBe(true);
                    }
                }
                expect(a.utc_offset).toBeDefined();
                expect(typeof a.utc_offset).toBe('number');
                expect(a.dst_offset).toBeDefined();
                expect(typeof a.dst_offset).toBe('number');
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.getDatePattern).toBeDefined();
                expect(typeof navigator.globalization.getDatePattern === 'function').toBe(true);
            });
            it('globalization.spec.17 getDatePattern using default options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDatePattern(function (a) {
                    checkDatePattern(a);
                    done();
                }, fail.bind(null, done));
            });
            it('globalization.spec.18 getDatePattern using formatLength=medium and selector=date options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDatePattern(function (a) {
                    checkDatePattern(a);
                    done();
                }, fail.bind(null, done),
                { formatLength: 'medium', selector: 'date' });
            });
        });

        describe('getDateNames', function () {
            var checkDateNames = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.value).toBeDefined();
                expect(a.value instanceof Array).toBe(true);
                expect(a.value.length > 0).toBe(true);
                expect(typeof a.value[0]).toBe('string');
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.getDateNames).toBeDefined();
                expect(typeof navigator.globalization.getDateNames === 'function').toBe(true);
            });
            it('globalization.spec.20 getDateNames using default options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDateNames(function (a) {
                    checkDateNames(a);
                    done();
                }, fail.bind(null, done));
            });
            it('globalization.spec.21 getDateNames using type=narrow and item=days options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDateNames(function (a) {
                    checkDateNames(a);
                    done();
                }, fail.bind(null, done),
                { type: 'narrow', item: 'days' });
            });
            it('globalization.spec.22 getDateNames using type=narrow and item=months options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDateNames(function (a) {
                    checkDateNames(a);
                    done();
                }, fail.bind(null, done),
                { type: 'narrow', item: 'months' });
            });
            it('globalization.spec.23 getDateNames using type=wide and item=days options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDateNames(function (a) {
                    checkDateNames(a);
                    done();
                }, fail.bind(null, done),
                { type: 'wide', item: 'days' });
            });
            it('globalization.spec.24 getDateNames using type=wide and item=months options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.getDateNames(function (a) {
                    checkDateNames(a);
                    done();
                }, fail.bind(null, done),
                { type: 'wide', item: 'months' });
            });
        });

        describe('isDayLightSavingsTime', function () {
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.isDayLightSavingsTime).toBeDefined();
                expect(typeof navigator.globalization.isDayLightSavingsTime === 'function').toBe(true);
            });
            it('globalization.spec.26 isDayLightSavingsTime using default options, success callback should be called with a Properties object', function (done) {
                navigator.globalization.isDayLightSavingsTime(new Date(), function (a) {
                    expect(a).toBeDefined();
                    expect(typeof a).toBe('object');
                    expect(a.dst).toBeDefined();
                    expect(typeof a.dst).toBe('boolean');
                    done();
                }, fail.bind(null, done));
            });
        });

        describe('getFirstDayOfWeek', function () {
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.getFirstDayOfWeek).toBeDefined();
                expect(typeof navigator.globalization.getFirstDayOfWeek === 'function').toBe(true);
            });
            it('globalization.spec.28 getFirstDayOfWeek success callback should be called with a Properties object', function (done) {
                navigator.globalization.getFirstDayOfWeek(function (a) {
                    expect(a).toBeDefined();
                    expect(typeof a).toBe('object');
                    expect(a.value).toBeDefined();
                    expect(typeof a.value).toBe('number');
                    done();
                }, fail.bind(null, done));
            });
        });

        describe('numberToString', function () {
            var checkNumberToString = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.value).toBeDefined();
                expect(typeof a.value).toBe('string');
                expect(a.value.length > 0).toBe(true);
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.numberToString).toBeDefined();
                expect(typeof navigator.globalization.numberToString === 'function').toBe(true);
            });
            it('globalization.spec.30 numberToString using default options, should be called with a Properties object', function (done) {
                navigator.globalization.numberToString(3.25, function (a) {
                    checkNumberToString(a);
                    done();
                }, fail.bind(null, done));
            });
            it('globalization.spec.31 numberToString using type=percent options, should be called with a Properties object', function (done) {
                navigator.globalization.numberToString(0.25, function (a) {
                    checkNumberToString(a);
                    done();
                }, fail.bind(null, done),
                { type: 'percent' });
            });
            it('globalization.spec.32 numberToString using type=currency options, should be called with a Properties object', function (done) {
                // the numberToString using type=currency is not supported on browser
                // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-7
                if (isBrowser) {
                    pending();
                }
                navigator.globalization.numberToString(5.20, function (a) {
                    checkNumberToString(a);
                    done();
                }, fail.bind(null, done),
                { type: 'currency' });
            });
        });

        describe('stringToNumber', function () {
            var checkStringToNumber = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.value).toBeDefined();
                expect(typeof a.value).toBe('number');
                expect(a.value > 0).toBe(true);
            };
            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.stringToNumber).toBeDefined();
                expect(typeof navigator.globalization.stringToNumber === 'function').toBe(true);
            });
            it('globalization.spec.34 stringToNumber using default options, should be called with a Properties object', function (done) {
                // the stringToNumber is not supported on browser
                // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#supported-platforms-11
                if (isBrowser) {
                    pending();
                }
                var win = function (a) {
                    checkStringToNumber(a);
                    done();
                };

                navigator.globalization.numberToString(3.25, function (a) {
                    navigator.globalization.stringToNumber(a.value, win, fail.bind(null, done));
                }, fail.bind(null, done));
            });
            it('globalization.spec.35 stringToNumber using type=percent options, should be called with a Properties object', function (done) {
                // the stringToNumber is not supported on browser
                // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#supported-platforms-11
                if (isBrowser) {
                    pending();
                }
                var win = function (a) {
                    checkStringToNumber(a);
                    done();
                };

                navigator.globalization.numberToString(0.25, function (a) {
                    navigator.globalization.stringToNumber(a.value, win, fail.bind(null, done), { type: 'percent' });
                }, fail.bind(null, done), { type: 'percent' });
            });
        });

        describe('getNumberPattern', function () {
            var checkNumberPattern = function (a) {
                expect(a).toBeDefined();
                expect(typeof a).toBe('object');
                expect(a.pattern).toBeDefined();
                expect(typeof a.pattern).toBe('string');
                expect(a.pattern.length > 0).toBe(true);
                expect(typeof a.symbol).toBe('string');
                expect(typeof a.fraction).toBe('number');
                expect(typeof a.rounding).toBe('number');
                expect(a.positive).toBeDefined();
                expect(typeof a.positive).toBe('string');
                expect(a.positive.length >= 0).toBe(true);
                expect(a.negative).toBeDefined();
                expect(typeof a.negative).toBe('string');
                expect(a.negative.length >= 0).toBe(true);
                expect(a.decimal).toBeDefined();
                expect(typeof a.decimal).toBe('string');
                expect(a.decimal.length > 0).toBe(true);
                expect(a.grouping).toBeDefined();
                expect(typeof a.grouping).toBe('string');
                expect(a.grouping.length > 0).toBe(true);
            };

            it('globalization.spec.1 should exist', function () {
                expect(typeof navigator.globalization.getNumberPattern).toBeDefined();
                expect(typeof navigator.globalization.getNumberPattern === 'function').toBe(true);
            });
            it('globalization.spec.37 getNumberPattern using default options, success callback should be called with a Properties object', function (done) {
                // the pattern property is not supported on windows, windows phone and browser
                // https://github.com/apache/cordova-plugin-globalization/blob/master/doc/index.md#windows-phone-8-quirks-5
                // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-6
                if (isWindows || isWindowsPhone || isBrowser) {
                    pending();
                }
                navigator.globalization.getNumberPattern(function (a) {
                    checkNumberPattern(a);
                    done();
                }, fail.bind(null, done));
            });
            it('globalization.spec.38 getNumberPattern using type=percent, success callback should be called with a Properties object', function (done) {
                // the pattern property is not supported on windows, windows phone and browser
                // https://github.com/apache/cordova-plugin-globalization/blob/master/doc/index.md#windows-phone-8-quirks-5
                // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-6
                if (isWindows || isWindowsPhone || isBrowser) {
                    pending();
                }
                navigator.globalization.getNumberPattern(function (a) {
                    checkNumberPattern(a);
                    done();
                }, fail.bind(null, done), { type: 'percent' });
            });
            it('globalization.spec.39 getNumberPattern using type=currency, success callback should be called with a Properties object', function (done) {
                // the pattern property is not supported on windows, windows phone and browser
                // https://github.com/apache/cordova-plugin-globalization/blob/master/doc/index.md#windows-phone-8-quirks-5
                // https://github.com/apache/cordova-plugin-globalization/blob/21f8a0ffa5aa2497ee970b6b5092b4c65fc4bf7e/README.md#browser-quirks-6
                if (isWindows || isWindowsPhone || isBrowser) {
                    pending();
                }
                navigator.globalization.getNumberPattern(function (a) {
                    checkNumberPattern(a);
                    done();
                }, fail.bind(null, done), { type: 'currency' });
            });
        });

        describe('getCurrencyPattern', function () {
            it('globalization.spec.1 should exist', function () {
                // wp8 is unsupported
                if (isWindowsPhone) {
                    pending();
                }
                expect(typeof navigator.globalization.getCurrencyPattern).toBeDefined();
                expect(typeof navigator.globalization.getCurrencyPattern === 'function').toBe(true);
            });
            it('globalization.spec.41 getCurrencyPattern using EUR for currency, success callback should be called with a Properties object', function (done) {
                // only `code` and `fraction` properties are supported on windows
                // https://github.com/apache/cordova-plugin-globalization/blob/master/doc/index.md#windows-quirks-3
                // wp8 and browser are unsupported
                if (isWindowsPhone || isWindows || isBrowser) {
                    pending();
                }
                navigator.globalization.getCurrencyPattern('EUR', function (a) {
                    expect(a).toBeDefined();
                    expect(typeof a).toBe('object');
                    expect(a.pattern).toBeDefined();
                    expect(typeof a.pattern).toBe('string');
                    expect(a.pattern.length > 0).toBe(true);
                    expect(a.code).toBeDefined();
                    expect(typeof a.code).toBe('string');
                    expect(a.code.length > 0).toBe(true);
                    expect(typeof a.fraction).toBe('number');
                    expect(typeof a.rounding).toBe('number');
                    expect(a.decimal).toBeDefined();
                    expect(typeof a.decimal).toBe('string');
                    expect(a.decimal.length >= 0).toBe(true);
                    expect(a.grouping).toBeDefined();
                    expect(typeof a.grouping).toBe('string');
                    expect(a.grouping.length >= 0).toBe(true);
                    done();
                }, fail.bind(null, done));
            });
        });
    });
};
