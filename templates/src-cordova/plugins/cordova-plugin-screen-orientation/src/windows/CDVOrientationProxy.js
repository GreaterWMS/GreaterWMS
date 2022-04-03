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

var DisplayInfo = Windows.Graphics.Display.DisplayInformation;
var Orientations = Windows.Graphics.Display.DisplayOrientations;

if (!window.Promise) {
    window.Promise = WinJS.Promise;
}

module.exports = {
    screenOrientation: function (win, fail, args) {
        //console.log("screenOrientation proxy called with " + args);

        try {
            var prefOrients = args[0];
            var winPrefs = 0;

            if (prefOrients & 1) { // UIInterfaceOrientationPortrait
                winPrefs = winPrefs |  Orientations.portrait;
            }
            if (prefOrients & 2) { // UIInterfaceOrientationPortraitUpsideDown
                winPrefs = winPrefs | Orientations.portraitFlipped;
            }
            if(prefOrients & 4) { // UIInterfaceOrientationLandscapeLeft
                winPrefs = winPrefs | Orientations.landscape;
            }
            if (prefOrients & 8) { // UIInterfaceOrientationLandscapeRight
                winPrefs = winPrefs | Orientations.landscapeFlipped;
            }
            setTimeout(function () {
                DisplayInfo.autoRotationPreferences = winPrefs;
                win();
            }, 0);
        }
        catch (err) {
            console.log("error :: " + err);
            fail();
        }

    }
};

require("cordova/exec/proxy").add("CDVOrientation", module.exports);
