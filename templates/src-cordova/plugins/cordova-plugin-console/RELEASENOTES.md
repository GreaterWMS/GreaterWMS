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

### 1.1.0 (Sep 18, 2017)
* [CB-13170](https://issues.apache.org/jira/browse/CB-13170) Integrated this plugin into `cordova-ios@4.5.0`. This plugin will not install for `cordova-ios >= 4.5.0`.
* [CB-13028](https://issues.apache.org/jira/browse/CB-13028) (CI) **Browser** builds on `Travis` and `AppVeyor`
* [CB-13000](https://issues.apache.org/jira/browse/CB-13000) (CI) Speed up **Android** builds
* [CB-12991](https://issues.apache.org/jira/browse/CB-12991) (CI) Updated CI badges
* [CB-12935](https://issues.apache.org/jira/browse/CB-12935) (**windows**) Enable paramedic builds on AppVeyor
* [CB-12935](https://issues.apache.org/jira/browse/CB-12935) (**ios**, **Android**) Run `paramedic` builds on `Travis`
* [CB-12847](https://issues.apache.org/jira/browse/CB-12847) added `bugs` entry to `package.json`.

### 1.0.7 (Apr 27, 2017)
* [CB-12622](https://issues.apache.org/jira/browse/CB-12622) Added **Android 6.0** build badge to `README`
* [CB-12685](https://issues.apache.org/jira/browse/CB-12685) added `package.json` to tests folder

### 1.0.6 (Feb 28, 2017)
* [CB-12363](https://issues.apache.org/jira/browse/CB-12363) Added build badges for **iOS 9.3** and **iOS 10.0**
* [CB-12230](https://issues.apache.org/jira/browse/CB-12230) Removed **Windows 8.1** build badges

### 1.0.5 (Dec 07, 2016)
* [CB-12224](https://issues.apache.org/jira/browse/CB-12224) Updated version and RELEASENOTES.md for release 1.0.5
* [CB-11917](https://issues.apache.org/jira/browse/CB-11917) - Remove pull request template checklist item: "iCLA has been submitted…"
* [CB-11832](https://issues.apache.org/jira/browse/CB-11832) Incremented plugin version.

### 1.0.4 (Sep 08, 2016)
* [CB-11795](https://issues.apache.org/jira/browse/CB-11795) Add 'protective' entry to `cordovaDependencies`
* add `JIRA` issue tracker link
* Add badges for paramedic builds on Jenkins
* Add pull request template.
* [CB-10996](https://issues.apache.org/jira/browse/CB-10996) Adding front matter to README.md

### 1.0.3 (Apr 15, 2016)
* [CB-10720](https://issues.apache.org/jira/browse/CB-10720) Minor spelling/formatting changes.
* [CB-10636](https://issues.apache.org/jira/browse/CB-10636) Add `JSHint` for plugins

### 1.0.2 (Nov 18, 2015)
* [CB-10035](https://issues.apache.org/jira/browse/CB-10035) Updated `RELEASENOTES` to be newest to oldest
* Fixing contribute link.
* Document formatting options for the console object
* [CB-5089](https://issues.apache.org/jira/browse/CB-5089) Document supported methods for console object
* reverted `d58f218b9149d362ebb0b8ce697cf403569d14cd` because `logger` is not needed on **Android**

### 1.0.1 (Jun 17, 2015)
* move logger.js and console-via-logger.js to common modules, instead of the numerous repeats that were there.
* clean up tests, info is below log level so it does not exist by default.
* add a couple tests
* [CB-9191](https://issues.apache.org/jira/browse/CB-9191) Add basic test
* [CB-9128](https://issues.apache.org/jira/browse/CB-9128) cordova-plugin-console documentation translation: cordova-plugin-console
* attempt to fix npm markdown issue

### 1.0.0 (Apr 15, 2015)
* [CB-8746](https://issues.apache.org/jira/browse/CB-8746) gave plugin major version bump
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) changed plugin-id to pacakge-name
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) updated translated docs to use new id
* Use TRAVIS_BUILD_DIR, install paramedic by npm
* docs: renamed Windows8 to Windows
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) Updated Readme
* [CB-8560](https://issues.apache.org/jira/browse/CB-8560) Integrate TravisCI
* [CB-8438](https://issues.apache.org/jira/browse/CB-8438) cordova-plugin-console documentation translation: cordova-plugin-console
* [CB-8538](https://issues.apache.org/jira/browse/CB-8538) Added package.json file
* [CB-8362](https://issues.apache.org/jira/browse/CB-8362) Add Windows platform section to Console plugin

### 0.2.13 (Feb 04, 2015)
* [CB-8351](https://issues.apache.org/jira/browse/CB-8351) ios: Use argumentForIndex rather than NSArray extension

### 0.2.12 (Dec 02, 2014)
* [CB-7977](https://issues.apache.org/jira/browse/CB-7977) Mention `deviceready` in plugin docs
* [CB-7700](https://issues.apache.org/jira/browse/CB-7700) cordova-plugin-console documentation translation: cordova-plugin-console

### 0.2.11 (Sep 17, 2014)
* [CB-7249](https://issues.apache.org/jira/browse/CB-7249) cordova-plugin-console documentation translation

### 0.2.10 (Aug 06, 2014)
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Updated translations for docs

### 0.2.9 (Jun 05, 2014)
* [CB-6848](https://issues.apache.org/jira/browse/CB-6848) Add Android quirk, list applicable platforms
* [CB-6796](https://issues.apache.org/jira/browse/CB-6796) Add license
* [CB-6491](https://issues.apache.org/jira/browse/CB-6491) add CONTRIBUTING.md

### 0.2.8 (Apr 17, 2014)
* [CB-6460](https://issues.apache.org/jira/browse/CB-6460): Update license headers
* Add NOTICE file

### 0.2.7 (Feb 05, 2014)
* Native console needs to be called DebugConsole to avoid ambiguous reference. This commit requires the 3.4.0 version of the native class factory
* [CB-4718](https://issues.apache.org/jira/browse/CB-4718) fixed Console plugin not working on wp

### 0.2.6 (Jan 02, 2014)
* [CB-5658](https://issues.apache.org/jira/browse/CB-5658) Add doc/index.md for Console plugin

### 0.2.5 (Dec 4, 2013)
* add ubuntu platform

### 0.2.4 (Oct 28, 2013)
* [CB-5154](https://issues.apache.org/jira/browse/CB-5154) log formatting incorrectly to native
* [CB-5128](https://issues.apache.org/jira/browse/CB-5128): added repo + issue tag to plugin.xml for console plugin
* [CB-4915](https://issues.apache.org/jira/browse/CB-4915) Incremented plugin version on dev branch.

### 0.2.3 (Sept 25, 2013)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) bumping&resetting version
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming org.apache.cordova.core.console to org.apache.cordova.console
* Rename CHANGELOG.md -> RELEASENOTES.md
* [CB-4752](https://issues.apache.org/jira/browse/CB-4752) Incremented plugin version on dev branch.


