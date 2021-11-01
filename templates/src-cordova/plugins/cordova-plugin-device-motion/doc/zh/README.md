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

# cordova-plugin-device-motion

[![Build Status](https://travis-ci.org/apache/cordova-plugin-device-motion.svg)](https://travis-ci.org/apache/cordova-plugin-device-motion)

這個外掛程式提供了對設備的加速度計的訪問。 加速度計是動作感應器檢測到的更改 (*三角洲*) 在相對於當前的設備方向，在三個維度沿*x*、 *y*和*z*軸運動。

訪問是通過一個全球 `navigator.accelerometer` 物件。

雖然該物件附加到全球範圍內 `導航器`，它不可用直到 `deviceready` 事件之後。

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.accelerometer);
    }
    

## 安裝

    cordova plugin add cordova-plugin-device-motion
    

## 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 瀏覽器
  * 火狐瀏覽器作業系統
  * iOS
  * Tizen
  * Windows Phone 8
  * Windows

## 方法

  * navigator.accelerometer.getCurrentAcceleration
  * navigator.accelerometer.watchAcceleration
  * navigator.accelerometer.clearWatch

## 物件

  * 加速度

## navigator.accelerometer.getCurrentAcceleration

得到當前加速度沿 *x*、 *y* 和 *z* 軸。

這些加速度值將返回到 `accelerometerSuccess` 回呼函數。

    navigator.accelerometer.getCurrentAcceleration(accelerometerSuccess, accelerometerError);
    

### 示例

    function onSuccess(acceleration) {
        alert('Acceleration X: ' + acceleration.x + '\n' +
              'Acceleration Y: ' + acceleration.y + '\n' +
              'Acceleration Z: ' + acceleration.z + '\n' +
              'Timestamp: '      + acceleration.timestamp + '\n');
    };
    
    function onError() {
        alert('onError!');
    };
    
    navigator.accelerometer.getCurrentAcceleration(onSuccess, onError);
    

### 瀏覽器的怪癖

值 X、 Y、 Z 議案是所有中隨機生成的訂單來類比加速度感應器。

### iOS 的怪癖

  * iOS 不會認識到在任何給定的點獲取當前加速度的概念。

  * 你必須看加速和捕獲的資料在特定的時間間隔。

  * 因此， `getCurrentAcceleration` 收益率從報告的最後一個值的函數 `watchAccelerometer` 調用。

## navigator.accelerometer.watchAcceleration

在週期性時間間隔，執行 `accelerometerSuccess` 回呼函數每次檢索設備的當前 `Accelerometer`。 指定的間隔，以毫秒為單位通過 `acceleratorOptions` 物件的 `frequency` 參數。

返回的表 ID 引用加速度計的手錶時間間隔，並且可以與 `navigator.accelerometer.clearWatch` 用來停止觀看了加速度計。

    var watchID = navigator.accelerometer.watchAcceleration(accelerometerSuccess,
                                                           accelerometerError,
                                                           accelerometerOptions);
    

  * **accelerometerOptions**： 具有以下可選的鍵的物件： 
      * **期間**： 請求的期間的調用的 accelerometerSuccess 與加速度資料以毫秒為單位。*（人數）*（預設值： 10000）

### 示例

    function onSuccess(acceleration) {
        alert('Acceleration X: ' + acceleration.x + '\n' +
              'Acceleration Y: ' + acceleration.y + '\n' +
              'Acceleration Z: ' + acceleration.z + '\n' +
              'Timestamp: '      + acceleration.timestamp + '\n');
    };
    
    function onError() {
        alert('onError!');
    };
    
    var options = { frequency: 3000 };  // Update every 3 seconds
    
    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    

### iOS 的怪癖

API 呼叫成功的回呼函數在時間間隔的要求，但將請求的範圍限制為 40ms年之間裝置和 1000ms。 例如，如果您請求的時間間隔為 3 秒，（3000ms），API 請求資料從設備每隔 1 秒，但只是執行成功回檔每 3 秒。

## navigator.accelerometer.clearWatch

別看 `watchID` 參數所引用的 `Accelerometer`。

    navigator.accelerometer.clearWatch(watchID);
    

  * **watchID**： 由返回的 ID`navigator.accelerometer.watchAcceleration`.

### 示例

    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.accelerometer.clearWatch(watchID);
    

## 加速度

包含在時間中捕獲的特定點的 `Accekerometer` 資料。 加速度值包括重力的作用 (9.81 m/s ^2），這樣當設備在於扁和朝上，*x*，*y*，*z* 返回的值應該是 ``、 `` 度和 `9.81`.

### 屬性

  * **x**： 在 X 軸上的加速度量。（在 m/s ^2)*（人數）*
  * **y**： 在 y 軸上的加速度量。（在 m/s ^2)*（人數）*
  * **z**： 在 Z 軸上的加速度量。（在 m/s ^2)*（人數）*
  * **timestamp**： 創建時間戳記以毫秒為單位。*() DOMTimeStamp*