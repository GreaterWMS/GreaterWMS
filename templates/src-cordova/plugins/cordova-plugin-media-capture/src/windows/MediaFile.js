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

/* global Windows:true */

var MediaFileData = require('cordova-plugin-media-capture.MediaFileData');
var CaptureError = require('cordova-plugin-media-capture.CaptureError');

module.exports = {

    getFormatData: function (successCallback, errorCallback, args) {
        Windows.Storage.StorageFile.getFileFromPathAsync(this.fullPath).then(
            function (storageFile) {
                var mediaTypeFlag = String(storageFile.contentType).split('/')[0].toLowerCase();
                if (mediaTypeFlag === 'audio') {
                    storageFile.properties.getMusicPropertiesAsync().then(
                        function (audioProperties) {
                            successCallback(new MediaFileData(null, audioProperties.bitrate, 0, 0, audioProperties.duration / 1000));
                        }, function () {
                            errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                        }
                    );
                } else if (mediaTypeFlag === 'video') {
                    storageFile.properties.getVideoPropertiesAsync().then(
                        function (videoProperties) {
                            successCallback(new MediaFileData(null, videoProperties.bitrate, videoProperties.height, videoProperties.width, videoProperties.duration / 1000));
                        }, function () {
                            errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                        }
                    );
                } else if (mediaTypeFlag === 'image') {
                    storageFile.properties.getImagePropertiesAsync().then(
                        function (imageProperties) {
                            successCallback(new MediaFileData(null, 0, imageProperties.height, imageProperties.width, 0));
                        }, function () {
                            errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                        }
                    );
                } else {
                    errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                }
            }, function () {
                errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
            }
        );
    }
};
