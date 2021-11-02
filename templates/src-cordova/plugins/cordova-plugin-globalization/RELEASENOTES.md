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

### 1.11.0 (Apr 12, 2018)
* Updating `moment.js` to version 2.20.1 (#64)

### 1.0.9 (Dec 15, 2017)
* Deprecated this plugin. Read our migration guide at https://cordova.apache.org/news/2017/11/20/migrate-from-cordova-globalization-plugin.html
* Update moment.js to version `2.19.1`

### 1.0.8 (Nov 06, 2017)
* [CB-13473](https://issues.apache.org/jira/browse/CB-13473) (CI) Removed **Browser** builds from AppVeyor
* [CB-13472](https://issues.apache.org/jira/browse/CB-13472) (CI) Fixed Travis **Android** builds again
* [CB-13299](https://issues.apache.org/jira/browse/CB-13299) (CI) Fix **Android** builds
* [CB-12895](https://issues.apache.org/jira/browse/CB-12895) added `eslint` and removed `jshint`
* [CB-13028](https://issues.apache.org/jira/browse/CB-13028) (CI) **Browser** builds on Travis and AppVeyor
* [CB-12847](https://issues.apache.org/jira/browse/CB-12847) added `bugs` entry to `package.json`.

### 1.0.7 (Apr 27, 2017)
* [CB-12622](https://issues.apache.org/jira/browse/CB-12622) Added **Android 6.0** build badge to `README`
* [CB-12685](https://issues.apache.org/jira/browse/CB-12685) added `package.json` to tests folder

### 1.0.6 (Feb 28, 2017)
* [CB-12029](https://issues.apache.org/jira/browse/CB-12029) **blackberry10**: Remove logging code that causes crashes on **BB10**
* [CB-12369](https://issues.apache.org/jira/browse/CB-12369) Add plugin typings from `DefinitelyTyped`
* [CB-12363](https://issues.apache.org/jira/browse/CB-12363) Added build badges for **iOS 9.3** and **iOS 10.0**
* [CB-11154](https://issues.apache.org/jira/browse/CB-11154) **Windows:** Return `IANA` timezone as an empty string instead of `undefined`
* [CB-11154](https://issues.apache.org/jira/browse/CB-11154) **Android**, **iOS** Add `IANA` timezone
* [CB-12230](https://issues.apache.org/jira/browse/CB-12230) Removed **Windows 8.1** build badges

### 1.0.5 (Dec 07, 2016)
* [CB-12224](https://issues.apache.org/jira/browse/CB-12224) Updated version and RELEASENOTES.md for release 1.0.5
* [CB-11917](https://issues.apache.org/jira/browse/CB-11917) - Remove pull request template checklist item: "iCLA has been submitted…"
* [CB-11832](https://issues.apache.org/jira/browse/CB-11832) Incremented plugin version.

### 1.0.4 (Sep 08, 2016)
* [CB-11795](https://issues.apache.org/jira/browse/CB-11795) Add 'protective' entry to cordovaDependencies
* Add badges for paramedic builds on Jenkins
* Add pull request template.
* [CB-10996](https://issues.apache.org/jira/browse/CB-10996) Adding front matter to README.md

### 1.0.3 (Mar 09, 2016)
* [CB-10792](https://issues.apache.org/jira/browse/CB-10792) -Cannot install cordova-plugin-globalization with cordova-windows on Ubuntu
* [CB-10636](https://issues.apache.org/jira/browse/CB-10636) Add JSHint for plugins
* Minor changes to readme
* [CB-10605](https://issues.apache.org/jira/browse/CB-10605) fix deprecation warnings on **iOS**
* chore: edit package.json license to match SPDX id

### 1.0.2 (Nov 18, 2015)
* [CB-10035](https://issues.apache.org/jira/browse/CB-10035) Updated `RELEASENOTES` to be newest to oldest
* Fixing contribute link.
* [CB-9409](https://issues.apache.org/jira/browse/CB-9409) check that `localeIdentifier` has underscore
* [CB-9476](https://issues.apache.org/jira/browse/CB-9476): `Mobilespec` crash on startup when running on **Windows 10**.
* Fixing license headers and adding `moment.js` to `.ratignore`.

### 1.0.1 (Jun 17, 2015)
* added moment.js to ratignore
* added license headers
* Adding .ratignore file.
* [CB-9128](https://issues.apache.org/jira/browse/CB-9128) cordova-plugin-globalization documentation translation: cordova-plugin-globalization
* fix npm md issue

### 1.0.0 (Apr 15, 2015)
* [CB-8746](https://issues.apache.org/jira/browse/CB-8746) gave plugin major version bump
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) updated tizen and browser specific references of old id to new id
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) changed plugin-id to pacakge-name
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) properly updated translated docs to use new id
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) updated translated docs to use new id
* Use TRAVIS_BUILD_DIR, install paramedic by npm
* separate section in plugin.xml and docs for Windows8 platform
* [CB-7960](https://issues.apache.org/jira/browse/CB-7960) Add cordova-plugin-globalization support for browser platform
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) Updated Readme
* [CB-8659](https://issues.apache.org/jira/browse/CB-8659): ios: 4.0.x Compatibility: Remove use of initWebView method
* [CB-8569](https://issues.apache.org/jira/browse/CB-8569) Integrate TravisCI
* [CB-8438](https://issues.apache.org/jira/browse/CB-8438) cordova-plugin-globalization documentation translation: cordova-plugin-globalization
* [CB-8538](https://issues.apache.org/jira/browse/CB-8538) Added package.json file
* [CB-8394](https://issues.apache.org/jira/browse/CB-8394) pended unsupported tests for windows and wp8

### 0.3.4 (Feb 04, 2015)
* [CB-8351](https://issues.apache.org/jira/browse/CB-8351) ios: Use argumentForIndex rather than NSArray extension
* [CB-7972](https://issues.apache.org/jira/browse/CB-7972) Add cordova-plugin-globalization support for Windows platform

### 0.3.3 (Dec 02, 2014)
* [CB-7977](https://issues.apache.org/jira/browse/CB-7977) Mention `deviceready` in plugin docs
* [CB-7766](https://issues.apache.org/jira/browse/CB-7766) Add quirk note about **Android** `dateToString`
* Errors in weekdays fixedli; `getDateNames` should return (Sun - Sat) in all locales; `getFirstDayOfWeek` should return 1 for Sunday and 2 for Monday; bunch of jsHint fixes
* [CB-7700](https://issues.apache.org/jira/browse/CB-7700) cordova-plugin-globalization documentation translation: cordova-plugin-globalization

### 0.3.2 (Oct 03, 2014)
* [CB-7548](https://issues.apache.org/jira/browse/CB-7548) [BlackBerry10] Re-implement getPreferredLanguage() and getLocaleName().

### 0.3.1 (Sep 17, 2014)
* [CB-6490](https://issues.apache.org/jira/browse/CB-6490) [BlackBerry10] Use hyphen instead of underscore in getLocaleName().
* [CB-7548](https://issues.apache.org/jira/browse/CB-7548) [BlackBerry10] Allow any numeric type as date in dateToString method.
* Hold the information if L10n was ready before.
* [CB-7233](https://issues.apache.org/jira/browse/CB-7233) [BlackBerry10] Globalization is now supported
* Renamed test dir, added nested plugin.xml
* Clean-up: removed duplicate code
* Added test to complete [CB-7064](https://issues.apache.org/jira/browse/CB-7064), added tests that check for W3C compliance in language tags generated from PreferredLanguage and GetLocale methods
* [CB-6962](https://issues.apache.org/jira/browse/CB-6962) Ported globalization tests to framework

### 0.3.0 (Aug 06, 2014)
* The right Apache License 2.0 added
* Update headers and NOTICE file
* [BlackBerry10] Implement Globalization for BB10
* Initial implementation for **FirefoxOS**
* [CB-4602](https://issues.apache.org/jira/browse/CB-4602) ios: Use normalized values for getPreferredLanguage.
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Updated translations for docs
* [CB-4602](https://issues.apache.org/jira/browse/CB-4602) geolocation.getPreferredLanguage and geolocation.getLocaleName now return strings with hypen (-) to stay compliant with current standards

### 0.2.8 (Jun 05, 2014)
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Spanish and French Translations added. Github close #7
* [CB-6805](https://issues.apache.org/jira/browse/CB-6805) Add license
* clean up pull request. this closes #11
* [CB-4602](https://issues.apache.org/jira/browse/CB-4602) Added clarification to docs
* [CB-4602](https://issues.apache.org/jira/browse/CB-4602) [CB-6490](https://issues.apache.org/jira/browse/CB-6490) [CB-4822](https://issues.apache.org/jira/browse/CB-4822) WP Globalization
* getLocale,getLanguage, and docs
* Android should return BCP47 tag, not localized string
* [CB-6491](https://issues.apache.org/jira/browse/CB-6491) add CONTRIBUTING.md
* [CB-5980](https://issues.apache.org/jira/browse/CB-5980) Updated version and RELEASENOTES.md for release 0.2.6

### 0.2.7 (Apr 17, 2014)
* [CB-4908](https://issues.apache.org/jira/browse/CB-4908): [android] Long.valueOf(0) instead of new Long(0)
* [CB-6212](https://issues.apache.org/jira/browse/CB-6212): [iOS] fix warnings compiled under arm64 64-bit
* [CB-6460](https://issues.apache.org/jira/browse/CB-6460): Update license headers
* [CB-6465](https://issues.apache.org/jira/browse/CB-6465): Add license headers to Tizen code
* Add NOTICE file

### 0.2.6 (Feb 05, 2014)
* Add Tizen plugin support

### 0.2.5 (Jan 02, 2014)
* [CB-5658](https://issues.apache.org/jira/browse/CB-5658) Add doc/index.md for Globalization plugin

### 0.2.4 (Dec 4, 2013)
* [ubuntu] add missing file
* add ubuntu platform
* Added amazon-fireos platform. Change to use amazon-fireos as a platform if the user agent string contains 'cordova-amazon-fireos'

### 0.2.3 (Oct 28, 2013)
* [CB-5128](https://issues.apache.org/jira/browse/CB-5128): added repo + issue tag to plugin.xml for globalization plugin
* [CB-4915](https://issues.apache.org/jira/browse/CB-4915) Incremented plugin version on dev branch.

### 0.2.2 (Sept 25, 2013)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) bumping&resetting version
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming org.apache.cordova.core.globalization to org.apache.cordova.globalization
* Rename CHANGELOG.md -> RELEASENOTES.md
* [CB-4752](https://issues.apache.org/jira/browse/CB-4752) Incremented plugin version on dev branch.
