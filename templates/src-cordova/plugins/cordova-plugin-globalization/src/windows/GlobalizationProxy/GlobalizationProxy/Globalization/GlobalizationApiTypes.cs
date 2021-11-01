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
using System.Runtime.Serialization;

namespace GlobalizationProxy.Globalization
{
    #region Globalization errors

    /// <summary>
    /// Globalization error codes.
    /// </summary>
    enum ErrorCode : int
    {
        UnknownError = 0,
        FormattingError = 1,
        ParsingError = 2,
        PatternError = 3
    }

    /// <summary>
    /// Represents globalization error object.
    /// </summary>
    [DataContract]
    class GlobalizationError
    {
        #region Error messages
        /// <summary>
        /// Error messages
        /// </summary>        
        public const string UnknownError = "UNKNOWN_ERROR";
        public const string FormattingError = "FORMATTIN_ERROR";
        public const string ParsingError = "PARSING_ERROR";
        public const string PatternError = "PATTERN_ERROR";

        #endregion

        /// <summary>
        /// Error code
        /// </summary>
        [DataMember(Name = "code", IsRequired = true)]
        public ErrorCode Code { get; set; }

        /// <summary>
        /// Error message
        /// </summary>
        [DataMember(Name = "message", IsRequired = true)]
        public string Message { get; set; }

        /// <summary>
        /// Default constructor
        /// </summary>
        public GlobalizationError()
        {
            this.Code = ErrorCode.UnknownError;
            this.Message = UnknownError;
        }

        /// <summary>
        /// Constructor setting error code
        /// </summary>
        public GlobalizationError(ErrorCode error)
        {
            this.Code = error;

            switch (error)
            {
                case ErrorCode.ParsingError:
                    {
                        this.Message = ParsingError;
                        break;
                    }
                case ErrorCode.FormattingError:
                    {
                        this.Message = FormattingError;
                        break;
                    }
                case ErrorCode.PatternError:
                    {
                        this.Message = PatternError;
                        break;
                    }
                default:
                    {
                        this.Message = UnknownError;
                        break;
                    }
            }
        }

        /// <summary>
        /// Constructor setting error code and message
        /// </summary>
        public GlobalizationError(ErrorCode code, string message)
        {
            this.Code = code;
            this.Message = message ?? String.Empty;
        }
    }

    #endregion

    #region Globalization options

    /// <summary>
    /// Represents globalization options.
    /// </summary>
    [DataContract]
    class GlobalizationOptions
    {
        #region available option values
        /// <summary>
        /// Number pattern types.
        /// </summary>        
        public const string Percent = "percent";
        public const string Currency = "currency";
        public const string Decimal = "decimal";

        /// <summary>
        /// Format length types
        /// </summary>        
        public const string Short = "short";
        public const string Medium = "medium";
        public const string Long = "long";
        public const string Full = "full";

        /// <summary>
        /// Selector types
        /// </summary>        
        public const string TimeSelector = "time";
        public const string DateSelector = "date";
        public const string DateAndTimeSelector = "date and time";

        /// <summary>
        /// Date name types
        /// </summary>        
        public const string Narrow = "narrow";
        public const string Wide = "wide";

        /// <summary>
        /// Date name items
        /// </summary>        
        public const string Months = "months";
        public const string Days = "days";

        #endregion

        /// <summary>
        /// Additional options
        /// </summary>
        [DataMember(Name = "options", IsRequired = false)]
        public Options AdditionalOptions { get; set; }

        /// <summary>
        /// Date to convert
        /// </summary>
        [DataMember(Name = "date", IsRequired = false)]
        public long Date { get; set; }

        /// <summary>
        /// Date as stirng
        /// </summary>
        [DataMember(Name = "dateString", IsRequired = false)]
        public string DateString { get; set; }

        /// <summary>
        /// Currency code
        /// </summary>
        [DataMember(Name = "currencyCode", IsRequired = false)]
        public string CurrencyCode { get; set; }

        /// <summary>
        /// Number as string
        /// </summary>
        [DataMember(Name = "numberString", IsRequired = false)]
        public string NumberString { get; set; }

        /// <summary>
        /// Number to convert
        /// </summary>
        [DataMember(Name = "number", IsRequired = false)]
        public double Number { get; set; }
    }

    /// <summary>
    /// Represents additional options
    /// </summary>
    [DataContract]
    class Options
    {
        /// <summary>
        /// Pattern type
        /// </summary>
        [DataMember(Name = "type", IsRequired = false)]
        public string Type { get; set; }

        /// <summary>
        /// Format length
        /// </summary>
        [DataMember(Name = "formatLength", IsRequired = false)]
        public string FormatLength { get; set; }

        /// <summary>
        /// Selector
        /// </summary>
        [DataMember(Name = "selector", IsRequired = false)]
        public string Selector { get; set; }

        /// <summary>
        /// Date name item
        /// </summary>
        [DataMember(Name = "item", IsRequired = false)]
        public string Item { get; set; }
    }

    #endregion

    #region Returned objects

    #region Number pattern object

    /// <summary>
    /// Represents number pattern
    /// </summary>
    [DataContract]
    class NumberPattern
    {
        /// <summary>
        /// Pattern
        /// </summary>
        [DataMember(Name = "pattern", IsRequired = false)]
        public string Pattern { get; set; }

        /// <summary>
        /// Symbol
        /// </summary>
        [DataMember(Name = "symbol", IsRequired = false)]
        public string Symbol { get; set; }

        /// <summary>
        /// Fraction
        /// </summary>
        [DataMember(Name = "fraction", IsRequired = false)]
        public int Fraction { get; set; }

        /// <summary>
        /// Positive
        /// </summary>
        [DataMember(Name = "positive", IsRequired = false)]
        public string Positive { get; set; }

        /// <summary>
        /// Negative
        /// </summary>
        [DataMember(Name = "negative", IsRequired = false)]
        public string Negative { get; set; }

        /// <summary>
        /// Rounding
        /// </summary>
        [DataMember(Name = "rounding", IsRequired = false)]
        public int Rounding { get; set; }

        /// <summary>
        /// Decimal
        /// </summary>
        [DataMember(Name = "decimal", IsRequired = false)]
        public string Decimal { get; set; }

        /// <summary>
        /// Grouping
        /// </summary>
        [DataMember(Name = "grouping", IsRequired = false)]
        public string Grouping { get; set; }

        /// <summary>
        /// Constructor of the class
        /// </summary>
        /// <param name="pattern"></param>
        /// <param name="symbol"></param>
        /// <param name="fraction"></param>
        /// <param name="positive"></param>
        /// <param name="negative"></param>
        /// <param name="rounding"></param>
        /// <param name="dec"></param>
        /// <param name="grouping"></param>
        public NumberPattern(string pattern, string symbol, int fraction, string positive, string negative, int rounding, string dec, string grouping)
        {
            this.Pattern = pattern;
            this.Symbol = symbol;
            this.Fraction = fraction;
            this.Positive = positive;
            this.Negative = negative;
            this.Rounding = rounding;
            this.Decimal = dec;
            this.Grouping = grouping;
        }
    }
    #endregion

    #region Date format object

    /// <summary>
    /// Represents date format
    /// </summary>
    [DataContract]
    class DateFormat
    {
        /// <summary>
        /// Year
        /// </summary>
        [DataMember(Name = "year", IsRequired = false)]
        public int Year { get; set; }

        /// <summary>
        /// Month
        /// </summary>
        [DataMember(Name = "month", IsRequired = false)]
        public int Month { get; set; }

        /// <summary>
        /// Day
        /// </summary>
        [DataMember(Name = "day", IsRequired = false)]
        public int Day { get; set; }

        /// <summary>
        /// Hour
        /// </summary>
        [DataMember(Name = "hour", IsRequired = false)]
        public int Hour { get; set; }

        /// <summary>
        /// Minute
        /// </summary>
        [DataMember(Name = "minute", IsRequired = false)]
        public int Minute { get; set; }

        /// <summary>
        /// Second
        /// </summary>
        [DataMember(Name = "second", IsRequired = false)]
        public int Second { get; set; }

        /// <summary>
        /// Millisecond
        /// </summary>
        [DataMember(Name = "millisecond", IsRequired = false)]
        public int Millisecond { get; set; }

        public DateFormat(int year, int month, int day, int hour, int minute, int second, int millisecond)
        {
            this.Year = year;
            this.Month = month;
            this.Day = day;
            this.Hour = hour;
            this.Minute = minute;
            this.Millisecond = millisecond;
        }

    }
    #endregion

    #region Date pattern object

    /// <summary>
    /// Represents date pattern object
    /// </summary>
    [DataContract]
    class DatePattern
    {

        /// <summary>
        /// Date pattern
        /// </summary>
        [DataMember(Name = "pattern", IsRequired = false)]
        public string Pattern { get; set; }

        /// <summary>
        /// TimeZone
        /// </summary>
        [DataMember(Name = "timezone", IsRequired = false)]
        public string TimeZone { get; set; }

        /// <summary>
        /// IANA TimeZone
        /// </summary>
        [DataMember(Name = "iana_timezone", IsRequired = false)]
        public string IanaTimeZone { get; set; }

        /// <summary>
        /// UTC offset
        /// </summary>
        [DataMember(Name = "utc_offset", IsRequired = false)]
        public double UtcOffset { get; set; }

        /// <summary>
        /// Dst offset
        /// </summary>
        [DataMember(Name = "dst_offset", IsRequired = false)]
        public double DstOffset { get; set; }

        /// <summary>
        /// Constructor of the class
        /// </summary>
        /// <param name="pattern"></param>
        /// <param name="timezone"></param>
        /// <param name="ianaTimezone"></param>
        /// <param name="utcOffset"></param>
        /// <param name="dstOffset"></param>
        public DatePattern(string pattern, string timezone, string ianaTimezone, double utcOffset, double dstOffset)
        {
            this.Pattern = pattern;
            this.TimeZone = timezone;
            this.IanaTimeZone = ianaTimezone;
            this.UtcOffset = utcOffset;
            this.DstOffset = dstOffset;
        }

    }

    #endregion

    #endregion
}
