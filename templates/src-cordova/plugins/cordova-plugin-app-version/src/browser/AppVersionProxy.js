"use strict";

var cache = null;

function readConfig(success, fail) {
    if(cache === null) {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", function () {
            try {
                var parser = new DOMParser();
                var doc = parser.parseFromString(xhr.responseText, "application/xml");
                var widget = doc.getElementsByTagName("widget").item(0);

                cache = {
                    appVersion: widget.getAttribute('version'),
                    appName: widget.getElementsByTagName("name").item(0).textContent,
                    packageName: widget.getAttribute('id'),
                    versionCode: widget.getAttribute('browser-versionCode')
                };
                success(cache);
            }
            catch(e) {
                fail(e);
            }
        });

        xhr.addEventListener("error", function () {
            fail(e);
        });
        xhr.open("get", "../config.xml", true);
        xhr.send();
    }
    else {
        setTimeout(function() {
            success(cache);
        },0);
    }
}


var getAppVersion = function (success, fail) {
    readConfig(function(data) {
        success(data.appVersion);
    }, fail);
};

getAppVersion.getAppName = function (success, fail) {
    readConfig(function(data) {
        success(data.appName);
    }, fail);
};

getAppVersion.getPackageName = function (success, fail) {
    readConfig(function(data) {
        success(data.packageName);
    }, fail);
};

getAppVersion.getVersionNumber = function (success, fail) {
    readConfig(function(data) {
        success(data.appVersion);
    }, fail);
};

getAppVersion.getVersionCode = function (success, fail) {
    readConfig(function(data) {
        success(data.versionCode);
    }, fail);
};

module.exports = getAppVersion;


require("cordova/exec/proxy").add("AppVersion", module.exports);

