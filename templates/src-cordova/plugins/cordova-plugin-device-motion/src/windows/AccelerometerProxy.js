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

/*global Windows:true */

var Acceleration = require('cordova-plugin-device-motion.Acceleration');

/* This is the actual implementation part that returns the result on Windows 8
*/
var gConstant = -9.81;

module.exports = {
    onDataChanged:null,
    start:function(win,lose){

        var accel = Windows.Devices.Sensors.Accelerometer.getDefault();
        if(!accel) {
            if (lose) {
                lose("No accelerometer found");
            }
        }
        else {
            accel.reportInterval = Math.max(16,accel.minimumReportInterval);

            // store our bound function
            this.onDataChanged = function(e) {
                var a = e.reading;
                win(new Acceleration(a.accelerationX * gConstant, a.accelerationY * gConstant, a.accelerationZ * gConstant), {keepCallback: true});
            };
            accel.addEventListener("readingchanged",this.onDataChanged);

            setTimeout(function(){
                var a = accel.getCurrentReading();
                win(new Acceleration(a.accelerationX * gConstant, a.accelerationY * gConstant, a.accelerationZ * gConstant), {keepCallback: true});
            },0); // async do later
        }
    },
    stop:function(win,lose){
        win = win || function(){};
        var accel = Windows.Devices.Sensors.Accelerometer.getDefault();
        if(!accel) {
            if (lose) {
                lose("No accelerometer found");
            }
        }
        else {
            accel.removeEventListener("readingchanged",this.onDataChanged);
            this.onDataChanged = null;
            accel.reportInterval = 0; // back to the default
            win();
        }
    }
};

require("cordova/exec/proxy").add("Accelerometer",module.exports);
