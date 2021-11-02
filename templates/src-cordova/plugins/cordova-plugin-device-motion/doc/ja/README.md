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

このプラグインは、デバイスの加速度計へのアクセスを提供します。 加速度計の現在のデバイスの向き、 *x* *y*、および*z*軸に沿って 3 つの次元の相対運動の変更 (*デルタ*) を検出するモーション センサーです。

アクセスは、グローバル `navigator.accelerometer` オブジェクトを介して。

オブジェクトは、グローバル スコープの `ナビゲーター` に添付、それがないまで `deviceready` イベントの後。

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.accelerometer);
    }
    

## インストール

    cordova plugin add cordova-plugin-device-motion
    

## サポートされているプラットフォーム

  * アマゾン火 OS
  * アンドロイド
  * ブラックベリー 10
  * ブラウザー
  * Firefox の OS
  * iOS
  * Tizen
  * Windows Phone 8
  * Windows

## メソッド

  * navigator.accelerometer.getCurrentAcceleration
  * navigator.accelerometer.watchAcceleration
  * navigator.accelerometer.clearWatch

## オブジェクト

  * 加速

## navigator.accelerometer.getCurrentAcceleration

*X* *y*、および *z* 軸に沿って現在の加速を取得します。

これらの加速度値が `accelerometerSuccess` コールバック関数に返されます。

    navigator.accelerometer.getCurrentAcceleration(accelerometerSuccess, accelerometerError);
    

### 例

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
    

### ブラウザーの癖

値 X、Y、Z モーションは、加速度計をシミュレートするためにすべてのランダムに生成される順序です。

### iOS の癖

  * iOS は、任意の時点で現在の加速度を得ることの概念を認識しません。

  * 加速度を見るし、データをキャプチャする必要があります指定した時間間隔で。

  * したがって、 `getCurrentAcceleration` 関数から報告された最後の値が生成されます、 `watchAccelerometer` を呼び出します。

## navigator.accelerometer.watchAcceleration

たびに `accelerometerSuccess` コールバック関数を実行する定期的な間隔で、デバイスの現在の `Acceleration` を取得します。 `acceleratorOptions` オブジェクトの `frquency` パラメーターを介してミリ秒単位で間隔を指定します。

返される時計 ID、加速度計腕時計間隔を参照し、加速度計を見て停止する `navigator.accelerometer.clearWatch` を使用することができます。

    var watchID = navigator.accelerometer.watchAcceleration(accelerometerSuccess,
                                                           accelerometerError,
                                                           accelerometerOptions);
    

  * **accelerometerOptions**: 次のオプションのキーを持つオブジェクト: 
      * **期間**: ミリ秒単位での加速度データと accelerometerSuccess への呼び出しの要求された期間。*(数)*(デフォルト: 10000）

### 例

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
    

### iOS の癖

API は、要求された間隔で、成功コールバック関数を呼び出しますが 40 ms の間デバイスへの要求の範囲を制限し、1000 ミリ秒になります。 たとえば、(ms) 3 秒の間隔を要求した場合、API 1 秒ごとに、デバイスからデータを要求がのみ成功コールバック 3 秒ごとを実行します。

## navigator.accelerometer.clearWatch

`watchID` パラメーターによって参照される `加速` を見て停止します。

    navigator.accelerometer.clearWatch(watchID);
    

  * **watchID**: によって返される ID`navigator.accelerometer.watchAcceleration`.

### 例

    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.accelerometer.clearWatch(watchID);
    

## 加速

特定の時点でキャプチャした `Accelerometer` データが含まれています。 加速度値のとおり重力の効果 (9.81 m/s ^2) デバイスにあるフラットと *x* *y*、直面していると返された *z* 値は `` ``、および `9.81` をする必要がありますように、.

### プロパティ

  * **x**: x 軸の加速度の量です。（m/s ^2)*(数)*
  * **y**: y 軸の加速度の量です。（m/s ^2)*(数)*
  * **z**: z 軸の加速度の量です。（m/s ^2)*(数)*
  * **タイムスタンプ**: 作成時のタイムスタンプ (ミリ秒単位)。*（，）*