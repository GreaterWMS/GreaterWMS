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

[![Android Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/android.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/android.yml) [![Chrome Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/chrome.yml) [![iOS Testsuite](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/ios.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/ios.yml) [![Lint Test](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml/badge.svg)](https://github.com/apache/cordova-plugin-splashscreen/actions/workflows/lint.yml)

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
      - [Dark Mode](#dark-mode)
      - [Example Android Configuration](#example-android-configuration)
    - [iOS-specific Information](#ios-specific-information)
      - [Launch Storyboard Images](#launch-storyboard-images)
        - [Designing Launch Storyboard Images](#designing-launch-storyboard-images)
        - [Scale](#scale)
        - [Idioms](#idioms)
        - [Size classes](#size-classes)
        - [Single-image launch screen](#single-image-launch-screen)
        - [Multi-image launch screen](#multi-image-launch-screen)
        - [Dark Mode](#dark-mode-1)
        - [Quirks and Known Issues](#quirks-and-known-issues)
    - [Windows-specific Information](#windows-specific-information)
  - [Preferences](#preferences)
    - [config.xml](#configxml)
    - [Quirks](#quirks)
      - [Android Quirks](#android-quirks)
      - [Browser Quirks](#browser-quirks)
      - [iOS Quirks](#ios-quirks)
      - [Windows Quirks](#windows-quirks)
  - [Methods](#methods)
    - [splashscreen.hide](#splashscreenhide)
      - [iOS Quirk](#ios-quirk)
    - [splashscreen.show](#splashscreenshow)

## Installation

    // npm hosted (new) id
    cordova plugin add cordova-plugin-splashscreen

    // you may also install directly from this repo
    cordova plugin add https://github.com/apache/cordova-plugin-splashscreen.git

## Supported Platforms

- Android
- iOS  
  __Note__: iOS implementation has been moved to the core framework.  
    If using `cordova-ios@5` or earlier, use `cordova-plugin-splashscreen@5`  
    If using `cordova-ios@6` or later, use `cordova-plugin-splashscreen@6`. If developing exclusively for the iOS platform, this plugin can be uninstalled.
- Windows (`cordova-windows` version >= 4.4.0 is required)  
  __Note__: Extended splashscreen does not require the plugin on Windows (as opposed to Android and iOS) in case you don't use the plugin API, i.e. programmatic hide/show.
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
            ios
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

<platform name="ios">
    <!-- Storyboard (supports all devices):
      -- Note: images are determined by scale, idiom, and size traits. The following
      -- are suggested based on current device form factors -->
    <splash src="res/screen/ios/Default@2x~universal~anyany.png" />
    <splash src="res/screen/ios/Default@2x~universal~comany.png" />
    <splash src="res/screen/ios/Default@2x~universal~comcom.png" />
    <splash src="res/screen/ios/Default@3x~universal~anyany.png" />
    <splash src="res/screen/ios/Default@3x~universal~anycom.png" />
    <splash src="res/screen/ios/Default@3x~universal~comany.png" />
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

### iOS-specific Information

Launch storyboard images are sized based on scale, idiom, and size classes. It supports all devices, and can be used with split-screen/slide-over multitasking.

There is no official support for providing a native-resolution launch image for the iPad Pro 12.9 or for providing launch images that work with split-screen multitasking or slide-over.

**Note:** Since iOS 11, for iPhone X devices and greater (with notch screen), make sure to add `viewport-fit=cover` to the viewport meta tag in your `index.html` file to display the app correctly like so: `<meta name="viewport" content="user-scalable=no, initial-scale=1, width=device-width, viewport-fit=cover">` and make some modification to your app style by adding: `padding: env(safe-area-inset-top)` to your `index.css` file to avoid the unsafe areas behind notches in the screen.

#### Launch Storyboard Images

To support newer form factors and split-screen/slide-over multitasking, launch storyboard images are used.

- images are not specific to a given device.
- images are scaled to fill the available viewport (while maintaining the aspect ratio).
- the outer edges of the images will be cropped, and the amount will vary based on device an viewport.
- there is no need to provide an image for each possible device, viewport, and orientation; iOS will choose the best image for the situation automatically.

##### Designing Launch Storyboard Images

The key to designing a launch storyboard image is understanding that the edges of the image will almost certainly be cropped. Therefore, one should not place any important information near the edges of any images provided to the launch storyboard. Only the center is a safe area, and this all but guarantees that following Apple's advice of presenting an unpopulated user interface will not work well.

Instead, the following tips should enable you to create a launch image that works across a multitude of form factors, viewports, and orientations:

- Important graphics (logos, icons, titles) should be centered. The safe bounding region will vary, so you will need to test to ensure that the important graphics are never cropped. Better yet, don't supply any important graphics in the first place.

  - You _can_ fine-tune the placement and size of these graphics.

- Use a simple color wash. If you use two colors, you'll want one color to fill the top half of the image, and the second to fill the bottom half.  If you use a gradient, you'll probably want to ensure that the middle of the gradient lines up with the center of the image.

- Don't worry about pixel perfection -- because the images are scaled, there's almost no chance the images will be perfectly fit to the pixel grid. Since all supported iOS devices use retina screens, users will be hard pressed to notice it anyway.

It is important to understand the concept of scale, idiom, and size class traits in order to use launch storyboard images effectively. Of the images supplied to the launch storyboard, iOS will choose the image that best matches the device and viewport and render that image. It is possible to supply only one launch image if so desired, but it is also possible to fine-tune the displayed launch image based on traits. When fine-tuning, one can ignore traits that aren't targeted or supported by the app.

##### Scale

|    scale    |    devices             |
|:-----------:|:----------------------:|
|     1x      | All non-retina devices |
|     2x      | Most retina devices    |
|     3x      | iPhone 6+/6s+,7s+      |

In general, you'll want to supply 2x and 3x images. Cordova only supports retina devices now, so there's no point in supplying 1x images.

##### Idioms

|    idiom    |    devices    |
|:-----------:|:-------------:|
|    ipad     | All iPads     |
|   iphone    | All iPhones and iPod Touches    |
|  universal  | All devices   |

You only need to provide universal images unless you need to fine-tune for a specific device idiom.

##### Size classes

There are two size classes applies to both screen axes. Narrow viewports are considered to be the "compact" size class, and remaining viewports are considered "regular". When supplying images to Xcode, however, one must choose between "any & compact" and "any & regular". To stay consistent with the native terminology, this feature will match based on "any" and "compact". `any` will match regular-sized viewports. 

Note: this feature uses `com` as an abbreviation for "compact" classes.

The following classes are supported by this feature:

|    width    |    height    |    orientation    |
|:-----------:|:------------:|:-----------------:|
|     any     |     any      |        any        |
|     com     |     any      |     portrait      |
|     any     |     com      |  landscape (wide) |
|     com     |     com      | landscape (narrow)|

To see the complete list of size classes associated with devices and viewports, see <http://www.sizeclasses.com>.

##### Single-image launch screen

If your launch image is simple, you may be able to avoid creating a lot of different launch images and supply only one. The launch image needs to meet the following requirements:

- the image should be square
- the image should be large enough to fit on an iPad Pro 12.9": 2732x2732
- anything important should fit within the center

Keep in mind that the image will be cropped, possibly quite severely, depending upon the viewport.

Once the image is created, you can include it in your project by adding the following to `config.xml`:

```xml
    <splash src="res/screen/ios/Default@2x~universal~anyany.png" />
```

Because only one image is provided, iOS will utilize it in every context.

##### Multi-image launch screen

If a single launch image won't meet your needs, you will probably need to supply at least six images, if not more. Furthermore, keep in mind that it will not be possible to fine tune the image to a specific device, but only to a device class, display factor, and viewport size.

If you don't need to target images to a specific idiom, you should create six images, as follows:

|    scale    |    idiom    |    width    |    height    |    size    |    filename    |
|:-----------:|:-----------:|:-----------:|:------------:|:----------:|:--------------:|
|     2x*     |  universal  |     any     |     any      | 2732x2732  | `Default@2x~universal~anyany.png` |
|     2x      |  universal  |     com     |     any      | 1278x2732  | `Default@2x~universal~comany.png` |
|     2x      |  universal  |     com     |     com      | 1334x750   | `Default@2x~universal~comcom.png` |
|     3x*     |  universal  |     any     |     any      | 2208x2208  | `Default@3x~universal~anyany.png` |
|     3x      |  universal  |     any     |     com      | 2208x1242  | `Default@3x~universal~anycom.png` |
|     3x      |  universal  |     com     |     any      | 1242x2208  | `Default@3x~universal~comany.png` |

\* this image is required in order for iOS utilize the other images within this scale and idiom.

> Note: If the 3x sizes look small too you, that's because there's only one device class that currently has a 3x density: the iPhone 6+/6s+/7+.

The above looks like the following snippet when present in `config.xml`:

```xml
    <splash src="res/screen/ios/Default@2x~universal~anyany.png" />
    <splash src="res/screen/ios/Default@2x~universal~comany.png" />
    <splash src="res/screen/ios/Default@2x~universal~comcom.png" />
    <splash src="res/screen/ios/Default@3x~universal~anyany.png" />
    <splash src="res/screen/ios/Default@3x~universal~anycom.png" />
    <splash src="res/screen/ios/Default@3x~universal~comany.png" />
```

Should one need to further fine tune based upon device idiom, one can do so. This might look like so:

|    scale    |    idiom    |    width    |    height    |    size    |    filename    |
|:-----------:|:-----------:|:-----------:|:------------:|:----------:|:--------------:|
|     2x*     |    iphone   |     any     |     any      | 1334x1334  | `Default@2x~iphone~anyany.png` |
|     2x      |    iphone   |     com     |     any      | 750x1334   | `Default@2x~iphone~comany.png` |
|     2x      |    iphone   |     com     |     com      | 1334x750   | `Default@2x~iphone~comcom.png` |
|     3x*     |    iphone   |     any     |     any      | 2208x2208  | `Default@3x~iphone~anyany.png` |
|     3x      |    iphone   |     any     |     com      | 2208x1242  | `Default@3x~iphone~anycom.png` |
|     3x      |    iphone   |     com     |     any      | 1242x2208  | `Default@3x~iphone~comany.png` |
|     2x*     |     ipad    |     any     |     any      | 2732x2732  | `Default@2x~ipad~anyany.png`   |
|     2x      |     ipad    |     com     |     any      | 1278x2732  | `Default@2x~ipad~comany.png`   |

\* this image is required in order for iOS utilize the other images within this scale and idiom.

The above looks like the following in `config.xml`:

```xml
    <splash src="res/screen/ios/Default@2x~iphone~anyany.png" />
    <splash src="res/screen/ios/Default@2x~iphone~comany.png" />
    <splash src="res/screen/ios/Default@2x~iphone~comcom.png" />
    <splash src="res/screen/ios/Default@3x~iphone~anyany.png" />
    <splash src="res/screen/ios/Default@3x~iphone~anycom.png" />
    <splash src="res/screen/ios/Default@3x~iphone~comany.png" />
    <splash src="res/screen/ios/Default@2x~ipad~anyany.png" />
    <splash src="res/screen/ios/Default@2x~ipad~comany.png" />
```

##### Dark Mode

Since [Cordova-iOS@6.1.0](https://github.com/apache/cordova-ios), it is now possible to optionally specify different SplashScreen images to use when the app is running in dark mode. The luminosity of SplashScreen images can be defined in `config.xml` using the `~dark` and `~light` suffixes.

```xml
<!-- Default image to be used for all modes -->
<splash src="res/screen/ios/Default@2x~universal~anyany.png" />

<!-- Image to use specifically for dark mode devices -->
<splash src="res/screen/ios/Default@2x~universal~anyany~dark.png" />

<!-- Image to use specifically for light mode devices -->
<splash src="res/screen/ios/Default@2x~universal~anyany~light.png" />
```

**Note:** This works since iOS 13. iOS 12 and below will use the default SplashScreen without a luminosity suffix specified.

##### Quirks and Known Issues

1. **App on target may not reflect changes to images**
   Once you run the app on a target, iOS caches the launch image. Unfortunately, when you change the image, iOS does _not_ invalidate the cache, which means you'll still see the old launch image. You should either: delete the app, or reset content & settings (simulator).

2. **Simulator may not show expected images when launched from CLI**
   When Xcode deploys to a specific simulator, it only copies the assets that match the simulator's characteristics. For example, if you try to run an app on the iPhone 6s Plus simulator, only @3x launch images are copied. When compiling from the CLI, however, the default is to assume an iPhone 5s, which means only @2x launch images are copied. Unless your launch images are markedly different, chances are good the difference would go unnoticed, but this does mean that the only accurate method of testing is to test on a physical device.

3. **`anyany` must be provided for other variations to be used**
   If you don't provide an `anyany` version of the launch image for a specific scale and idiom, the other variations (like `anycom`, `comany`, and `comcom`) will ignored. 

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

    **iOS Quirk**: to disable the splashscreen on `ios` platform you should also add `<preference name="FadeSplashScreenDuration" value="0"/>` to `config.xml`.

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

#### iOS Quirks

- In iOS, the splash screen images are called launch images. These images are mandatory on iOS.

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


#### iOS Quirk

The `config.xml` file's `AutoHideSplashScreen` setting must be
`false`. To delay hiding the splash screen for two seconds, add a
timer such as the following in the `deviceready` event handler:

```js
setTimeout(function() {
    navigator.splashscreen.hide();
}, 2000);
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
