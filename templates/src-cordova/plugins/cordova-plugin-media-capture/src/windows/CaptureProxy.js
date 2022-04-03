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

var MediaFile = require('cordova-plugin-media-capture.MediaFile');
var CaptureError = require('cordova-plugin-media-capture.CaptureError');
var CaptureAudioOptions = require('cordova-plugin-media-capture.CaptureAudioOptions');
var CaptureVideoOptions = require('cordova-plugin-media-capture.CaptureVideoOptions');
var MediaFileData = require('cordova-plugin-media-capture.MediaFileData');

/*
 * Class that combines all logic for capturing picture and video on WP8.1
 */
function MediaCaptureProxy () {

    var previewContainer;
    var capturePreview = null;
    var captureCancelButton = null; // eslint-disable-line no-unused-vars
    var captureSettings = null;
    var captureStarted = false;
    var capturedPictureFile;
    var capturedVideoFile;
    var capture = null;

    var CaptureNS = Windows.Media.Capture;

    /**
     * Helper function that toggles visibility of DOM elements with provided ids
     * @param {String} variable number of elements' ids which visibility needs to be toggled
     */
    function toggleElements () {
        // convert arguments to array
        var args = Array.prototype.slice.call(arguments);
        args.forEach(function (buttonId) {
            var buttonEl = document.getElementById(buttonId);
            if (buttonEl) {
                var curDisplayStyle = buttonEl.style.display;
                buttonEl.style.display = curDisplayStyle === 'none' ? 'block' : 'none';
            }
        });
    }

    /**
     * Creates basic camera UI with preview 'video' element and 'Cancel' button
     * Capture starts, when you clicking on preview.
     */
    function createCameraUI () {

        var buttonStyle = 'margin: 7px; border: 2.5px solid white; width: 45%; height: 35px; color: white; background-color: black;';

        previewContainer = document.createElement('div');
        previewContainer.style.cssText = 'background-position: 50% 50%; background-repeat: no-repeat; background-size: contain; background-color: black; left: 0px; top: 0px; width: 100%; height: 100%; position: fixed; z-index: 9999';
        previewContainer.innerHTML =
            '<video id="capturePreview" style="width: 100%; height: 100%"></video>' +
            '<div id="previewButtons" style="width: 100%; bottom: 0px; display: flex; position: absolute; justify-content: space-around; background-color: black;">' +
                '<button id="takePicture" style="' + buttonStyle + '">Capture</button>' +
                '<button id="cancelCapture" style="' + buttonStyle + '">Cancel</button>' +
                '<button id="selectPicture" style="display: none; ' + buttonStyle + '">Accept</button>' +
                '<button id="retakePicture" style="display: none; ' + buttonStyle + '">Retake</button>' +
            '</div>';

        document.body.appendChild(previewContainer);

        // Create fullscreen preview
        capturePreview = document.getElementById('capturePreview');

        // Create cancel button
        captureCancelButton = document.getElementById('cancelCapture');

        capture = new CaptureNS.MediaCapture();

        captureSettings = new CaptureNS.MediaCaptureInitializationSettings();
        captureSettings.streamingCaptureMode = CaptureNS.StreamingCaptureMode.audioAndVideo;
    }

    /**
     * Starts camera preview and binds provided callbacks to controls
     * @param  {function} takeCallback   Callback for Take button
     * @param  {function} errorCallback  Callback for Cancel button + default error callback
     * @param  {function} selectCallback Callback for Select button
     * @param  {function} retakeCallback Callback for Retake button
     */
    function startCameraPreview (takeCallback, errorCallback, selectCallback, retakeCallback) {
        // try to select appropriate device for capture
        // rear camera is preferred option
        var expectedPanel = Windows.Devices.Enumeration.Panel.back;
        Windows.Devices.Enumeration.DeviceInformation.findAllAsync(Windows.Devices.Enumeration.DeviceClass.videoCapture).done(function (devices) {
            if (devices.length > 0) {
                devices.forEach(function (currDev) {
                    if (currDev.enclosureLocation && currDev.enclosureLocation.panel && currDev.enclosureLocation.panel === expectedPanel) {
                        captureSettings.videoDeviceId = currDev.id;
                    }
                });

                capture.initializeAsync(captureSettings).done(function () {
                    // This is necessary since WP8.1 MediaCapture outputs video stream rotated 90 degrees CCW
                    // TODO: This can be not consistent across devices, need additional testing on various devices
                    // msdn.microsoft.com/en-us/library/windows/apps/hh452807.aspx
                    capture.setPreviewRotation(Windows.Media.Capture.VideoRotation.clockwise90Degrees);
                    capturePreview.msZoom = true;

                    capturePreview.src = URL.createObjectURL(capture); // eslint-disable-line no-undef
                    capturePreview.play();

                    previewContainer.style.display = 'block';

                    // Bind events to controls
                    capturePreview.onclick = takeCallback;
                    document.getElementById('takePicture').onclick = takeCallback;
                    document.getElementById('cancelCapture').onclick = function () {
                        errorCallback(CaptureError.CAPTURE_NO_MEDIA_FILES);
                    };
                    document.getElementById('selectPicture').onclick = selectCallback;
                    document.getElementById('retakePicture').onclick = retakeCallback;
                }, function (err) {
                    destroyCameraPreview();
                    errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, err);
                });
            } else {
                // no appropriate devices found
                destroyCameraPreview();
                errorCallback(CaptureError.CAPTURE_INTERNAL_ERR);
            }
        });
    }

    /**
     * Destroys camera preview, removes all elements created
     */
    function destroyCameraPreview () {
        capturePreview.pause();
        capturePreview.src = null;
        if (previewContainer) {
            document.body.removeChild(previewContainer);
        }
        if (capture) {
            capture.stopRecordAsync();
            capture = null;
        }
    }

    return {
        /**
         * Initiate video capture using MediaCapture class
         * @param  {function} successCallback Called, when user clicked on preview, with captured file object
         * @param  {function} errorCallback   Called on any error
         */
        captureVideo: function (successCallback, errorCallback) {
            try {
                createCameraUI();
                startCameraPreview(function () {
                    // This callback called twice: whem video capture started and when it ended
                    // so we need to check capture status
                    if (!captureStarted) {
                        // remove cancel button and rename 'Take' button to 'Stop'
                        toggleElements('cancelCapture');
                        document.getElementById('takePicture').text = 'Stop';

                        var encodingProperties = Windows.Media.MediaProperties.MediaEncodingProfile.createMp4(Windows.Media.MediaProperties.VideoEncodingQuality.auto);
                        var generateUniqueCollisionOption = Windows.Storage.CreationCollisionOption.generateUniqueName;
                        var localFolder = Windows.Storage.ApplicationData.current.localFolder;

                        localFolder.createFileAsync('cameraCaptureVideo.mp4', generateUniqueCollisionOption).done(function (capturedFile) {
                            capture.startRecordToStorageFileAsync(encodingProperties, capturedFile).done(function () {
                                capturedVideoFile = capturedFile;
                                captureStarted = true;
                            }, function (err) {
                                destroyCameraPreview();
                                errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, err);
                            });
                        }, function (err) {
                            destroyCameraPreview();
                            errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, err);
                        });
                    } else {
                        capture.stopRecordAsync().done(function () {
                            destroyCameraPreview();
                            successCallback(capturedVideoFile);
                        });
                    }
                }, errorCallback);
            } catch (ex) {
                destroyCameraPreview();
                errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, ex);
            }
        },

        /**
         * Initiate image capture using MediaCapture class
         * @param  {function} successCallback Called, when user clicked on preview, with captured file object
         * @param  {function} errorCallback   Called on any error
         */
        capturePhoto: function (successCallback, errorCallback) {
            try {
                createCameraUI();
                startCameraPreview(
                    // Callback for Take button - captures intermediate image file.
                    function () {
                        var encodingProperties = Windows.Media.MediaProperties.ImageEncodingProperties.createJpeg();
                        var overwriteCollisionOption = Windows.Storage.CreationCollisionOption.replaceExisting;
                        var tempFolder = Windows.Storage.ApplicationData.current.temporaryFolder;

                        tempFolder.createFileAsync('cameraCaptureImage.jpg', overwriteCollisionOption).done(function (capturedFile) {
                            capture.capturePhotoToStorageFileAsync(encodingProperties, capturedFile).done(function () {
                                // store intermediate result in object's global variable
                                capturedPictureFile = capturedFile;
                                // show pre-captured image and toggle visibility of all buttons
                                previewContainer.style.backgroundImage = 'url("' + 'ms-appdata:///temp/' + capturedFile.name + '")';
                                toggleElements('capturePreview', 'takePicture', 'cancelCapture', 'selectPicture', 'retakePicture');
                            }, function (err) {
                                destroyCameraPreview();
                                errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, err);
                            });
                        }, function (err) {
                            destroyCameraPreview();
                            errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, err);
                        });
                    },
                    // error + cancel callback
                    function (err) {
                        destroyCameraPreview();
                        errorCallback(err);
                    },
                    // Callback for Select button - copies intermediate file into persistent application's storage
                    function () {
                        var generateUniqueCollisionOption = Windows.Storage.CreationCollisionOption.generateUniqueName;
                        var localFolder = Windows.Storage.ApplicationData.current.localFolder;

                        capturedPictureFile.copyAsync(localFolder, capturedPictureFile.name, generateUniqueCollisionOption).done(function (copiedFile) {
                            destroyCameraPreview();
                            successCallback(copiedFile);
                        }, function (err) {
                            destroyCameraPreview();
                            errorCallback(err);
                        });
                    },
                    // Callback for retake button - just toggles visibility of necessary elements
                    function () {
                        toggleElements('capturePreview', 'takePicture', 'cancelCapture', 'selectPicture', 'retakePicture');
                    }
                );
            } catch (ex) {
                destroyCameraPreview();
                errorCallback(CaptureError.CAPTURE_INTERNAL_ERR, ex);
            }
        }
    };
}

module.exports = {

    captureAudio: function (successCallback, errorCallback, args) {
        var options = args[0];

        var audioOptions = new CaptureAudioOptions();
        if (typeof (options.duration) === 'undefined') {
            audioOptions.duration = 3600; // Arbitrary amount, need to change later
        } else if (options.duration > 0) {
            audioOptions.duration = options.duration;
        } else {
            errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
            return;
        }

        // Some shortcuts for long namespaces
        var CaptureNS = Windows.Media.Capture;
        var MediaPropsNS = Windows.Media.MediaProperties;
        var localAppData = Windows.Storage.ApplicationData.current.localFolder;
        var generateUniqueName = Windows.Storage.NameCollisionOption.generateUniqueName;

        var mediaCapture = new CaptureNS.MediaCapture();
        var mediaCaptureSettings = new CaptureNS.MediaCaptureInitializationSettings();
        var mp3EncodingProfile = new MediaPropsNS.MediaEncodingProfile.createMp3(MediaPropsNS.AudioEncodingQuality.auto); // eslint-disable-line new-cap
        var m4aEncodingProfile = new MediaPropsNS.MediaEncodingProfile.createM4a(MediaPropsNS.AudioEncodingQuality.auto); // eslint-disable-line new-cap

        mediaCaptureSettings.streamingCaptureMode = CaptureNS.StreamingCaptureMode.audio;

        var capturedFile;
        var stopRecordTimeout;

        var stopRecord = function () {
            mediaCapture.stopRecordAsync().then(function () {
                capturedFile.getBasicPropertiesAsync().then(function (basicProperties) {
                    var result = new MediaFile(capturedFile.name, 'ms-appdata:///local/' + capturedFile.name, capturedFile.contentType, basicProperties.dateModified, basicProperties.size);
                    result.fullPath = capturedFile.path;
                    successCallback([result]);
                }, function () {
                    errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                });
            }, function () { errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES)); });
        };

        mediaCapture.initializeAsync(mediaCaptureSettings).done(function () {
            localAppData.createFileAsync('captureAudio.mp3', generateUniqueName).then(function (storageFile) {
                capturedFile = storageFile;
                mediaCapture.startRecordToStorageFileAsync(mp3EncodingProfile, capturedFile).then(function () {
                    stopRecordTimeout = setTimeout(stopRecord, audioOptions.duration * 1000);
                }, function (err) {
                    // -1072868846 is the error code for "No suitable transform was found to encode or decode the content."
                    // so we try to use another (m4a) format
                    if (err.number === -1072868846) {
                        // first we clear existing timeout to prevent success callback to be called with invalid arguments
                        // second we start same actions to try to record m4a audio
                        clearTimeout(stopRecordTimeout);
                        localAppData.createFileAsync('captureAudio.m4a', generateUniqueName).then(function (storageFile) {
                            capturedFile = storageFile;
                            mediaCapture.startRecordToStorageFileAsync(m4aEncodingProfile, capturedFile).then(function () {
                                stopRecordTimeout = setTimeout(stopRecord, audioOptions.duration * 1000);
                            }, function () {
                                // if we here, we're totally failed to record either mp3 or m4a
                                errorCallback(new CaptureError(CaptureError.CAPTURE_INTERNAL_ERR));

                            });
                        });
                    } else {
                        errorCallback(new CaptureError(CaptureError.CAPTURE_INTERNAL_ERR));

                    }
                });
            }, function () { errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES)); });
        });
    },

    captureImage: function (successCallback, errorCallback, args) {
        var CaptureNS = Windows.Media.Capture;

        function fail (code, data) {
            var err = new CaptureError(code);
            err.message = data;
            errorCallback(err);
        }

        // Check if necessary API available
        if (!CaptureNS.CameraCaptureUI) {
            // We are running on WP8.1 which lacks CameraCaptureUI class
            // so we need to use MediaCapture class instead and implement custom UI for camera

            var proxy = new MediaCaptureProxy();

            proxy.capturePhoto(function (photoFile) {
                photoFile.getBasicPropertiesAsync().done(function (basicProperties) {
                    var result = new MediaFile(photoFile.name, 'ms-appdata:///local/' + photoFile.name, photoFile.contentType, basicProperties.dateModified, basicProperties.size);
                    result.fullPath = photoFile.path;
                    successCallback([result]);
                }, function (err) {
                    fail(CaptureError.CAPTURE_INTERNAL_ERR, err);
                });
            }, function (err) {
                fail(err);
            });

        } else {
            var cameraCaptureUI = new Windows.Media.Capture.CameraCaptureUI();
            cameraCaptureUI.photoSettings.allowCropping = true;
            cameraCaptureUI.photoSettings.maxResolution = Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution.highestAvailable;
            cameraCaptureUI.photoSettings.format = Windows.Media.Capture.CameraCaptureUIPhotoFormat.jpeg;
            cameraCaptureUI.captureFileAsync(Windows.Media.Capture.CameraCaptureUIMode.photo).done(function (file) {
                if (file) {
                    file.moveAsync(Windows.Storage.ApplicationData.current.localFolder, 'cameraCaptureImage.jpg', Windows.Storage.NameCollisionOption.generateUniqueName).then(function () {
                        file.getBasicPropertiesAsync().then(function (basicProperties) {
                            var result = new MediaFile(file.name, 'ms-appdata:///local/' + file.name, file.contentType, basicProperties.dateModified, basicProperties.size);
                            result.fullPath = file.path;
                            successCallback([result]);
                        }, function () {
                            errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                        });
                    }, function () {
                        errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                    });
                } else {
                    errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                }
            }, function () {
                errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
            });
        }
    },

    captureVideo: function (successCallback, errorCallback, args) {
        var options = args[0];
        var CaptureNS = Windows.Media.Capture;

        function fail (code, data) {
            var err = new CaptureError(code);
            err.message = data;
            errorCallback(err);
        }

        // Check if necessary API available
        if (!CaptureNS.CameraCaptureUI) {
            // We are running on WP8.1 which lacks CameraCaptureUI class
            // so we need to use MediaCapture class instead and implement custom UI for camera

            var proxy = new MediaCaptureProxy();

            proxy.captureVideo(function (videoFile) {
                videoFile.getBasicPropertiesAsync().done(function (basicProperties) {
                    var result = new MediaFile(videoFile.name, 'ms-appdata:///local/' + videoFile.name, videoFile.contentType, basicProperties.dateModified, basicProperties.size);
                    result.fullPath = videoFile.path;
                    successCallback([result]);
                }, function (err) {
                    fail(CaptureError.CAPTURE_INTERNAL_ERR, err);
                });
            }, fail);

        } else {

            var videoOptions = new CaptureVideoOptions();
            if (options.duration && options.duration > 0) {
                videoOptions.duration = options.duration;
            }
            if (options.limit > 1) {
                videoOptions.limit = options.limit;
            }
            var cameraCaptureUI = new Windows.Media.Capture.CameraCaptureUI();
            cameraCaptureUI.videoSettings.allowTrimming = true;
            cameraCaptureUI.videoSettings.format = Windows.Media.Capture.CameraCaptureUIVideoFormat.mp4;
            cameraCaptureUI.videoSettings.maxDurationInSeconds = videoOptions.duration;
            cameraCaptureUI.captureFileAsync(Windows.Media.Capture.CameraCaptureUIMode.video).then(function (file) {
                if (file) {
                    file.moveAsync(Windows.Storage.ApplicationData.current.localFolder, 'cameraCaptureVideo.mp4', Windows.Storage.NameCollisionOption.generateUniqueName).then(function () {
                        file.getBasicPropertiesAsync().then(function (basicProperties) {
                            var result = new MediaFile(file.name, 'ms-appdata:///local/' + file.name, file.contentType, basicProperties.dateModified, basicProperties.size);
                            result.fullPath = file.path;
                            successCallback([result]);
                        }, function () {
                            errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                        });
                    }, function () {
                        errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                    });
                } else {
                    errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES));
                }
            }, function () { errorCallback(new CaptureError(CaptureError.CAPTURE_NO_MEDIA_FILES)); });
        }
    },

    getFormatData: function (successCallback, errorCallback, args) {
        Windows.Storage.StorageFile.getFileFromPathAsync(args[0]).then(
            function (storageFile) {
                var mediaTypeFlag = String(storageFile.contentType).split('/')[0].toLowerCase();
                if (mediaTypeFlag === 'audio') {
                    storageFile.properties.getMusicPropertiesAsync().then(function (audioProperties) {
                        successCallback(new MediaFileData(null, audioProperties.bitrate, 0, 0, audioProperties.duration / 1000));
                    }, function () {
                        errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                    });
                } else if (mediaTypeFlag === 'video') {
                    storageFile.properties.getVideoPropertiesAsync().then(function (videoProperties) {
                        successCallback(new MediaFileData(null, videoProperties.bitrate, videoProperties.height, videoProperties.width, videoProperties.duration / 1000));
                    }, function () {
                        errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                    });
                } else if (mediaTypeFlag === 'image') {
                    storageFile.properties.getImagePropertiesAsync().then(function (imageProperties) {
                        successCallback(new MediaFileData(null, 0, imageProperties.height, imageProperties.width, 0));
                    }, function () {
                        errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
                    });
                } else { errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT)); }
            }, function () {
                errorCallback(new CaptureError(CaptureError.CAPTURE_INVALID_ARGUMENT));
            }
        );
    }
};

require('cordova/exec/proxy').add('Capture', module.exports);
