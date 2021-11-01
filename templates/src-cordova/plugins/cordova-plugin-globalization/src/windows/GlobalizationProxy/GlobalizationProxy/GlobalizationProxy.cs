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
using GlobalizationProxy.Cordova.JSON;
using GlobalizationProxy.Globalization;

namespace GlobalizationProxy
{
    public sealed class GlobalizationProxy
    {
        public static void SetLocale(string name)
        {
            SettableCultureInfo.SubstituteCurrentLocale(name);
        }

        private static string Invoke<T>(Func<string, T> action, string options, 
            ErrorCode expectedErrorCode = ErrorCode.UnknownError)
        {
            object result;
            try
            {
                result = action(options);
            }
            catch (SerializationException ex)
            {
                result = new GlobalizationError(ErrorCode.UnknownError, ex.Message);
            }
            catch (Exception ex)
            {
                // Using a method' specific expected error code here
                result = new GlobalizationError(expectedErrorCode, ex.Message);
            }

            string resultJSON = result as string;
            if (resultJSON != null)
            {
                return resultJSON;
            }

            // This is either a DataContract type or a GlobalizationError
            return JsonHelper.Serialize(result);
        }

        public static string getLocaleName(string options)
        {
            return Invoke(GlobalizationImpl.getLocaleName, options);
        }
        
        public static string isDayLightSavingsTime(string options)
        {
            return Invoke(GlobalizationImpl.isDayLightSavingsTime, options);
        }

        public static string getFirstDayOfWeek(string options)
        {
            return Invoke(GlobalizationImpl.getFirstDayOfWeek, options);
        }

        public static string dateToString(string options)
        {
            return Invoke(GlobalizationImpl.dateToString, options, ErrorCode.FormattingError);
        }

        public static string stringToDate(string options)
        {
            return Invoke(GlobalizationImpl.stringToDate, options, ErrorCode.ParsingError);
        }

        public static string getDateNames(string options)
        {
            return Invoke(GlobalizationImpl.getDateNames, options);
        }

        public static string numberToString(string options)
        {
            return Invoke(GlobalizationImpl.numberToString, options, ErrorCode.FormattingError);
        }

        public static string stringToNumber(string options)
        {
            return Invoke(GlobalizationImpl.stringToNumber, options, ErrorCode.ParsingError);
        }

        public static string getDatePattern(string options)
        {
            return Invoke(GlobalizationImpl.getDatePattern, options, ErrorCode.PatternError);
        }

        public static string getNumberPattern(string options)
        {
            return Invoke(GlobalizationImpl.getNumberPattern, options, ErrorCode.PatternError);
        }
    }
}