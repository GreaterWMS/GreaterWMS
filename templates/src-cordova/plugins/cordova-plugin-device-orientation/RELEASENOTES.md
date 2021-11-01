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

### 2.0.1 (April 13, 2017)
* [CB-14002](https://issues.apache.org/jira/browse/CB-14002): Fix `cordovaDependencies` to allow plugin install 

### 2.0.0 (Sep 18, 2017)
* [CB-13076](https://issues.apache.org/jira/browse/CB-13076) added deprecation notice to info tag
* [CB-12728](https://issues.apache.org/jira/browse/CB-12728) Device Orientation - SUNSET
* [CB-13028](https://issues.apache.org/jira/browse/CB-13028) (CI) **Browser** builds on `Travis` and `AppVeyor`
* [CB-12667](https://issues.apache.org/jira/browse/CB-12667) Reset changes for searching Samsung sensors
* [CB-13000](https://issues.apache.org/jira/browse/CB-13000) (CI) Speed up **Android** builds
* [CB-12991](https://issues.apache.org/jira/browse/CB-12991) (CI) Updated CI badges
* [CB-12935](https://issues.apache.org/jira/browse/CB-12935) (**windows**) Enable paramedic builds on `AppVeyor`
* [CB-12935](https://issues.apache.org/jira/browse/CB-12935) (**ios**, **Android**) Enable paramedic builds on `Travis CI`
* [CB-12667](https://issues.apache.org/jira/browse/CB-12667) **Android**: Added logic for searching sensors from Samsung vendor
* [CB-12847](https://issues.apache.org/jira/browse/CB-12847) added `bugs` entry to `package.json`.

### 1.0.7 (Apr 27, 2017)
* [CB-12622](https://issues.apache.org/jira/browse/CB-12622) Added **Android 6.0** build badge to `README`
* [CB-12685](https://issues.apache.org/jira/browse/CB-12685) added `package.json` to tests folder

### 1.0.6 (Feb 28, 2017)
* [CB-12353](https://issues.apache.org/jira/browse/CB-12353) Corrected merges usage in `plugin.xml`
* [CB-12369](https://issues.apache.org/jira/browse/CB-12369) Add plugin typings from `DefinitelyTyped`
* [CB-12363](https://issues.apache.org/jira/browse/CB-12363) Added build badges for **iOS 9.3** and **iOS 10.0**
* [CB-12230](https://issues.apache.org/jira/browse/CB-12230) Removed **Windows 8.1** build badges

### 1.0.5 (Dec 07, 2016)
* [CB-12224](https://issues.apache.org/jira/browse/CB-12224) Updated version and RELEASENOTES.md for release 1.0.5
* [CB-9179](https://issues.apache.org/jira/browse/CB-9179) (ios) Fixed trueHeading being always 0
* [CB-11917](https://issues.apache.org/jira/browse/CB-11917) - Remove pull request template checklist item: "iCLA has been submitted…"
* [CB-11832](https://issues.apache.org/jira/browse/CB-11832) Incremented plugin version.

### 1.0.4 (Sep 08, 2016)
* [CB-11795](https://issues.apache.org/jira/browse/CB-11795) Add 'protective' entry to cordovaDependencies
* Add badges for paramedic builds on Jenkins
* Add pull request template.
* [CB-10996](https://issues.apache.org/jira/browse/CB-10996) Adding front matter to README.md
* Removed ios quirk code + documentation

### 1.0.3 (Apr 15, 2016)
* Remove `warning` emoji, as it doesn't correctly display in the docs website: http://cordova.apache.org/docs/en/dev/cordova-plugin-device-orientation/index.html
* [CB-10636](https://issues.apache.org/jira/browse/CB-10636) Add `JSHint` for plugins

### 1.0.2 (Nov 18, 2015)
* [CB-10035](https://issues.apache.org/jira/browse/CB-10035) Updated `RELEASENOTES` to be newest to oldest
* [CB-4596](https://issues.apache.org/jira/browse/CB-4596) Fix `timestamp` to be `DOMTimeStamp` across the board
* Fixing contribute link.
* [CB-9426](https://issues.apache.org/jira/browse/CB-9426) Fix exception when using device orientation plugin on **browser** platform.

### 1.0.1 (Jun 17, 2015)
* [CB-9128](https://issues.apache.org/jira/browse/CB-9128) cordova-plugin-device-orientation documentation translation: cordova-plugin-device-orientation
* fix npm md issue
* Remove console log message from test

### 1.0.0 (Apr 15, 2015)
* [CB-8746](https://issues.apache.org/jira/browse/CB-8746) gave plugin major version bump
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) updated windows and tizen specific references of old id to new id
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) changed plugin-id to pacakge-name
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) properly updated translated docs to use new id
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) updated translated docs to use new id
* Use TRAVIS_BUILD_DIR, install paramedic by npm
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) Updated Readme
* [CB-8659](https://issues.apache.org/jira/browse/CB-8659): ios: 4.0.x Compatibility: Remove use of initWebView method
* [CB-8659](https://issues.apache.org/jira/browse/CB-8659): ios: 4.0.x Compatibility: Remove use of deprecated headers
* force async callbacks
* Updated plugin to be 'windows' instead of 'windows8'
* [CB-8614](https://issues.apache.org/jira/browse/CB-8614) Fixed getCurrentHeading and watchHeading on windows platform
* [CB-8563](https://issues.apache.org/jira/browse/CB-8563) Integrate TravisCI
* [CB-8438](https://issues.apache.org/jira/browse/CB-8438) cordova-plugin-device-orientation documentation translation: cordova-plugin-device-orientation
* [CB-8538](https://issues.apache.org/jira/browse/CB-8538) Added package.json file
* [CB-8458](https://issues.apache.org/jira/browse/CB-8458) Fixes false failure of test, when compass hardware is not available

### 0.3.11 (Feb 04, 2015)
* [CB-8351](https://issues.apache.org/jira/browse/CB-8351) ios: Use argumentForIndex rather than NSArray extension

### 0.3.10 (Dec 02, 2014)
* [CB-7977](https://issues.apache.org/jira/browse/CB-7977) Mention `deviceready` in plugin docs
* [CB-7700](https://issues.apache.org/jira/browse/CB-7700) cordova-plugin-device-orientation documentation translation: cordova-plugin-device-orientation
* [CB-7571](https://issues.apache.org/jira/browse/CB-7571) Bump version of nested plugin to match parent plugin

### 0.3.9 (Sep 17, 2014)
* [CB-7471](https://issues.apache.org/jira/browse/CB-7471) cordova-plugin-device-orientation documentation translation: cordova-plugin-device-orientation
* Fixed problem with watchCompass if pressed twice
* [CB-7086](https://issues.apache.org/jira/browse/CB-7086) Renamed dir, added nested plugin.xml
* added documentation for manual tests
* Fixed problem with watchCompass if pressed twice
* [CB-7086](https://issues.apache.org/jira/browse/CB-7086) Renamed dir, added nested plugin.xml
* added documentation for manual tests
* Updated docs for browser
* Add support for the browser
* [CB-7249](https://issues.apache.org/jira/browse/CB-7249) cordova-plugin-device-orientation documentation translation
* [CB-6960](https://issues.apache.org/jira/browse/CB-6960) Added manual tests
* [CB-6960](https://issues.apache.org/jira/browse/CB-6960) Port compass tests to plugin-test-framework

### 0.3.8 (Aug 06, 2014)
* **FFOS** update compass.js
* [CB-7187](https://issues.apache.org/jira/browse/CB-7187) ios: Add explicit dependency on CoreLocation.framework
* [CB-7187](https://issues.apache.org/jira/browse/CB-7187) Delete unused #import of CDVShared.h

### 0.3.7 (Jun 05, 2014)
* [CB-6799](https://issues.apache.org/jira/browse/CB-6799) Add license
* windows8. makes getHeading callback spec compliant
* [CB-6491](https://issues.apache.org/jira/browse/CB-6491) add CONTRIBUTING.md

### 0.3.6 (Apr 17, 2014)
* [CB-6381](https://issues.apache.org/jira/browse/CB-6381): [WP8] unexpected error object
* [CB-6422](https://issues.apache.org/jira/browse/CB-6422): [windows8] use cordova/exec/proxy
* [CB-6460](https://issues.apache.org/jira/browse/CB-6460): Update license headers
* [CB-6465](https://issues.apache.org/jira/browse/CB-6465): Add license headers to Tizen code
* Add NOTICE file

### 0.3.5 (Feb 05, 2014)
* [ubuntu] request sensors permission
* [ubuntu] add missing files
* Add support for Tizen.
* FFOS info added

### 0.3.4 (Jan 02, 2014)
* [CB-5658](https://issues.apache.org/jira/browse/CB-5658) Add doc/index.md for Compass plugin

### 0.3.3 (Dec 4, 2013)
* add ubuntu platform
* 1. Added amazon-fireos platform. 2. Change to use amazon-fireos as a platform if user agent string contains 'cordova-amazon-fireos'.

### 0.3.2 (Oct 28, 2013)
* orientation plugin
* [CB-5128](https://issues.apache.org/jira/browse/CB-5128): added repo + issue tag to plugin.xml for device orientation plugin
* [CB-4915](https://issues.apache.org/jira/browse/CB-4915) Incremented plugin version on dev branch.

### 0.3.1 (Sept 25, 2013)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming id
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming core in CompassProxy
* [CB-4900](https://issues.apache.org/jira/browse/CB-4900) Windows 8 Compass plugin have extra define breaks plugin loading
* [windows8] commandProxy was moved
* Rename CHANGELOG.md -> RELEASENOTES.md
* [CB-4752](https://issues.apache.org/jira/browse/CB-4752) Incremented plugin version on dev branch.

### 0.3.0 (Sept 5, 2013)
* [CB-3687](https://issues.apache.org/jira/browse/CB-3687) Added blackberry10 support
