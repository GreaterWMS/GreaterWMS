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

// Default parameter values including image size can be changed in `config.xml`
var splashImageWidth = 170;
var splashImageHeight = 200;
var position = { x: 0, y: 0, width: splashImageWidth, height: splashImageHeight };
var localSplash; // the image to display
var localSplashImage;
var bgColor = '#464646';
var imageSrc = '/img/logo.png';
var splashScreenDelay = 3000; // in milliseconds
var showSplashScreen = true; // show splashcreen by default
var cordova = require('cordova');
var configHelper = cordova.require('cordova/confighelper');
var autoHideSplashScreen = true;

function updateImageLocation () {
    position.width = Math.min(splashImageWidth, window.innerWidth);
    position.height = position.width * (splashImageHeight / splashImageWidth);

    localSplash.style.width = window.innerWidth + 'px';
    localSplash.style.height = window.innerHeight + 'px';
    localSplash.style.top = '0px';
    localSplash.style.left = '0px';

    localSplashImage.style.top = '50%';
    localSplashImage.style.left = '50%';
    localSplashImage.style.height = position.height + 'px';
    localSplashImage.style.width = position.width + 'px';
    localSplashImage.style.marginTop = (-position.height / 2) + 'px';
    localSplashImage.style.marginLeft = (-position.width / 2) + 'px';
}

function onResize () {
    updateImageLocation();
}

var SplashScreen = {
    setBGColor: function (cssBGColor) {
        bgColor = cssBGColor;
        if (localSplash) {
            localSplash.style.backgroundColor = bgColor;
        }
    },
    show: function () {
        if (!localSplash) {
            window.addEventListener('resize', onResize, false);
            localSplash = document.createElement('div');
            localSplash.style.backgroundColor = bgColor;
            localSplash.style.position = 'absolute';
            localSplash.style['z-index'] = '99999';

            localSplashImage = document.createElement('img');
            localSplashImage.src = imageSrc;
            localSplashImage.style.position = 'absolute';

            updateImageLocation();

            localSplash.appendChild(localSplashImage);
            document.body.appendChild(localSplash);

            // deviceready fires earlier than the plugin init on cold-start
            if (SplashScreen.shouldHideImmediately) {
                SplashScreen.shouldHideImmediately = false;
                window.setTimeout(function () {
                    SplashScreen.hide();
                }, 1000);
            }
        }
    },
    hide: function () {
        if (localSplash) {
            var innerLocalSplash = localSplash;
            localSplash = null;
            window.removeEventListener('resize', onResize, false);

            innerLocalSplash.style.opacity = '0';
            innerLocalSplash.style['-webkit-transition'] = 'opacity 1s ease-in-out';
            innerLocalSplash.style['-moz-transition'] = 'opacity 1s ease-in-out';
            innerLocalSplash.style['-ms-transition'] = 'opacity 1s ease-in-out';
            innerLocalSplash.style['-o-transition'] = 'opacity 1s ease-in-out';

            window.setTimeout(function () {
                document.body.removeChild(innerLocalSplash);
                innerLocalSplash = null;
            }, 1000);
        } else {
            SplashScreen.shouldHideImmediately = true;
        }
    }
};

/**
 * Reads preferences via ConfigHelper and substitutes default parameters.
 */
function readPreferencesFromCfg (cfg) {
    try {
        var value = cfg.getPreferenceValue('ShowSplashScreen');
        if (typeof value !== 'undefined') {
            showSplashScreen = value === 'true';
        }

        splashScreenDelay = cfg.getPreferenceValue('SplashScreenDelay') || splashScreenDelay;
        splashScreenDelay = parseInt(splashScreenDelay, 10);

        imageSrc = cfg.getPreferenceValue('SplashScreen') || imageSrc;
        bgColor = cfg.getPreferenceValue('SplashScreenBackgroundColor') || bgColor;
        splashImageWidth = cfg.getPreferenceValue('SplashScreenWidth') || splashImageWidth;
        splashImageHeight = cfg.getPreferenceValue('SplashScreenHeight') || splashImageHeight;
        autoHideSplashScreen = cfg.getPreferenceValue('AutoHideSplashScreen') || autoHideSplashScreen;
        autoHideSplashScreen = (autoHideSplashScreen === true || autoHideSplashScreen.toLowerCase() === 'true');
    } catch (e) {
        var msg = '[Browser][SplashScreen] Error occurred on loading preferences from config.xml: ' + JSON.stringify(e);
        console.error(msg);
    }
}

/**
 * Shows and hides splashscreen if it is enabled, with a delay according the current preferences.
 */
function showAndHide () {
    if (showSplashScreen) {
        SplashScreen.show();

        window.setTimeout(function () {
            SplashScreen.hide();
        }, splashScreenDelay);
    }
}

/**
 * Tries to read config.xml and override default properties and then shows and hides splashscreen if it is enabled.
 */
(function initAndShow () {
    configHelper.readConfig(function (config) {
        readPreferencesFromCfg(config);
        if (autoHideSplashScreen) {
            showAndHide();
        } else {
            SplashScreen.show();
        }
    }, function (err) {
        console.error(err);
    });
})();

module.exports = SplashScreen;

require('cordova/exec/proxy').add('SplashScreen', SplashScreen);
