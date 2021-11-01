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

# cordova-plugin-globalization

[![Build Status](https://travis-ci.org/apache/cordova-plugin-globalization.svg)](https://travis-ci.org/apache/cordova-plugin-globalization)

這個外掛程式獲取的資訊，並執行操作特定于使用者的地區設定、 語言和時區。 注意到地區設定和語言之間的區別： 數位、 日期和時間的顯示方式為一個區域，雖然語言確定什麼語言文本的地區設定控制項顯示為，與地區設定無關。 開發人員經常使用的地區設定來設置這兩個設置，但使用者不能將她的語言設置為"英語"沒有理由但地區設定為"法語"這樣的文本顯示在英語但日期、 時間等，同時會顯示他們是在法國。 不幸的是，大多數移動平臺目前不做這些設置之間的區別。

這個外掛程式定義全球 `navigator.globalization` 物件。

雖然在全球範圍內，它不可用直到 `deviceready` 事件之後。

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## 安裝

    cordova plugin add cordova-plugin-globalization
    

## 物件

  * GlobalizationError

## 方法

  * navigator.globalization.getPreferredLanguage
  * navigator.globalization.getLocaleName
  * navigator.globalization.dateToString
  * navigator.globalization.stringToDate
  * navigator.globalization.getDatePattern
  * navigator.globalization.getDateNames
  * navigator.globalization.isDayLightSavingsTime
  * navigator.globalization.getFirstDayOfWeek
  * navigator.globalization.numberToString
  * navigator.globalization.stringToNumber
  * navigator.globalization.getNumberPattern
  * navigator.globalization.getCurrencyPattern

## navigator.globalization.getPreferredLanguage

獲取用戶端的當前語言的 BCP 47 語言標記。

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### 說明

BCP 47 相容的語言識別項標記作為參數返回 `successCallback` 與 `屬性` 物件。 該物件應該具有 `value` 值的 `String` 屬性。

如果獲取語言時出錯，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.UNKNOWN_ERROR`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `EN-US）` 語言時，此時應顯示彈出一個對話方塊文本 `語言： EN-US`：

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### Android 的怪癖

  * 返回的 ISO 639-1 雙字母語言代碼、 大寫 ISO 3166-1 國家代碼和由連字號分隔的變形。例子："en"、"EN-US"，"美國"

### Windows Phone 8 怪癖

  * 返回 ISO 639-1 兩個字母語言代碼和相應的設置，由連字號分隔的"語言"區域變形的 ISO 3166-1 國家代碼。
  * 請注意的區域變體是的"語言"設置的屬性，並不由 Windows Phone 上的無關的"國家/地區"設置決定的。

### Windows 的怪癖

  * 返回 ISO 639-1 兩個字母語言代碼和相應的設置，由連字號分隔的"語言"區域變形的 ISO 3166-1 國家代碼。

### 瀏覽器的怪癖

  * Falls back on getLocaleName

## navigator.globalization.getLocaleName

返回用戶端的目前範圍設置的 BCP 47 相容標記。

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### 說明

BCP 47 相容的地區設定識別碼字串作為參數返回 `successCallback` 與 `屬性` 物件。 該物件應該具有 `value` 值的 `String` 屬性。 Locale 標記將由兩個字母小寫語言代碼和兩個字母大寫國家/地區代碼，（未指定） 的變數代碼，由連字號分隔。

如果獲取地區設定時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.UNKNOWN_ERROR`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `EN-US` 地區設定時，這將顯示彈出一個對話方塊文本 `地區設定： EN-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Android 的怪癖

  * JAVA 不區分一集的"語言"和設置"地區設定"，所以這種方法本質上是相同的 `navigator.globalizatin.getPreferredLanguage()`.

### Windows Phone 8 怪癖

  * 返回 ISO 639-1 兩個字母的語言代碼和 ISO 3166-1 國家/地區代碼的區域的 variant 類型的值對應于"區域格式"設置，由連字號分隔。

### Windows 的怪癖

  * 在控制台中時鐘、 語言和區域-> 格式，格式區域-> 和-> 區域的格式在 Windows Phone 8.1 上的地區設定中，可以更改地區設定。

### 瀏覽器的怪癖

  * IE 返回作業系統的地區設定。Chrome、 火狐瀏覽器，返回瀏覽器語言標記。

## navigator.globalization.dateToString

返回一個日期格式設置為一個字串，根據用戶端的地區設定和時區。

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### 說明

可從該物件作為參數傳遞給 `successCallback` 訪問通過 `value` 屬性返回格式化的日期 `String`.

入站的 `date` 參數應該是 `Date` 類型.

如果格式化日期時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.FORMATTING_ERROR`.

`options` 參數是可選的且其預設值：

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` 可以 `short`、 `medium`、 `long`、 或 `full`.

`options.selector` 可以是 `date`、 `time` 或 `date and time`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

如果瀏覽器設置為 `en_US` 地區設定，這將顯示彈出一個對話方塊文本類似于 `日期： 2012/9/25 4:21 下午` 使用預設選項：

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Android 的怪癖

  * 預設選項 `formatLenght` 取決於使用者所選的日期格式內 <0>設置-> 系統-> 日期和時間-> 選擇日期格式</0>，<0>年</0> 模式僅提供 4 位數位，不 2 位數。 預設選項 `short` 取決於使用者所選的日期格式內 `設置-> 系統-> 日期和時間-> 選擇日期格式`，`年` 模式僅提供 4 位數位，不 2 位數。 這意味著它不完全對齊與 [ICU](http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US).

### Windows Phone 8 怪癖

  * `formatLength` 選項支援只有 `short` 和 `full` 的值。

  * 日期和時間的選擇器模式一直是一種完整的日期時間格式。

  * 返回的值可能取決於使用者的地區設定與 ICU 不完全對齊。

### Windows 的怪癖

  * `formatLength` 選項支援只有 `short` 和 `full` 的值。

  * 日期和時間的選擇器模式一直是一種完整的日期時間格式。

  * 返回的值可能取決於使用者的地區設定與 ICU 不完全對齊。

### 瀏覽器的怪癖

  * 只有 79 地區設定支援是因為 moment.js 此方法中使用。

  * 返回的值可能取決於使用者的地區設定與 ICU 不完全對齊。

  * `time`選擇器支援`short`和`full`formatLength 只。

### 火狐瀏覽器作業系統的怪癖

  * `formatLength` 不區分 `long` 和 `full` 
  * 顯示日期 （沒有 `long` 或 `full` 的版本） 的唯一方法

## navigator.globalization.getCurrencyPattern

返回一個模式字串格式化和解析貨幣值根據用戶端的使用者首選項和 ISO 4217 貨幣代碼。

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### 說明

返回到 `successCallback` 與 `屬性` 物件作為參數的模式。該物件應包含以下屬性：

  * **pattern**： 要格式化和解析貨幣值的貨幣模式。 模式遵循[Unicode 技術標準 #35](http://unicode.org/reports/tr35/tr35-4.html)。 *（字串）*

  * **code**： 模式的 ISO 4217 貨幣代碼。*（字串）*

  * **fraction**： 解析和貨幣的格式時要使用的小數位數的數目。*（數）*

  * **rounding**： 舍入增量解析和格式時要使用。*（數）*

  * **decimal**： 小數點符號用於分析和格式設置。*（字串）*

  * **grouping**： 分組符號用於分析和格式設置。*（字串）*

入站的 `currencyCode` 參數應該是一個 `字串` 的 ISO 4217 貨幣代碼，例如 '美元' 之一。

如果獲取模式時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.FORMATTING_ERROR`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * iOS
  * Windows 8
  * Windows

### 示例

當瀏覽器設置為 `en_US` 地區設定，所選的幣種是美元時，此示例顯示彈出一個對話方塊文本類似于遵循的效果：

    navigator.globalization.getCurrencyPattern(
        'USD',
        function (pattern) {
            alert('pattern: '  + pattern.pattern  + '\n' +
                  'code: '     + pattern.code     + '\n' +
                  'fraction: ' + pattern.fraction + '\n' +
                  'rounding: ' + pattern.rounding + '\n' +
                  'decimal: '  + pattern.decimal  + '\n' +
                  'grouping: ' + pattern.grouping);
        },
        function () { alert('Error getting pattern\n'); }
    );
    

預期的結果：

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### Windows 的怪癖

  * 支援的唯一的 'code' 和 'fraction' 屬性

## navigator.globalization.getDateNames

返回陣列的各月的名稱或一周，具體取決於用戶端的使用者首選項和日曆天。

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### 說明

返回到 `successCallback` 與 `properties` 物件的名稱的陣列作為參數。 該物件包含帶有 `value` 值的 `Array` 的 `String` 屬性。 陣列特徵名稱從任一開始一年或一周，具體取決於所選的選項的第一天中的第一個月。

如果獲得名稱時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.UNKNOWN_ERROR`.

`options` 參數是可選的且其預設值：

    {type:'wide', item:'months'}
    

`options.type` 值可以 `narrow` 或 `wide`.

`options.item` 的值可以是 `months` 或 `days`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `en_US` 地區設定時，本示例顯示一系列的十二個彈出對話方塊，每個月，與類似的文本一 `個月： 1 月`：

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### 火狐瀏覽器作業系統的怪癖

  * `options.type` 支援 `genitive` 的價值，對於某些語言重要

### Windows Phone 8 怪癖

  * 月份的陣列包含 13 個元素。
  * 返回的陣列可能根據使用者的地區設定與 ICU 不完全對齊。

### Windows 的怪癖

  * 月份的陣列包含 12 種元素。
  * 返回的陣列可能根據使用者的地區設定與 ICU 不完全對齊。

### 瀏覽器的怪癖

  * 日期名稱不完全符合 ICU
  * 月份的陣列包含 12 種元素。

## navigator.globalization.getDatePattern

返回一個模式字串格式化和解析日期根據用戶端的使用者首選項。

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### 說明

返回到 `successCallback` 的模式。作為一個參數傳遞進來的物件包含以下屬性：

  * **pattern**： 要格式化和解析日期的日期和時間模式。 模式遵循[Unicode 技術標準 #35](http://unicode.org/reports/tr35/tr35-4.html)。 *（字串）*

  * **timezone**： 在用戶端上的時區的縮寫的名稱。*（字串）*

  * **utc_offset**： 用戶端時區的時間和協調通用時間以秒為單位的當前區別。*（數）*

  * **dst_offset**： 用戶端的非夏令時之間的秒數的當前的日光節約時間偏移量的時區和用戶端的夏時制節約的時區。*（數）*

如果獲取模式時發生錯誤，則 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.PATTERN_ERROR`.

`options` 參數是可選的並且預設為以下值：

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` 可以 `short`、 `medium`、 `long`、 或 `full` `options.selector` 可以是 `date`、 `time` 或 `date and time`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `en_US` 地區設定時，本示例顯示彈出一個對話方塊文本如 `模式： 按/yyyy h:mm`：

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 怪癖

  * `formatLength` 選項支援只有 `short` 和 `full` 的值。

  * `pattern` 的 `date and time` 模式返回只完整的日期時間格式。

  * `timezone` 返回完整時區名稱。

  * `dst_offset` 屬性不受支援，並且始終返回零。

  * 該模式可能根據使用者的地區設定與 ICU 不完全對齊。

### Windows 的怪癖

  * `formatLength` 選項支援只有 `short` 和 `full` 的值。

  * `pattern` 的 `date and time` 模式返回只完整的日期時間格式。

  * `timezone` 返回完整時區名稱。

  * `dst_offset` 屬性不受支援，並且始終返回零。

  * 該模式可能根據使用者的地區設定與 ICU 不完全對齊。

### 瀏覽器的怪癖

  * 模式屬性不支援，則返回空字串。

  * 只有鉻返回時區屬性。其格式是"世界/{City} 的一部分"。 其他瀏覽器返回空字串。

## navigator.globalization.getFirstDayOfWeek

返回根據用戶端的使用者首選項和日曆周的第一天。

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### 說明

星期數編號從 1，這裡假設 1 是星期日。 返回一天到 `successCallback` 與 `properties` 物件作為一個參數。 該物件應該具有 `value` 值的 `String` 屬性。

如果獲取模式時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.UNKNOWN_ERROR`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `en_US` 地區設定時，這將顯示彈出一個對話方塊文本類似于 `的一天： 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

### Windows 的怪癖

  * 對 Windows 8.0/8.1 所示的值取決於使用者的日曆首選項。在 Windows Phone 8.1 的值取決於當前的地區設定。

### 瀏覽器的怪癖

  * 只有 79 地區設定支援是因為 moment.js 此方法中使用。

## navigator.globalization.getNumberPattern

返回一個模式字串格式化和解析數位根據用戶端的使用者首選項。

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### 說明

返回到 `successCallback` 與 `屬性` 物件作為參數的模式。該物件包含以下屬性：

  * **pattern**： 要格式化和解析數位的數位模式。 模式遵循[Unicode 技術標準 #35](http://unicode.org/reports/tr35/tr35-4.html)。 *（字串）*

  * **symbol**： 要使用時格式化和解析，例如，%或貨幣符號的符號。*（字串）*

  * **fraction**： 解析和貨幣的格式時要使用的小數位數的數目。*（數）*

  * **rounding**： 舍入增量解析和格式時要使用。*（數）*

  * **positive**： 要為正數時分析和格式設置使用的符號。*（字串）*

  * **negative**： 要為負數時分析和格式設置使用的符號。*（字串）*

  * **decimal**： 小數點符號用於分析和格式設置。*（字串）*

  * **grouping**： 分組符號用於分析和格式設置。*（字串）*

如果獲取模式時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.PATTERN_ERROR`.

`options` 參數是可選的且其預設值：

    {type:'decimal'}
    

`options.type` 可以是 `decimal`、 `percent` 或 `currency`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `en_US` 地區設定時，此時應顯示彈出一個對話方塊文本類似于遵循的效果：

    navigator.globalization.getNumberPattern(
        function (pattern) {alert('pattern: '  + pattern.pattern  + '\n' +
                                  'symbol: '   + pattern.symbol   + '\n' +
                                  'fraction: ' + pattern.fraction + '\n' +
                                  'rounding: ' + pattern.rounding + '\n' +
                                  'positive: ' + pattern.positive + '\n' +
                                  'negative: ' + pattern.negative + '\n' +
                                  'decimal: '  + pattern.decimal  + '\n' +
                                  'grouping: ' + pattern.grouping);},
        function () {alert('Error getting pattern\n');},
        {type:'decimal'}
    );
    

結果：

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 怪癖

  * `pattern` 屬性不受支援，並返回一個空字串。

  * `fraction` 屬性不受支援，並返回零。

### Windows 的怪癖

  * `pattern` 屬性不受支援，並返回一個空字串。

### 瀏覽器的怪癖

  * getNumberPattern 支援 Chrome 裡只;唯一定義的屬性是`模式`.

## navigator.globalization.isDayLightSavingsTime

指示是否夏令時實際上是針對給定的日期，使用客戶機的時區和日曆。

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### 說明

指示夏令時實際上是 `successCallback` 與作為參數的 `屬性` 物件。 該物件應該具有 `Boolean` 值的 `dst` 屬性。 `true` 值表示日光節約時間實際上是在給定的日期和事件 ； `false` 指示它不是。

傳入的參數 【 `date` 應該是 `Date` 類型.

如果閱讀日期時發生錯誤，然後 `errorCallback` 執行。預期的錯誤碼是 `GlobalizationError.UNKNOWN_ERROR`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

在夏季，如果瀏覽器設置為啟用 DST 的時區，這應該顯示彈出一個對話方塊文本類似于 `dst： 真正`：

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

返回一個數位的格式設置為根據用戶端的使用者首選項的字串。

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### 說明

返回帶格式的數位字串到 `successCallback` 與 `屬性` 物件作為一個參數。 該物件應該具有 `value` 值的 `String` 屬性。

如果格式數時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.FORMATTING_ERROR`.

`options` 參數是可選的且其預設值：

    {type:'decimal'}
    

`options.type` 可以 'decimal'、 'percent' 或 'currency'。

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `en_US` 地區設定時，這將顯示彈出一個對話方塊文本類似于 `號碼： 3.142`：

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows 的怪癖

  * Windows 8.0 不支援數位舍入，因此值，不會自動四捨五入。

  * Windows 8.1 和 Windows Phone 8.1 小數部分會被截斷而不是圓形時 `percent` 數位類型因此小數位數計數設置為 0。

  * `percent` 數位不進行分組，他們無法分析在 stringToNumber 如果分組。

### 瀏覽器的怪癖

  * `currency`類型不受支援。

## navigator.globalization.stringToDate

分析日期格式設置為一個字串，根據用戶端的使用者首選項和日曆使用時區的用戶端，並返回對應的 date 物件。

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### 說明

作為一個參數與 `properties` 物件的成功回檔返回的日期。該物件應具有以下屬性：

  * **year**： 四位數表示的年份。*（數）*

  * **month**： （0-11) 個月。*（數）*

  * **day**： 從 （1-31) 天。*（數）*

  * **hour**： 從 （0-23） 小時。*（數）*

  * **minute**： 從 （0-59) 分鐘。*（數）*

  * **second**： 的第二位 （0-59)。*（數）*

  * **milisecond**： 的毫秒數 （從 0-999），在所有平臺上不可用。*（數）*

入站的 `dateString` 參數應該是 `String` 類型.

`options` 參數是可選的並且預設為以下值：

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` 可以 `short`、 `medium`、 `long`、 或 `full` `options.selector` 可以是 `date`、 `time` 或 `date and time`.

如果解析日期字串時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.PARSING_ERROR`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * 瀏覽器

### 示例

當瀏覽器設置為 `en_US` 地區設定時，這將顯示彈出一個對話方塊文本類似于 `月： 8 天： 25 年： 2012 年`。 請注意，整數是一個月小於字串，作為月整數表示陣列索引。

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 怪癖

  * `formatLength` 選項支援只有 `short` 和 `full` 的值。

  * 日期和時間的選擇器模式一直是一種完整的日期時間格式。

  * 入站的 `dateString` 參數應根據返回的 getDatePattern 模式形成。這種模式可能根據使用者的地區設定與 ICU 不完全對齊。

### Windows 的怪癖

  * `formatLength` 選項支援只有 `short` 和 `full` 的值。

  * 日期和時間的選擇器模式一直是一種完整的日期時間格式。

  * 入站的 `dateString` 參數應根據返回的 getDatePattern 模式形成。這種模式可能根據使用者的地區設定與 ICU 不完全對齊。

### 瀏覽器的怪癖

  * 只有 79 地區設定支援是因為 moment.js 此方法中使用。

  * 傳入的字串應符合`dateToString`的輸出格式和五月不完全符合重症監護病房，根據使用者的地區設定。

  * `time`選擇器支援`short`和`full`formatLength 只。

## navigator.globalization.stringToNumber

分析的數位格式化為根據用戶端的使用者首選項的字串並返回相應的數位。

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### 說明

返回到 `successCallback` 與 `properties` 物件作為參數的數。該物件應該具有 `value` 值的 `Number` 屬性。

如果分析數位字串時發生錯誤，然後 `errorCallback` 執行同一個 `GlobalizationError` 物件作為一個參數。 預期的錯誤碼是 `GlobalizationError.PARSING_ERROR`.

`options` 參數是可選的並且預設為以下值：

    {type:'decimal'}
    

`options.type` 可以是 `decimal`、 `percent` 或 `currency`.

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows

### 示例

當瀏覽器設置為 `en_US` 地區設定時，此時應顯示彈出一個對話方塊文本類似于 `號碼： 1234.56`：

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 怪癖

  * 在 `percent` 類型發生時返回的值不被除以 100。

### Windows 的怪癖

  * 該字串必須嚴格符合地區設定格式。例如，百分比符號就應該用 EN-US 地區設定的空間分隔，如果類型參數是 '%'。

  * 不必須分組 `percent` 數位正確解析。

## GlobalizationError

從全球化的 API 表示一個錯誤的物件。

### 屬性

  * **code**： 表示錯誤類型的以下代碼之一 *（數）* 
      * GlobalizationError.UNKNOWN_ERROR: 0
      * GlobalizationError.FORMATTING_ERROR: 1
      * GlobalizationError.PARSING_ERROR: 2
      * GlobalizationError.PATTERN_ERROR: 3
  * **message**： 文本消息，包括有關錯誤的解釋，和/或詳細說明 *（字串）*

### 說明

此物件創建和填充的科爾多瓦，並返回到出現錯誤時的回檔。

### 支援的平臺

  * 亞馬遜火 OS
  * Android 系統
  * 黑莓 10
  * 火狐瀏覽器作業系統
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows

### 示例

當以下錯誤回檔執行時，它會顯示彈出一個對話方塊文本類似于 `code: 3` 和 `message:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };