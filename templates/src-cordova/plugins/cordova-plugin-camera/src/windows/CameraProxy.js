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

/* global Windows:true, URL:true, module:true, require:true, WinJS:true */

var Camera = require('./Camera');

var getAppData = function () {
    return Windows.Storage.ApplicationData.current;
};
var encodeToBase64String = function (buffer) {
    return Windows.Security.Cryptography.CryptographicBuffer.encodeToBase64String(buffer);
};
var OptUnique = Windows.Storage.CreationCollisionOption.generateUniqueName;
var CapMSType = Windows.Media.Capture.MediaStreamType;
var webUIApp = Windows.UI.WebUI.WebUIApplication;
var fileIO = Windows.Storage.FileIO;
var pickerLocId = Windows.Storage.Pickers.PickerLocationId;

module.exports = {

    // args will contain :
    //  ...  it is an array, so be careful
    // 0 quality:50,
    // 1 destinationType:Camera.DestinationType.FILE_URI,
    // 2 sourceType:Camera.PictureSourceType.CAMERA,
    // 3 targetWidth:-1,
    // 4 targetHeight:-1,
    // 5 encodingType:Camera.EncodingType.JPEG,
    // 6 mediaType:Camera.MediaType.PICTURE,
    // 7 allowEdit:false,
    // 8 correctOrientation:false,
    // 9 saveToPhotoAlbum:false,
    // 10 popoverOptions:null
    // 11 cameraDirection:0

    takePicture: function (successCallback, errorCallback, args) {
        var sourceType = args[2];

        if (sourceType !== Camera.PictureSourceType.CAMERA) {
            takePictureFromFile(successCallback, errorCallback, args);
        } else {
            takePictureFromCamera(successCallback, errorCallback, args);
        }
    }
};

// https://msdn.microsoft.com/en-us/library/windows/apps/ff462087(v=vs.105).aspx
var windowsVideoContainers = ['.avi', '.flv', '.asx', '.asf', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf', '.wmv', '.vob'];
var windowsPhoneVideoContainers = ['.avi', '.3gp', '.3g2', '.wmv', '.3gp', '.3g2', '.mp4', '.m4v'];

// Default aspect ratio 1.78 (16:9 hd video standard)
var DEFAULT_ASPECT_RATIO = '1.8';

// Highest possible z-index supported across browsers. Anything used above is converted to this value.
var HIGHEST_POSSIBLE_Z_INDEX = 2147483647;

// Resize method
function resizeImage (successCallback, errorCallback, file, targetWidth, targetHeight, encodingType) {
    var tempPhotoFileName = '';
    var targetContentType = '';

    if (encodingType === Camera.EncodingType.PNG) {
        tempPhotoFileName = 'camera_cordova_temp_return.png';
        targetContentType = 'image/png';
    } else {
        tempPhotoFileName = 'camera_cordova_temp_return.jpg';
        targetContentType = 'image/jpeg';
    }

    var storageFolder = getAppData().localFolder;
    file.copyAsync(storageFolder, file.name, Windows.Storage.NameCollisionOption.replaceExisting)
        .then(function (storageFile) {
            return fileIO.readBufferAsync(storageFile);
        })
        .then(function (buffer) {
            var strBase64 = encodeToBase64String(buffer);
            var imageData = 'data:' + file.contentType + ';base64,' + strBase64;
            var image = new Image(); /* eslint no-undef : 0 */
            image.src = imageData;
            image.onload = function () {
                var ratio = Math.min(targetWidth / this.width, targetHeight / this.height);
                var imageWidth = ratio * this.width;
                var imageHeight = ratio * this.height;

                var canvas = document.createElement('canvas');
                var storageFileName;

                canvas.width = imageWidth;
                canvas.height = imageHeight;

                canvas.getContext('2d').drawImage(this, 0, 0, imageWidth, imageHeight);

                var fileContent = canvas.toDataURL(targetContentType).split(',')[1];

                var storageFolder = getAppData().localFolder;

                storageFolder.createFileAsync(tempPhotoFileName, OptUnique)
                    .then(function (storagefile) {
                        var content = Windows.Security.Cryptography.CryptographicBuffer.decodeFromBase64String(fileContent);
                        storageFileName = storagefile.name;
                        return fileIO.writeBufferAsync(storagefile, content);
                    })
                    .done(function () {
                        successCallback('ms-appdata:///local/' + storageFileName);
                    }, errorCallback);
            };
        })
        .done(null, function (err) {
            errorCallback(err);
        });
}

// Because of asynchronous method, so let the successCallback be called in it.
function resizeImageBase64 (successCallback, errorCallback, file, targetWidth, targetHeight) {
    fileIO.readBufferAsync(file).done(function (buffer) {
        var strBase64 = encodeToBase64String(buffer);
        var imageData = 'data:' + file.contentType + ';base64,' + strBase64;

        var image = new Image(); /* eslint no-undef : 0 */
        image.src = imageData;

        image.onload = function () {
            var ratio = Math.min(targetWidth / this.width, targetHeight / this.height);
            var imageWidth = ratio * this.width;
            var imageHeight = ratio * this.height;
            var canvas = document.createElement('canvas');

            canvas.width = imageWidth;
            canvas.height = imageHeight;

            var ctx = canvas.getContext('2d');
            ctx.drawImage(this, 0, 0, imageWidth, imageHeight);

            // The resized file ready for upload
            var finalFile = canvas.toDataURL(file.contentType);

            // Remove the prefix such as "data:" + contentType + ";base64," , in order to meet the Cordova API.
            var arr = finalFile.split(',');
            var newStr = finalFile.substr(arr[0].length + 1);
            successCallback(newStr);
        };
    }, function (err) { errorCallback(err); });
}

function takePictureFromFile (successCallback, errorCallback, args) {
    // Detect Windows Phone
    if (navigator.appVersion.indexOf('Windows Phone 8.1') >= 0) {
        takePictureFromFileWP(successCallback, errorCallback, args);
    } else {
        takePictureFromFileWindows(successCallback, errorCallback, args);
    }
}

function takePictureFromFileWP (successCallback, errorCallback, args) {
    var mediaType = args[6];
    var destinationType = args[1];
    var targetWidth = args[3];
    var targetHeight = args[4];
    var encodingType = args[5];

    /*
        Need to add and remove an event listener to catch activation state
        Using FileOpenPicker will suspend the app and it's required to catch the PickSingleFileAndContinue
        https://msdn.microsoft.com/en-us/library/windows/apps/xaml/dn631755.aspx
    */
    var filePickerActivationHandler = function (eventArgs) {
        if (eventArgs.kind === Windows.ApplicationModel.Activation.ActivationKind.pickFileContinuation) {
            var file = eventArgs.files[0];
            if (!file) {
                errorCallback("User didn't choose a file.");
                webUIApp.removeEventListener('activated', filePickerActivationHandler);
                return;
            }
            if (destinationType === Camera.DestinationType.FILE_URI) {
                if (targetHeight > 0 && targetWidth > 0) {
                    resizeImage(successCallback, errorCallback, file, targetWidth, targetHeight, encodingType);
                } else {
                    var storageFolder = getAppData().localFolder;
                    file.copyAsync(storageFolder, file.name, Windows.Storage.NameCollisionOption.replaceExisting).done(function (storageFile) {
                        successCallback(URL.createObjectURL(storageFile));
                    }, function () {
                        errorCallback("Can't access localStorage folder.");
                    });
                }
            } else {
                if (targetHeight > 0 && targetWidth > 0) {
                    resizeImageBase64(successCallback, errorCallback, file, targetWidth, targetHeight);
                } else {
                    fileIO.readBufferAsync(file).done(function (buffer) {
                        var strBase64 = encodeToBase64String(buffer);
                        successCallback(strBase64);
                    }, errorCallback);
                }
            }
            webUIApp.removeEventListener('activated', filePickerActivationHandler);
        }
    };

    var fileOpenPicker = new Windows.Storage.Pickers.FileOpenPicker();
    if (mediaType === Camera.MediaType.PICTURE) {
        fileOpenPicker.fileTypeFilter.replaceAll(['.png', '.jpg', '.jpeg']);
        fileOpenPicker.suggestedStartLocation = pickerLocId.picturesLibrary;
    } else if (mediaType === Camera.MediaType.VIDEO) {
        fileOpenPicker.fileTypeFilter.replaceAll(windowsPhoneVideoContainers);
        fileOpenPicker.suggestedStartLocation = pickerLocId.videosLibrary;
    } else {
        fileOpenPicker.fileTypeFilter.replaceAll(['*']);
        fileOpenPicker.suggestedStartLocation = pickerLocId.documentsLibrary;
    }

    webUIApp.addEventListener('activated', filePickerActivationHandler);
    fileOpenPicker.pickSingleFileAndContinue();
}

function takePictureFromFileWindows (successCallback, errorCallback, args) {
    var mediaType = args[6];
    var destinationType = args[1];
    var targetWidth = args[3];
    var targetHeight = args[4];
    var encodingType = args[5];

    var fileOpenPicker = new Windows.Storage.Pickers.FileOpenPicker();
    if (mediaType === Camera.MediaType.PICTURE) {
        fileOpenPicker.fileTypeFilter.replaceAll(['.png', '.jpg', '.jpeg']);
        fileOpenPicker.suggestedStartLocation = pickerLocId.picturesLibrary;
    } else if (mediaType === Camera.MediaType.VIDEO) {
        fileOpenPicker.fileTypeFilter.replaceAll(windowsVideoContainers);
        fileOpenPicker.suggestedStartLocation = pickerLocId.videosLibrary;
    } else {
        fileOpenPicker.fileTypeFilter.replaceAll(['*']);
        fileOpenPicker.suggestedStartLocation = pickerLocId.documentsLibrary;
    }

    fileOpenPicker.pickSingleFileAsync().done(function (file) {
        if (!file) {
            errorCallback("User didn't choose a file.");
            return;
        }
        if (destinationType === Camera.DestinationType.FILE_URI) {
            if (targetHeight > 0 && targetWidth > 0) {
                resizeImage(successCallback, errorCallback, file, targetWidth, targetHeight, encodingType);
            } else {
                var storageFolder = getAppData().localFolder;
                file.copyAsync(storageFolder, file.name, Windows.Storage.NameCollisionOption.replaceExisting).done(function (storageFile) {
                    successCallback(URL.createObjectURL(storageFile));
                }, function () {
                    errorCallback("Can't access localStorage folder.");
                });
            }
        } else {
            if (targetHeight > 0 && targetWidth > 0) {
                resizeImageBase64(successCallback, errorCallback, file, targetWidth, targetHeight);
            } else {
                fileIO.readBufferAsync(file).done(function (buffer) {
                    var strBase64 = encodeToBase64String(buffer);
                    successCallback(strBase64);
                }, errorCallback);
            }
        }
    }, function () {
        errorCallback("User didn't choose a file.");
    });
}

function takePictureFromCamera (successCallback, errorCallback, args) {
    // Check if necessary API available
    if (!Windows.Media.Capture.CameraCaptureUI) {
        takePictureFromCameraWP(successCallback, errorCallback, args);
    } else {
        takePictureFromCameraWindows(successCallback, errorCallback, args);
    }
}

function takePictureFromCameraWP (successCallback, errorCallback, args) {
    // We are running on WP8.1 which lacks CameraCaptureUI class
    // so we need to use MediaCapture class instead and implement custom UI for camera
    var destinationType = args[1];
    var targetWidth = args[3];
    var targetHeight = args[4];
    var encodingType = args[5];
    var saveToPhotoAlbum = args[9];
    var cameraDirection = args[11];
    var capturePreview = null;
    var cameraCaptureButton = null;
    var cameraCancelButton = null;
    var capture = null;
    var captureSettings = null;
    var CaptureNS = Windows.Media.Capture;
    var sensor = null;

    function createCameraUI () {
        // create style for take and cancel buttons
        var buttonStyle = 'width:45%;padding: 10px 16px;font-size: 18px;line-height: 1.3333333;color: #333;background-color: #fff;border-color: #ccc; border: 1px solid transparent;border-radius: 6px; display: block; margin: 20px; z-index: 1000;border-color: #adadad;';

        // Create fullscreen preview
        // z-order style element for capturePreview and cameraCancelButton elts
        // is necessary to avoid overriding by another page elements, -1 sometimes is not enough
        capturePreview = document.createElement('video');
        capturePreview.style.cssText = 'position: fixed; left: 0; top: 0; width: 100%; height: 100%; z-index: ' + (HIGHEST_POSSIBLE_Z_INDEX - 1) + ';';

        // Create capture button
        cameraCaptureButton = document.createElement('button');
        cameraCaptureButton.innerText = 'Take';
        cameraCaptureButton.style.cssText = buttonStyle + 'position: fixed; left: 0; bottom: 0; margin: 20px; z-index: ' + HIGHEST_POSSIBLE_Z_INDEX + ';';

        // Create cancel button
        cameraCancelButton = document.createElement('button');
        cameraCancelButton.innerText = 'Cancel';
        cameraCancelButton.style.cssText = buttonStyle + 'position: fixed; right: 0; bottom: 0; margin: 20px; z-index: ' + HIGHEST_POSSIBLE_Z_INDEX + ';';

        capture = new CaptureNS.MediaCapture();

        captureSettings = new CaptureNS.MediaCaptureInitializationSettings();
        captureSettings.streamingCaptureMode = CaptureNS.StreamingCaptureMode.video;
    }

    function continueVideoOnFocus () {
        // if preview is defined it would be stuck, play it
        if (capturePreview) {
            capturePreview.play();
        }
    }

    function startCameraPreview () {
        // Search for available camera devices
        // This is necessary to detect which camera (front or back) we should use
        var DeviceEnum = Windows.Devices.Enumeration;
        var expectedPanel = cameraDirection === 1 ? DeviceEnum.Panel.front : DeviceEnum.Panel.back;

        // Add focus event handler to capture the event when user suspends the app and comes back while the preview is on
        window.addEventListener('focus', continueVideoOnFocus);

        DeviceEnum.DeviceInformation.findAllAsync(DeviceEnum.DeviceClass.videoCapture).then(function (devices) {
            if (devices.length <= 0) {
                destroyCameraPreview();
                errorCallback('Camera not found');
                return;
            }

            devices.forEach(function (currDev) {
                if (currDev.enclosureLocation.panel && currDev.enclosureLocation.panel === expectedPanel) {
                    captureSettings.videoDeviceId = currDev.id;
                }
            });

            captureSettings.photoCaptureSource = Windows.Media.Capture.PhotoCaptureSource.photo;

            return capture.initializeAsync(captureSettings);
        }).then(function () {
            // create focus control if available
            var VideoDeviceController = capture.videoDeviceController;
            var FocusControl = VideoDeviceController.focusControl;

            if (FocusControl.supported === true) {
                capturePreview.addEventListener('click', function () {
                    // Make sure function isn't called again before previous focus is completed
                    if (this.getAttribute('clicked') === '1') {
                        return false;
                    } else {
                        this.setAttribute('clicked', '1');
                    }
                    var preset = Windows.Media.Devices.FocusPreset.autoNormal;
                    var parent = this;
                    FocusControl.setPresetAsync(preset).done(function () {
                        // set the clicked attribute back to '0' to allow focus again
                        parent.setAttribute('clicked', '0');
                    });
                });
            }

            // msdn.microsoft.com/en-us/library/windows/apps/hh452807.aspx
            capturePreview.msZoom = true;
            capturePreview.src = URL.createObjectURL(capture);
            capturePreview.play();

            // Bind events to controls
            sensor = Windows.Devices.Sensors.SimpleOrientationSensor.getDefault();
            if (sensor !== null) {
                sensor.addEventListener('orientationchanged', onOrientationChange);
            }

            // add click events to capture and cancel buttons
            cameraCaptureButton.addEventListener('click', onCameraCaptureButtonClick);
            cameraCancelButton.addEventListener('click', onCameraCancelButtonClick);

            // Change default orientation
            if (sensor) {
                setPreviewRotation(sensor.getCurrentOrientation());
            } else {
                setPreviewRotation(Windows.Graphics.Display.DisplayInformation.getForCurrentView().currentOrientation);
            }

            // Get available aspect ratios
            var aspectRatios = getAspectRatios(capture);

            // Couldn't find a good ratio
            if (aspectRatios.length === 0) {
                destroyCameraPreview();
                errorCallback('There\'s not a good aspect ratio available');
                return;
            }

            // add elements to body
            document.body.appendChild(capturePreview);
            document.body.appendChild(cameraCaptureButton);
            document.body.appendChild(cameraCancelButton);

            if (aspectRatios.indexOf(DEFAULT_ASPECT_RATIO) > -1) {
                return setAspectRatio(capture, DEFAULT_ASPECT_RATIO);
            } else {
                // Doesn't support 16:9 - pick next best
                return setAspectRatio(capture, aspectRatios[0]);
            }
        }).done(null, function (err) {
            destroyCameraPreview();
            errorCallback('Camera intitialization error ' + err);
        });
    }

    function destroyCameraPreview () {
        // If sensor is available, remove event listener
        if (sensor !== null) {
            sensor.removeEventListener('orientationchanged', onOrientationChange);
        }

        // Pause and dispose preview element
        capturePreview.pause();
        capturePreview.src = null;

        // Remove event listeners from buttons
        cameraCaptureButton.removeEventListener('click', onCameraCaptureButtonClick);
        cameraCancelButton.removeEventListener('click', onCameraCancelButtonClick);

        // Remove the focus event handler
        window.removeEventListener('focus', continueVideoOnFocus);

        // Remove elements
        [capturePreview, cameraCaptureButton, cameraCancelButton].forEach(function (elem) {
            if (elem /* && elem in document.body.childNodes */) {
                document.body.removeChild(elem);
            }
        });

        // Stop and dispose media capture manager
        if (capture) {
            capture.stopRecordAsync();
            capture = null;
        }
    }

    function captureAction () {
        var encodingProperties;
        var fileName;
        var tempFolder = getAppData().temporaryFolder;

        if (encodingType === Camera.EncodingType.PNG) {
            fileName = 'photo.png';
            encodingProperties = Windows.Media.MediaProperties.ImageEncodingProperties.createPng();
        } else {
            fileName = 'photo.jpg';
            encodingProperties = Windows.Media.MediaProperties.ImageEncodingProperties.createJpeg();
        }

        tempFolder.createFileAsync(fileName, OptUnique)
            .then(function (tempCapturedFile) {
                return new WinJS.Promise(function (complete) {
                    var photoStream = new Windows.Storage.Streams.InMemoryRandomAccessStream();
                    var finalStream = new Windows.Storage.Streams.InMemoryRandomAccessStream();
                    capture.capturePhotoToStreamAsync(encodingProperties, photoStream)
                        .then(function () {
                            return Windows.Graphics.Imaging.BitmapDecoder.createAsync(photoStream);
                        })
                        .then(function (dec) {
                            finalStream.size = 0; // BitmapEncoder requires the output stream to be empty
                            return Windows.Graphics.Imaging.BitmapEncoder.createForTranscodingAsync(finalStream, dec);
                        })
                        .then(function (enc) {
                            // We need to rotate the photo wrt sensor orientation
                            enc.bitmapTransform.rotation = orientationToRotation(sensor.getCurrentOrientation());
                            return enc.flushAsync();
                        })
                        .then(function () {
                            return tempCapturedFile.openAsync(Windows.Storage.FileAccessMode.readWrite);
                        })
                        .then(function (fileStream) {
                            return Windows.Storage.Streams.RandomAccessStream.copyAndCloseAsync(finalStream, fileStream);
                        })
                        .done(function () {
                            photoStream.close();
                            finalStream.close();
                            complete(tempCapturedFile);
                        }, function () {
                            photoStream.close();
                            finalStream.close();
                            throw new Error('An error has occured while capturing the photo.');
                        });
                });
            })
            .done(function (capturedFile) {
                destroyCameraPreview();
                savePhoto(capturedFile, {
                    destinationType: destinationType,
                    targetHeight: targetHeight,
                    targetWidth: targetWidth,
                    encodingType: encodingType,
                    saveToPhotoAlbum: saveToPhotoAlbum
                }, successCallback, errorCallback);
            }, function (err) {
                destroyCameraPreview();
                errorCallback(err);
            });
    }

    function getAspectRatios (capture) {
        var videoDeviceController = capture.videoDeviceController;
        var photoAspectRatios = videoDeviceController.getAvailableMediaStreamProperties(CapMSType.photo).map(function (element) {
            return (element.width / element.height).toFixed(1);
        }).filter(function (element, index, array) { return (index === array.indexOf(element)); });

        var videoAspectRatios = videoDeviceController.getAvailableMediaStreamProperties(CapMSType.videoRecord).map(function (element) {
            return (element.width / element.height).toFixed(1);
        }).filter(function (element, index, array) { return (index === array.indexOf(element)); });

        var videoPreviewAspectRatios = videoDeviceController.getAvailableMediaStreamProperties(CapMSType.videoPreview).map(function (element) {
            return (element.width / element.height).toFixed(1);
        }).filter(function (element, index, array) { return (index === array.indexOf(element)); });

        var allAspectRatios = [].concat(photoAspectRatios, videoAspectRatios, videoPreviewAspectRatios);

        var aspectObj = allAspectRatios.reduce(function (map, item) {
            if (!map[item]) {
                map[item] = 0;
            }
            map[item]++;
            return map;
        }, {});

        return Object.keys(aspectObj).filter(function (k) {
            return aspectObj[k] === 3;
        });
    }

    function setAspectRatio (capture, aspect) {
        // Max photo resolution with desired aspect ratio
        var videoDeviceController = capture.videoDeviceController;
        var photoResolution = videoDeviceController.getAvailableMediaStreamProperties(CapMSType.photo)
            .filter(function (elem) {
                return ((elem.width / elem.height).toFixed(1) === aspect);
            })
            .reduce(function (prop1, prop2) {
                return (prop1.width * prop1.height) > (prop2.width * prop2.height) ? prop1 : prop2;
            });

        // Max video resolution with desired aspect ratio
        var videoRecordResolution = videoDeviceController.getAvailableMediaStreamProperties(CapMSType.videoRecord)
            .filter(function (elem) {
                return ((elem.width / elem.height).toFixed(1) === aspect);
            })
            .reduce(function (prop1, prop2) {
                return (prop1.width * prop1.height) > (prop2.width * prop2.height) ? prop1 : prop2;
            });

        // Max video preview resolution with desired aspect ratio
        var videoPreviewResolution = videoDeviceController.getAvailableMediaStreamProperties(CapMSType.videoPreview)
            .filter(function (elem) {
                return ((elem.width / elem.height).toFixed(1) === aspect);
            })
            .reduce(function (prop1, prop2) {
                return (prop1.width * prop1.height) > (prop2.width * prop2.height) ? prop1 : prop2;
            });

        return videoDeviceController.setMediaStreamPropertiesAsync(CapMSType.photo, photoResolution)
            .then(function () {
                return videoDeviceController.setMediaStreamPropertiesAsync(CapMSType.videoPreview, videoPreviewResolution);
            })
            .then(function () {
                return videoDeviceController.setMediaStreamPropertiesAsync(CapMSType.videoRecord, videoRecordResolution);
            });
    }

    /**
     * When Capture button is clicked, try to capture a picture and return
     */
    function onCameraCaptureButtonClick () {
        // Make sure user can't click more than once
        if (this.getAttribute('clicked') === '1') {
            return false;
        } else {
            this.setAttribute('clicked', '1');
        }
        captureAction();
    }

    /**
     * When Cancel button is clicked, destroy camera preview and return with error callback
     */
    function onCameraCancelButtonClick () {
        // Make sure user can't click more than once
        if (this.getAttribute('clicked') === '1') {
            return false;
        } else {
            this.setAttribute('clicked', '1');
        }
        destroyCameraPreview();
        errorCallback('no image selected');
    }

    /**
     * When the phone orientation change, get the event and change camera preview rotation
     * @param  {Object} e - SimpleOrientationSensorOrientationChangedEventArgs
     */
    function onOrientationChange (e) {
        setPreviewRotation(e.orientation);
    }

    /**
     * Converts SimpleOrientation to a VideoRotation to remove difference between camera sensor orientation
     * and video orientation
     * @param  {number} orientation - Windows.Devices.Sensors.SimpleOrientation
     * @return {number} - Windows.Media.Capture.VideoRotation
     */
    function orientationToRotation (orientation) {
        // VideoRotation enumerable and BitmapRotation enumerable have the same values
        // https://msdn.microsoft.com/en-us/library/windows/apps/windows.media.capture.videorotation.aspx
        // https://msdn.microsoft.com/en-us/library/windows/apps/windows.graphics.imaging.bitmaprotation.aspx

        switch (orientation) {
        // portrait
        case Windows.Devices.Sensors.SimpleOrientation.notRotated:
            return Windows.Media.Capture.VideoRotation.clockwise90Degrees;
        // landscape
        case Windows.Devices.Sensors.SimpleOrientation.rotated90DegreesCounterclockwise:
            return Windows.Media.Capture.VideoRotation.none;
        // portrait-flipped (not supported by WinPhone Apps)
        case Windows.Devices.Sensors.SimpleOrientation.rotated180DegreesCounterclockwise:
            // Falling back to portrait default
            return Windows.Media.Capture.VideoRotation.clockwise90Degrees;
        // landscape-flipped
        case Windows.Devices.Sensors.SimpleOrientation.rotated270DegreesCounterclockwise:
            return Windows.Media.Capture.VideoRotation.clockwise180Degrees;
        // faceup & facedown
        default:
            // Falling back to portrait default
            return Windows.Media.Capture.VideoRotation.clockwise90Degrees;
        }
    }

    /**
     * Rotates the current MediaCapture's video
     * @param {number} orientation - Windows.Devices.Sensors.SimpleOrientation
     */
    function setPreviewRotation (orientation) {
        capture.setPreviewRotation(orientationToRotation(orientation));
    }

    try {
        createCameraUI();
        startCameraPreview();
    } catch (ex) {
        errorCallback(ex);
    }
}

function takePictureFromCameraWindows (successCallback, errorCallback, args) {
    var destinationType = args[1];
    var targetWidth = args[3];
    var targetHeight = args[4];
    var encodingType = args[5];
    var allowCrop = !!args[7];
    var saveToPhotoAlbum = args[9];
    var WMCapture = Windows.Media.Capture;
    var cameraCaptureUI = new WMCapture.CameraCaptureUI();

    cameraCaptureUI.photoSettings.allowCropping = allowCrop;

    if (encodingType === Camera.EncodingType.PNG) {
        cameraCaptureUI.photoSettings.format = WMCapture.CameraCaptureUIPhotoFormat.png;
    } else {
        cameraCaptureUI.photoSettings.format = WMCapture.CameraCaptureUIPhotoFormat.jpeg;
    }

    // decide which max pixels should be supported by targetWidth or targetHeight.
    var maxRes = null;
    var UIMaxRes = WMCapture.CameraCaptureUIMaxPhotoResolution;
    var totalPixels = targetWidth * targetHeight;

    if (targetWidth === -1 && targetHeight === -1) {
        maxRes = UIMaxRes.highestAvailable;
        // Temp fix for CB-10539
    /* else if (totalPixels <= 320 * 240) {
        maxRes = UIMaxRes.verySmallQvga;
    } */
    } else if (totalPixels <= 640 * 480) {
        maxRes = UIMaxRes.smallVga;
    } else if (totalPixels <= 1024 * 768) {
        maxRes = UIMaxRes.mediumXga;
    } else if (totalPixels <= 3 * 1000 * 1000) {
        maxRes = UIMaxRes.large3M;
    } else if (totalPixels <= 5 * 1000 * 1000) {
        maxRes = UIMaxRes.veryLarge5M;
    } else {
        maxRes = UIMaxRes.highestAvailable;
    }

    cameraCaptureUI.photoSettings.maxResolution = maxRes;

    var cameraPicture;

    // define focus handler for windows phone 10.0
    var savePhotoOnFocus = function () {
        window.removeEventListener('focus', savePhotoOnFocus);
        // call only when the app is in focus again
        savePhoto(cameraPicture, {
            destinationType: destinationType,
            targetHeight: targetHeight,
            targetWidth: targetWidth,
            encodingType: encodingType,
            saveToPhotoAlbum: saveToPhotoAlbum
        }, successCallback, errorCallback);
    };

    // if windows phone 10, add and delete focus eventHandler to capture the focus back from cameraUI to app
    if (navigator.appVersion.indexOf('Windows Phone 10.0') >= 0) {
        window.addEventListener('focus', savePhotoOnFocus);
    }

    cameraCaptureUI.captureFileAsync(WMCapture.CameraCaptureUIMode.photo).done(function (picture) {
        if (!picture) {
            errorCallback("User didn't capture a photo.");
            // Remove the focus handler if present
            window.removeEventListener('focus', savePhotoOnFocus);
            return;
        }
        cameraPicture = picture;

        // If not windows 10, call savePhoto() now. If windows 10, wait for the app to be in focus again
        if (navigator.appVersion.indexOf('Windows Phone 10.0') < 0) {
            savePhoto(cameraPicture, {
                destinationType: destinationType,
                targetHeight: targetHeight,
                targetWidth: targetWidth,
                encodingType: encodingType,
                saveToPhotoAlbum: saveToPhotoAlbum
            }, successCallback, errorCallback);
        }
    }, function () {
        errorCallback('Fail to capture a photo.');
        window.removeEventListener('focus', savePhotoOnFocus);
    });
}

function savePhoto (picture, options, successCallback, errorCallback) {
    // success callback for capture operation
    var success = function (picture) {
        if (options.destinationType === Camera.DestinationType.FILE_URI) {
            if (options.targetHeight > 0 && options.targetWidth > 0) {
                resizeImage(successCallback, errorCallback, picture, options.targetWidth, options.targetHeight, options.encodingType);
            } else {
                // CB-11714: check if target content-type is PNG to just rename as *.jpg since camera is captured as JPEG
                if (options.encodingType === Camera.EncodingType.PNG) {
                    picture.name = picture.name.replace(/\.png$/, '.jpg');
                }

                picture.copyAsync(getAppData().localFolder, picture.name, OptUnique).done(function (copiedFile) {
                    successCallback('ms-appdata:///local/' + copiedFile.name);
                }, errorCallback);
            }
        } else {
            if (options.targetHeight > 0 && options.targetWidth > 0) {
                resizeImageBase64(successCallback, errorCallback, picture, options.targetWidth, options.targetHeight);
            } else {
                fileIO.readBufferAsync(picture).done(function (buffer) {
                    var strBase64 = encodeToBase64String(buffer);
                    picture.deleteAsync().done(function () {
                        successCallback(strBase64);
                    }, function (err) {
                        errorCallback(err);
                    });
                }, errorCallback);
            }
        }
    };

    if (!options.saveToPhotoAlbum) {
        success(picture);
    } else {
        var savePicker = new Windows.Storage.Pickers.FileSavePicker();
        var saveFile = function (file) {
            if (file) {
                // Prevent updates to the remote version of the file until we're done
                Windows.Storage.CachedFileManager.deferUpdates(file);
                picture.moveAndReplaceAsync(file)
                    .then(function () {
                        // Let Windows know that we're finished changing the file so
                        // the other app can update the remote version of the file.
                        return Windows.Storage.CachedFileManager.completeUpdatesAsync(file);
                    })
                    .done(function (updateStatus) {
                        if (updateStatus === Windows.Storage.Provider.FileUpdateStatus.complete) {
                            success(picture);
                        } else {
                            errorCallback('File update status is not complete.');
                        }
                    }, errorCallback);
            } else {
                errorCallback('Failed to select a file.');
            }
        };
        savePicker.suggestedStartLocation = pickerLocId.picturesLibrary;

        if (options.encodingType === Camera.EncodingType.PNG) {
            savePicker.fileTypeChoices.insert('PNG', ['.png']);
            savePicker.suggestedFileName = 'photo.png';
        } else {
            savePicker.fileTypeChoices.insert('JPEG', ['.jpg']);
            savePicker.suggestedFileName = 'photo.jpg';
        }

        // If Windows Phone 8.1 use pickSaveFileAndContinue()
        if (navigator.appVersion.indexOf('Windows Phone 8.1') >= 0) {
            /*
                Need to add and remove an event listener to catch activation state
                Using FileSavePicker will suspend the app and it's required to catch the pickSaveFileContinuation
                https://msdn.microsoft.com/en-us/library/windows/apps/xaml/dn631755.aspx
            */
            var fileSaveHandler = function (eventArgs) {
                if (eventArgs.kind === Windows.ApplicationModel.Activation.ActivationKind.pickSaveFileContinuation) {
                    var file = eventArgs.file;
                    saveFile(file);
                    webUIApp.removeEventListener('activated', fileSaveHandler);
                }
            };
            webUIApp.addEventListener('activated', fileSaveHandler);
            savePicker.pickSaveFileAndContinue();
        } else {
            savePicker.pickSaveFileAsync()
                .done(saveFile, errorCallback);
        }
    }
}

require('cordova/exec/proxy').add('Camera', module.exports);
