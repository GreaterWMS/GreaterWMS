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

이 플러그인 디바이스의 나침반에 대 한 액세스를 제공합니다. 나침반 방향 또는 표제는 장치 지적 이다, 일반적으로 장치 위에서 감지 하는 센서입니다. 359.99, 0가 북쪽을 0에서도에서 머리글을 측정 합니다.

글로벌 `navigator.compass` 개체를 통해 액세스가입니다.

개체 `navigator` 글로벌 범위 첨부 아니에요 때까지 사용할 수 있는 `deviceready` 이벤트 후.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.compass);
    }
    

## 설치

    cordova plugin add cordova-plugin-device-orientation
    

## 지원 되는 플랫폼

  * 아마존 화재 운영 체제
  * 안 드 로이드
  * 블랙베리 10
  * 브라우저
  * Firefox 운영 체제
  * iOS
  * Tizen
  * Windows Phone 7, 8 (사용 가능한 경우 하드웨어)
  * 윈도우 8

## 메서드

  * navigator.compass.getCurrentHeading
  * navigator.compass.watchHeading
  * navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

현재 나침반 제목 좀. 나침반 제목 `compassSuccess` 콜백 함수를 사용 하 여 `CompassHeading` 개체를 통해 반환 됩니다.

    navigator.compass.getCurrentHeading(compassSuccess, compassError);
    

### 예를 들어

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

정기적 장치의 현재 머리글을 가져옵니다. 제목 검색 때마다 `headingSuccess` 콜백 함수가 실행 됩니다.

반환 된 시계 ID 나침반 시계 간격을 참조합니다. 시계 ID는 navigator.compass를 보는 중지 하 `navigator.compass.clearWatch`와 함께 사용할 수 있습니다.

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions`는 다음 키를 포함할 수 있습니다.

  * **frequency**: 자주 밀리초에서 나침반 머리글을 검색 하는 방법. *(수)* (기본값: 100)
  * **filter**:도 watchHeading 성공 콜백을 시작 하는 데 필요한 변경. 이 값을 설정 하는 경우 **주파수** 는 무시 됩니다. *(수)*

### 예를 들어

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
    

### 브라우저 만지면

현재 제목에 대 한 값은 나침반을 시뮬레이션 하기 위해 임의로 생성 됩니다.

### iOS 단점

하나의 `watchHeading` iOS에서 한 번에 적용에서 될 수 있습니다. `watchHeading` 필터를 사용 하는 경우 `getCurrentHeading` 또는 `watchHeading` 호출 사용 하 여 기존 필터 값 지정 제목 변경. 필터와 제목 변화를 보고 시간을 간격으로 보다 더 효율적입니다.

### 아마존 화재 OS 단점

  * `filter`지원 되지 않습니다.

### 안 드 로이드 단점

  * 대 한 지원`filter`.

### 파이어 폭스 OS 단점

  * 대 한 지원`filter`.

### Tizen 특수

  * 대 한 지원`filter`.

### Windows Phone 7, 8 특수

  * 대 한 지원`filter`.

## navigator.compass.clearWatch

시계 ID 매개 변수에서 참조 하는 나침반을 보고 중지 합니다.

    navigator.compass.clearWatch(watchID);
    

  * **watchID**: ID 반환`navigator.compass.watchHeading`.

### 예를 들어

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

`CompassHeading` 개체는 `compassSuccess` 콜백 함수에 반환 됩니다.

### 속성

  * **magneticHeading**: 단일 시점에서 0-359.99에서도 제목. *(수)*

  * **trueHeading**: 단일 시점에서 0-359.99에서에서 지리적 북극을 기준으로 향하고. 음수 값을 나타냅니다 진정한 표제를 확인할 수 없습니다. *(수)*

  * **headingAccuracy**: 보고 된 머리글 사이의 진정한 제목도 편차. *(수)*

  * **타임 스탬프**:이 제목 결정 하는 시간. *(밀리초)*

### 아마존 화재 OS 단점

  * `trueHeading`지원 되지 않습니다 하지만 같은 값으로 보고`magneticHeading`

  * `headingAccuracy`항상 0 사이 차이가 있기 때문에 `magneticHeading` 와`trueHeading`

### 안 드 로이드 단점

  * `trueHeading`속성은 지원 되지 않습니다 하지만 같은 값으로 보고`magneticHeading`.

  * `headingAccuracy`속성은 항상 0 사이 차이가 있기 때문에 `magneticHeading` 와`trueHeading`.

### 파이어 폭스 OS 단점

  * `trueHeading`속성은 지원 되지 않습니다 하지만 같은 값으로 보고`magneticHeading`.

  * `headingAccuracy`속성은 항상 0 사이 차이가 있기 때문에 `magneticHeading` 와`trueHeading`.

### iOS 단점

  * `trueHeading`속성을 통해 위치 서비스에 대 한 반환만`navigator.geolocation.watchLocation()`.

## CompassError

`CompassError` 개체는 오류가 발생 하면 `compassError` 콜백 함수에 반환 됩니다.

### 속성

  * **코드**: 미리 정의 된 오류 코드 중 하나가 아래에 나열 된.

### 상수

  * `CompassError.COMPASS_INTERNAL_ERR`
  * `CompassError.COMPASS_NOT_SUPPORTED`