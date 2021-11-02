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
using System.Collections.Generic;
using System.Runtime.Serialization;
using System.Threading;
using Microsoft.Devices.Sensors;
using System.Globalization;
using System.Diagnostics;
using System.Windows.Threading;

namespace WPCordovaClassLib.Cordova.Commands
{
    /// <summary>
    /// Captures device motion in the x, y, and z direction.
    /// </summary>
    public class Accelerometer : BaseCommand
    {
        #region Status codes and Constants

        public const int Stopped = 0;
        public const int Starting = 1;
        public const int Running = 2;
        public const int ErrorFailedToStart = 3;

        public const double gConstant = -9.81;

        #endregion

        #region Static members

        /// <summary>
        /// Status of listener
        /// </summary>
        private static int currentStatus;

        /// <summary>
        /// Accelerometer
        /// </summary>
        private static readonly Windows.Devices.Sensors.Accelerometer accelerometer = Windows.Devices.Sensors.Accelerometer.GetDefault();

        /// <summary>
        /// Timer which is used to update
        /// </summary>
        private static Timer updateTimer;

        /// <summary>
        /// Callback Id to report acceleration result in watch mode
        /// </summary>
        private static string watchCallbackId;
 
        #endregion

        /// <summary>
        /// Starts listening for acceleration sensor
        /// </summary>
        /// <returns>status of listener</returns>
        public void start(string options)
        {
            watchCallbackId = GetCallbackIdFromOptions(options);

            if (currentStatus == Running)
            {
                return;
            }

            try
            {
                // we use 20ms as a minimum allowed update interval
                int minReportInterval = Math.Max((int)accelerometer.MinimumReportInterval, 20);

                updateTimer = new Timer(ReportAccelerationValue, null, 0, minReportInterval);
                this.SetStatus(Running);

                PluginResult result = new PluginResult(PluginResult.Status.OK, GetCurrentAccelerationFormatted());
                result.KeepCallback = true;
                DispatchCommandResult(result, watchCallbackId);
            }
            catch (Exception ex)
            {
                this.SetStatus(ErrorFailedToStart);
                DispatchCommandResult(new PluginResult(PluginResult.Status.IO_EXCEPTION, ErrorFailedToStart), watchCallbackId);
            }
        }

        public void stop(string options)
        {
            string callbackId = GetCallbackIdFromOptions(options);

            if (currentStatus == Running)
            {
                watchCallbackId = null;
                updateTimer.Dispose();
                this.SetStatus(Stopped);
            }

            DispatchCommandResult(new PluginResult(PluginResult.Status.OK), callbackId);
        }

        public void getCurrentAcceleration(string options)
        {
            string callbackId = GetCallbackIdFromOptions(options);

            DispatchCommandResult(new PluginResult(PluginResult.Status.OK, GetCurrentAccelerationFormatted()), callbackId);
        }

        private void ReportAccelerationValue(object stateInfo)
        {
            if (String.IsNullOrEmpty(watchCallbackId)) {
                // soemthing goes wrong, callback has been called after stop..
                return;
            }
            string currentAccelerationFormatted = GetCurrentAccelerationFormatted();
            var result = currentAccelerationFormatted == null ? new PluginResult(PluginResult.Status.NO_RESULT)
                                                              : new PluginResult(PluginResult.Status.OK, currentAccelerationFormatted);
            result.KeepCallback = true;
            DispatchCommandResult(result, watchCallbackId);
        }

        /// <summary>
        /// Formats current coordinates into JSON format
        /// </summary>
        /// <returns>Coordinates in JSON format</returns>
        private string GetCurrentAccelerationFormatted()
        {
            try
            {
                var currentReading = accelerometer.GetCurrentReading();
                var currentCoordinates = String.Format("\"x\":{0},\"y\":{1},\"z\":{2}",
                                (currentReading.AccelerationX * gConstant).ToString("0.00000", CultureInfo.InvariantCulture),
                                (currentReading.AccelerationY * gConstant).ToString("0.00000", CultureInfo.InvariantCulture),
                                (currentReading.AccelerationZ * gConstant).ToString("0.00000", CultureInfo.InvariantCulture));

                return "{" + currentCoordinates + "}";
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// Sets current status
        /// </summary>
        /// <param name="status">current status</param>
        private void SetStatus(int status)
        {
            currentStatus = status;
        }

        private string GetCallbackIdFromOptions(string options)
        {
            try
            {
                string[] optionsString = JSON.JsonHelper.Deserialize<string[]>(options);

                return optionsString[0];
            }
            catch (Exception)
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.JSON_EXCEPTION), this.CurrentCommandCallbackId);
                return null;
            }
        }
    }
}
