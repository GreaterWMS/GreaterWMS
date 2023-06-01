---
title: Splashscreen
description: Control the splash screen for your app.
---
<!--
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

# cordova-plugin-splashscreen

[![Android Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/android.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/android.yml) [![Chrome Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml) [![Lint Test](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml)

This plugin displays and hides a splash screen while your web application is launching. Using its methods you can also show and hide the splash screen manually.

- [cordova-plugin-splashscreen](#cordova-plugin-splashscreen)
  - [Installation](#installation)
  - [Supported Platforms](#supported-platforms)
  - [Platform Splash Screen Image Configuration](#platform-splash-screen-image-configuration)
    - [Example Configuration](#example-configuration)
    - [Android-specific Information](#android-specific-information)
      - [Image Layout](#image-layout)
      - [`density`](#density)
      - [Image Sizing Table](#image-sizing-table)
      - [Dark Mode (API 28+)](#dark-mode-api-28)
      - [Example Android Configuration](#example-android-configuration)
    - [Windows-specific Information](#windows-specific-information)
  - [Preferences](#preferences)
    - [config.xml](#configxml)
    - [Quirks](#quirks)
      - [Android Quirks](#android-quirks)
      - [Browser Quirks](#browser-quirks)
      - [Windows Quirks](#windows-quirks)
  - [Methods](#methods)
    - [splashscreen.hide](#splashscreenhide)
    - [splashscreen.show](#splashscreenshow)

## Installation

    // npm hosted (new) id
    cordova plugin add cordova-plugin-splashscreen

    // you may also install directly from this repo
    cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git

## Supported Platforms

- Android
  __Note__: Android implementation has been moved to the core framework.
    If using `cordova-android@10.x` or earlier, use `cordova-plugin-splashscreen@6.x`
    If using `cordova-android@11.x` or later and exclusively developing for Android, this plugin can be uninstalled.
- Windows (`cordova-windows` version >= 4.4.0 is required)  
  __Note__: Extended splashscreen does not require the plugin on Windows (as opposed to Android) in case you don't use the plugin API, i.e. programmatic hide/show.
- Browser

## Platform Splash Screen Image Configuration

### Example Configuration

In the top-level `config.xml` file (not the one in `platforms`), add configuration elements like those specified here.

The value of the "src" attribute is relative to the project root directory and NOT to the `www` directory (see `Directory structure` below). You can name the source image file whatever you like. The internal name in the application is automatically determined by Cordova.

Directory structure:

```
projectRoot
    hooks
    platforms
    plugins
    www
        css
        img
        js
    res
        screen
            android
            windows
```

```xml
<platform name="android">
    <splash src="res/screen/android/splash-land-hdpi.png" density="land-hdpi" />
    <splash src="res/screen/android/splash-land-ldpi.png" density="land-ldpi" />
    <splash src="res/screen/android/splash-land-mdpi.png" density="land-mdpi" />
    <splash src="res/screen/android/splash-land-xhdpi.png" density="land-xhdpi" />
    <splash src="res/screen/android/splash-land-xxhdpi.png" density="land-xxhdpi" />
    <splash src="res/screen/android/splash-land-xxxhdpi.png" density="land-xxxhdpi" />

    <splash src="res/screen/android/splash-port-hdpi.png" density="port-hdpi" />
    <splash src="res/screen/android/splash-port-ldpi.png" density="port-ldpi" />
    <splash src="res/screen/android/splash-port-mdpi.png" density="port-mdpi" />
    <splash src="res/screen/android/splash-port-xhdpi.png" density="port-xhdpi" />
    <splash src="res/screen/android/splash-port-xxhdpi.png" density="port-xxhdpi" />
    <splash src="res/screen/android/splash-port-xxxhdpi.png" density="port-xxxhdpi" /> 
</platform>

<!-- Configuration using MRT concept (Recommended, see "Windows-specific information" section for details): -->
<platform name="windows">
    <splash src="res/screen/windows/splashscreen.png" target="SplashScreen"/>
    <splash src="res/screen/windows/splashscreenphone.png" target="SplashScreenPhone"/>
</platform>

<!-- Configuration using image size: -->
<!--<platform name="windows">
    <splash src="res/screen/windows/splashscreen.png" width="620" height="300"/>
    <splash src="res/screen/windows/splashscreenphone.png" width="1152" height="1920"/>
</platform>-->

<preference name="SplashScreenDelay" value="10000" />
```

### Android-specific Information

To effectively create your Android SplashScreen assets, it is important to understand the idiom and sizes used for the assets.

Android defined its assets by the image's layout and `density`.

#### Image Layout

- `land` short for landscape mode
- `port` short for portrait mode

#### `density`

The image's density refers to the number of pixels per square inch. Android, interchangeably refers to this as DPI.

Not all devices have the same pixel size so it is important to create images for all DPI to ensure that the quality of the image for each device is great.

If not all DPI images are considered, some devices might not show a SplashScreen or will use an incorrect DPI image that can result in a blurry scaled image.

#### Image Sizing Table

|  size   | portrait  | landscape |
| :-----: | :-------: | :-------: |
|  ldpi   |  200x320  |  320x200  |
|  mdpi   |  320x480  |  480x320  |
|  hdpi   |  480x800  |  800x480  |
|  xhdpi  | 720x1280  | 1280x720  |
| xxhdpi  | 960x1600  | 1600x960  |
| xxxhdpi | 1280x1920 | 1920x1280 |

#### Dark Mode (API 28+)

You can optionally provide an extra SplashScreen image to be used in dark/night mode when enabled on supported devices.
To do this, add the `-night` keyword in between the **layout** and **size** keywords of the image's `density` attribute value. E.g.: `land-night-hdpi`

For more examples, please see [the Example Configuration](#example-android-configuration) section.

#### Example Android Configuration

```xml
<platform name="android">
    <!-- Default 
    Note: You should specify default resources for each density.
      -- For instance, if the device(hdpi) is in landscape orientation and [density="land-hdpi"] 
      -- does not exists, [density="hdpi"] will be selected 
      If you do not declare this you will get MissingDefaultResource lint check errors.
      -->
    <splash src="res/screen/android/splash-port-hdpi.png" density="hdpi"/>
    <splash src="res/screen/android/splash-port-ldpi.png" density="ldpi"/>
    <splash src="res/screen/android/splash-port-mdpi.png" density="mdpi"/>
    <splash src="res/screen/android/splash-port-xhdpi.png" density="xhdpi"/>
    <splash src="res/screen/android/splash-port-xxhdpi.png" density="xxhdpi"/>

    <!-- Landscape -->
    <splash src="res/screen/android/splash-land-hdpi.png" density="land-hdpi" />
    <splash src="res/screen/android/splash-land-ldpi.png" density="land-ldpi" />
    <splash src="res/screen/android/splash-land-mdpi.png" density="land-mdpi" />
    <splash src="res/screen/android/splash-land-xhdpi.png" density="land-xhdpi" />
    <splash src="res/screen/android/splash-land-xxhdpi.png" density="land-xxhdpi" />
    <splash src="res/screen/android/splash-land-xxxhdpi.png" density="land-xxxhdpi" />

    <!-- Portrait -->
    <splash src="res/screen/android/splash-port-hdpi.png" density="port-hdpi" />
    <splash src="res/screen/android/splash-port-ldpi.png" density="port-ldpi" />
    <splash src="res/screen/android/splash-port-mdpi.png" density="port-mdpi" />
    <splash src="res/screen/android/splash-port-xhdpi.png" density="port-xhdpi" />
    <splash src="res/screen/android/splash-port-xxhdpi.png" density="port-xxhdpi" />
    <splash src="res/screen/android/splash-port-xxxhdpi.png" density="port-xxxhdpi" />
  
    <!-- Dark Mode -->
    <splash src="res/screen/android/splash-land-night-hdpi.png" density="land-night-hdpi" />
    <splash src="res/screen/android/splash-land-night-ldpi.png" density="land-night-ldpi" />
    <splash src="res/screen/android/splash-land-night-mdpi.png" density="land-night-mdpi" />
    <splash src="res/screen/android/splash-land-night-xhdpi.png" density="land-night-xhdpi" />
    <splash src="res/screen/android/splash-land-night-xxhdpi.png" density="land-night-xxhdpi" />
    <splash src="res/screen/android/splash-land-night-xxxhdpi.png" density="land-night-xxxhdpi" />

    <splash src="res/screen/android/splash-port-night-hdpi.png" density="port-night-hdpi" />
    <splash src="res/screen/android/splash-port-night-ldpi.png" density="port-night-ldpi" />
    <splash src="res/screen/android/splash-port-night-mdpi.png" density="port-night-mdpi" />
    <splash src="res/screen/android/splash-port-night-xhdpi.png" density="port-night-xhdpi" />
    <splash src="res/screen/android/splash-port-night-xxhdpi.png" density="port-night-xxhdpi" />
    <splash src="res/screen/android/splash-port-night-xxxhdpi.png" density="port-night-xxxhdpi" />
</platform>
```

### Windows-specific Information

Splash screen images can be defined using the [MRT](https://cordova.apache.org/docs/en/dev/config_ref/images.html#windows) concept.  
If you specify `src="res/windows/splashscreen.png"` the following files will be copied into the application's images folder:  
`res/windows/splashscreen.png` | `res/windows/splashscreen.scale-100.png`, `res/windows/splashscreen.scale-125.png`, etc.  

The following are supported:

|   Scale, %   |       Project       |    Width    |    Height    |             Filename              |
|:------------:|:-------------------:|:-----------:|:------------:|:---------------------------------:|
|     100      |  Windows 10/8.1     |     620     |     300      | `splashscreen.png` \| `splashscreen.scale-100.png`              |
|     125      |  Windows 10         |     775     |     375      | `splashscreen.scale-125.png`      |
|     150      |  Windows 10         |     930     |     450      | `splashscreen.scale-150.png`      |
|     200      |  Windows 10         |     1240    |     600      | `splashscreen.scale-200.png`      |
|     400      |  Windows 10         |     2480    |     1200     | `splashscreen.scale-400.png`      |
|     140      |  Windows 8.1        |     868     |     420      | `splashscreen.scale-140.png`      |
|     180      |  Windows 8.1        |     1116    |     540      | `splashscreen.scale-180.png`      |
|     100      |  Windows Phone 8.1  |     480     |     800      | `splashscreenphone.png` \| `splashscreenphone.scale-100.png`         |
|     140      |  Windows Phone 8.1  |     672     |     1120     | `splashscreenphone.scale-140.png` |
|     240      |  Windows Phone 8.1  |     1152    |     1920     | `splashscreenphone.scale-240.png` |

__Note__: SplashScreens size for Windows 10 project should not exceed 200 KBytes.  
__Note__: Supported formats are `.png`, `.jpg`, `.jpeg`. Mixing of the extensions within a target is not supported. I.e. you can have `splashscreen.jpg` and `splashscreenphone.png` but not `splashscreen.scale-100.png`, `splashscreen.scale-400.jpg`.  
__Note__: You may need to reopen Visual Studio solution after changing the images and doing a `cordova prepare` for the changes to take effect.

## Preferences

### config.xml

- `AutoHideSplashScreen` (boolean, default to `true`). Indicates whether to hide splash screen automatically or not. The splash screen is hidden after the amount of time specified in the `SplashScreenDelay` preference.

    ```xml
    <preference name="AutoHideSplashScreen" value="true" />
    ```

- `SplashScreenDelay` (number, default to 3000). Amount of time in milliseconds to wait before automatically hide splash screen.

    ```xml
    <preference name="SplashScreenDelay" value="3000" />
    ```

    This value used to be in seconds (but is now milliseconds) so values less than 30 will continue to be treated as seconds. (Consider this a deprecated patch that will disapear in some future version.)

    To disable the splashscreen add the following preference to `config.xml`:
    ```xml
    <preference name="SplashScreenDelay" value="0"/>
    ```

    **Windows Quirk**: You should disable the splashscreen in case you are updating the entire document body dynamically (f.e. with a SPA router) to avoid affecting UI/controls.  
    Note that you should also directly reference `WinJS/base.js` in the page HTML in this case to avoid the issues with activation context ([CB-11658](https://issues.apache.org/jira/browse/CB-11658)).

- `FadeSplashScreen` (boolean, defaults to `true`): Set to `false` to
  prevent the splash screen from fading in and out when its display
  state changes.

    ```xml
    <preference name="FadeSplashScreen" value="false"/>
    ```

- `FadeSplashScreenDuration` (float, defaults to `500`): Specifies the
  number of milliseconds for the splash screen fade effect to execute.

    ```xml
    <preference name="FadeSplashScreenDuration" value="750"/>
    ```

    _Note_: `FadeSplashScreenDuration` is included into `SplashScreenDelay`, for example if you have `<preference name="SplashScreenDelay" value="3000" />` and `<preference name="FadeSplashScreenDuration" value="1000"/>` defined in `config.xml`:

    - 00:00 - splashscreen is shown
    - 00:02 - fading has started
    - 00:03 - splashscreen is hidden

    Turning the fading off via `<preference name="FadeSplashScreen" value="false"/>` technically means fading duration to be `0` so that in this example the overall splash screen delay will still be 3 seconds.

    _Note_: This only applies to the application startup - you need to take the fading timeout into account when manually showing/hiding the splash screen in your application's code:

    ```javascript
    navigator.splashscreen.show();
    window.setTimeout(function () {
        navigator.splashscreen.hide();
    }, splashDuration - fadeDuration);
    ```

- `ShowSplashScreenSpinner` (boolean, defaults to `true`): Set to `false`
  to hide the splash screen spinner.

    ```xml
    <preference name="ShowSplashScreenSpinner" value="false"/>
    ```
    
    _Note_: Does not work on Browser or Windows platforms.

### Quirks

#### Android Quirks

In your `config.xml`, you can add the following preferences:

```xml
<preference name="SplashMaintainAspectRatio" value="true|false" />
<preference name="SplashShowOnlyFirstTime" value="true|false" />
<preference name="SplashScreenSpinnerColor" value="white" />
```

`SplashMaintainAspectRatio` preference is optional. If set to `true`, the splash screen drawable is not stretched to fit the full screen, but instead simply "covers" the screen, like CSS "background-size:cover". This is very useful when splash screen images cannot be distorted in any way, for example when they contain scenery or text. This setting works best with images that have large margins (safe areas) that can be safely cropped on screens with different aspect ratios.

The splash screen plugin reloads the splash screen whenever the orientation changes so that you can specify different splash screen images for portrait and landscape orientations.

`SplashShowOnlyFirstTime` preference is  optional and defaults to `true`. When set to `true` the splash screen will only appear on application launch. However, if you plan to use `navigator.app.exitApp()` to close the application and force the splash screen appear on the application's next launch, you should set this property to `false` (this also applies to closing the application with the Back button).

`SplashScreenSpinnerColor` preference is also optional and is ignored when not set. Setting it to a valid color name or HEX color code will change the color of the spinner on Android 5.0+ devices.

#### Browser Quirks

You can use the following preferences in your `config.xml`:

```xml
<platform name="browser">
    <preference name="SplashScreen" value="/images/browser/splashscreen.jpg" /> <!-- defaults to "/img/logo.png" -->
    <preference name="AutoHideSplashScreen" value="true" /> <!-- defaults to "true" -->
    <preference name="SplashScreenDelay" value="3000" /> <!-- defaults to "3000" -->
    <preference name="SplashScreenBackgroundColor" value="green" /> <!-- defaults to "#464646" -->
    <preference name="ShowSplashScreen" value="false" /> <!-- defaults to "true" -->
    <preference name="SplashScreenWidth" value="600" /> <!-- defaults to "170" -->
    <preference name="SplashScreenHeight" value="300" /> <!-- defaults to "200" -->
</platform>
```

__Note__: `SplashScreen` value should be absolute in order to work in a sub-page. The `SplashScreen` value is used only for the browser platform. The value will be ignored for other platforms.

#### Windows Quirks

- `SplashScreenSpinnerColor` (string, defaults to system accent color): hash, rgb notation or CSS color name.

    ```xml
    <preference name="SplashScreenSpinnerColor" value="#242424"/>
    <preference name="SplashScreenSpinnerColor" value="DarkRed"/>
    <preference name="SplashScreenSpinnerColor" value="rgb(50,128,128)"/>
    ```

- `SplashScreenBackgroundColor` (string, defaults to #464646): hex notation.

    ```xml
    <preference name="SplashScreenBackgroundColor" value="0xFFFFFFFF"/>
    ```

## Methods

- splashscreen.show
- splashscreen.hide

### splashscreen.hide

Dismiss the splash screen.

```js
navigator.splashscreen.hide();
```

### splashscreen.show

Displays the splash screen.

```js
navigator.splashscreen.show();
```

Your application cannot call `navigator.splashscreen.show()` until the application has
started and the `deviceready` event has fired. But since typically the splash
screen is meant to be visible before your application has started, that would seem to
defeat the purpose of the splash screen.  Providing any parameters in
`config.xml` will automatically `show` the splash screen immediately after your
application is launched and before it has fully started and received the `deviceready`
event. For this reason, it is unlikely you will need to call `navigator.splashscreen.show()` to make the splash
screen visible for application startup.
