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

using System;
using System.Globalization;
using System.Runtime.Serialization;

#if NETFX_CORE
// Windows

// Because WinRT' CurrentCulture does not take into account the locale (it falls back on application language)
// we are substituting it with a locale constructed from locale name passed from JS proxy.
using CultureInfo = GlobalizationProxy.Globalization.SettableCultureInfo;

using JsonHelper = GlobalizationProxy.Cordova.JSON.JsonHelper;
#else
using WPCordovaClassLib.Cordova.JSON;
#endif

namespace GlobalizationProxy.Globalization
{
    class GlobalizationImpl
    {
        public const string OPTS_DESERIALIZE_FAIL = "Could not deserialize options";

        // By default JSON serialization is performed using CurrentCulture but
        // float numbers need to be formatted in "en-US" culture to be deserialized in JavaScript.
        private const string JS_DEFAULT_LANG_TAG = "en-US";
        private static CultureInfo JS_DEFAULT_CULTURE = new CultureInfo(JS_DEFAULT_LANG_TAG);

        #region Locale info

        /// <summary>
        /// Gets the string identifier for the client's current locale setting.
        /// </summary>
        /// <param name="options"></param>               
        public static string getLocaleName(string options)
        {
            return WrapIntoJSON(CultureInfo.CurrentCulture.Name);
        }

        /// <summary>
        /// Gets the string identifier for the client's current language.
        /// </summary>
        /// <param name="options"></param>               
        public static string getPreferredLanguage(string options)
        {
            return WrapIntoJSON(CultureInfo.CurrentUICulture.Name);
        }

        #endregion Locale info

        #region Date and time info

        /// <summary>
        /// Gets whether daylight savings time is in effect for a given date using the client's 
        /// time zone and calendar.        
        /// </summary>
        /// <param name="opitons">Date to daylight savings check.</param>
        public static string isDayLightSavingsTime(string options)
        {
            var globalOptions = ReadOptions(options);
            if (globalOptions == null)
                throw new SerializationException(OPTS_DESERIALIZE_FAIL);

            var start = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
            var date = start.AddMilliseconds(globalOptions.Date).ToLocalTime();
            TimeZoneInfo localZone = TimeZoneInfo.Local;
            bool isDaylightSavingTime = localZone.IsDaylightSavingTime(date);

            return WrapIntoJSON(isDaylightSavingTime, "dst");
        }

        /// <summary>
        /// Gets the first day of the week according to the client's user preferences and calendar.
        /// The days of the week are numbered starting from 1 where 1 is considered to be Sunday.
        /// </summary>
        /// <param name="options"></param>
        public static string getFirstDayOfWeek(string options)
        {
            // DateTimeFormat returns days of the week numbered from zero, so we have to increase returned value by one.
            return WrapIntoJSON((int)CultureInfo.CurrentCulture.DateTimeFormat.FirstDayOfWeek + 1);
        }

        #endregion Date and time info

        #region Formatting

        /// <summary>
        /// Gets a date formatted as a string according to the client's user preferences and calendar using the time zone of the client. 
        /// </summary>
        /// <param name="options"></param>
        public static string dateToString(string options)
        {
            var globalOptions = ReadOptions(options);

            var start = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
            var date = start.AddMilliseconds(globalOptions.Date).ToLocalTime();

            string format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.FullDateTimePattern + "}"; //short datetime by default
            int formatLength = 0; //default format
            int selector = 0; //default selector 

            if (globalOptions.AdditionalOptions != null)
            {
                if (globalOptions.AdditionalOptions.FormatLength != null)
                {
                    string t = globalOptions.AdditionalOptions.FormatLength;

                    if (t.Equals(GlobalizationOptions.Full))
                    {
                        formatLength++;
                    }
                }

                if (globalOptions.AdditionalOptions.Selector != null)
                {
                    string t = globalOptions.AdditionalOptions.Selector;

                    if (t.Equals(GlobalizationOptions.DateSelector))
                    {
                        selector += 10;
                    }
                    else if (t.Equals(GlobalizationOptions.TimeSelector))
                    {
                        selector += 20;
                    }
                }

                //determine return value
                int method = formatLength + selector;

                switch (method)
                {
                    case 1: // full datetime
                        {
                            format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.FullDateTimePattern + "}";
                            break;
                        }
                    case 10: // short date
                        {
                            format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.ShortDatePattern + "}";
                            break;
                        }
                    case 11: // full date
                        {
                            format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.LongDatePattern + "}";
                            break;
                        }
                    case 20: // short time
                        {
                            format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.ShortTimePattern + "}";
                            break;
                        }
                    case 21: // full time
                        {
                            format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.LongTimePattern + "}";
                            break;
                        }
                    default: // short datetime
                        {
                            // Seems like C# doesn't support short datetime pattern so we use full format
                            // http://msdn.microsoft.com/en-us/library/1at0z4ew%28v=vs.71%29.aspx
                            format = "{0:" + CultureInfo.CurrentCulture.DateTimeFormat.FullDateTimePattern + "}";
                            break;
                        }
                }
            }

            string formattedValue = string.Format(CultureInfo.CurrentCulture, format, date);
            return WrapIntoJSON(formattedValue);
        }

        /// <summary>
        /// Parses a date formatted as a string according to the client's user preferences and calendar using the time zone of the client and returns the corresponding date object
        /// </summary>
        /// <param name="options"></param>
        public static DateFormat stringToDate(string options)
        {
            var globalOptions = ReadOptions(options);

            if (string.IsNullOrEmpty(globalOptions.DateString))
            {
                throw new SerializationException("DateString is empty");
            }

            string format = CultureInfo.CurrentCulture.DateTimeFormat.FullDateTimePattern; // short datetime by default
            int formatLength = 0; //default format
            int selector = 0; //default selector 

            if (globalOptions.AdditionalOptions != null)
            {
                if (globalOptions.AdditionalOptions.FormatLength != null)
                {
                    string t = globalOptions.AdditionalOptions.FormatLength;

                    if (t.Equals(GlobalizationOptions.Full))
                    {
                        formatLength++;
                    }
                }

                if (globalOptions.AdditionalOptions.Selector != null)
                {
                    string t = globalOptions.AdditionalOptions.Selector;

                    if (t.Equals(GlobalizationOptions.DateSelector))
                    {
                        selector += 10;
                    }
                    else if (t.Equals(GlobalizationOptions.TimeSelector))
                    {
                        selector += 20;
                    }
                }

                //determine return value
                int method = formatLength + selector;

                switch (method)
                {
                    case 1: // full datetime
                        {
                            format = CultureInfo.CurrentCulture.DateTimeFormat.FullDateTimePattern;
                            break;
                        }
                    case 10: // short date
                        {
                            format = CultureInfo.CurrentCulture.DateTimeFormat.ShortDatePattern;
                            break;
                        }
                    case 11: // full date
                        {
                            format = CultureInfo.CurrentCulture.DateTimeFormat.LongDatePattern;
                            break;
                        }
                    case 20: // short time
                        {
                            format = CultureInfo.CurrentCulture.DateTimeFormat.ShortTimePattern;
                            break;
                        }
                    case 21: // full time
                        {
                            format = CultureInfo.CurrentCulture.DateTimeFormat.LongTimePattern;
                            break;
                        }
                    default: // short datetime
                        {
                            // Seems like C# doesn't support short datetime pattern so we use full format
                            // http://msdn.microsoft.com/en-us/library/1at0z4ew%28v=vs.71%29.aspx
                            format = CultureInfo.CurrentCulture.DateTimeFormat.FullDateTimePattern;
                            break;
                        }
                }
            }

            DateTime date = DateTime.ParseExact(globalOptions.DateString, format, CultureInfo.CurrentCulture);
            return new DateFormat(date.Year, date.Month - 1, date.Day, date.Hour, date.Minute, date.Second, date.Millisecond);
        }

        /// <summary>
        /// Gets a pattern string for formatting and parsing dates according to the client's user preferences.
        /// </summary>
        /// <param name="options"></param>
        public static DatePattern getDatePattern(string options)
        {
            var globalOptions = ReadOptions(options);

            DateTimeFormatInfo dateFormatInfo = CultureInfo.CurrentCulture.DateTimeFormat;
            string pattern = dateFormatInfo.FullDateTimePattern; // full datetime by default
            int formatLength = 0; //default format
            int selector = 0; //default selector 

            if (globalOptions.AdditionalOptions != null)
            {
                if (globalOptions.AdditionalOptions.FormatLength != null)
                {
                    string t = globalOptions.AdditionalOptions.FormatLength;

                    if (t.Equals(GlobalizationOptions.Full))
                    {
                        formatLength++;
                    }
                }

                if (globalOptions.AdditionalOptions.Selector != null)
                {
                    string t = globalOptions.AdditionalOptions.Selector;

                    if (t.Equals(GlobalizationOptions.DateSelector))
                    {
                        selector += 10;
                    }
                    else if (t.Equals(GlobalizationOptions.TimeSelector))
                    {
                        selector += 20;
                    }
                }

                //determine return value
                int method = formatLength + selector;

                switch (method)
                {
                    case 1: // full datetime
                        {
                            pattern = dateFormatInfo.FullDateTimePattern;
                            break;
                        }
                    case 10: // short date
                        {
                            pattern = dateFormatInfo.ShortDatePattern;
                            break;
                        }
                    case 11: // full date
                        {
                            pattern = dateFormatInfo.LongDatePattern;
                            break;
                        }
                    case 20: // short time
                        {
                            pattern = dateFormatInfo.ShortTimePattern;
                            break;
                        }
                    case 21: // full time
                        {
                            pattern = dateFormatInfo.LongTimePattern;
                            break;
                        }
                    default: // short datetime
                        {
                            // Seems like C# doesn't support short datetime pattern so we use full format
                            // http://msdn.microsoft.com/en-us/library/1at0z4ew%28v=vs.71%29.aspx
                            pattern = dateFormatInfo.FullDateTimePattern;
                            break;
                        }
                }
            }

            TimeZoneInfo localZone = TimeZoneInfo.Local;
            return new DatePattern(pattern, localZone.DisplayName, String.Empty, localZone.BaseUtcOffset.TotalSeconds, 0);
        }

        /// <summary>
        /// Gets an array of either the names of the months or days of the week according to the client's user preferences and calendar.
        /// </summary>
        /// <param name="options"></param>
        public static string getDateNames(string options)
        {
            var globalOptions = ReadOptions(options);

            int type = 0; //default wide
            int item = 0; //default months 

            if (globalOptions.AdditionalOptions != null)
            {
                if (globalOptions.AdditionalOptions.Type != null)
                {
                    string t = globalOptions.AdditionalOptions.Type;

                    if (t.Equals(GlobalizationOptions.Narrow))
                    {
                        type++;
                    }
                }

                if (globalOptions.AdditionalOptions.Item != null)
                {
                    string t = globalOptions.AdditionalOptions.Item;

                    if (t.Equals(GlobalizationOptions.Days))
                    {
                        item += 10;
                    }
                }
            }

            //determine return value
            int method = item + type;
            string[] namesArray;
            CultureInfo currentCulture = CultureInfo.CurrentCulture;

            if (method == 1) //months and narrow
            {
                namesArray = currentCulture.DateTimeFormat.AbbreviatedMonthNames;
            }
            else if (method == 10) //days and wide
            {
                namesArray = currentCulture.DateTimeFormat.DayNames;
            }
            else if (method == 11) //days and narrow
            {
                namesArray = currentCulture.DateTimeFormat.AbbreviatedDayNames;
            }
            else //default: months and wide
            {
                namesArray = currentCulture.DateTimeFormat.MonthNames;
            }

            return WrapIntoJSON(namesArray);
        }

        /// <summary>
        /// Gets a number formatted as a string according to the client's user preferences. 
        /// </summary>
        /// <param name="options"></param>
        public static string numberToString(string options)
        {
            var globalOptions = ReadOptions(options);
           
            string format = string.Empty;
            string numberFormatType = (globalOptions.AdditionalOptions == null || string.IsNullOrEmpty(globalOptions.AdditionalOptions.Type)) ?
                GlobalizationOptions.Decimal : globalOptions.AdditionalOptions.Type;

            switch (numberFormatType)
            {
                case GlobalizationOptions.Percent:
                    {
                        format = "{0:p}";
                        break;
                    }

                case GlobalizationOptions.Currency:
                    {
                        format = "{0:c}";
                        break;
                    }

                default:
                    {
                        format = "{0:f}";
                        break;
                    }
            }

            string formattedValue = string.Format(CultureInfo.CurrentCulture, format, globalOptions.Number);
            return WrapIntoJSON(formattedValue);
        }

        /// <summary>
        /// Gets a number formatted as a string according to the client's user preferences and returns the corresponding number.
        /// </summary>
        /// <param name="options"></param>
        public static string stringToNumber(string options)
        {
            var globalOptions = ReadOptions(options);
           
            if (string.IsNullOrEmpty(globalOptions.NumberString))
            {
                throw new SerializationException("NumberString is empty");
            }

            string numberString = globalOptions.NumberString;
            string numberFormatType = (globalOptions.AdditionalOptions == null || string.IsNullOrEmpty(globalOptions.AdditionalOptions.Type)) ?
                GlobalizationOptions.Decimal : globalOptions.AdditionalOptions.Type;

            NumberStyles numberStyle;

            switch (numberFormatType)
            {
                case GlobalizationOptions.Percent:
                    {
                        numberStyle = NumberStyles.Any;
                        numberString = numberString.Replace(System.Globalization.CultureInfo.CurrentCulture.NumberFormat.PercentSymbol, "");
                        break;
                    }

                case GlobalizationOptions.Currency:
                    {
                        numberStyle = NumberStyles.Currency;
                        break;
                    }

                default:
                    {
                        numberStyle = NumberStyles.Number;
                        break;
                    }
            }

            double value = double.Parse(numberString, numberStyle, CultureInfo.CurrentCulture);

            // By default JSON serialization is performed using CurrentCulture but
            // float numbers need to be formatted in "en-US" culture to be deserialized in JavaScript.
            string stringifiedData = value.ToString(JS_DEFAULT_CULTURE);

            return WrapIntoJSON(value, stringifiedData: stringifiedData);
        }

        /// <summary>
        /// Gets a pattern string for formatting and parsing numbers according to the client's user preferences.
        /// </summary>
        /// <param name="options"></param>
        public static NumberPattern getNumberPattern(string options)
        {
            var globalOptions = ReadOptions(options);
           
            CultureInfo cultureInfo = CultureInfo.CurrentCulture;
            NumberFormatInfo formatInfo = cultureInfo.NumberFormat;
            string numberFormatType = (globalOptions.AdditionalOptions == null || string.IsNullOrEmpty(globalOptions.AdditionalOptions.Type)) ?
                GlobalizationOptions.Decimal : globalOptions.AdditionalOptions.Type;
            NumberPattern pattern = null;
            string symbol;

            // TODO find out how to get format pattern and the number of fraction digits
            switch (numberFormatType)
            {
                case GlobalizationOptions.Percent:
                    {
                        symbol = formatInfo.PercentSymbol;
                        pattern = new NumberPattern("", symbol, 0, formatInfo.PercentPositivePattern.ToString(), formatInfo.NegativeSign, 0, formatInfo.PercentDecimalSeparator, formatInfo.PercentGroupSeparator);
                        break;
                    }
                case GlobalizationOptions.Currency:
                    {
                        symbol = formatInfo.CurrencySymbol;
                        pattern = new NumberPattern("", symbol, 0, formatInfo.CurrencyPositivePattern.ToString(), formatInfo.NegativeSign, 0, formatInfo.CurrencyDecimalSeparator, formatInfo.CurrencyGroupSeparator);
                        break;
                    }
                default:
                    {
                        symbol = formatInfo.NumberDecimalSeparator;
                        pattern = new NumberPattern("", symbol, 0, "", formatInfo.NegativeSign, 0, formatInfo.NumberDecimalSeparator, formatInfo.NumberGroupSeparator);
                        break;
                    }
            }

            return pattern;
        }

        /// <summary>
        /// Gets a pattern string for formatting and parsing currency values according to the client's user preferences and ISO 4217 currency code.
        /// </summary>
        /// <param name="options"></param>
        public static string getCurrencyPattern(string options)
        {
            var globalOptions = ReadOptions(options);
                       
            if (string.IsNullOrEmpty(globalOptions.CurrencyCode))
            {
                throw new SerializationException("CurrencyCode is empty");
            }

            // TODO find the way to get currency info from currency code
            // http://stackoverflow.com/questions/12373800/3-digit-currency-code-to-currency-symbol
            // http://stackoverflow.com/questions/6924067/how-to-get-specific-culture-currency-pattern
            // CultureInfo cultureInfo = new CultureInfo(currencyCode);
            // NumberFormatInfo numberFormat = cultureInfo.NumberFormat;

            // temporary not supported via lack of api required
            throw new NotImplementedException("Not supported");
        }

        #endregion Formatting

        private static GlobalizationOptions ReadOptions(string options)
        {
            GlobalizationOptions globalOptions;
            try
            {
                globalOptions = JsonHelper.Deserialize<GlobalizationOptions>(options);
            }
            catch (Exception)
            {
                throw new SerializationException(OPTS_DESERIALIZE_FAIL);
            }
            return globalOptions;
        }

        /// <summary>
        /// Wraps data into JSON format
        /// </summary>
        /// <param name="data">data</param>
        /// <returns>data formatted as JSON object</returns>
        static string WrapIntoJSON<T>(T data, string keyName = "value", string stringifiedData = null)
        {
            string param = "{0}";
            stringifiedData = stringifiedData ?? data.ToString();

            if (data.GetType() == typeof(string))
            {
                param = "\"" + param + "\"";
            }

            if (data.GetType() == typeof(bool))
            {
                stringifiedData = stringifiedData.ToLower();
            }

            if (data.GetType() == typeof(string[]))
            {
                stringifiedData = JsonHelper.Serialize(data);
            }

            var formattedData = string.Format("\"" + keyName + "\":" + param, stringifiedData);
            formattedData = "{" + formattedData + "}";

            return formattedData;
        }
    }
}
