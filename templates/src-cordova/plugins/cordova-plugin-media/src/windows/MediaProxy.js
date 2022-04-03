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

var Media = require('cordova-plugin-media.Media');
var MediaError = require('cordova-plugin-media.MediaError');

var recordedFile;
var tempFolderAppDataBasePath = 'ms-appdata:///temp/',
    localFolderAppDataBasePath = 'ms-appdata:///local/',
    tempFolderFullPath = Windows.Storage.ApplicationData.current.temporaryFolder.path,
    localFolderFullPath = Windows.Storage.ApplicationData.current.localFolder.path;

var PARAMETER_IS_INCORRECT = -2147024809;
var SUPPORTED_EXTENSIONS = ['.mp3', '.wma', '.wav', '.cda', '.adx', '.wm', '.m3u', '.wmx', '.m4a'];
var SUPPORTED_PREFIXES = ['http', 'https', 'rstp'];

var fsTypes = {
    PERSISTENT: 'PERSISTENT',
    TEMPORARY: 'TEMPORARY'
};

module.exports = {
    mediaCaptureMrg:null,

    // Initiates the audio file
    create:function(win, lose, args) {
        var id = args[0];

        var srcUri = processUri(args[1]);

        var createAudioNode = !!args[2];
        var thisM = Media.get(id);

        Media.prototype.node = null;

        var prefix = args[1].split(':').shift();
        var extension = srcUri.extension;
        if (thisM.node === null) {
            if (SUPPORTED_EXTENSIONS.indexOf(extension) === -1 && SUPPORTED_PREFIXES.indexOf(prefix) === -1) {
                if (lose) {
                    lose({ code: MediaError.MEDIA_ERR_ABORTED });
                }
                return false; // unable to create
            }

            // Don't create Audio object in case of record mode
            if (createAudioNode === true) {
                thisM.node = new Audio();
                thisM.node.msAudioCategory = "BackgroundCapableMedia";
                thisM.node.src = srcUri.absoluteCanonicalUri;

                thisM.node.onloadstart = function () {
                    Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_STARTING);
                };

                thisM.node.ontimeupdate = function (e) {
                    Media.onStatus(id, Media.MEDIA_POSITION, e.target.currentTime);
                };

                thisM.node.onplaying = function () {
                    Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_RUNNING);
                };

                thisM.node.ondurationchange = function (e) {
                    Media.onStatus(id, Media.MEDIA_DURATION, e.target.duration || -1);
                };

                thisM.node.onerror = function (e) {
                    // Due to media.spec.15 It should return MediaError for bad filename
                    var err = e.target.error.code === MediaError.MEDIA_ERR_SRC_NOT_SUPPORTED ?
                        { code: MediaError.MEDIA_ERR_ABORTED } :
                        e.target.error;

                    Media.onStatus(id, Media.MEDIA_ERROR, err);
                };

                thisM.node.onended = function () {
                    Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_STOPPED);
                };
            }
        }

        return true; // successfully created
    },

    // Start playing the audio
    startPlayingAudio:function(win, lose, args) {
        var id = args[0];
        //var src = args[1];
        //var options = args[2];

        var thisM = Media.get(id);
        // if Media was released, then node will be null and we need to create it again
        if (!thisM.node) {
            args[2] = true; // Setting createAudioNode to true
            if (!module.exports.create(win, lose, args)) {
                // there is no reason to continue if we can't create media
                // corresponding callback has been invoked in create so we don't need to call it here
                return;
            }
        }

        try {
            thisM.node.play();
        } catch (err) {
            if (lose) {
                lose({code:MediaError.MEDIA_ERR_ABORTED});
            }
        }
    },

    // Stops the playing audio
    stopPlayingAudio:function(win, lose, args) {
        var id = args[0];
        try {
            var thisM = Media.get(id);
            thisM.node.pause();
            thisM.node.currentTime = 0;
            Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_STOPPED);
        } catch (err) {
            lose("Failed to stop: "+err);
        }
    },

    // Seeks to the position in the audio
    seekToAudio:function(win, lose, args) {
        var id = args[0];
        var milliseconds = args[1];
        var thisM = Media.get(id);
        try {
            thisM.node.currentTime = milliseconds / 1000;
            win(thisM.node.currentTime);
        } catch (err) {
            lose("Failed to seek: "+err);
        }
    },

    // Pauses the playing audio
    pausePlayingAudio:function(win, lose, args) {
        var id = args[0];
        var thisM = Media.get(id);
        try {
            thisM.node.pause();
            Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_PAUSED);
        } catch (err) {
            lose("Failed to pause: "+err);
        }
    },

    // Gets current position in the audio
    getCurrentPositionAudio:function(win, lose, args) {
        var id = args[0];
        try {
            var p = (Media.get(id)).node.currentTime;
            win(p);
        } catch (err) {
            lose(err);
        }
    },

    // Start recording audio
    startRecordingAudio:function(win, lose, args) {
        var id = args[0];
        var srcUri = processUri(args[1]);

        var dest = parseUriToPathAndFilename(srcUri);
        var destFileName = dest.fileName;

        var success = function () {
            Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_RUNNING);
        };

        var error = function (reason) {
            Media.onStatus(id, Media.MEDIA_ERROR, reason);
        };

        // Initialize device
        Media.prototype.mediaCaptureMgr = null;
        var thisM = (Media.get(id));
        var captureInitSettings = new Windows.Media.Capture.MediaCaptureInitializationSettings();
        captureInitSettings.streamingCaptureMode = Windows.Media.Capture.StreamingCaptureMode.audio;
        thisM.mediaCaptureMgr = new Windows.Media.Capture.MediaCapture();
        thisM.mediaCaptureMgr.addEventListener("failed", error);

        thisM.mediaCaptureMgr.initializeAsync(captureInitSettings).done(function (result) {
            thisM.mediaCaptureMgr.addEventListener("recordlimitationexceeded", error);
            thisM.mediaCaptureMgr.addEventListener("failed", error);

            // Start recording
            Windows.Storage.ApplicationData.current.temporaryFolder.createFileAsync(destFileName, Windows.Storage.CreationCollisionOption.replaceExisting).done(function (newFile) {
                recordedFile = newFile;
                var encodingProfile = null;
                switch (newFile.fileType) {
                    case '.m4a':
                        encodingProfile = Windows.Media.MediaProperties.MediaEncodingProfile.createM4a(Windows.Media.MediaProperties.AudioEncodingQuality.auto);
                        break;
                    case '.mp3':
                        encodingProfile = Windows.Media.MediaProperties.MediaEncodingProfile.createMp3(Windows.Media.MediaProperties.AudioEncodingQuality.auto);
                        break;
                    case '.wma':
                        encodingProfile = Windows.Media.MediaProperties.MediaEncodingProfile.createWma(Windows.Media.MediaProperties.AudioEncodingQuality.auto);
                        break;
                    default:
                        error("Invalid file type for record");
                        break;
                }
                thisM.mediaCaptureMgr.startRecordToStorageFileAsync(encodingProfile, newFile).done(success, error);
            }, error);
        }, error);
    },

    // Stop recording audio
    stopRecordingAudio:function(win, lose, args) {
        var id = args[0];
        var thisM = Media.get(id);
        var srcUri = processUri(thisM.src);

        var dest = parseUriToPathAndFilename(srcUri);
        var destPath = dest.path;
        var destFileName = dest.fileName;
        var fsType = dest.fsType;

        var success = function () {
            Media.onStatus(id, Media.MEDIA_STATE, Media.MEDIA_STOPPED);
        };

        var error = function (reason) {
            Media.onStatus(id, Media.MEDIA_ERROR, reason);
        };

        thisM.mediaCaptureMgr.stopRecordAsync().done(function () {
            if (fsType === fsTypes.TEMPORARY) {
                if (!destPath) {
                    // if path is not defined, we leave recorded file in temporary folder (similar to iOS)
                    success();
                } else {
                    Windows.Storage.ApplicationData.current.temporaryFolder.getFolderAsync(destPath).done(function (destFolder) {
                        recordedFile.copyAsync(destFolder, destFileName, Windows.Storage.CreationCollisionOption.replaceExisting).done(success, error);
                    }, error);
                }
            } else {
                // Copying file to persistent storage
                if (!destPath) {
                    recordedFile.copyAsync(Windows.Storage.ApplicationData.current.localFolder, destFileName, Windows.Storage.CreationCollisionOption.replaceExisting).done(success, error);
                } else {
                    Windows.Storage.ApplicationData.current.localFolder.getFolderAsync(destPath).done(function (destFolder) {
                        recordedFile.copyAsync(destFolder, destFileName, Windows.Storage.CreationCollisionOption.replaceExisting).done(success, error);
                    }, error);
                }
            }
        }, error);
    },

    // Release the media object
    release:function(win, lose, args) {
        var id = args[0];
        var thisM = Media.get(id);
        try {
            if (thisM.node) {
                thisM.node.onloadedmetadata = null;
                // Unsubscribing as the media object is being released
                thisM.node.onerror = null;
                // Needed to avoid "0x80070005 - JavaScript runtime error: Access is denied." on copyAsync
                thisM.node.src = null;
                delete thisM.node;
            }
        } catch (err) {
            lose("Failed to release: "+err);
        }
    },
    setVolume:function(win, lose, args) {
        var id = args[0];
        var volume = args[1];
        var thisM = Media.get(id);
        thisM.volume = volume;
    }
};

/**
 * Converts a path to Windows.Foundation.Uri basing on App data temporary folder 
 * if scheme is not defined, e.g.: path/to/file.m4a -> ms-appdata:///temp/path/to/file.m4a
 * @param  {String} src Input path
 * @return {Object}     Windows.Foundation.Uri
 */
function setTemporaryFsByDefault(src) {
    var uri;
    try {
        uri = new Windows.Foundation.Uri(src);
    } catch (e) {
        if (e.number === PARAMETER_IS_INCORRECT) {
            // Use TEMPORARY fs there is no 'scheme:'
            uri = new Windows.Foundation.Uri(tempFolderAppDataBasePath, src);
        } else {
            throw e;
        }
    } finally {
        return uri;
    }
}

/**
 * Convert native full path to ms-appdata path
 * @param  {Object} uri Windows.Foundation.Uri
 * @return {Object}     ms-appdata Windows.Foundation.Uri
 */
function fullPathToAppData(uri) {
    if (uri.schemeName === 'file') {
        if (uri.rawUri.indexOf(Windows.Storage.ApplicationData.current.localFolder.path) !== -1) {
            // Also remove path' beginning slash to avoid losing folder name part
            uri = new Windows.Foundation.Uri(localFolderAppDataBasePath, uri.rawUri.replace(localFolderFullPath, '').replace(/^[\\\/]{1,2}/, ''));
        } else if (uri.rawUri.indexOf(Windows.Storage.ApplicationData.current.temporaryFolder.path) !== -1) {
            uri = new Windows.Foundation.Uri(tempFolderAppDataBasePath, uri.rawUri.replace(tempFolderFullPath, '').replace(/^[\\\/]{1,2}/, ''));
        } else {
            throw new Error('Not supported file uri: ' + uri.rawUri);
        }
    }

    return uri;
}

/**
 * Converts cdvfile paths to ms-appdata path
 * @param  {Object} uri Input cdvfile scheme Windows.Foundation.Uri
 * @return {Object}     Windows.Foundation.Uri based on App data path
 */
function cdvfileToAppData(uri) {
    var cdvFsRoot;

    if (uri.schemeName === 'cdvfile') {
        cdvFsRoot = uri.path.split('/')[1];
        if (cdvFsRoot === 'temporary') {
            return new Windows.Foundation.Uri(tempFolderAppDataBasePath, uri.path.split('/').slice(2).join('/'));
        } else if (cdvFsRoot === 'persistent') {
            return new Windows.Foundation.Uri(localFolderAppDataBasePath, uri.path.split('/').slice(2).join('/'));
        } else {
            throw new Error(cdvFsRoot + ' cdvfile root is not supported on Windows');
        }
    }

    return uri;
}

/**
 * Prepares media src for internal usage
 * @param  {String} src Input media path
 * @return {Object}     Windows.Foundation.Uri
 */
function processUri(src) {
    // Collapse double slashes (File plugin issue): ms-appdata:///temp//recs/memos/media.m4a => ms-appdata:///temp/recs/memos/media.m4a
    src = src.replace(/([^\/:])(\/\/)([^\/])/g, '$1/$3');

    // Remove beginning slashes
    src = src.replace(/^[\\\/]{1,2}/, '');

    var uri = setTemporaryFsByDefault(src);

    uri = fullPathToAppData(uri);
    uri = cdvfileToAppData(uri);

    return uri;
}

/**
 * Extracts path, filename and filesystem type from Uri
 * @param  {Object} uri Windows.Foundation.Uri
 * @return {Object}     Object containing path, filename and filesystem type
 */
function parseUriToPathAndFilename(uri) {
    // Removing scheme and location, using backslashes: ms-appdata:///local/path/to/file.m4a -> path\\to\\file.m4a
    var normalizedSrc = uri.path.split('/').slice(2).join('\\');

    var path = normalizedSrc.substr(0, normalizedSrc.lastIndexOf('\\'));
    var fileName = normalizedSrc.replace(path + '\\', '');

    var fsType;

    if (uri.path.split('/')[1] === 'local') {
        fsType = fsTypes.PERSISTENT;
    } else if (uri.path.split('/')[1] === 'temp') {
        fsType = fsTypes.TEMPORARY;
    }

    return {
        path: path,
        fileName: fileName,
        fsType: fsType
    };
}

require("cordova/exec/proxy").add("Media",module.exports);
