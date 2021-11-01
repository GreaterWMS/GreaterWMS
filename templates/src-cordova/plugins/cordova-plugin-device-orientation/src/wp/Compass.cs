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
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;
using DeviceCompass = Microsoft.Devices.Sensors.Compass;
using System.Windows.Threading;
using System.Runtime.Serialization;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.Threading;
using Microsoft.Devices.Sensors;

namespace WPCordovaClassLib.Cordova.Commands
{

    public class Compass : BaseCommand
    {
        #region Static members

        /// <summary>
        /// Status of listener
        /// </summary>
        private static int currentStatus;

        /// <summary>
        /// Id for get getCompass method
        /// </summary>
        private static string getCompassId = "getCompassId";

        /// <summary>
        /// Compass
        /// </summary>
        private static DeviceCompass compass = new DeviceCompass();

        /// <summary>
        /// Listeners for callbacks
        /// </summary>
        private static Dictionary<string, Compass> watchers = new Dictionary<string, Compass>();

        #endregion

        #region Status codes

        public const int Stopped = 0;
        public const int Starting = 1;
        public const int Running = 2;
        public const int ErrorFailedToStart = 4;
        public const int Not_Supported = 20;

        /*
         *   // Capture error codes
            CompassError.COMPASS_INTERNAL_ERR = 0;
            CompassError.COMPASS_NOT_SUPPORTED = 20;
         * */

        #endregion

        #region CompassOptions class
        /// <summary>
        /// Represents Accelerometer options.
        /// </summary>
        [DataContract]
        public class CompassOptions
        {
            /// <summary>
            /// How often to retrieve the Acceleration in milliseconds
            /// </summary>
            [DataMember(IsRequired = false, Name = "frequency")]
            public int Frequency { get; set; }

            /// <summary>
            /// The change in degrees required to initiate a watchHeadingFilter success callback.
            /// </summary>
            [DataMember(IsRequired = false, Name = "filter")]
            public int Filter { get; set; }

            /// <summary>
            /// Watcher id
            /// </summary>
            [DataMember(IsRequired = false, Name = "id")]
            public string Id { get; set; }

        }
        #endregion


        /// <summary>
        /// Time the value was last changed
        /// </summary>
        //private DateTime lastValueChangedTime;

        /// <summary>
        /// Accelerometer options
        /// </summary>
        private CompassOptions compassOptions;

        //bool isDataValid;

        //bool calibrating = false;

        public Compass()
        {

        }

        /// <summary>
        /// Formats current coordinates into JSON format
        /// </summary>
        /// <returns>Coordinates in JSON format</returns>
        private string GetHeadingFormatted(CompassReading reading)
        {   
            // NOTE: timestamp is generated on the JS side, to avoid issues with format conversions
            string result = String.Format("\"magneticHeading\":{0},\"headingAccuracy\":{1},\"trueHeading\":{2}",
                            reading.MagneticHeading.ToString("0.0", CultureInfo.InvariantCulture),
                            reading.HeadingAccuracy.ToString("0.0", CultureInfo.InvariantCulture),
                            reading.TrueHeading.ToString("0.0", CultureInfo.InvariantCulture));
            return "{" + result + "}";
        }

        public void getHeading(string options)
        {
            if (!DeviceCompass.IsSupported)
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, Not_Supported));
            }
            else
            {
                //if (compass == null)
                //{
                //    // Instantiate the compass.
                //    compass = new DeviceCompass();
                //    compass.TimeBetweenUpdates = TimeSpan.FromMilliseconds(40);
                //    compass.CurrentValueChanged += new EventHandler<Microsoft.Devices.Sensors.SensorReadingEventArgs<Microsoft.Devices.Sensors.CompassReading>>(compass_CurrentValueChanged);
                //    compass.Calibrate += new EventHandler<Microsoft.Devices.Sensors.CalibrationEventArgs>(compass_Calibrate);
                //}


                //compass.Start();

            }

            try
            {
                if (currentStatus != Running)
                {
                    lock (compass)
                    {
                        compass.CurrentValueChanged += compass_SingleHeadingValueChanged;
                        compass.Start();
                        this.SetStatus(Starting);
                    }

                    long timeout = 2000;
                    while ((currentStatus == Starting) && (timeout > 0))
                    {
                        timeout = timeout - 100;
                        Thread.Sleep(100);
                    }

                    if (currentStatus != Running)
                    {
                        DispatchCommandResult(new PluginResult(PluginResult.Status.IO_EXCEPTION, ErrorFailedToStart));
                        return;
                    }
                }
                lock (compass)
                {
                    compass.CurrentValueChanged -= compass_SingleHeadingValueChanged;
                    if (watchers.Count < 1)
                    {
                        compass.Stop();
                        this.SetStatus(Stopped);
                    }
                }
            }
            catch (UnauthorizedAccessException)
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.ILLEGAL_ACCESS_EXCEPTION, ErrorFailedToStart));
            }
            catch (Exception)
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, ErrorFailedToStart));
            }
        }

        void compass_SingleHeadingValueChanged(object sender, Microsoft.Devices.Sensors.SensorReadingEventArgs<CompassReading> e)
        {
            this.SetStatus(Running);
            if (compass.IsDataValid)
            {
                // trueHeading :: The heading in degrees from 0 - 359.99 at a single moment in time.
                //  magneticHeading:: The heading relative to the geographic North Pole in degrees 0 - 359.99 at a single moment in time. 
                //  A negative value indicates that the true heading could not be determined.
                // headingAccuracy :: The deviation in degrees between the reported heading and the true heading.
                //rawMagnetometerReading = e.SensorReading.MagnetometerReading;

                //Debug.WriteLine("Compass Result :: " + GetHeadingFormatted(e.SensorReading));

                PluginResult result = new PluginResult(PluginResult.Status.OK, GetHeadingFormatted(e.SensorReading));

                DispatchCommandResult(result);
            }
        }

        /// <summary>
        /// Starts listening for compass sensor
        /// </summary>
        /// <returns>status of listener</returns>
        private int start()
        {
            if ((currentStatus == Running) || (currentStatus == Starting))
            {
                return currentStatus;
            }
            try
            {
                lock (compass)
                {
                    watchers.Add(getCompassId, this);
                    compass.CurrentValueChanged += watchers[getCompassId].compass_CurrentValueChanged;
                    compass.Start();
                    this.SetStatus(Starting);
                }
            }
            catch (Exception)
            {
                this.SetStatus(ErrorFailedToStart);
            }
            return currentStatus;
        }

        public void startWatch(string options)
        {
            if (!DeviceCompass.IsSupported)
            {
                DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, Not_Supported));
            }

            try
            {
                compassOptions = JSON.JsonHelper.Deserialize<CompassOptions>(options);
            }
            catch (Exception ex)
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.JSON_EXCEPTION, ex.Message));
                return;
            }

            if (string.IsNullOrEmpty(compassOptions.Id))
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.JSON_EXCEPTION));
                return;
            }

            try
            {
                lock (compass)
                {
                    watchers.Add(compassOptions.Id, this);
                    compass.CurrentValueChanged += watchers[compassOptions.Id].compass_CurrentValueChanged;
                    compass.Start();
                    this.SetStatus(Starting);
                }
            }
            catch (Exception)
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.ERROR, ErrorFailedToStart));
                return;
            }
        }

        public void stopWatch(string options)
        {
            try
            {
                compassOptions = JSON.JsonHelper.Deserialize<CompassOptions>(options);
            }
            catch (Exception ex)
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.JSON_EXCEPTION, ex.Message));
                return;
            }

            if (string.IsNullOrEmpty(compassOptions.Id))
            {
                this.DispatchCommandResult(new PluginResult(PluginResult.Status.JSON_EXCEPTION));
                return;
            }

            if (currentStatus != Stopped)
            {
                lock (compass)
                {
                    Compass watcher = watchers[compassOptions.Id];
                    compass.CurrentValueChanged -= watcher.compass_CurrentValueChanged;
                    watchers.Remove(compassOptions.Id);
                    watcher.Dispose();
                }
            }
            this.SetStatus(Stopped);

            this.DispatchCommandResult();
        }

        void compass_Calibrate(object sender, Microsoft.Devices.Sensors.CalibrationEventArgs e)
        {
            //throw new NotImplementedException();
            // TODO: pass calibration error to JS
        }

        void compass_CurrentValueChanged(object sender, Microsoft.Devices.Sensors.SensorReadingEventArgs<CompassReading> e)
        {
            this.SetStatus(Running);
            if (compass.IsDataValid)
            {
                // trueHeading :: The heading in degrees from 0 - 359.99 at a single moment in time.
                //  magneticHeading:: The heading relative to the geographic North Pole in degrees 0 - 359.99 at a single moment in time. 
                //  A negative value indicates that the true heading could not be determined.
                // headingAccuracy :: The deviation in degrees between the reported heading and the true heading.
                //rawMagnetometerReading = e.SensorReading.MagnetometerReading;

                //Debug.WriteLine("Compass Result :: " + GetHeadingFormatted(e.SensorReading));

                PluginResult result = new PluginResult(PluginResult.Status.OK, GetHeadingFormatted(e.SensorReading));
                result.KeepCallback = true;

                DispatchCommandResult(result);
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

    }
}
