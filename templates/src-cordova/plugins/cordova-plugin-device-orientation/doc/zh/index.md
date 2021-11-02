<!---
    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
-->

# cordova-plugin-device-orientation

這個外掛程式提供了對設備的指南針的訪問。 羅盤是感應器，可檢測的方向或設備通常指從設備的頂部的標題。 它的措施中從 0 度到 359.99，其中 0 是北部的標題。

訪問是通過一個全球 `navigator.compass` 物件。

雖然該物件附加到全球範圍內 `導航器`，它不可用直到 `deviceready` 事件之後。

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.compass);
    }
    

## 安裝

    cordova plugin add cordova-plugin-device-orientation
    

## 支援的平臺

*   亞馬遜火 OS
*   Android 系統
*   黑莓 10
*   瀏覽器
*   火狐瀏覽器的作業系統
*   iOS
*   泰
*   Windows Phone 7 和第 8 （如果在硬體中可用）
*   Windows 8

## 方法

*   navigator.compass.getCurrentHeading
*   navigator.compass.watchHeading
*   navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

獲取當前的羅經航向。羅經航向被經由一個 `CompassHeading` 物件，使用 `compassSuccess` 回呼函數。

    navigator.compass.getCurrentHeading(compassSuccess, compassError);
    

### 示例

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

獲取設備的當前標題的間隔時間定期。檢索到的標題，每次執行 `headingSuccess` 回呼函數。

返回的表 ID 引用的指南針手錶的時間間隔。表 ID 可用於與 `navigator.compass.clearWatch` 停止看 navigator.compass。

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions` 可能包含以下項：

*   **frequency**： 經常如何檢索以毫秒為單位的羅經航向。*（Number）*（預設值： 100）
*   **filter**： 啟動 watchHeading 成功回檔所需的度的變化。當設置此值時，**frequency**將被忽略。*（Number）*

### 示例

    function onSuccess(heading) {
        var element = document.getElementById('heading');
        element.innerHTML = 'Heading: ' + heading.magneticHeading;
    };
    
    function onError(compassError) {
        alert('Compass error: ' + compassError.code);
    };
    
    var options = {
        frequency: 3000
    }; // Update every 3 seconds
    
    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    

### 瀏覽器的怪癖

隨機生成當前標題的值，以便類比羅盤。

### iOS 的怪癖

只有一個 `watchHeading` 可以在 iOS 中一次的效果。 如果 `watchHeading` 使用一個篩選器，致電 `getCurrentHeading` 或 `watchHeading` 使用現有的篩選器值來指定標題的變化。 帶有篩選器看標題的變化是與時間間隔比效率更高。

### 亞馬遜火 OS 怪癖

*   `filter`不受支援。

### Android 的怪癖

*   不支援`filter`.

### 火狐瀏覽器作業系統的怪癖

*   不支援`filter`.

### 泰怪癖

*   不支援`filter`.

### Windows Phone 7 和 8 的怪癖

*   不支援`filter`.

## navigator.compass.clearWatch

別看手錶 ID 參數所引用的指南針。

    navigator.compass.clearWatch(watchID);
    

*   **watchID**： 由返回的 ID`navigator.compass.watchHeading`.

### 示例

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

`CompassSuccess` 回呼函數返回一個 `CompassHeading` 物件。

### 屬性

*   **magneticHeading**： 在某一時刻在時間中從 0-359.99 度的標題。*（人數）*

*   **trueHeading**： 在某一時刻的時間與地理北極在 0-359.99 度標題。 負值表示不能確定真正的標題。 *（人數）*

*   **headingAccuracy**： 中度報告的標題和真正標題之間的偏差。*（人數）*

*   **timestamp**： 本項決定在其中的時間。*（毫秒）*

### 亞馬遜火 OS 怪癖

*   `trueHeading`不受支援，但報告相同的值`magneticHeading`

*   `headingAccuracy`是始終為 0 因為有沒有區別 `magneticHeading` 和`trueHeading`

### Android 的怪癖

*   `trueHeading`屬性不受支援，但報告相同的值`magneticHeading`.

*   `headingAccuracy`屬性始終是 0 因為有沒有區別 `magneticHeading` 和`trueHeading`.

### 火狐瀏覽器作業系統的怪癖

*   `trueHeading`屬性不受支援，但報告相同的值`magneticHeading`.

*   `headingAccuracy`屬性始終是 0 因為有沒有區別 `magneticHeading` 和`trueHeading`.

### iOS 的怪癖

*   `trueHeading`屬性只返回位置服務通過以下方式啟用`navigator.geolocation.watchLocation()`.

## CompassError

當發生錯誤時，`compassError` 回呼函數情況下會返回一個 `CompassError` 物件。

### 屬性

*   **code**： 下面列出的預定義的錯誤代碼之一。

### 常量

*   `CompassError.COMPASS_INTERNAL_ERR`
*   `CompassError.COMPASS_NOT_SUPPORTED`
