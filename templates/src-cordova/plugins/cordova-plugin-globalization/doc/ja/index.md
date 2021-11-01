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

# cordova-plugin-globalization

このプラグインは、情報を取得し、ユーザーのロケール、言語、およびタイム ゾーンに固有の操作を実行します。 ロケールと言語の違いに注意してください: ロケール コントロール番号、日付、および時刻の表示方法、地域の言語で決まりますがどのような言語のテキストの間のように、ロケールの設定とは無関係です。 多くの開発者を使用してロケール設定両方、しかしユーザーは「英語」彼女言語を設定できませんでした理由はない"フランス語"ロケールので英語が日付時刻等でテキストが表示されますが表示されるフランスでは。 残念ながら、ほとんどのモバイルプラット フォーム現在行いませんこれらの設定の間の区別。

このプラグインでは、グローバル `navigator.globalization` オブジェクトを定義します。

グローバル スコープではあるがそれがないまで `deviceready` イベントの後です。

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## インストール

    cordova plugin add cordova-plugin-globalization
    

## オブジェクト

*   GlobalizationError

## メソッド

*   navigator.globalization.getPreferredLanguage
*   navigator.globalization.getLocaleName
*   navigator.globalization.dateToString
*   navigator.globalization.stringToDate
*   navigator.globalization.getDatePattern
*   navigator.globalization.getDateNames
*   navigator.globalization.isDayLightSavingsTime
*   navigator.globalization.getFirstDayOfWeek
*   navigator.globalization.numberToString
*   navigator.globalization.stringToNumber
*   navigator.globalization.getNumberPattern
*   navigator.globalization.getCurrencyPattern

## navigator.globalization.getPreferredLanguage

クライアントの現在の言語の BCP 47 言語タグを取得します。

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### 説明

`プロパティ` オブジェクトに `successCallback` を BCP 47 準拠の言語識別子タグをパラメーターとして返します。 そのオブジェクトの `文字列` 値を `value` プロパティがあります。

言語を取得中にエラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.UNKNOWN_ERROR`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

テキストとポップアップ ダイアログが表示されるときに、`EN-US` 言語にブラウザーを設定すると、`言語: アン米`：

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### Android の癖

*   ISO 639-1 の 2 文字の言語コード、大文字の ISO 3166-1 国名コードおよびハイフンで区切られたバリアントを返します。例:"en"、"EN-US"、「米国」

### Windows Phone 8 癖

*   返します ISO 639-1 の 2 文字言語コードと設定、ハイフンで区切られた「言語」に対応する地域バリアントの ISO 3166-1 国名コード。
*   地域バリアント「言語」の設定のプロパティは Windows Phone に無関係な"国/地域] の設定によって決定できないことに注意してください。

### Windows の癖

*   返します ISO 639-1 の 2 文字言語コードと設定、ハイフンで区切られた「言語」に対応する地域バリアントの ISO 3166-1 国名コード。

## navigator.globalization.getLocaleName

クライアントの現在のロケール設定 BCP 47 準拠タグを返します。

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### 解説

`properties` オブジェクト `successCallback` にパラメーターとして BCP 47 準拠のロケール id 文字列を返します。 そのオブジェクトの `String` 値を `value` プロパティがあります。 ロケール タグは 2 文字の小文字の言語コード、大文字 2 文字の国コード、ハイフンで区切られた (不特定) のバリアント型コードで構成されます。

ロケールを取得中にエラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.UNKNOWN_ERROR`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

ブラウザーは、`EN-US` ロケールに設定されて、テキストとポップアップ ダイアログが表示されます `ロケール: EN-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Android の癖

*   Java は区別されません設定「言語」と「ロケール設定、」ので、このメソッドは、本質的に `navigator.globalizatin.getPreferredLanguage()` と同じ.

### Windows Phone 8 癖

*   返します ISO 639-1 の 2 文字言語コードおよびハイフンで区切られた「地域形式」の設定に対応する地域バリアントの ISO 3166-1 国名コード。

### Windows の癖

*   コントロール パネルの [時計、言語および地域地域フォーマット形式、->->->-> と-> 地域の形式で Windows Phone 8.1-> の地域の設定ロケール設定を変更することができます。

## navigator.globalization.dateToString

日付を返します、クライアントのロケールおよびタイムゾーンに従って文字列として書式設定されます。

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### 解説

`successCallback` にパラメーターとして渡されたオブジェクトからアクセス可能な `値` プロパティ経由で書式設定された日付 `文字列` を返します.

受信 `日付` パラメーターは `Date` 型である必要があります。.

日付の書式設定エラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.FORMATTING_ERROR`.

`options` パラメーターはオプションであり、既定値は。

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` `short`、`medium`、`long`、または `full` にすることができます。.

`date`、`time` または `date and time` にすることができます `options.selector`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

ようなテキストとポップアップ ダイアログが表示されます、ブラウザーは `en_US` ロケールの場合、`日付: 2012/09/25 16:21`、既定のオプションを使用して。

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Android の癖

*   `formatLength` オプションは Unicode [UTS #35][1] のサブセットです。 `短い` 既定オプション内でユーザーの選択した日付形式によって異なります `設定 -> システム -> 日付 ＆ 時間 -> 選択日付形式`、4 桁、2 桁の数字だけで、`年` のパターンを提供します。 つまり、ことそれ完全に平行でない [ICU][2].

 [1]: http://unicode.org/reports/tr35/tr35-4.html
 [2]: http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US

### Windows Phone 8 癖

*   `formatLength` オプションは `short` と `full` の値だけをサポートします。

*   '日付と時刻' のセレクターのパターンは常に完全な datetime 形式です。

*   返される値が完全にユーザーのロケールに応じて ICU で配置されます。

### Windows の癖

*   `formatLength` オプションは `short` と `full` の値だけをサポートします。

*   '日付と時刻' のセレクターのパターンは常に完全な datetime 形式です。

*   返される値が完全にユーザーのロケールに応じて ICU で配置されます。

### Firefox OS 癖

*   `formatLength` は `long` と `full` に識別されません。 
*   1 つだけ （`long` または `full` バージョンなし） の日付を表示する方法

## navigator.globalization.getCurrencyPattern

書式設定および通貨の値によると、クライアントのユーザーの基本設定と ISO 4217 通貨コードを解析するパターン文字列を返します。

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### 解説

`properties` オブジェクト `successCallback` にパラメーターとしてパターンを返します。そのオブジェクトは、次のプロパティを含める必要があります。

*   **pattern**: 通貨パターンを書式設定および通貨の値を解析します。 パターンは、[Unicode 技術標準 #35][1] に従ってください。 *(文字列)*

*   **code**: パターンの ISO 4217 通貨コード。*(文字列)*

*   **fraction**: 解析および通貨を書式設定するときに使用する小数部の桁の数。*(数)*

*   **rounding**: 解析および書式設定するときに使用するインクリメントに丸め。*(数)*

*   **decimal**: 解析および書式設定を使用する小数点の記号。*(文字列)*

*   **grouping**: 解析および書式設定を使用する区切り記号。*(文字列)*

受信 `currencyCode` パラメーター、ISO 4217 通貨コードは、たとえば 'USD' のいずれかの `文字列` でなければなりません。

パターンを取得時にエラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.FORMATTING_ERROR`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   iOS
*   Windows

### 例

この例では、ブラウザーは `en_US` ロケールに設定され、選択した通貨は米国ドル、に従って結果のようなテキストとポップアップ ダイアログが表示されます。

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
    

期待される結果:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### Windows の癖

*   唯一の 'コード' と '分数' プロパティはサポートされて

## navigator.globalization.getDateNames

月の名前またはクライアントのユーザーの好みやカレンダーに応じて曜日の配列を返します。

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### 解説

`properties` オブジェクト `successCallback` にパラメーターとして名前の配列を返します。 そのオブジェクトには `value` 値の `Array` と `String` のプロパティが含まれます。 年または選択したオプションに応じて、週の最初の日の最初の月のいずれかから始まってアレイ機能の名前。

名前の取得エラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.UNKNOWN_ERROR`.

`options` パラメーターはオプションであり、既定値は。

    {type:'wide', item:'months'}
    

`options.type` の値は `narrowく` または `wide` ことができます。.

`options.item` の値は `month` または `days` をすることができます。.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

`En_US` ロケールにブラウザーを設定すると、この例のようなテキストで、毎月 1 つ 12 のポップアップ ダイアログのシリーズが表示されます `ヶ月: 1 月`。

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### Firefox OS 癖

*   `options.type` のいくつかの言語の重要な `genitive` の値をサポートしています

### Windows Phone 8 癖

*   数ヶ月の配列には 13 の要素が含まれます。
*   返される配列が完全にユーザーのロケールに応じて ICU で配置されます。

### Windows の癖

*   数ヶ月の配列には 12 の要素が含まれます。
*   返される配列が完全にユーザーのロケールに応じて ICU で配置されます。

## navigator.globalization.getDatePattern

クライアントのユーザーの設定に従った日付を解析するパターン文字列を返します。

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### 説明

`successCallback` にパターンを返します。パラメーターとして渡されたオブジェクトには、次のプロパティが含まれています。

*   **pattern**: 書式し、日付を解析する日付と時刻のパターン。 パターンは、[Unicode 技術標準 #35][1] に従ってください。 *(文字列)*

*   **timezone**: クライアントのタイム ゾーンの省略名。*(文字列)*

*   **utc_offset**: クライアントのタイム ゾーンと世界協定時刻間の秒で現在の差異。*(数)*

*   **dst_offset**： クライアントの非夏時間 (秒単位) は、現在の夏時間オフセットのタイムゾーンとクライアントの夏時間保存のタイム ゾーン。*(数)*

パターンを取得時にエラーがある場合、`解り` パラメーターとして `GlobalizationError` オブジェクトで実行します。 予想されるエラーコードは `GlobalizationError.PATTERN_ERROR`.

`options` のパラメーターはオプションであり、次の値を既定値します。

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` `short`、`medium`、`long`、または `full` にすることができます。 `date`、`time` または `date and time` にすることができます `options.selector`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   iOS
*   Windows Phone 8
*   Windows

### 例

ブラウザーは `en_US` ロケールに設定されて、この例が表示されますテキストとポップアップ ダイアログなど `パターン： M/d と yyyy h:mm、`：

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 癖

*   `formatLength` オプションは `short` と `full` の値だけをサポートします。

*   `日付と時刻` のパターンの `パターン` は完全な datetime 形式のみを返します。

*   `timezone` のタイム ゾーン名を返します。

*   `dst_offset` プロパティはサポートされていませんし、常にゼロを返します。

*   パターンは、可能性がありますいない完全にユーザーのロケールに応じて ICU で配置されます。

### Windows の癖

*   `formatLength` オプションは `short` と `full` の値だけをサポートします。

*   `日付と時刻` のパターンの `パターン` は完全な datetime 形式のみを返します。

*   `timezone` のタイム ゾーン名を返します。

*   `dst_offset` プロパティはサポートされていませんし、常にゼロを返します。

*   パターンは、可能性がありますいない完全にユーザーのロケールに応じて ICU で配置されます。

## navigator.globalization.getFirstDayOfWeek

よると、クライアントのユーザー設定カレンダー週の最初の曜日を返します。

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### 解説

週の日 1 日曜日であると見なされます、1 から始まる番号が付けられます。 `プロパティ` オブジェクト `successCallback` にパラメーターとして返します。 そのオブジェクトの `文字列` 値を `value` プロパティがあります。

パターンを取得時にエラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.UNKNOWN_ERROR`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

ブラウザーは `en_US` ロケールに設定されてのようなテキストとポップアップ ダイアログが表示されます `日： 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

### Windows の癖

*   Windows 8.0/8.1 値によって異なりますユーザー ' 好みのカレンダーします。Windows Phone 8.1 の値は現在のロケールに依存します。

## navigator.globalization.getNumberPattern

クライアントのユーザーの設定に従って数値を解析するパターン文字列を返します。

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### 解説

`properties` オブジェクト `successCallback` にパラメーターとしてパターンを返します。そのオブジェクトは、次のプロパティを含める必要があります。

*   **pattern**: 番号のパターンを書式設定および解析の数字。 パターンは、[Unicode 技術標準 #35][1] に従ってください。 *(文字列)*

*   **symbol**: 書式設定と解析、パーセントや通貨記号などのときに使用するシンボル。*(文字列)*

*   **fraction**: 解析および通貨を書式設定するときに使用する小数部の桁の数。*(数)*

*   **rounding**: 解析および書式設定するときに使用するインクリメントに丸め。*(数)*

*   **positive**： 正の数の解析および書式設定するときに使用する記号。*(文字列)*

*   **negative**: 負の数の解析および書式設定するときに使用する記号。*(文字列)*

*   **decimal**: 解析および書式設定を使用する小数点の記号。*(文字列)*

*   **grouping**: 解析および書式設定を使用する区切り記号。*(文字列)*

パターンを取得時にエラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.PATTERN_ERROR`.

`options` パラメーターはオプションであり、既定値は。

    {type:'decimal'}
    

`options.type` は `10 decimal`、`percent`、および `currency` をすることができます。.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   iOS
*   Windows Phone 8
*   Windows

### 例

`En_US` ロケールにブラウザーを設定すると、次の結果のようなテキストとポップアップ ダイアログが表示されるこの必要があります。

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
    

結果:

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 癖

*   `pattern` プロパティはサポートされていませんし、空の文字列を返します。

*   `fraction` プロパティはサポートされていませんし、ゼロを返します。

### Windows の癖

*   `pattern` プロパティはサポートされていませんし、空の文字列を返します。

## navigator.globalization.isDayLightSavingsTime

夏時間の時間が、クライアントのタイム ゾーンとカレンダーを使用して特定の日付に対して有効かどうかを示します。

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### 説明

夏時間が有効で `successCallback` `properties` オブジェクトをパラメーターとして使用するかどうかを示します。 そのオブジェクトは `dst` プロパティの `Boolean` 値が必要です。 値 `true` は夏時間が有効で特定の日付の `false の場合それがない` ことを示します。

受信パラメーター `date` `Date` 型である必要があります。.

日付の読み取り中にエラーがある場合は `解り` が実行します。予想されるエラーコードは `GlobalizationError.UNKNOWN_ERROR`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

夏の間、これのようなテキストとポップアップ ダイアログを表示する必要がありますブラウザーは、DST が有効なタイム ゾーンに設定されている場合と `dst: true`。

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

クライアントのユーザーの設定に従って文字列として書式設定された数を返します。

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### 解説

`properties` オブジェクトに `successCallback` をパラメーターとして書式設定された数値文字列を返します。 そのオブジェクトの `String` 値を `value` プロパティがあります。

数書式設定エラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.FORMATTING_ERROR`.

`options` パラメーターはオプションであり、既定値は。

    {type:'decimal'}
    

`options.type` は 'decimal'、'percent' または 'currency' することができます。

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   iOS
*   Windows Phone 8
*   Windows

### 例

ブラウザーは `en_US` ロケールに設定されてのようなテキストとポップアップ ダイアログが表示されます `数: 3.142`。

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows の癖

*   Windows 8.0 数の丸めをサポートしていない、その値は丸められません自動的に。

*   Windows 8.1 および Windows Phone 8.1 小数部が切り捨てられているのではなく `パーセント` 型したがって小数桁数の場合丸めカウントを 0 に設定されます。

*   としてグループ化された場合に stringToNumber で解析できません、`％` の数字はグループ化されません。

## navigator.globalization.stringToDate

クライアントのユーザーの基本設定や、クライアントのタイム ゾーンを使用して予定表によると、文字列として書式設定された日付を解析し、対応する日付オブジェクトを返します。

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### 解説

`properties` オブジェクトで成功コールバックにパラメーターとして日付を返します。そのオブジェクトは、次のプロパティが必要です。

*   **year**： 4 桁の年。*(数)*

*   **month**: (0-11) から 1 カ月。*(数)*

*   **day**: 日 (1 から 31)。*(数)*

*   **hour**: 時間 (0-23) から。*(数)*

*   **minute**: (0-59） から分です。*(数)*

*   **second**: (0-59） から 2 番目。*(数)*

*   **milisecond**： 時間をミリ秒単位 (0 ～ 999) まですべてのプラットフォームでは利用できません。*(数)*

受信 `dateString` パラメーターは `String` 型である必要があります。.

`options` のパラメーターはオプションであり、次の値を既定値します。

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` `short`、`medium`、`long`、または `full` にすることができます。 `date`、`time` または `date and time` にすることができます `options.selector`.

日付文字列の解析エラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.PARSING_ERROR`.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

`En_US` ロケールにブラウザーを設定すると、`1 ヶ月： 8 日： 25 年: 2012年` のようなテキストとポップアップ ダイアログが表示されます。 注意： 整数は 1 ヶ月未満の文字列、月整数として配列のインデックスを表します。

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 癖

*   `formatLength` オプションは `short` と `full` の値だけをサポートします。

*   '日付と時刻' のセレクターのパターンは常に完全な datetime 形式です。

*   getDatePattern によって返されるパターンに準拠して受信 `dateString` パラメーターを形成する必要があります。このパターンは完全にユーザーのロケールに応じて ICU で配置されます。

### Windows の癖

*   `formatLength` オプションは `short` と `full` の値だけをサポートします。

*   '日付と時刻' のセレクターのパターンは常に完全な datetime 形式です。

*   getDatePattern によって返されるパターンに準拠して受信 `dateString` パラメーターを形成する必要があります。このパターンは完全にユーザーのロケールに応じて ICU で配置されます。

## navigator.globalization.stringToNumber

クライアントのユーザーの設定に従って文字列として書式設定された数を解析し、対応する番号を返します。

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### 解説

`properties` オブジェクト `successCallback` にパラメーターとして数を返します。そのオブジェクト `value` 値を持つ `Number` のプロパティがあります。

数値文字列の解析エラーがある場合、パラメーターとしての `GlobalizationError` オブジェクトに `解り` 実行しますし。 予想されるエラーコードは `GlobalizationError.PARSING_ERROR`.

`options` のパラメーターはオプションであり、次の値を既定値します。

    {type:'decimal'}
    

`options.type` は `10 decimal`、`percent`、および `currency` をすることができます。.

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   iOS
*   Windows Phone 8
*   Windows

### 例

これのようなテキストとポップアップ ダイアログを表示するブラウザー `en_US` ロケールを設定すると、`数: 1234.56`。

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 癖

*   `percent` 型の場合、返される値は 100 で分けられていません。

### Windows の癖

*   文字列をロケールの形式に厳密に従う必要があります。型パラメーターは '%' たとえば、パーセント記号必要があります - 英語ロケールのためのスペースで区切られました。

*   `percent` の数値する必要があります正しく解析化されません。

## GlobalizationError

グローバリゼーション API からエラーを表すオブジェクト。

### プロパティ

*   **code**: エラーの種類を表す次のコードの 1 つ *(数)* 
    *   GlobalizationError.UNKNOWN_ERROR: 0
    *   GlobalizationError.FORMATTING_ERROR: 1
    *   GlobalizationError.PARSING_ERROR: 2
    *   GlobalizationError.PATTERN_ERROR: 3
*   **message**: エラーの説明が含まれていますおよび/または *(文字列)* の詳細をテキスト メッセージ

### 解説

このオブジェクト作成しコルドバ、によって移入され、エラーの場合のコールバックに返されます。

### サポートされているプラットフォーム

*   アマゾン火 OS
*   アンドロイド
*   ブラックベリー 10
*   Firefox の OS
*   iOS
*   Windows Phone 8
*   Windows

### 例

次のエラー コールバックを実行するのようなテキストとポップアップ ダイアログが表示されます `コード: 3` と `メッセージ:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };
