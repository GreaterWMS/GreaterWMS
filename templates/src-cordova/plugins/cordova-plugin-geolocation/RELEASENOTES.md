<!--
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
-->
# Release Notes

### 4.1.0 (Nov 06, 2020)

* [GH-214](https://github.com/apache/cordova-plugin-geolocation/pull/214) chore(npm): rebuild `package-lock.json`
* [GH-209](https://github.com/apache/cordova-plugin-geolocation/pull/209) ci(travis): update osx xcode image
* ci(travis): updates **Android** API level
* [GH-202](https://github.com/apache/cordova-plugin-geolocation/pull/202) chore: adds `package-lock` file
* [GH-200](https://github.com/apache/cordova-plugin-geolocation/pull/200) refactor(`eslint`): use `cordova-eslint` /w fix
* [GH-201](https://github.com/apache/cordova-plugin-geolocation/pull/201) chore(npm): use short notation in `package.json`
* chore(asf): update git notification settings
* chore: update `CONTRIBUTING.md`
* [GH-194](https://github.com/apache/cordova-plugin-geolocation/pull/194) docs: Removed misleading text
* [GH-181](https://github.com/apache/cordova-plugin-geolocation/pull/181) Add missing information for **iOS**
* [GH-193](https://github.com/apache/cordova-plugin-geolocation/pull/193) ci: updates Node.js versions
* [GH-192](https://github.com/apache/cordova-plugin-geolocation/pull/192) chore(npm): improve ignore list
* [GH-189](https://github.com/apache/cordova-plugin-geolocation/pull/189) Variable for Require GPS Hardware
* ci(travis): upgrade to node8

### 4.0.2 (Jun 27, 2019)

-   chore: fix repo and issue urls and license in package.json and plugin.xml ([`4d2e901`](https://github.com/apache/cordova-plugin-geolocation/commit/4d2e901))
-   build: add `.gitattributes` to force LF (instead of possible CRLF on Windows) ([`74417bb`](https://github.com/apache/cordova-plugin-geolocation/commit/74417bb))
-   build: add `.npmignore` to remove unneeded files from npm package ([`d4a1ac5`](https://github.com/apache/cordova-plugin-geolocation/commit/d4a1ac5))
-   ci(travis): Update Travis CI configuration for new paramedic ([#154](https://github.com/apache/cordova-plugin-geolocation/issues/154)) ([`1636d98`](https://github.com/apache/cordova-plugin-geolocation/commit/1636d98))
-   chore(github): Add or update GitHub pull request and issue template ([`6fd7847`](https://github.com/apache/cordova-plugin-geolocation/commit/6fd7847))
-   docs: remove JIRA link ([`2fc992b`](https://github.com/apache/cordova-plugin-geolocation/commit/2fc992b))
-   docs: Remove outdated docs translations ([#117](https://github.com/apache/cordova-plugin-geolocation/issues/117)) ([`9408fdd`](https://github.com/apache/cordova-plugin-geolocation/commit/9408fdd))
-   ci(travis): add android-27 to `android update sdk -u --filter` ([`3b1f63a`](https://github.com/apache/cordova-plugin-geolocation/commit/3b1f63a))
-   fix(ios): [CB-14020](https://issues.apache.org/jira/browse/CB-14020) (ios) Fix "Collection was mutated while being enumerated" crash ([#104](https://github.com/apache/cordova-plugin-geolocation/issues/104)) ([`ba45595`](https://github.com/apache/cordova-plugin-geolocation/commit/ba45595))
-   docs: Add Apache Cordova issue tracker link to Readme ([#107](https://github.com/apache/cordova-plugin-geolocation/issues/107)) ([`91c7313`](https://github.com/apache/cordova-plugin-geolocation/commit/91c7313))
-   ci(travis): [CB-13748](https://issues.apache.org/jira/browse/CB-13748) Add build-tools-26.0.2 to travis ([#103](https://github.com/apache/cordova-plugin-geolocation/issues/103)) ([`a6cbe40`](https://github.com/apache/cordova-plugin-geolocation/commit/a6cbe40), [`e74c87a`](https://github.com/apache/cordova-plugin-geolocation/commit/e74c87a))
-   docs: Fix release notes ([#102](https://github.com/apache/cordova-plugin-geolocation/issues/102)) ([`e679a5d`](https://github.com/apache/cordova-plugin-geolocation/commit/e679a5d))


### 4.0.1 (Dec 27, 2017)
* [CB-13705](https://issues.apache.org/jira/browse/CB-13705) Fix to allow 4.0.0 version install

### 4.0.0 (Dec 15, 2017)
* [CB-13664](https://issues.apache.org/jira/browse/CB-13664) remove deprecated platforms

### 3.0.0 (Nov 06, 2017)
* [CB-13267](https://issues.apache.org/jira/browse/CB-13267) (iOS): Remove **iOS** usage descriptions
* [CB-13516](https://issues.apache.org/jira/browse/CB-13516) (all): Add 'protective' entry to `cordovaDependencies`
* [CB-13472](https://issues.apache.org/jira/browse/CB-13472) (CI) Fixed Travis **Android** builds again
* [CB-13294](https://issues.apache.org/jira/browse/CB-13294) Remove `cordova-plugin-compat`
* [CB-13299](https://issues.apache.org/jira/browse/CB-13299) (CI) Fix **Android** builds
* [CB-12895](https://issues.apache.org/jira/browse/CB-12895) added `eslint` and removed `jshint`
* [CB-12847](https://issues.apache.org/jira/browse/CB-12847) added `bugs` entry to `package.json`.

### 2.4.3 (Apr 27, 2017)
* [CB-12622](https://issues.apache.org/jira/browse/CB-12622) Added **Android 6.0** build badge to `README`
* [CB-12685](https://issues.apache.org/jira/browse/CB-12685) added `package.json` to tests folder

### 2.4.2 (Feb 28, 2017)
* [CB-12363](https://issues.apache.org/jira/browse/CB-12363) Added build badges for **iOS 9.3** and **iOS 10.0**
* [CB-12230](https://issues.apache.org/jira/browse/CB-12230) Removed **Windows 8.1** build badges

### 2.4.1 (Dec 07, 2016)
* [CB-12224](https://issues.apache.org/jira/browse/CB-12224) Updated version and RELEASENOTES.md for release 2.4.1
* corrected KCLAuthorizationStatus error, changed to always removed user of [manager locationServicesEnabled].  Must return [CLLocationManager locationServicesEnabled] or 'none'
* [CB-11962](https://issues.apache.org/jira/browse/CB-11962) (ios) Added variable for setting NSLocationWhenInUseUsageDescription
* [CB-11917](https://issues.apache.org/jira/browse/CB-11917) - Remove pull request template checklist item: "iCLA has been submitted…"
* [CB-11904](https://issues.apache.org/jira/browse/CB-11904) Incremented plugin version.

### 2.4.0 (Sep 26, 2016)
* **Ubuntu** Fix altitude & accuracies retrieval
* [CB-11875](https://issues.apache.org/jira/browse/CB-11875) added `android.hardware.location.gps` `uses-feature`.

### 2.3.0 (Sep 08, 2016)
* [CB-11795](https://issues.apache.org/jira/browse/CB-11795) Add 'protective' entry to cordovaDependencies
* Plugin uses `Android Log class` and not `Cordova LOG class`
* Add badges for paramedic builds on Jenkins
* Add pull request template.
* Adding links to reference content and sample content to the top of the readme file
* Update **iOS** geolocation plugin to avoid `THREAD WARNING: ['Geolocation']`, operation occurs in new Thread
* [CB-10996](https://issues.apache.org/jira/browse/CB-10996) Adding front matter to README.md

### 2.2.0 (Apr 15, 2016)
* Replace `PermissionHelper.java` with `cordova-plugin-compat`
* [CB-10691](https://issues.apache.org/jira/browse/CB-10691) Check the context to avoid null errors
* [CB-10636](https://issues.apache.org/jira/browse/CB-10636) Add `JSHint` for plugins
* Using a fallback epsilon in case `Number.EPSILON` is not defined.
* [CB-10574](https://issues.apache.org/jira/browse/CB-10574) MobileSpec can't get results for **WP8.1** Builds

### 2.1.0 (Jan 15, 2016)
* [CB-10319](https://issues.apache.org/jira/browse/CB-10319) **Android** Adding reflective helper methods for permission requests
* [CB-8523](https://issues.apache.org/jira/browse/CB-8523) Fixed accuracy when `enableHighAccuracy: false` on **iOS**.
* [CB-10286](https://issues.apache.org/jira/browse/CB-10286) Don't skip automatic tests on **Android** devices
* [CB-10277](https://issues.apache.org/jira/browse/CB-10277) Error callback should be called w/ `PositionError` when location access is denied
* [CB-10285](https://issues.apache.org/jira/browse/CB-10285) Added tests for `PositionError` constants
* [CB-10278](https://issues.apache.org/jira/browse/CB-10278) geolocation `watchPosition` doesn't return `watchID` string
* [CB-8443](https://issues.apache.org/jira/browse/CB-8443) **Android** nothing happens if `GPS` is turned off
* [CB-10204](https://issues.apache.org/jira/browse/CB-10204) Fix `getCurrentPosition` options on **Android**
* [CB-7146](https://issues.apache.org/jira/browse/CB-7146) Remove built-in `WebView navigator.geolocation` manual tests
* [CB-2845](https://issues.apache.org/jira/browse/CB-2845) `PositionError` constants not attached to prototype as specified in W3C document

### 2.0.0 (Nov 18, 2015)
* [CB-10035](https://issues.apache.org/jira/browse/CB-10035) Updated `RELEASENOTES` to be newest to oldest
* [CB-9907](https://issues.apache.org/jira/browse/CB-9907) Handle **iOS** tests that fail when ios simulator does not have a location
* [CB-8826](https://issues.apache.org/jira/browse/CB-8826) Check for `NSLocationWhenInUseUsageDescription` first
* [CB-9105](https://issues.apache.org/jira/browse/CB-9105): Fixing `JS` errors in the shim
* Added support for new permissions model for **Android 6.0** aka **Marshmallow**
* Expect `lastPosition` to have a `timestamp` that is already in `msecs`
* [CB-4596](https://issues.apache.org/jira/browse/CB-4596) Date objects are supposed to be `DOMTimeStamp`
* Fixing contribute link.
* [CB-9355](https://issues.apache.org/jira/browse/CB-9355) Fix Geolocation plugin start watch fail related to unset `MovementThreshold` on **Windows 10**

### 1.0.1 (Jun 17, 2015)
* [CB-9128](https://issues.apache.org/jira/browse/CB-9128) cordova-plugin-geolocation documentation translation: cordova-plugin-geolocation
* fix npm md issue
* [CB-8845](https://issues.apache.org/jira/browse/CB-8845) Updated comment why Android tests are currently pended
* [CB-8845](https://issues.apache.org/jira/browse/CB-8845) Pended tests for Android
* Add more install text for legacy versions of cordova tools. This closes #36

### 1.0.0 (Apr 15, 2015)
* [CB-8746](https://issues.apache.org/jira/browse/CB-8746) gave plugin major version bump
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) changed plugin-id to pacakge-name
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) properly updated translated docs to use new id
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) updated translated docs to use new id
* Use TRAVIS_BUILD_DIR, install paramedic by npm
* [CB-8681](https://issues.apache.org/jira/browse/CB-8681) Fixed occasional test failures
* docs: added Windows to supported platforms
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) Updated Readme
* [CB-8659](https://issues.apache.org/jira/browse/CB-8659): ios: 4.0.x Compatibility: Remove use of initWebView method
* [CB-8659](https://issues.apache.org/jira/browse/CB-8659): ios: 4.0.x Compatibility: Remove use of deprecated headers
* Wrong parameter in Firefox OS plugin
* [CB-8568](https://issues.apache.org/jira/browse/CB-8568) Integrate TravisCI
* [CB-8438](https://issues.apache.org/jira/browse/CB-8438) cordova-plugin-geolocation documentation translation: cordova-plugin-geolocation
* [CB-8538](https://issues.apache.org/jira/browse/CB-8538) Added package.json file
* [CB-8443](https://issues.apache.org/jira/browse/CB-8443) Geolocation tests fail on Windows due to done is called multiple times

### 0.3.12 (Feb 04, 2015)
* [CB-8351](https://issues.apache.org/jira/browse/CB-8351) ios: Use argumentForIndex rather than NSArray extension

### 0.3.11 (Dec 02, 2014)
* Do not stop updating location when the error is `kCLErrorLocationUnknown`
* [CB-8094](https://issues.apache.org/jira/browse/CB-8094) Pended auto tests for **Windows** Store since they require user interaction
* [CB-8085](https://issues.apache.org/jira/browse/CB-8085) Fix geolocation plugin on **Windows**
* [CB-7977](https://issues.apache.org/jira/browse/CB-7977) Mention `deviceready` in plugin docs
* [CB-7700](https://issues.apache.org/jira/browse/CB-7700) cordova-plugin-geolocation documentation translation: cordova-plugin-geolocation

### 0.3.10 (Sep 17, 2014)
* [CB-7556](https://issues.apache.org/jira/browse/CB-7556) iOS: Clearing all Watches does not stop Location Services
* [CB-7158](https://issues.apache.org/jira/browse/CB-7158) Fix geolocation for ios 8
* Revert [CB-6911](https://issues.apache.org/jira/browse/CB-6911) partially (keeping Info.plist key installation for iOS 8)
* [CB-6911](https://issues.apache.org/jira/browse/CB-6911) Geolocation fails in iOS 8
* [CB-5114](https://issues.apache.org/jira/browse/CB-5114) **Windows 8.1** - Use a new proxy as old geolocation methods is deprecated
* [CB-5114](https://issues.apache.org/jira/browse/CB-5114) Append **Windows 8.1** into plugin.xml + Optimize Windows 8 Geolocation proxy
* Renamed test dir, added nested plugin.xml
* added documentation for manual tests
* [CB-7146](https://issues.apache.org/jira/browse/CB-7146) Added manual tests
* Removed js-module for tests from plugin.xml
* Changing cdvtest format to use module exports
* register tests using new style
* Convert tests to new style
* Removed amazon-fireos code for geolocation.
* [CB-7571](https://issues.apache.org/jira/browse/CB-7571) Bump version of nested plugin to match parent plugin

### 0.3.9 (Aug 06, 2014)
* **FFOS** update GeolocationProxy.js
* [CB-7187](https://issues.apache.org/jira/browse/CB-7187) ios: Add explicit dependency on CoreLocation.framework
* [CB-7187](https://issues.apache.org/jira/browse/CB-7187) Delete unused #import of CDVShared.h
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Updated translations for docs
* ios: Changed distanceFilter from none to 5 meters, prevents it from spamming the callback even though nothing changed.

### 0.3.8 (Jun 05, 2014)
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Spanish and French Translations added. Github close #14
* [CB-6804](https://issues.apache.org/jira/browse/CB-6804) Add license
* [CB-5416](https://issues.apache.org/jira/browse/CB-5416) - Adding support for auto-managing permissions
* [CB-6491](https://issues.apache.org/jira/browse/CB-6491) add CONTRIBUTING.md
* pass by only coords
* proper implementation for firefoxos
* call FxOS's getCurrentProxy added

### 0.3.7 (Apr 17, 2014)
* [CB-6422](https://issues.apache.org/jira/browse/CB-6422): [windows8] use cordova/exec/proxy
* [CB-6212](https://issues.apache.org/jira/browse/CB-6212): [iOS] fix warnings compiled under arm64 64-bit
* [CB-5977](https://issues.apache.org/jira/browse/CB-5977): [android] Removing the Android Geolocation Code.  Mission Accomplished.
* [CB-6460](https://issues.apache.org/jira/browse/CB-6460): Update license headers
* Add NOTICE file

### 0.3.6 (Feb 05, 2014)
* add ubuntu platform support
* [CB-5326](https://issues.apache.org/jira/browse/CB-5326) adding FFOS permission and updating supported platforms
* [CB-5729](https://issues.apache.org/jira/browse/CB-5729) [BlackBerry10] Update GeolocationProxy to return collapsed object

### 0.3.5 (Jan 02, 2014)
* [CB-5658](https://issues.apache.org/jira/browse/CB-5658) Add doc/index.md for Geolocation plugin
* windows8: adds missing reference to PositionError (w/o it the app crashes)
* Removing incorrectly added closing comments for wp7 platform in plugin.xml

### 0.3.4 (Dec 4, 2013)
* Append proxy to platform definition in plugin.xml
* Append windows 8 Geolocation proxy
* Code clean-up for android src.
* Updated amazon-fireos platform + reverting some of the fixes in android code.
* Added amazon-fireos platform + some of the fixes in android code.
* [CB-5334](https://issues.apache.org/jira/browse/CB-5334) [BlackBerry10] Use command proxy
* call FxOS's getCurrentProxy added
* pass by only coords
* proper implementation for firefoxos

### 0.3.3 (Oct 28, 2013)
* [CB-5128](https://issues.apache.org/jira/browse/CB-5128): add repo + issue tag to plugin.xml for geolocation plugin
* [CB-4915](https://issues.apache.org/jira/browse/CB-4915) Incremented plugin version on dev branch.

### 0.3.2 (Sept 25, 2013)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) bumping&resetting version
* [BlackBerry10] removed uneeded permission tags in plugin.xml
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming org.apache.cordova.core.geolocation to org.apache.cordova.geolocation

### 0.3.0 (Sept 5, 2013)
* Added support for windows 8 (Adds required permission)
