/*
 * Copyright (c) Microsoft Open Technologies, Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
 */

var urlutil = require('cordova/urlutil');

var CAMERA_STREAM_STATE_CHECK_RETRY_TIMEOUT = 200; // milliseconds
var OPERATION_IS_IN_PROGRESS = -2147024567;
var REGDB_E_CLASSNOTREG = -2147221164;
var INITIAL_FOCUS_DELAY = 200; // milliseconds
var CHECK_PLAYING_TIMEOUT = 100; // milliseconds

/**
 * List of supported barcode formats from ZXing library. Used to return format
 *   name instead of number code as per plugin spec.
 *
 * @enum {String}
 */
var BARCODE_FORMAT = {
    1: 'AZTEC',
    2: 'CODABAR',
    4: 'CODE_39',
    8: 'CODE_93',
    16: 'CODE_128',
    32: 'DATA_MATRIX',
    64: 'EAN_8',
    128: 'EAN_13',
    256: 'ITF',
    512: 'MAXICODE',
    1024: 'PDF_417',
    2048: 'QR_CODE',
    4096: 'RSS_14',
    8192: 'RSS_EXPANDED',
    16384: 'UPC_A',
    32768: 'UPC_E',
    61918: 'All_1D',
    65536: 'UPC_EAN_EXTENSION',
    131072: 'MSI',
    262144: 'PLESSEY'
};

/**
 * Detects the first appropriate camera located at the back panel of device. If
 *   there is no back cameras, returns the first available.
 *
 * @returns {Promise<String>} Camera id
 */
function findCamera() {
    var Devices = Windows.Devices.Enumeration;

    // Enumerate cameras and add them to the list
    return Devices.DeviceInformation.findAllAsync(Devices.DeviceClass.videoCapture)
    .then(function (cameras) {

        if (!cameras || cameras.length === 0) {
            throw new Error("No cameras found");
        }

        var backCameras = cameras.filter(function (camera) {
            return camera.enclosureLocation && camera.enclosureLocation.panel === Devices.Panel.back;
        });

        // If there is back cameras, return the id of the first,
        // otherwise take the first available device's id
        return (backCameras[0] || cameras[0]).id;
    });
}

/**
 * @param {Windows.Graphics.Display.DisplayOrientations} displayOrientation
 * @return {Number}
 */
function videoPreviewRotationLookup(displayOrientation, isMirrored) {
    var degreesToRotate;

    switch (displayOrientation) {
        case Windows.Graphics.Display.DisplayOrientations.landscape:
            degreesToRotate = 0;
            break;
        case Windows.Graphics.Display.DisplayOrientations.portrait:
            if (isMirrored) {
                degreesToRotate = 270;
            } else {
                degreesToRotate = 90;
            }
            break;
        case Windows.Graphics.Display.DisplayOrientations.landscapeFlipped:
            degreesToRotate = 180;
            break;
        case Windows.Graphics.Display.DisplayOrientations.portraitFlipped:
            if (isMirrored) {
                degreesToRotate = 90;
            } else {
                degreesToRotate = 270;
            }
            break;
        default:
            degreesToRotate = 0;
            break;
    }

    return degreesToRotate;
}

/**
 * The pure JS implementation of barcode reader from WinRTBarcodeReader.winmd.
 *   Works only on Windows 10 devices and more efficient than original one.
 *
 * @class {BarcodeReader}
 */
function BarcodeReader () {
    this._promise = null;
    this._cancelled = false;
}

/**
 * Returns an instance of Barcode reader, depending on capabilities of Media
 *   Capture API
 *
 * @static
 * @constructs {BarcodeReader}
 *
 * @param   {MediaCapture}   mediaCaptureInstance  Instance of
 *   Windows.Media.Capture.MediaCapture class
 *
 * @return  {BarcodeReader}  BarcodeReader instance that could be used for
 *   scanning
 */
BarcodeReader.get = function (mediaCaptureInstance) {
    if (mediaCaptureInstance.getPreviewFrameAsync && ZXing.BarcodeReader) {
        return new BarcodeReader();
    }

    // If there is no corresponding API (Win8/8.1/Phone8.1) use old approach with WinMD library
    return new WinRTBarcodeReader.Reader();

};

/**
 * Initializes instance of reader.
 *
 * @param   {MediaCapture}  capture  Instance of
 *   Windows.Media.Capture.MediaCapture class, used for acquiring images/ video
 *   stream for barcode scanner.
 * @param   {Number}  width    Video/image frame width
 * @param   {Number}  height   Video/image frame height
 */
BarcodeReader.prototype.init = function (capture, width, height) {
    this._capture = capture;
    this._width = width;
    this._height = height;
    this._zxingReader = new ZXing.BarcodeReader();
    this._zxingReader.tryHarder = true;

    var formatsList = BarcodeReader.scanCallArgs.args.length > 0 && BarcodeReader.scanCallArgs.args[0].formats;	
	if (formatsList) {		
        var possibleFormats = formatsList
            .split(",")
            .map(format => {
                for (var index in BARCODE_FORMAT) {
                    if (BARCODE_FORMAT[index] === format) {                        
                        return index;
                    }
                }
            });

        this._zxingReader.possibleFormats = possibleFormats;
    }
};

/**
 * Starts barcode search routines asyncronously.
 *
 * @return  {Promise<ScanResult>}  barcode scan result or null if search
 *   cancelled.
 */
BarcodeReader.prototype.readCode = function () {

    /**
     * Grabs a frame from preview stream uning Win10-only API and tries to
     *   get a barcode using zxing reader provided. If there is no barcode
     *   found, returns null.
     */
    function scanBarcodeAsync(mediaCapture, zxingReader, frameWidth, frameHeight) {
        // Shortcuts for namespaces
        var Imaging = Windows.Graphics.Imaging;
        var Streams = Windows.Storage.Streams;

        var frame = new Windows.Media.VideoFrame(Imaging.BitmapPixelFormat.bgra8, frameWidth, frameHeight);
        return mediaCapture.getPreviewFrameAsync(frame)
        .then(function (capturedFrame) {

            // Copy captured frame to buffer for further deserialization
            var bitmap = capturedFrame.softwareBitmap;
            var rawBuffer = new Streams.Buffer(bitmap.pixelWidth * bitmap.pixelHeight * 4);
            capturedFrame.softwareBitmap.copyToBuffer(rawBuffer);
            capturedFrame.close();

            // Get raw pixel data from buffer
            var data = new Uint8Array(rawBuffer.length);
            var dataReader = Streams.DataReader.fromBuffer(rawBuffer);
            dataReader.readBytes(data);
            dataReader.close();

            return zxingReader.decode(data, frameWidth, frameHeight, ZXing.BitmapFormat.bgra32);
        });
    }

    var self = this;
    return scanBarcodeAsync(this._capture, this._zxingReader, this._width, this._height)
    .then(function (result) {
        if (self._cancelled)
            return null;

        return result || (self._promise = self.readCode());
    });
};

/**
 * Stops barcode search
 */
BarcodeReader.prototype.stop = function () {
    this._cancelled = true;
};

function degreesToRotation(degrees) {
    switch (degrees) {
        // portrait
        case 90:
            return Windows.Media.Capture.VideoRotation.clockwise90Degrees;
        // landscape
        case 0:
            return Windows.Media.Capture.VideoRotation.none;
        // portrait-flipped
        case 270:
            return Windows.Media.Capture.VideoRotation.clockwise270Degrees;
        // landscape-flipped
        case 180:
            return Windows.Media.Capture.VideoRotation.clockwise180Degrees;
        default:
            // Falling back to portrait default
            return Windows.Media.Capture.VideoRotation.clockwise90Degrees;
    }
}

module.exports = {

    /**
     * Scans image via device camera and retieves barcode from it.
     * @param  {function} success Success callback
     * @param  {function} fail    Error callback
     * @param  {array} args       Arguments array
     */
    scan: function (success, fail, args) {
        var capturePreview,
            capturePreviewAlignmentMark,
            captureCancelButton,
            navigationButtonsDiv,
            previewMirroring,
            closeButton,
            capture,
            reader;

        // Save call state for suspend/resume
        BarcodeReader.scanCallArgs = {
            success: success,
            fail: fail,
            args: args
        };

        function updatePreviewForRotation(evt) {
            if (!capture) {
                return;
            }

            var displayInformation = (evt && evt.target) || Windows.Graphics.Display.DisplayInformation.getForCurrentView();
            var currentOrientation = displayInformation.currentOrientation;

            previewMirroring = capture.getPreviewMirroring();

            // Lookup up the rotation degrees.
            var rotDegree = videoPreviewRotationLookup(currentOrientation, previewMirroring);

            capture.setPreviewRotation(degreesToRotation(rotDegree));
            return WinJS.Promise.as();
        }

        /**
         * Creates a preview frame and necessary objects
         */
        function createPreview() {

            // Create fullscreen preview
            var capturePreviewFrameStyle = document.createElement('link');
            capturePreviewFrameStyle.rel = "stylesheet";
            capturePreviewFrameStyle.type = "text/css";
            capturePreviewFrameStyle.href = urlutil.makeAbsolute("/www/css/plugin-barcodeScanner.css");

            document.head.appendChild(capturePreviewFrameStyle);

            capturePreviewFrame = document.createElement('div');
            capturePreviewFrame.className = "barcode-scanner-wrap";

            capturePreview = document.createElement("video");
            capturePreview.className = "barcode-scanner-preview";
            capturePreview.addEventListener('click', function () {
                focus();
            });

            capturePreviewAlignmentMark = document.createElement('div');
            capturePreviewAlignmentMark.className = "barcode-scanner-mark";

            navigationButtonsDiv = document.createElement("div");
            navigationButtonsDiv.className = "barcode-scanner-app-bar";
            navigationButtonsDiv.onclick = function (e) {
                e.cancelBubble = true;
            };

            closeButton = document.createElement("div");
            closeButton.innerText = "close";
            closeButton.className = "app-bar-action action-close";
            navigationButtonsDiv.appendChild(closeButton);

            BarcodeReader.scanCancelled = false;
            closeButton.addEventListener("click", cancelPreview, false);
            document.addEventListener('backbutton', cancelPreview, false);

            [capturePreview, capturePreviewAlignmentMark, navigationButtonsDiv].forEach(function (element) {
                capturePreviewFrame.appendChild(element);
            });
        }

        function focus(controller) {

            var result = WinJS.Promise.wrap();

            if (!capturePreview || capturePreview.paused) {
                // If the preview is not yet playing, there is no sense in running focus
                return result;
            }

            if (!controller) {
                try {
                    controller = capture && capture.videoDeviceController;
                } catch (err) {
                    console.log('Failed to access focus control for current camera: ' + err);
                    return result;
                }
            }

            if (!controller.focusControl || !controller.focusControl.supported) {
                console.log('Focus control for current camera is not supported');
                return result;
            }

            // Multiple calls to focusAsync leads to internal focusing hang on some Windows Phone 8.1 devices
            // Also need to wrap in try/catch to avoid crash on Surface 3 - looks like focusState property
            // somehow is not accessible there. See https://github.com/phonegap/phonegap-plugin-barcodescanner/issues/288
            try {
                if (controller.focusControl.focusState === Windows.Media.Devices.MediaCaptureFocusState.searching) {
                    return result;
                }
            } catch (e) {
                // Nothing to do - just continue w/ focusing
            }

            // The delay prevents focus hang on slow devices
            return WinJS.Promise.timeout(INITIAL_FOCUS_DELAY)
            .then(function () {
                try {
                    return controller.focusControl.focusAsync().then(function () {
                        return result;
                    }, function (e) {
                        // This happens on mutliple taps
                        if (e.number !== OPERATION_IS_IN_PROGRESS) {
                            console.error('focusAsync failed: ' + e);
                            return WinJS.Promise.wrapError(e);
                        }
                        return result;
                    });
                } catch (e) {
                    // This happens on mutliple taps
                    if (e.number !== OPERATION_IS_IN_PROGRESS) {
                        console.error('focusAsync failed: ' + e);
                        return WinJS.Promise.wrapError(e);
                    }
                    return result;
                }
            });
        }

        function setupFocus(focusControl) {

            function supportsFocusMode(mode) {
                return focusControl.supportedFocusModes.indexOf(mode).returnValue;
            }

            if (!focusControl || !focusControl.supported || !focusControl.configure) {
                return WinJS.Promise.wrap();
            }

            var FocusMode = Windows.Media.Devices.FocusMode;
            var focusConfig = new Windows.Media.Devices.FocusSettings();
            focusConfig.autoFocusRange = Windows.Media.Devices.AutoFocusRange.normal;

            // Determine a focus position if the focus search fails:
            focusConfig.disableDriverFallback = false;

            if (supportsFocusMode(FocusMode.continuous)) {
                console.log("Device supports continuous focus mode");
                focusConfig.mode = FocusMode.continuous;
            } else if (supportsFocusMode(FocusMode.auto)) {
                console.log("Device doesn\'t support continuous focus mode, switching to autofocus mode");
                focusConfig.mode = FocusMode.auto;
            }

            focusControl.configure(focusConfig);

            // Continuous focus should start only after preview has started. See 'Remarks' at
            // https://msdn.microsoft.com/en-us/library/windows/apps/windows.media.devices.focuscontrol.configure.aspx
            function waitForIsPlaying() {
                var isPlaying = !capturePreview.paused && !capturePreview.ended && capturePreview.readyState > 2;

                if (!isPlaying) {
                    return WinJS.Promise.timeout(CHECK_PLAYING_TIMEOUT)
                    .then(function () {
                        return waitForIsPlaying();
                    });
                }

                return focus();
            }

            return waitForIsPlaying();
        }

        function disableZoomAndScroll() {
            document.body.classList.add('no-zoom');
            document.body.classList.add('no-scroll');
        }

        function enableZoomAndScroll() {
            document.body.classList.remove('no-zoom');
            document.body.classList.remove('no-scroll');
        }

        /**
         * Starts stream transmission to preview frame and then run barcode search
         */
        function startPreview() {
            return findCamera()
            .then(function (id) {
                var captureSettings;

                try {
                    captureSettings = new Windows.Media.Capture.MediaCaptureInitializationSettings();
                } catch (e) {
                    if (e.number === REGDB_E_CLASSNOTREG) {
                        throw new Error('Ensure that you have Windows Media Player and Media Feature pack installed.');
                    }

                    throw e;
                }

                captureSettings.streamingCaptureMode = Windows.Media.Capture.StreamingCaptureMode.video;
                captureSettings.photoCaptureSource = Windows.Media.Capture.PhotoCaptureSource.videoPreview;
                captureSettings.videoDeviceId = id;

                capture = new Windows.Media.Capture.MediaCapture();
                return capture.initializeAsync(captureSettings);
            })
            .then(function () {

                var controller = capture.videoDeviceController;
                var deviceProps = controller.getAvailableMediaStreamProperties(Windows.Media.Capture.MediaStreamType.videoPreview);

                deviceProps = Array.prototype.slice.call(deviceProps);
                deviceProps = deviceProps.filter(function (prop) {
                    // filter out streams with "unknown" subtype - causes errors on some devices
                    return prop.subtype !== "Unknown";
                }).sort(function (propA, propB) {
                    // sort properties by resolution
                    return propB.width - propA.width;
                });

                var preferredProps = deviceProps.filter(function(prop){
                    // Filter out props where frame size is between 640*480 and 1280*720
                    return prop.width >= 640 && prop.height >= 480 && prop.width <= 1280 && prop.height <= 720;
                });

                // prefer video frame size between between 640*480 and 1280*720
                // use maximum resolution otherwise
                var maxResProps = preferredProps[0] || deviceProps[0];
                return controller.setMediaStreamPropertiesAsync(Windows.Media.Capture.MediaStreamType.videoPreview, maxResProps)
                .then(function () {
                    return {
                        capture: capture,
                        width: maxResProps.width,
                        height: maxResProps.height
                    };
                });
            })
            .then(function (captureSettings) {

                capturePreview.msZoom = true;
                capturePreview.src = URL.createObjectURL(capture);
                capturePreview.play();

                // Insert preview frame and controls into page
                document.body.appendChild(capturePreviewFrame);

                disableZoomAndScroll();

                return setupFocus(captureSettings.capture.videoDeviceController.focusControl)
                .then(function () {
                    Windows.Graphics.Display.DisplayInformation.getForCurrentView().addEventListener("orientationchanged", updatePreviewForRotation, false);
                    return updatePreviewForRotation();
                })
                .then(function () {

                    if (!Windows.Media.Devices.CameraStreamState) {
                        // CameraStreamState is available starting with Windows 10 so skip this check for 8.1
                        // https://msdn.microsoft.com/en-us/library/windows/apps/windows.media.devices.camerastreamstate
                        return WinJS.Promise.as();
                    }

                    function checkCameraStreamState() {
                        if (capture.cameraStreamState !== Windows.Media.Devices.CameraStreamState.streaming) {

                            // Using loop as MediaCapture.CameraStreamStateChanged does not fire with CameraStreamState.streaming state.
                            return WinJS.Promise.timeout(CAMERA_STREAM_STATE_CHECK_RETRY_TIMEOUT)
                            .then(function () {
                                return checkCameraStreamState();
                            });
                        }

                        return WinJS.Promise.as();
                    }

                    // Ensure CameraStreamState is Streaming
                    return checkCameraStreamState();
                })
                .then(function () {
                    return captureSettings;
                });
            });
        }

        /**
         * Removes preview frame and corresponding objects from window
         */
        function destroyPreview() {
            var promise = WinJS.Promise.as();

            Windows.Graphics.Display.DisplayInformation.getForCurrentView().removeEventListener("orientationchanged", updatePreviewForRotation, false);
            document.removeEventListener('backbutton', cancelPreview);

            if (capturePreview) {
                var isPlaying = !capturePreview.paused && !capturePreview.ended && capturePreview.readyState > 2;
                if (isPlaying) {
                    capturePreview.pause();
                }

                // http://stackoverflow.com/a/28060352/4177762
                capturePreview.src = "";
                if (capturePreview.load) {
                    capturePreview.load();
                }
            }

            if (capturePreviewFrame) {
                try {
                    document.body.removeChild(capturePreviewFrame);
                } catch (e) {
                    // Catching NotFoundError
                    console.error(e);
                }
            }
            capturePreviewFrame = null;

            reader && reader.stop();
            reader = null;

            if (capture) {
                try {
                    promise = capture.stopRecordAsync();
                } catch (e) {
                    // Catching NotFoundError
                    console.error(e);
                }
            }
            capture = null;

            enableZoomAndScroll();

            return promise;
        }

        /**
         * Stops preview and then call success callback with cancelled=true
         * See https://github.com/phonegap-build/BarcodeScanner#using-the-plugin
         */
        function cancelPreview() {
            BarcodeReader.scanCancelled = true;
            reader && reader.stop();
        }

        function checkCancelled() {
            if (BarcodeReader.scanCancelled || BarcodeReader.suspended) {
                throw new Error('Canceled');
            }
        }

        // Timeout is needed so that the .done finalizer below can be attached to the promise.
        BarcodeReader.scanPromise = WinJS.Promise.timeout()
        .then(function() {
            createPreview();
            checkCancelled();
            return startPreview();
        })
        .then(function (captureSettings) {
            checkCancelled();
            reader = BarcodeReader.get(captureSettings.capture);
            reader.init(captureSettings.capture, captureSettings.width, captureSettings.height);

            // Add a small timeout before capturing first frame otherwise
            // we would get an 'Invalid state' error from 'getPreviewFrameAsync'
            return WinJS.Promise.timeout(200)
            .then(function () {
                checkCancelled();
                return reader.readCode();
            });
        })
        .then(function (result) {
            // Suppress null result (cancel) on suspending
            if (BarcodeReader.suspended) {
                return;
            }

            destroyPreview();
            success({
                text: result && result.text,
                format: result && BARCODE_FORMAT[result.barcodeFormat],
                cancelled: !result
            });
        });

        // Catching any errors here
        BarcodeReader.scanPromise.done(function () { }, function (error) {
            // Suppress null result (cancel) on suspending
            if (BarcodeReader.suspended) {
                return;
            }

            destroyPreview();
            if (error.message == 'Canceled') {
                success({
                    cancelled: true
                });
            } else {
                fail(error);
            }
        });

        BarcodeReader.videoPreviewIsVisible = function () {
            return capturePreviewFrame !== null;
        }

        BarcodeReader.destroyPreview = destroyPreview;
    },

    /**
     * Encodes specified data into barcode
     * @param  {function} success Success callback
     * @param  {function} fail    Error callback
     * @param  {array} args       Arguments array
     */
    encode: function (success, fail, args) {
        fail("Not implemented yet");
    }
};

var app = WinJS.Application;

function waitForScanEnd() {
    return BarcodeReader.scanPromise || WinJS.Promise.as();
}

function suspend(args) {
    BarcodeReader.suspended = true;
    if (args) {
        args.setPromise(BarcodeReader.destroyPreview()
        .then(waitForScanEnd, waitForScanEnd));
    } else {
        BarcodeReader.destroyPreview();
    }
}

function resume() {
    BarcodeReader.suspended = false;
    module.exports.scan(BarcodeReader.scanCallArgs.success, BarcodeReader.scanCallArgs.fail, BarcodeReader.scanCallArgs.args);
}

function onVisibilityChanged() {
    if (document.visibilityState === 'hidden'
        && BarcodeReader.videoPreviewIsVisible && BarcodeReader.videoPreviewIsVisible() && BarcodeReader.destroyPreview) {
        suspend();
    } else if (BarcodeReader.suspended) {
        resume();
    }
}

// Windows 8.1 projects
document.addEventListener('msvisibilitychange', onVisibilityChanged);
// Windows 10 projects
document.addEventListener('visibilitychange', onVisibilityChanged);

// About to be suspended
app.addEventListener('checkpoint', function (args) {
    if (BarcodeReader.videoPreviewIsVisible && BarcodeReader.videoPreviewIsVisible() && BarcodeReader.destroyPreview) {
        suspend(args);
    }
});

// Resuming from a user suspension
Windows.UI.WebUI.WebUIApplication.addEventListener("resuming", function () {
    if (BarcodeReader.suspended) {
        resume();
    }
}, false);

require("cordova/exec/proxy").add("BarcodeScanner", module.exports);
