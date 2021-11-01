cordova.define("cordova-plugin-media-capture.init", function(require, exports, module) {
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

var cordova = require('cordova');
var helpers = require('./helpers');

var SUCCESS_EVENT = 'pendingcaptureresult';
var FAILURE_EVENT = 'pendingcaptureerror';

var sChannel = cordova.addStickyDocumentEventHandler(SUCCESS_EVENT);
var fChannel = cordova.addStickyDocumentEventHandler(FAILURE_EVENT);

// We fire one of two events in the case where the activity gets killed while
// the user is capturing audio, image, video, etc. in a separate activity
document.addEventListener('deviceready', function () {
    document.addEventListener('resume', function (event) {
        if (event.pendingResult && event.pendingResult.pluginServiceName === 'Capture') {
            if (event.pendingResult.pluginStatus === 'OK') {
                var mediaFiles = helpers.wrapMediaFiles(event.pendingResult.result);
                sChannel.fire(mediaFiles);
            } else {
                fChannel.fire(event.pendingResult.result);
            }
        }
    });
});

});
