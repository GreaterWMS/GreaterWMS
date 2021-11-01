---
title: Console
description: Get JavaScript logs in your native logs.
---
<!---
# license: Licensed to the Apache Software Foundation (ASF) under one
#         or more contributor license agreements.  See the NOTICE file
#         distributed with this work for additional information
#         regarding copyright ownership.  The ASF licenses this file
#         to you under the Apache License, Version 2.0 (the
#         "License"); you may not use this file except in compliance
#         with the License.  You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
#         Unless required by applicable law or agreed to in writing,
#         software distributed under the License is distributed on an
#         "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#         KIND, either express or implied.  See the License for the
#         specific language governing permissions and limitations
#         under the License.
-->

|AppVeyor|Travis CI|
|:-:|:-:|
|[![Build status](https://ci.appveyor.com/api/projects/status/github/apache/cordova-plugin-console?branch=master)](https://ci.appveyor.com/project/ApacheSoftwareFoundation/cordova-plugin-console)|[![Build Status](https://travis-ci.org/apache/cordova-plugin-console.svg?branch=master)](https://travis-ci.org/apache/cordova-plugin-console)|

# cordova-plugin-console

## Deprecated

> This plugin is no longer being worked on as the functionality provided by this plugin is now included in cordova-ios 4.5.0 or greater, and support is already built in to cordova-windows > 5.0.0. You should upgrade your application to use version 2.0.0 of this plugin. It will detect whether or not the plugin is required based on the version of cordova-ios and cordova-windows your app uses.
> Please file issues for this plugin against their respective platforms (cordova-ios, cordova-windows).

## Description

This plugin is meant to ensure that console.log() is as useful as it can be.
It adds additional function for iOS, Ubuntu, Windows Phone 8, and Windows. If
you are happy with how console.log() works for you, then you probably
don't need this plugin.

This plugin defines a global `console` object.

Although the object is in the global scope, features provided by this plugin
are not available until after the `deviceready` event.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log("console.log works well");
    }

:warning: Report issues on the [Apache Cordova issue tracker](https://issues.apache.org/jira/issues/?jql=project%20%3D%20CB%20AND%20status%20in%20%28Open%2C%20%22In%20Progress%22%2C%20Reopened%29%20AND%20resolution%20%3D%20Unresolved%20AND%20component%20%3D%20%22Plugin%20Console%22%20ORDER%20BY%20priority%20DESC%2C%20summary%20ASC%2C%20updatedDate%20DESC)


## Installation

    cordova plugin add cordova-plugin-console

### Android Quirks

On some platforms other than Android, console.log() will act on multiple
arguments, such as console.log("1", "2", "3"). However, Android will act only
on the first argument. Subsequent arguments to console.log() will be ignored.
This plugin is not the cause of that, it is a limitation of Android itself.

## Supported Methods

The plugin support following methods of the `console` object:

- `console.log`
- `console.error`
- `console.exception`
- `console.warn`
- `console.info`
- `console.debug`
- `console.assert`
- `console.dir`
- `console.dirxml`
- `console.time`
- `console.timeEnd`
- `console.table`

## Partially supported Methods

Methods of the `console` object which implemented, but behave different from browser implementation:

- `console.group`
- `console.groupCollapsed`

The grouping methods are just log name of the group and don't actually indicate grouping for later
calls to `console` object methods.

## Not supported Methods

Methods of the `console` object which are implemented, but do nothing:

- `console.clear`
- `console.trace`
- `console.groupEnd`
- `console.timeStamp`
- `console.profile`
- `console.profileEnd`
- `console.count`

## Supported formatting

The following formatting options available:

Format chars:

*  `%j` - format arg as JSON
*  `%o` - format arg as JSON
*  `%c` - format arg as `''`. No color formatting could be done.
*  `%%` - replace with `'%'`

Any other char following `%` will format its arg via `toString()`.
