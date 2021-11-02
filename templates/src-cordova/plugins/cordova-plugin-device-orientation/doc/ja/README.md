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

# cordova-plugin-device-orientation

[![Build Status](https://travis-ci.org/apache/cordova-plugin-device-orientation.svg)](https://travis-ci.org/apache/cordova-plugin-device-orientation)

このプラグインは、デバイスのコンパスへのアクセスを提供します。 コンパスは方向またはというデバイスは、通常から指摘装置の上部の見出しを検出するセンサーです。 359.99、0 は北に 0 からの角度で見出しを測定します。

アクセスは、グローバル `navigator.compass` オブジェクトを介して。

オブジェクトは、グローバル スコープの `ナビゲーター` に添付、それがないまで `deviceready` イベントの後。

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.compass);
    }
    

## インストール

    cordova plugin add cordova-plugin-device-orientation
    

## サポートされているプラットフォーム

  * アマゾン火 OS
  * アンドロイド
  * ブラックベリー 10
  * ブラウザー
  * Firefox の OS
  * iOS
  * Tizen
  * Windows Phone 7 および 8 (可能な場合ハードウェアで)
  * Windows 8

## メソッド

  * navigator.compass.getCurrentHeading
  * navigator.compass.watchHeading
  * navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

現在のコンパス方位を取得します。コンパス針路が `compassSuccess` コールバック関数を使用して `CompassHeading` オブジェクトを介して返されます。

    navigator.compass.getCurrentHeading(compassSuccess, compassError);
    

### 例

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

デバイスの定期的な間隔で現在の方位を取得します。見出しを取り出すたびに `headingSuccess` コールバック関数が実行されます。

返される時計 ID コンパス時計腕時計間隔を参照します。時計 ID は、navigator.compass を見て停止する `navigator.compass.clearWatch` を使用できます。

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions` は、次のキーを含めることができます。

  * **周波数**: 多くの場合、コンパス針路 (ミリ秒単位) を取得する方法。*(数)*(デフォルト: 100)
  * **フィルター**: watchHeading 成功時のコールバックを開始する必要度の変化。この値を設定すると、**頻度**は無視されます。*(数)*

### 例

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
    

### ブラウザーの癖

現在の見出しの値は、コンパスをシミュレートするためにランダムに生成されます。

### iOS の癖

1 つだけ `watchHeading` は iOS の効果を同時にすることができます。 `watchHeading` はフィルターを使用して、`getCurrentHeading` または `watchHeading` を呼び出す見出しの変更を指定する既存のフィルター値を使用します。 フィルターを使用して見出しの変更を見て時間間隔よりも効率的にファイルです。

### アマゾン火 OS 癖

  * `filter`サポートされていません。

### Android の癖

  * サポートされていません`filter`.

### Firefox OS 癖

  * サポートされていません`filter`.

### Tizen の癖

  * サポートされていません`filter`.

### Windows Phone 7 と 8 癖

  * サポートされていません`filter`.

## navigator.compass.clearWatch

時計 ID パラメーターによって参照されるコンパスを見て停止します。

    navigator.compass.clearWatch(watchID);
    

  * **watchID**: によって返される ID`navigator.compass.watchHeading`.

### 例

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

`CompassHeading` オブジェクトは、`compassSuccess` コールバック関数に返されます。

### プロパティ

  * **magneticHeading**: 1 つの時点で 0 359.99 から角度での見出し。*(数)*

  * **trueHeading**: 度 0 359.99 で地理的な北極を基準にして、1 つの時点での見出し。 負の値は真針路を特定できないことを示します。 *(数)*

  * **headingAccuracy**: 報告された見出しと真方位角度偏差。*(数)*

  * **タイムスタンプ**: この見出しを決定した時。*(ミリ秒)*

### アマゾン火 OS 癖

  * `trueHeading`レポートと同じ値はサポートされていません`magneticHeading`

  * `headingAccuracy`常に 0 の間の違いはありませんので、 `magneticHeading` と`trueHeading`

### Android の癖

  * `trueHeading`プロパティはサポートされていませんと同じ値を報告`magneticHeading`.

  * `headingAccuracy`プロパティは常に 0 の間の違いはありませんので、 `magneticHeading` と`trueHeading`.

### Firefox OS 癖

  * `trueHeading`プロパティはサポートされていませんと同じ値を報告`magneticHeading`.

  * `headingAccuracy`プロパティは常に 0 の間の違いはありませんので、 `magneticHeading` と`trueHeading`.

### iOS の癖

  * `trueHeading`経由で有効になっている位置情報サービスのプロパティが返されますのみ`navigator.geolocation.watchLocation()`.
 
## CompassError

`CompassError` オブジェクトにエラーが発生したときに `compassError` コールバック関数に返されます。

### プロパティ

  * **コード**: 次のいずれかの定義済みのエラー コード。

### 定数

  * `CompassError.COMPASS_INTERNAL_ERR`
  * `CompassError.COMPASS_NOT_SUPPORTED`