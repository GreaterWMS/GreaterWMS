# Cordova AppVersion plugin [unsupported]

Reads the version of your app from the target build settings.

We're [looking for maintainers](https://github.com/sampart/cordova-plugin-app-version/issues/100)!

## Installation

### With cordova-cli

If you are using [cordova-cli](https://github.com/apache/cordova-cli), install
with:

    cordova plugin add cordova-plugin-app-version

### With plugman

With a plain [plugman](https://github.com/apache/cordova-plugman), you should be
able to install with something like:

    plugman --platform <ios|android> --project <directory> --plugin https://github.com/sampart/cordova-plugin-app-version.git

### Manually in iOS

TODO: Write these instructions

### Manually in Android

TODO: Write these instructions

## Use from Javascript

If you are using jQuery, AngularJS, WinJS or any Promise/A library (Bluebird), promise style is supported. Use something like:

    cordova.getAppVersion.getVersionNumber().then(function (version) {
        $('.version').text(version);
    });

If not, pass a callback function:

    cordova.getAppVersion.getVersionNumber(function (version) {
        alert(version);
    });

In addition to the version number you can also retrieve other details about your application:

### getAppName

Returns the name of the app. E.g. "My Awesome App"

### getPackageName

Returns the package name of the app - the reversed domain name app identifier like com.example.myawesomeapp

### getVersionCode

Returns the build identifier of the app

### getVersionNumber

Returns the version number of the app

## Credits

Written by [Robert (Jamie) Munro](http://twitter.com/rjmunro) at
[White October](http://whiteoctober.co.uk/)

Various others have contributed fixes and new features. See the CHANGELOG.md for details.

Original code based on the following Stack Overflow posts:

* [iOS](http://stackoverflow.com/a/14713364/3408)
* [Android](http://stackoverflow.com/a/3637686/3408)
