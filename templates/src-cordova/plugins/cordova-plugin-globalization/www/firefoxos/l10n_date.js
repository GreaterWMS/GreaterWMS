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
 * This lib relies on `l10n.js' to implement localizable date/time strings.
 *
 * The proposed `DateTimeFormat' object should provide all the features that are
 * planned for the `Intl.DateTimeFormat' constructor, but the API does not match
 * exactly the ES-i18n draft.
 *   - https://bugzilla.mozilla.org/show_bug.cgi?id=769872
 *   - http://wiki.ecmascript.org/doku.php?id=globalization:specification_drafts
 *
 * Besides, this `DateTimeFormat' object provides two features that aren't
 * planned in the ES-i18n spec:
 *   - a `toLocaleFormat()' that really works (i.e. fully translated);
 *   - a `fromNow()' method to handle relative dates ("pretty dates").
 *
 * WARNING: this library relies on the non-standard `toLocaleFormat()' method,
 * which is specific to Firefox -- no other browser is supported.
 */

navigator.mozL10n.DateTimeFormat = function (locales, options) {
    'use strict';

    var _ = navigator.mozL10n.get;

    // https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Date/toLocaleFormat
    function localeFormat (d, format) {
        var tokens = format.match(/(%E.|%O.|%.)/g);

        for (var i = 0; tokens && i < tokens.length; i++) {
            var value = '';

            // http://pubs.opengroup.org/onlinepubs/007908799/xsh/strftime.html
            switch (tokens[i]) {
            // localized day/month names
            case '%a':
                value = _('weekday-' + d.getDay() + '-short');
                break;
            case '%A':
                value = _('weekday-' + d.getDay() + '-long');
                break;
            case '%b':
            case '%h':
                value = _('month-' + d.getMonth() + '-short');
                break;
            case '%B':
                value = _('month-' + d.getMonth() + '-long');
                break;
            case '%Eb':
                value = _('month-' + d.getMonth() + '-genitive');
                break;

            // like %H, but in 12-hour format and without any leading zero
            case '%I':
                value = d.getHours() % 12 || 12;
                break;

            // like %d, without any leading zero
            case '%e':
                value = d.getDate();
                break;

            // %p: 12 hours format (AM/PM)
            case '%p':
                value = d.getHours() < 12 ? _('time_am') : _('time_pm');
                break;

            // localized date/time strings
            case '%c':
            case '%x':
            case '%X':
            // ensure the localized format string doesn't contain any %c|%x|%X
                var tmp = _('dateTimeFormat_' + tokens[i]);
                if (tmp && !(/(%c|%x|%X)/).test(tmp)) {
                    value = localeFormat(d, tmp);
                }
                break;

            // other tokens don't require any localization
            }

            format = format.replace(tokens[i], value || d.toLocaleFormat(tokens[i]));
        }

        return format;
    }

    /**
    * Returns the parts of a number of seconds
    */
    function relativeParts (seconds) {
        seconds = Math.abs(seconds);
        var descriptors = {};
        var units = [
            'years', 86400 * 365,
            'months', 86400 * 30,
            'weeks', 86400 * 7,
            'days', 86400,
            'hours', 3600,
            'minutes', 60
        ];

        if (seconds < 60) {
            return {
                minutes: Math.round(seconds / 60)
            };
        }

        for (var i = 0, uLen = units.length; i < uLen; i += 2) {
            var value = units[i + 1];
            if (seconds >= value) {
                descriptors[units[i]] = Math.floor(seconds / value);
                seconds -= descriptors[units[i]] * value;
            }
        }
        return descriptors;
    }

    /**
    * Returns a translated string which respresents the
    * relative time before or after a date.
    * @param {String|Date} time before/after the currentDate.
    * @param {String} useCompactFormat whether to use a compact display format.
    * @param {Number} maxDiff returns a formatted date if the diff is greater.
    */
    function prettyDate (time, useCompactFormat, maxDiff) {
        maxDiff = maxDiff || 86400 * 10; // default = 10 days

        switch (time.constructor) {
        case String: // timestamp
            time = parseInt(time);
            break;
        case Date:
            time = time.getTime();
            break;
        }

        var secDiff = (Date.now() - time) / 1000;
        if (isNaN(secDiff)) {
            return _('incorrectDate');
        }

        if (Math.abs(secDiff) > 60) {
            // round milliseconds up if difference is over 1 minute so the result is
            // closer to what the user would expect (1h59m59s300ms diff should return
            // "in 2 hours" instead of "in an hour")
            secDiff = secDiff > 0 ? Math.ceil(secDiff) : Math.floor(secDiff);
        }

        if (secDiff > maxDiff) {
            return localeFormat(new Date(time), '%x');
        }

        var f = useCompactFormat ? '-short' : '-long';
        var parts = relativeParts(secDiff);

        var affix = secDiff >= 0 ? '-ago' : '-until';
        for (var i in parts) {
            return _(i + affix + f, { value: parts[i] });
        }
    }

    // API
    return {
        localeDateString: function localeDateString (d) {
            return localeFormat(d, '%x');
        },
        localeTimeString: function localeTimeString (d) {
            return localeFormat(d, '%X');
        },
        localeString: function localeString (d) {
            return localeFormat(d, '%c');
        },
        localeFormat: localeFormat,
        fromNow: prettyDate,
        relativeParts: relativeParts
    };
};
