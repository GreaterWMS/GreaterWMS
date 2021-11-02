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

### 2.0.2 (Jun 18, 2019)

-   build: add .npmignore to remove unneeded files from npm package ([`91513f1`](https://github.com/apache/cordova-plugin-dialogs/commit/91513f1))
-   build: add .gitattributes to force LF (instead of possible CRLF on Windows) ([`d4e8607`](https://github.com/apache/cordova-plugin-dialogs/commit/d4e8607))
-   docs(android): mention 2 lines content limit ([#125](https://github.com/apache/cordova-plugin-dialogs/issues/125)) ([`292e13a`](https://github.com/apache/cordova-plugin-dialogs/commit/292e13a))
-   ci(travis): Update Travis CI configuration for new paramedic ([#127](https://github.com/apache/cordova-plugin-dialogs/issues/127)) ([`f6e4165`](https://github.com/apache/cordova-plugin-dialogs/commit/f6e4165))
-   refactor(android): Cleanup Dialog plugin code ([#123](https://github.com/apache/cordova-plugin-dialogs/issues/123)) ([`419a838`](https://github.com/apache/cordova-plugin-dialogs/commit/419a838))
-   chore(github) Add or update GitHub pull request and issue template ([`d5f09ce`](https://github.com/apache/cordova-plugin-dialogs/commit/d5f09ce))
-   refactor: Cleanup: remove trailing whitespace ([#120](https://github.com/apache/cordova-plugin-dialogs/issues/120)) ([`ed0e465`](https://github.com/apache/cordova-plugin-dialogs/commit/ed0e465))
-   docs: remove JIRA link ([`0057715`](https://github.com/apache/cordova-plugin-dialogs/commit/0057715))
-   docs: Remove docs translations ([#107](https://github.com/apache/cordova-plugin-dialogs/issues/107)) ([`b87526e`](https://github.com/apache/cordova-plugin-dialogs/commit/b87526e))
-   ci(travis): also accept terms for android sdk `android-27` ([#102](https://github.com/apache/cordova-plugin-dialogs/issues/102)) ([`6d88a8c`](https://github.com/apache/cordova-plugin-dialogs/commit/6d88a8c), [`2bc54cf`](https://github.com/apache/cordova-plugin-dialogs/commit/2bc54cf))
-   ci(travis): CB-13756: Add build-tools-26.0.2 to travis ([`ef89d9f`](https://github.com/apache/cordova-plugin-dialogs/commit/ef89d9f))
-   chore(release): Fix release notes ([#101](https://github.com/apache/cordova-plugin-dialogs/issues/101)) ([`c24c733`](https://github.com/apache/cordova-plugin-dialogs/commit/c24c733))

### 2.0.1 (Dec 27, 2017)
* [CB-13703](https://issues.apache.org/jira/browse/CB-13703) Fix to allow 2.0.0 version install

### 2.0.0 (Dec 15, 2017)
* [CB-13671](https://issues.apache.org/jira/browse/CB-13671) Remove deprecated platforms
* [CB-13555](https://issues.apache.org/jira/browse/CB-13555) (ios) Present notification view controller by `InAppBrowser` view controller (#98)

### 1.3.4 (Nov 06, 2017)
* [CB-13473](https://issues.apache.org/jira/browse/CB-13473) (CI) Removed **Browser** builds from AppVeyor
* [CB-13472](https://issues.apache.org/jira/browse/CB-13472) (CI) Fixed Travis **Android** builds again
* [CB-12895](https://issues.apache.org/jira/browse/CB-12895) setup `eslint` and removed `jshint`
* [CB-13028](https://issues.apache.org/jira/browse/CB-13028) (CI) **Browser** builds on Travis and AppVeyor
* [CB-4615](https://issues.apache.org/jira/browse/CB-4615) document **Android** quirk around maximum number of button labels supported for the `confirm` method.
* [CB-13000](https://issues.apache.org/jira/browse/CB-13000) (CI) Speed up **Android** builds
* [CB-12847](https://issues.apache.org/jira/browse/CB-12847) added `bugs` entry to `package.json`.

### 1.3.3 (Apr 27, 2017)
* [CB-12622](https://issues.apache.org/jira/browse/CB-12622) Added **Android 6.0** build badge to `README`
* [CB-12685](https://issues.apache.org/jira/browse/CB-12685) added `package.json` to tests folder

### 1.3.2 (Feb 28, 2017)
* [CB-12353](https://issues.apache.org/jira/browse/CB-12353) Corrected merges usage in `plugin.xml`
* [CB-12369](https://issues.apache.org/jira/browse/CB-12369) Add plugin typings from `DefinitelyTyped`
* [CB-12363](https://issues.apache.org/jira/browse/CB-12363) Added build badges for **iOS 9.3** and **iOS 10.0**
* [CB-12230](https://issues.apache.org/jira/browse/CB-12230) Removed **Windows 8.1** build badges

### 1.3.1 (Dec 07, 2016)
* [CB-12224](https://issues.apache.org/jira/browse/CB-12224) Updated version and RELEASENOTES.md for release 1.3.1
* [CB-11917](https://issues.apache.org/jira/browse/CB-11917) - Remove pull request template checklist item: "iCLA has been submitted…"
* Replace empty buttonLabel with 'OK'
* Make sure the alert buttonLabel is a string
* Add enter key handling and map to default button.
* Added test for [windows] [CB-11281](https://issues.apache.org/jira/browse/CB-11281) when called without defaultText
* [CB-11832](https://issues.apache.org/jira/browse/CB-11832) Incremented plugin version.

### 1.3.0 (Sep 08, 2016)
* [CB-11832](https://issues.apache.org/jira/browse/CB-11832) updated missing header file
* Select the text and put default value in the input directly.
* [CB-11281](https://issues.apache.org/jira/browse/CB-11281) **windows**: `defaultText` is not taken as input if no input by user fixed
* Separated `CSS` from `JS` code. Fixed the prompt dialog CSS to look close to native. Fixed the positioning of the prompt dialog for Windows. Fixed minor JSHint issues.
* [CB-11795](https://issues.apache.org/jira/browse/CB-11795) Add 'protective' entry to cordovaDependencies
* [CB-8773](https://issues.apache.org/jira/browse/CB-8773) Fix for **iOS 8** keyboard not appearing on prompt
* [CB-11677](https://issues.apache.org/jira/browse/CB-11677) **Android**: made text, entered to prompt dialog visible
* CB-8947:(**ios**) Fix crash. Convert non-string messages to strings. Added tests.
* Add badges for paramedic builds on Jenkins
* Add pull request template.
* [CB-11218](https://issues.apache.org/jira/browse/CB-11218) Convert button list to appropriate type
* Simply add **Browser** to supported platforms
* [CB-10996](https://issues.apache.org/jira/browse/CB-10996) Adding front matter to README.md

### 1.2.1 (Apr 15, 2016)
* [CB-10097](https://issues.apache.org/jira/browse/CB-10097) dialog doesn't show on **iOS** when called from a select list `onChange` event
* Remove `warning` emoji, as it doesn't correctly display in the docs website: http://cordova.apache.org/docs/en/dev/cordova-plugin-dialogs/index.html
* [CB-10727](https://issues.apache.org/jira/browse/CB-10727) Dialogs plugin has warnings on **iOS**
* [CB-10636](https://issues.apache.org/jira/browse/CB-10636) Add `JSHint` for plugins

### 1.2.0 (Nov 18, 2015)
* [CB-10035](https://issues.apache.org/jira/browse/CB-10035) Updated `RELEASENOTES` to be newest to oldest
* [CB-8549](https://issues.apache.org/jira/browse/CB-8549) Updated source to pass `Fortify` scan.
* Fixing contribute link.
* add `CSS class` to prompt `div` for **Windows** platform
* [CB-9347](https://issues.apache.org/jira/browse/CB-9347) - fix to allow to stack multiple `UIAlertControllers`

### 1.1.1 (Jun 17, 2015)
* [CB-9128](https://issues.apache.org/jira/browse/CB-9128) cordova-plugin-dialogs documentation translation: cordova-plugin-dialogs
* fix npm md

### 1.1.0 (May 06, 2015)
* [CB-8928](https://issues.apache.org/jira/browse/CB-8928): Removed direct call to `toStaticHTML`, only call it if we are sure it's present. This closes #52
* [CB-7734](https://issues.apache.org/jira/browse/CB-7734) - `navigator.notification.alert` or `navigator.notification.confirm` seem have a "many words" issue. (closes #39)
 
### 1.0.0 (Apr 15, 2015)
* [CB-8746](https://issues.apache.org/jira/browse/CB-8746) gave plugin major version bump
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) updated wp and bb specific references of old id to new id
* [CB-8683](https://issues.apache.org/jira/browse/CB-8683) changed plugin-id to pacakge-name
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) properly updated translated docs to use new id
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) updated translated docs to use new id
* Use TRAVIS_BUILD_DIR, install paramedic by npm
* [CB-8653](https://issues.apache.org/jira/browse/CB-8653) Updated Readme
* [CB-8659](https://issues.apache.org/jira/browse/CB-8659): ios: 4.0.x Compatibility: Remove use of deprecated headers
* [CB-8565](https://issues.apache.org/jira/browse/CB-8565) Integrate TravisCI
* [CB-8438](https://issues.apache.org/jira/browse/CB-8438) cordova-plugin-dialogs documentation translation: cordova-plugin-dialogs
* [CB-8538](https://issues.apache.org/jira/browse/CB-8538) Added package.json file
* [CB-8367](https://issues.apache.org/jira/browse/CB-8367) [org.apache.cordova.dialogs] Add Prompt support on Windows

### 0.3.0 (Feb 04, 2015)
* Correct way to specify Windows platform in config.xml
* [CB-8351](https://issues.apache.org/jira/browse/CB-8351) ios: Use argumentForIndex rather than NSArray extension
* [CB-7955](https://issues.apache.org/jira/browse/CB-7955) Add support "browser" platform

### 0.2.11 (Dec 02, 2014)
* [CB-7737](https://issues.apache.org/jira/browse/CB-7737) lower min height for alert
* [CB-8038](https://issues.apache.org/jira/browse/CB-8038) backslash getting escaped twice in **BB10**
* [CB-8029](https://issues.apache.org/jira/browse/CB-8029) test 1-based indexing for confirm
* [CB-7639](https://issues.apache.org/jira/browse/CB-7639) Update docs + manual tests
* [CB-7639](https://issues.apache.org/jira/browse/CB-7639) Revert back `isAlertShowing` flag in case of exception to prevent queuing of future dialogs.
* [CB-7639](https://issues.apache.org/jira/browse/CB-7639) Handle button labels as array on windows
* [CB-7977](https://issues.apache.org/jira/browse/CB-7977) Mention `deviceready` in plugin docs
* Check for `setTextDirection` API level
* **Android** Make spinner dialog to use `THEME_DEVICE_DEFAULT_LIGHT` (same as the other dialogs)
* **Android** Unbreak `API` level < `14`
* [CB-7414](https://issues.apache.org/jira/browse/CB-7414) **BB10** Document callback parameter for `navigator.notification.alert`
* [CB-7700](https://issues.apache.org/jira/browse/CB-7700) cordova-plugin-dialogs documentation translation: cordova-plugin-dialogs
* [CB-7571](https://issues.apache.org/jira/browse/CB-7571) Bump version of nested plugin to match parent plugin

### 0.2.10 (Sep 17, 2014)
* [CB-7538](https://issues.apache.org/jira/browse/CB-7538) Android beep thread fix Beep now executes in it's own thread. It was previously executing in the main UI thread which was causing the application to lock up will the beep was occurring.  Closing pull request
* Set dialog text dir to locale
* Renamed test dir, added nested plugin.xml
* added documentation for manual tests
* [CB-6965](https://issues.apache.org/jira/browse/CB-6965) Added manual tests
* [CB-6965](https://issues.apache.org/jira/browse/CB-6965) Port notification tests to test-framework

### 0.2.9 (Aug 06, 2014)
* ubuntu: pass proper arguments to prompt callback
* ubuntu: use TextField instead of TextInput
* ubuntu: proper message escaping before passing to qml
* **FFOS** update notification.js
* [CB-6127](https://issues.apache.org/jira/browse/CB-6127) Updated translations for docs
* android: Explicitly apply default theme to dialogs
* Fix Beep exception on Android when no argument passed

### 0.2.8 (Jun 05, 2014)
* [CB-6801](https://issues.apache.org/jira/browse/CB-6801) Add license
* running original windows.open, inAppBrowser is overriding it no need to place CSS in every page anymore
* [CB-5945](https://issues.apache.org/jira/browse/CB-5945) [Windows8] do not call success callbacks until dialog is dismissed
* [CB-4616](https://issues.apache.org/jira/browse/CB-4616) Returned index 0 was not documented for notification.prompt
* update docs to state that prompt is supported on windowsphone
* [CB-6528](https://issues.apache.org/jira/browse/CB-6528) allow scroll on alert message content
* [CB-6628][amazon-fireos]dialogs plugin's confirm and prompt methods dont work confirm() method was missing amazon-fireos platform check. added that. prompt() method had bug. It is executed in a worker thread that does not have a message queue(or Looper object) associated with it and hence "can't create a handler" exception is thrown. To fix this issue, we need to create the EditText widget from within the UI thread. This was fixed sometime ago when we added fireos platform but commit got lost somewhere. So fixing it again now.
* [CB-6491](https://issues.apache.org/jira/browse/CB-6491) add CONTRIBUTING.md
* Added check for isFinishing() on the parent activity to prevent crashes when trying to display dialogs when activity is in this phase of it's lifecycle
* [CB-4966](https://issues.apache.org/jira/browse/CB-4966) Dialogs are in window now No need to add anything to manifest or index.html
* Removing FirefoxOS Quirks * no need to add special permission (it's different API with the same name) * notification.css is added automatically

### 0.2.7 (Apr 17, 2014)
* [CB-6212](https://issues.apache.org/jira/browse/CB-6212): [iOS] fix warnings compiled under arm64 64-bit
* [CB-6411](https://issues.apache.org/jira/browse/CB-6411): [BlackBerry10] Work around Audio playback issue
* [CB-6411](https://issues.apache.org/jira/browse/CB-6411): [BlackBerry10] Updates to beep
* [CB-6422](https://issues.apache.org/jira/browse/CB-6422): [windows8] use cordova/exec/proxy
* [CB-6460](https://issues.apache.org/jira/browse/CB-6460): Update license headers
* Add NOTICE file

### 0.2.6 (Feb 05, 2014)
* no need to recreate the manifest.webapp file after each `cordova prepare` for FFOS
* FFOS description added

### 0.2.5 (Jan 02, 2014)
* [CB-4696](https://issues.apache.org/jira/browse/CB-4696) Fix compile error for Xcode 4.5.
* [CB-5658](https://issues.apache.org/jira/browse/CB-5658) Add doc/index.md for Dialogs plugin
* [CB-3762](https://issues.apache.org/jira/browse/CB-3762) Change prompt default to empty string
* Move images from css to img

### 0.2.4 (Dec 4, 2013)
* add ubuntu platform
* 1. Added amazon-fireos platform. 2. Change to use amazon-fireos as a platform if user agent string contains 'cordova-amazon-fireos'.
* added beep funtionality using ms-winsoundevent:Notfication.Default

### 0.2.3 (Oct 28, 2013)
* [CB-5128](https://issues.apache.org/jira/browse/CB-5128): added repo + issue tag to plugin.xml for dialogs plugin
* new plugin execute arguments supported
* new plugin style
* smaller fonts styling input
* img files copied inside plugin
* style added
* prompt added
* styling from James
* fixed "exec" calls addedd css, but not working yet
* first (blind) try
* [CB-4915](https://issues.apache.org/jira/browse/CB-4915) Incremented plugin version on dev branch.

### 0.2.2 (Sept 25, 2013)
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) bumping&resetting version
* [windows8] commandProxy was moved
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming reference in Notification.cs
* [CB-4889](https://issues.apache.org/jira/browse/CB-4889) renaming org.apache.cordova.core.dialogs to org.apache.cordova.dialogs
* Rename CHANGELOG.md -> RELEASENOTES.md
* [CB-4592](https://issues.apache.org/jira/browse/CB-4592) [Blackberry10] Added beep support
* [CB-4752](https://issues.apache.org/jira/browse/CB-4752) Incremented plugin version on dev branch.
