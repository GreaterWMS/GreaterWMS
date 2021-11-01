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

/* global require, module */

var MediaFile = require('cordova-plugin-media-capture.MediaFile');
var MediaFileData = require('cordova-plugin-media-capture.MediaFileData');
var CaptureError = require('cordova-plugin-media-capture.CaptureError');

/**
 * Helper function that converts data URI to Blob
 * @param  {String} dataURI Data URI to convert
 * @return {Blob}           Blob, covnerted from DataURI String
 */
function dataURItoBlob (dataURI) {
    // convert base64 to raw binary data held in a string
    // doesn't handle URLEncoded DataURIs
    var byteString = atob(dataURI.split(',')[1]); // eslint-disable-line no-undef

    // separate out the mime component
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

    // write the bytes of the string to an ArrayBuffer
    var ab = new ArrayBuffer(byteString.length);
    var ia = new Uint8Array(ab);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }

    // write the ArrayBuffer to a blob, and you're done
    return new Blob([ab], { type: mimeString }); // eslint-disable-line no-undef
}

/**
 * Creates basic camera UI with preview 'video' element and 'Cancel' button
 * Capture starts, when you clicking on preview.
 */
function CameraUI () {

    // Root element for preview
    var container = document.createElement('div');
    container.style.cssText = 'left: 0px; top: 0px; width: 100%; height: 100%; position: fixed; z-index:9999;' +
                                   'padding: 40px; background-color: rgba(0,0,0,0.75);' +
                                   'text-align:center; visibility: hidden';

    // Set up root element contetnts
    container.innerHTML =
        '<div id="captureHint" style="height:100%; position:relative; display:inline-flex; align-content:flex-start;">' +
        '<h2 style="position: absolute; width: 100%; background-color: rgba(255,255,255,0.25); margin: 0">' +
            'Click on preview to capture image. Click outside of preview to cancel.</h1>' +
        '<video id="capturePreview" style="height: 100%"></video>' +
        '</div>';

    // Add container element to DOM but do not display it since visibility == hidden
    document.body.appendChild(container);

    // Create fullscreen preview
    var preview = document.getElementById('capturePreview');
    preview.autoplay = true;
    // We'll show preview only when video element content
    // is fully loaded to avoid glitches
    preview.onplay = function () {
        container.style.visibility = 'visible';
    };

    this.container = container;
    this.preview = preview;
}

/**
 * Displays capture preview
 * @param  {Number} count       Number of images to take
 * @param  {Function} successCB Success callback, that accepts data URL of captured image
 * @param  {Function} errorCB   Error callback
 */
CameraUI.prototype.startPreview = function (count, successCB, errorCB) {
    var that = this;

    this.preview.onclick = function (e) {
        // proceed with capture here
        // We don't need to propagate click event to parent elements.
        // Otherwise click on vieo element will trigger click event handler
        // for preview root element and cause preview cancellation
        e.stopPropagation();
        // Create canvas element, put video frame on it
        // and save its contant as Data URL
        var canvas = document.createElement('canvas');
        canvas.width = this.videoWidth;
        canvas.height = this.videoHeight;
        canvas.getContext('2d').drawImage(that.preview, 0, 0);
        successCB(canvas.toDataURL('image/jpeg'));
    };

    this.container.onclick = function () {
        // Cancel capture here
        errorCB(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
    };

    navigator.getUserMedia({video: true}, function (previewStream) {
        // Save video stream to be able to stop it later
        that._previewStream = previewStream;
        that.preview.src = URL.createObjectURL(previewStream); // eslint-disable-line no-undef
        // We don't need to set visibility = true for preview element
        // since this will be done automatically in onplay event handler
    }, function (/* err */) {
        errorCB(new CaptureError(CaptureError.CAPTURE_INTERNAL_ERR));
    });
};

/**
 * Destroys camera preview, removes all elements created
 */
CameraUI.prototype.destroyPreview = function () {
    this.preview.pause();
    this.preview.src = null;
    this._previewStream.stop();
    this._previewStream = null;
    if (this.container) {
        document.body.removeChild(this.container);
    }
};

module.exports = {
    captureAudio: function (successCallback, errorCallback) {
        if (errorCallback) {
            errorCallback(new CaptureError(CaptureError.CAPTURE_NOT_SUPPORTED));
        }
    },

    captureVideo: function (successCallback, errorCallback) {
        if (errorCallback) {
            errorCallback(new CaptureError(CaptureError.CAPTURE_NOT_SUPPORTED));
        }
    },

    captureImage: function (successCallback, errorCallback, args) {

        var fail = function (code) {
            if (errorCallback) {
                errorCallback(new CaptureError(code || CaptureError.CAPTURE_INTERNAL_ERR));
            }
        };

        var options = args[0];

        var limit = options.limit || 1;
        if (typeof limit !== 'number' || limit < 1) {
            fail(CaptureError.CAPTURE_INVALID_ARGUMENT);
            return;
        }

        // Counter for already taken images
        var imagesTaken = 0;

        navigator.getUserMedia = navigator.getUserMedia ||
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia ||
                         navigator.msGetUserMedia;

        if (!navigator.getUserMedia) {
            fail(CaptureError.CAPTURE_NOT_SUPPORTED);
            return;
        }

        var ui = new CameraUI();
        ui.startPreview(limit, function (data) {
            // Check if we're done with capture. If so, then destroy UI
            if (++imagesTaken >= limit) {
                ui.destroyPreview();
            }

            // Array of resultant MediaFiles
            var mediaFiles = [];

            // save data to file here
            window.requestFileSystem(window.TEMPORARY, data.length * limit, function (fileSystem) {
                // If we need to capture multiple files, then append counter to filename
                var fileName = limit <= 1 ? 'image.jpg' : 'image' + imagesTaken + '.jpg';
                fileSystem.root.getFile(fileName, {create: true}, function (file) {
                    file.createWriter(function (writer) {
                        writer.onwriteend = function () {
                            file.getMetadata(function (meta) {
                                mediaFiles.push(new MediaFile(file.name, file.toURL(), 'image/jpeg', meta.modificationTime, meta.size));
                                // Check if we're done with capture. If so, then call a successCallback
                                if (imagesTaken >= limit) {
                                    successCallback(mediaFiles);
                                }
                            }, fail);
                        };
                        writer.onerror = fail;
                        // Since success callback for start preview returns
                        // a base64 encoded string, we need to convert it to blob first
                        writer.write(dataURItoBlob(data));
                    });
                }, fail);
            }, fail);
        }, function (err) {
            ui.destroyPreview();
            fail(err.code);
        });
    },

    getFormatData: function (successCallback, errorCallback, args) {

        var img = document.createElement('img');
        img.src = args[0];
        img.onload = function () {
            if (successCallback) {
                successCallback(new MediaFileData(null, 0, img.height, img.width, 0));
            }
        };
    }
};

require('cordova/exec/proxy').add('Capture', module.exports);
