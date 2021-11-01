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

### 2.0.1 (April 13, 2018)
* [CB-14001](https://issues.apache.org/jira/browse/CB-14001): Fix `cordovaDependencies` to allow plugin install

### 2.0.0 (Sep 18, 2017)
* [CB-13068](https://issues.apache.org/jira/browse/CB-13068) added info tag for deprecation
* [CB-12726](https://issues.apache.org/jira/browse/CB-12726) Device Motion - SUNSET
* [CB-13115](https://issues.apache.org/jira/browse/CB-13115) **Browser** Fixed `getCurrentAcceleration()` on **Firefox**, **Safari** and **Edge**
* [CB-13028](https://issues.apache.org/jira/browse/CB-13028) (CI) **Browser** builds on `Travis` and `AppVeyor`
* [CB-13000](https://issues.apache.org/jira/browse/CB-13000) (CI) Speed up **Android** builds
* [CB-12991](https://issues.apache.org/jira/browse/CB-12991) (CI) Updated CI badges
* [CB-12935](https://issues.apache.org/jira/browse/CB-12935) (**windows**) Enable paramedic builds on `AppVeyor`
* [CB-12935](https://issues.apache.org/jira/browse/CB-12935) (**ios**, **Android**) Enable paramedic builds on `Travis CI`
* [CB-12847](https://issues.apache.org/jira/browse/CB-12847) added `bugs` entry to `package.json`.

### 1.2.5 (Apr 27, 2017)
* [CB-12622](https://issues.apache.org/jira/browse/CB-12622) Added **Android 6.0** build badge to `README`
* [CB-12685](https://issues.apache.org/jira/browse/CB-12685) added `package.json` to tests folder
* [CB-10559](https://issues.apache.org/jira/browse/CB-10559) (android) Relaxed a time stamp condition to fix flaky tests

### 1.2.4 (Feb 28, 2017)
* [CB-12353](https://issues.apache.org/jira/browse/CB-12353) Corrected merges usage in `plugin.xml`
* [CB-12369](https://issues.apache.org/jira/browse/CB-12369) Add plugin typings from `DefinitelyTyped`
* [CB-12363](https://issues.apache.org/jira/browse/CB-12363) Added build badges for **iOS 9.3** and **iOS 10.0**
* [CB-12230](https://issues.apache.org/jira/browse/CB-12230) Removed **Windows 8.1** build badges

### 1.2.3 (Dec 07, 2016)
* [CB-12224](https://issues.apache.org/jira/browse/CB-12224) Updated version and RELEASENOTES.md for release 1.2.3
* [CB-11917](https://issues.apache.org/jira/browse/CB-11917) - Remove pull request template checklist item: "iCLA has been submitted…"
* [CB-11832](https://issues.apache.org/jira/browse/CB-11832) Incremented plugin version.

### 1.2.2 (Sep 08, 2016)
* [CB-11795](https://issues.apache.org/jira/browse/CB-11795) Add 'protective' entry to cordovaDependencies
* [CB-11482](https://issues.apache.org/jira/browse/CB-11482) Fix unreliable tests on **Android**
* [CB-11531](https://issues.apache.org/jira/browse/CB-11531) Restart `Accelerometer` on `CyanogenMod 13`
* Add badges for paramedic builds on Jenkins
* Add pull request template.
* [CB-11188](https://issues.apache.org/jira/browse/CB-11188) `cordova-plugin-device-motion-tests` are failing in CI
* [CB-10996](https://issues.apache.org/jira/browse/CB-10996) Adding front matter to README.md

### 1.2.1 (Apr 15, 2016)
* [CB-10636](https://issues.apache.org/jira/browse/CB-10636) Add `JSHint` for plugins

### 1.2.0 (Nov 18, 2015)
* [CB-10035](https://issues.apache.org/jira/browse/CB-10035) Updated `RELEASENOTES` to be newest to oldest
* access all `accel` properties via getters
* Return error when `accelerometer` not available, skip/pending tests when accel not available, use getters for properties
* Returning an `OK PluginResult.Status` when starting
* Update `README.md`
* Added **Android** quirk 
* Fixing contribute link.
* [CB-9426](https://issues.apache.org/jira/browse/CB-9426) Fix exception when using device motion plugin on **browser** platform.
* [CB-9339](https://issues.apache.org/jira/browse/CB-9339) Increase the default sensor accuracy

### 1.1.1 (Jun 17, 2015)
* [CB-9128](https://issues.apache.org/jira/browse/CB-9128) cordova-plugin-device-motion documentation translation: cordova-plugin-device-motion
* fix npm md issue
* [CB-8842](https://issues.apache.org/jira/browse/CB-8842) Return cached values on Android if there is no updates from sensor

### 1.1.0 (May 06, 2015)
* [CB-8926](https://issues.apache.org/jira/browse/CB-8926): The tests module tries to access an undefined global `Accelerometer` on fail callbacks.  This results in another JS error, `ReferenceError: 'Accelerometer' is undefined.`  This change passes through the error message instead of attempting to index into it.
* [CB-8876](https://issues.apache.org/jira/browse/CB-8876) Introduced a small timeout between tests
* [CB-8876](https://issues.apache.org/jira/browse/CB-8876) Rewrote **wp8** impementation to be more stable

### 1.0.0 (Apr 15, 2015)
* [CB-8746](https://issues.apache.org/jira/browse/CB-8746) gave plugin major version bump
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) updated windows and tizen specific references of old id to new id
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) changed plugin-id to pacakge-name
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) properly updated translated docs to use new id
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) updated translated docs to use new id
* Use TRAVIS_BUILD_DIR, install paramedic by npm
* [CB-8312](https://issues.apache.org/jira/browse/CB-8312) Multiply accelerometer values by -g on Windows
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) Updated Readme
* [CB-8562](https://issues.apache.org/jira/browse/CB-8562) Integrate TravisCI
* [CB-8438](https://issues.apache.org/jira/browse/CB-8438) cordova-plugin-device-motion documentation translation: cordova-plugin-device-motion
* [CB-8538](https://issues.apache.org/jira/browse/CB-8538) Added package.json file
* [CB-8096](https://issues.apache.org/jira/browse/CB-8096) Pended recently added spec.12 if accelerometer doesn't exist on the device
* [CB-8096](https://issues.apache.org/jira/browse/CB-8096) Pended auto tests if accelerometer doesn't exist on the device
* [CB-8083](https://issues.apache.org/jira/browse/CB-8083) Adds test to make sure success callback is called each time

### 0.2.11 (Dec 02, 2014)
* [CB-8083](https://issues.apache.org/jira/browse/CB-8083) Fix `accelerometer` callback on **Windows**
* Renamed **Windows8** -> **Windows**
* [CB-7977](https://issues.apache.org/jira/browse/CB-7977) Mention `deviceready` in plugin docs
* [CB-7700](https://issues.apache.org/jira/browse/CB-7700) cordova-plugin-device-motion documentation translation: cordova-plugin-device-motion
* [CB-7571](https://issues.apache.org/jira/browse/CB-7571) Bump version of nested plugin to match parent plugin

### 0.2.10 (Sep 17, 2014)
* [CB-7471](https://issues.apache.org/jira/browse/CB-7471) cordova-plugin-device-motion documentation translation: cordova-plugin-device-motion
* Updated doc for browser
* Added support for the browser
* [CB-7249](https://issues.apache.org/jira/browse/CB-7249) cordova-plugin-device-motion documentation translation
* [CB-7313](https://issues.apache.org/jira/browse/CB-7313) minor tweak to documentation of watchAcceleration function parameters
* [CB-7160](https://issues.apache.org/jira/browse/CB-7160) move to tests dir, add nested plugin.xml
* Removed js-module for tests from plugin.xml
* [CB-7160](https://issues.apache.org/jira/browse/CB-7160) added manual tests
* added documentation for manual tests
* Removed js-module for tests from plugin.xml
* [CB-7160](https://issues.apache.org/jira/browse/CB-7160) added manual tests
* Changing cdvtest format to use module exports
* register tests using new style
* update
* Feature Branch: First attempt at new-style-tests

### 0.2.9 (Aug 06, 2014)
* [FFOS] update accelerometer.js
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Updated translations for docs
* FFOS added to supported platforms

### 0.2.8 (Jun 05, 2014)
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Spanish and French Translations added. Github close #10. Github close #12. Github close #11
* ubuntu: don't destroy callback after use
* [CB-6798](https://issues.apache.org/jira/browse/CB-6798) Add license
* [CB-6491](https://issues.apache.org/jira/browse/CB-6491) add CONTRIBUTING.md
* FFOS added to supported platforms

### 0.2.7 (Apr 17, 2014)
* [CB-6422](https://issues.apache.org/jira/browse/CB-6422): [windows8] use cordova/exec/proxy
* [CB-6460](https://issues.apache.org/jira/browse/CB-6460): Update license headers
* [CB-6465](https://issues.apache.org/jira/browse/CB-6465): Add license headers to Tizen code
* Add NOTICE file

### 0.2.6 (Feb 05, 2014)
* Add Tizen support

### 0.2.5 (Jan 02, 2014)
* [CB-5658](https://issues.apache.org/jira/browse/CB-5658) Add doc/index.md for Device Motion plugin

### 0.2.4 (Dec 4, 2013)
* add ubuntu platform
* 1. Added amazon-fireos platform. 2. Change to use amazon-fireos as the platform if the user agent string contains 'cordova-amazon-fireos'

### 0.2.3 (Oct 28, 2013)
* tweak scoping
* fixed the scope
* properly stop watching...
* adding timestamp to the response
* fix acceleromter for firefox os
* update firefoxos integration
* fixed callbacks
* accelerometer registers, but is not responding
* fxos added, not working
* [CB-5128](https://issues.apache.org/jira/browse/CB-5128): added repo + issue tag to plugin.xml for device motion
* [CB-5012](https://issues.apache.org/jira/browse/CB-5012) ensure result is returned
* [CB-4825](https://issues.apache.org/jira/browse/CB-4825) Add CoreMotion.framework to plugin.xml
* [CB-4825](https://issues.apache.org/jira/browse/CB-4825) avoid retain cycle in update block
* [CB-4825](https://issues.apache.org/jira/browse/CB-4825) use CoreMotion framework for accelerometer
* [CB-4915](https://issues.apache.org/jira/browse/CB-4915) Incremented plugin version on dev branch.

### 0.2.2 (Sept 25, 2013)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) bumping&resetting version
* [windows8] commandProxy was moved
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming core inside windows8
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming org.apache.cordova.core.device-motion to org.apache.cordova.device-motion
* Rename CHANGELOG.md -> RELEASENOTES.md
* [CB-4752](https://issues.apache.org/jira/browse/CB-4752) Incremented plugin version on dev branch.
