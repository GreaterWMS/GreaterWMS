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
using WPCordovaClassLib.Cordova.JSON;
using GlobalizationProxy.Globalization;

namespace WPCordovaClassLib.Cordova.Commands
{
    class Globalization : BaseCommand
    {
        private void Invoke<T>(Func<string, T> action, string options,
            ErrorCode expectedErrorCode = ErrorCode.UnknownError)
        {
            object result;
            try
            {
                result = action(ExtractGlobalizationOptions(options));
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

            if (result is GlobalizationError)
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, result));
            }
            else
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.OK, result));
            }
        }

        /// <summary>
        /// This is needed as globalization.js interface calls wp8 plugin like this:
        /// exec(successCB, failureCB, "Globalization", "stringToNumber", [{"numberString": numberString, "options": options}]);
        /// i.e. arguments are serialized twice - in an object and in an array, 
        /// but GlobalizationImpl takes just GlobalizationOptions object serialized
        /// </summary>
        /// <param name="options"></param>
        /// <returns></returns>
        private string ExtractGlobalizationOptions(string options)
        {
            try
            {
                string[] args = JsonHelper.Deserialize<string[]>(options);

                return args[0];
            }
            catch (Exception)
            {
                throw new SerializationException(GlobalizationImpl.OPTS_DESERIALIZE_FAIL);
            }
        }

        public void getLocaleName(string options)
        {
            Invoke(GlobalizationImpl.getLocaleName, options);
        }

        public void getPreferredLanguage(string options)
        {
            Invoke(GlobalizationImpl.getPreferredLanguage, options);
        }

        public void isDayLightSavingsTime(string options)
        {
            Invoke(GlobalizationImpl.isDayLightSavingsTime, options);
        }

        public void getFirstDayOfWeek(string options)
        {
            Invoke(GlobalizationImpl.getFirstDayOfWeek, options);
        }

        public void dateToString(string options)
        {
            Invoke(GlobalizationImpl.dateToString, options, ErrorCode.FormattingError);
        }

        public void stringToDate(string options)
        {
            Invoke(GlobalizationImpl.stringToDate, options, ErrorCode.ParsingError);
        }

        public void getDateNames(string options)
        {
            Invoke(GlobalizationImpl.getDateNames, options);
        }

        public void numberToString(string options)
        {
            Invoke(GlobalizationImpl.numberToString, options, ErrorCode.FormattingError);
        }

        public void stringToNumber(string options)
        {
            Invoke(GlobalizationImpl.stringToNumber, options, ErrorCode.ParsingError);
        }

        public void getDatePattern(string options)
        {
            Invoke(GlobalizationImpl.getDatePattern, options, ErrorCode.PatternError);
        }

        public void getNumberPattern(string options)
        {
            Invoke(GlobalizationImpl.getNumberPattern, options, ErrorCode.PatternError);
        }

        public void getCurrencyPattern(string options)
        {            
            this.DispatchCommandResult(new PluginResult(PluginResult.Status.INVALID_ACTION, "Not supported"));
        }
    }
}
