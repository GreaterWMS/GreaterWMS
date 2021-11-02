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

이 플러그인 정보를 가져오고 사용자의 로캘, 언어 및 표준 시간대에 특정 작업을 수행 합니다. 로캘 및 언어의 차이점을 참고: 로캘 어떻게 숫자, 날짜 및 시간 표시 되는 제어 영역의 언어 어떤 언어 텍스트를 결정 하는 반면, 로캘 설정에 관계 없이 나타납니다. 종종 개발자 로캘 설정을 모두를 사용 하 여 하지만 거기에 아무 이유 없이 사용자 "영어"로 그녀의 언어를 설정할 수 없습니다 있지만 "프랑스어" 로캘을 영어 하지만 날짜, 시간, 등, 텍스트 표시 되도록 표시 됩니다 그들은 프랑스에. 불행히도, 대부분의 모바일 플랫폼 현재 만들지 않는다 이러한 설정 구분.

이 플러그인 글로벌 `navigator.globalization` 개체를 정의합니다.

전역 범위에 있지만 그것은 불가능까지 `deviceready` 이벤트 후.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## 설치

    cordova plugin add cordova-plugin-globalization
    

## 개체

*   GlobalizationError

## 메서드

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

클라이언트의 현재 언어에 대 한 BCP 47 언어 태그를 얻을.

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### 설명

매개 변수로 `속성` 개체와 `successCallback`를 BCP 47 규격 언어 식별자 태그를 반환합니다. 해당 개체 `값` 속성을 `문자열` 값으로 있어야 합니다.

점점 언어 오류가 있는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.UNKNOWN_ERROR`.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

브라우저 `EN-US` 언어로 설정 되어,이 텍스트와 함께 팝업 대화 상자가 표시 되어야 합니다 `언어: en-US`:

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### 안 드 로이드 단점

*   ISO 639-1 두 자리 언어 코드, 대문자 ISO 3166-1 국가 코드와 하이픈으로 구분 된 variant를 반환 합니다. 예: "en", "en-US", "미국"

### Windows Phone 8 단점

*   반환 ISO 639-1 두 글자 언어 코드 및 ISO 3166-1 국가 코드의 "언어" 설정, 하이픈으로 구분 된 해당 지역 이체.
*   Note 지역 변종 "언어" 설정의 속성 이며 Windows Phone 관련 없는 "국가/지역" 설정에 의해 결정 되지.

### 윈도우 특수

*   반환 ISO 639-1 두 글자 언어 코드 및 ISO 3166-1 국가 코드의 "언어" 설정, 하이픈으로 구분 된 해당 지역 이체.

## navigator.globalization.getLocaleName

클라이언트의 현재 로캘 설정에 대 한 BCP 47 호환 태그를 반환합니다.

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### 설명

매개 변수로 `properties` 개체와 `successCallback`를 BCP 47 규격 언어 식별자 태그를 반환합니다. 해당 개체 `value` 속성을 `String` 값으로 있어야 합니다. 두 자리 소문자 언어 코드, 두 글자 대문자 국가 코드와 하이픈으로 분리 된 (지정 되지 않은) 변형 코드 로캘 태그 구성 됩니다.

로케일을 받고 오류가 있는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.UNKNOWN_ERROR`.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

이 텍스트와 함께 팝업 대화 상자를 표시 하는 브라우저는 `en-US` 로케일으로 설정 되어, `로캘: EN-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### 안 드 로이드 단점

*   자바 구분 하지 않습니다 설정된 "language"를 설정된 "locale" 그래서이 메서드는 기본적으로 `navigator.globalizatin.getPreferredLanguage()`와 동일.

### Windows Phone 8 단점

*   반환 ISO 639-1 두 글자 언어 코드 및 ISO 3166-1 국가 코드 지역 변형 하이픈으로 구분 된 "지역 포맷" 설정에 해당 합니다.

### 윈도우 특수

*   시계, 언어 및 지역 지역 포맷 형식,->->->-> 제어판에서 및 Windows Phone 8.1에 국가별 형식-> 지역의-> 설정에서 로캘 설정을 변경할 수 있습니다.

## navigator.globalization.dateToString

날짜를 반환 합니다 클라이언트의 로케일과 시간대에 따라 문자열로 서식이 지정 된.

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### 설명

`successCallback` 매개 변수로 전달 된 개체에서 액세스할 수 있는 `값` 속성을 통해 `문자열` 형식이 지정 된 날짜를 반환.

인바운드 `date` 매개 변수는 `Date` 형식 이어야 합니다..

날짜 형식 오류가 있는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.FORMATTING_ERROR`.

`options` 매개 변수는 선택적 이며 그것의 기본 값은:

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` `short`, `medium`, `long` 또는 `full` 수 있습니다..

`options.selector` `date`, `time` 또는 `date and time` 수 있습니다..

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

이 텍스트와 유사한 팝업 대화 상자를 표시 하는 브라우저 `en_US` 로케일으로 설정 되어 있으면 `날짜: 2012 년 9 월 25 일 오후 4 시 21 분` 기본 옵션을 사용 하 여:

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### 안 드 로이드 단점

*   `formatLength` 옵션은 유니코드 [UTS #35][1]의 하위 집합입니다. 내에서 사용자 선택한 날짜 형식에는 기본 옵션 `짧은` 따라 `설정-> 시스템-> 날짜 및 시간 날짜 형식을 선택->`, 4 자리, 2 자리 하지와 `년` 패턴을 제공 하는. 즉 그 하지 완전히 정렬 되 [중 환자 실][2].

 [1]: http://unicode.org/reports/tr35/tr35-4.html
 [2]: http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US

### Windows Phone 8 단점

*   `formatLength` 옵션 `short` 하 고 `full` 값만 지원합니다.

*   'date and time' 선택기에 대 한 패턴은 항상 전체 날짜/시간 형식입니다.

*   반환 된 값 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

### 윈도우 특수

*   `formatLength` 옵션 `short` 하 고 `full` 값만 지원합니다.

*   'date and time' 선택기에 대 한 패턴은 항상 전체 날짜/시간 형식입니다.

*   반환 된 값 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

### 파이어 폭스 OS 단점

*   `formatLength` `long` 및 `full`를 구별 하지는 
*   날짜 (아니 `long` 또는 `full` 버전)를 표시 하는 하나의 방법

## navigator.globalization.getCurrencyPattern

포맷 하 고 클라이언트의 사용자 환경 설정 및 ISO 4217 통화 부호에 따라 통화 값을 구문 분석 패턴 문자열을 반환 합니다.

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### 설명

매개 변수로 `properties` 개체와 `successCallback`에 패턴을 반환합니다. 해당 개체에는 다음과 같은 속성이 포함 되어야 합니다.

*   **pattern**: 통화 패턴 서식을 지정 하 여 통화 값을 구문 분석 합니다. 패턴에 따라 [유니코드 기술 표준 #35][1]. *(문자열)*

*   **code**: ISO 4217 통화 코드 패턴. *(문자열)*

*   **fraction**: 구문 분석 하 고 통화 서식을 사용 하 여 소수 자릿수의 수. *(수)*

*   **rounding**: 라운딩 때 구문 분석 및 서식 지정을 사용 하 여 증가 합니다. *(수)*

*   **decimal**: 구문 분석 및 서식 지정에 사용할 소수점 기호가. *(문자열)*

*   **grouping**: 구문 분석 및 서식 지정에 사용할 그룹화 기호. *(문자열)*

인바운드 `currencyCode` 매개 변수는 ISO 4217 통화 코드, 예를 들어 '미화' 중 하나의 `문자열` 이어야 합니다.

오류 패턴을 얻는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.FORMATTING_ERROR`.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   iOS
*   윈도우

### 예를 들어

브라우저 `en_US` 로케일으로 설정 되어 있고 선택한 통화는 미국 달러,이 예제 수행 결과를 유사한 텍스트 팝업 대화 상자를 표시 합니다.

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
    

예상된 결과:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### 윈도우 특수

*   'code'와 'fraction' 속성만 지원 됩니다.

## navigator.globalization.getDateNames

달의 이름 또는 클라이언트의 사용자 환경 설정 및 일정에 따라 매일의 배열을 반환합니다.

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### 설명

매개 변수로 `properties` 개체와 `successCallback`에 이름 배열을 반환합니다. 해당 개체에는 `value` 속성을의 `문자열` 값 `배열` 포함 되어 있습니다. 배열 기능 이름과 년 또는 선택한 옵션에 따라 일주일의 첫날 첫 번째 달에서 시작.

이름을 얻는 오류가 있는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.UNKNOWN_ERROR`.

`options` 매개 변수는 선택적 이며 그것의 기본 값은:

    {type:'wide', item:'months'}
    

`narrow` 또는 `wide` `options.type`의 값 수 있습니다..

`pptions.item`의 값은 `month` 또는 `days` 수 있습니다..

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

브라우저는 `en_US` 로케일으로 설정 되어,이 예에서는 표시 12 팝업 대화 상자, 텍스트 비슷한 한달에 하나 시리즈 `달: 1 월`:

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### 파이어 폭스 OS 단점

*   `options.type` `genitive` 값, 일부 언어에 대 한 중요 한 지원

### Windows Phone 8 단점

*   달의 배열 13 요소가 포함 됩니다.
*   반환 된 배열은 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

### 윈도우 특수

*   달의 배열에는 12 요소가 포함 됩니다.
*   반환 된 배열은 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

## navigator.globalization.getDatePattern

포맷 하 고 클라이언트의 사용자 환경 설정에 따라 날짜 구문 분석 패턴 문자열을 반환 합니다.

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### 설명

`SuccessCallback`에 패턴을 반환합니다. 매개 변수로 전달 된 개체에는 다음 속성이 포함 되어 있습니다.

*   **pattern**: 포맷 하 고 날짜를 구문 분석할 날짜 및 시간 패턴. 패턴에 따라 [유니코드 기술 표준 #35][1]. *(문자열)*

*   **timezone**: 클라이언트에 표준 시간대의 약식된 이름. *(문자열)*

*   **utc_offset**: 클라이언트의 시간대와 세계시 간의 초에서 현재 차이. *(수)*

*   **dst_offset**: 클라이언트의 비 일광 절약 간격 (초)에 현재 일광 절약 시간제 오프셋의 시간대와 클라이언트의 일광 절약의 시간대. *(수)*

오류 패턴을 얻는 경우에, `errorCallback` `GlobalizationError` 개체와 매개 변수로 실행 합니다. 오류의 예상된 코드는 `GlobalizationError.PATTERN_ERROR`.

`options` 매개 변수는 선택적 이며 기본값은 다음 값:

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` `short`, `medium`, `long` 또는 `full` 수 있습니다. `options.selector` `date`, `time` 또는 `date and time` 수 있습니다..

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

브라우저 `en_US` 로케일으로 설정 하면이 예제에서는 같은 텍스트와 함께 팝업 대화 표시 `패턴: M/d/yyyy h:mm를`:

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 단점

*   `formatLength` 옵션 `short` 하 고 `full` 값만 지원합니다.

*   `date and time` 패턴에 대 한 `pattern` 전체 datetime 형식만을 반환합니다.

*   `timezone` 전체 시간 영역 이름을 반환합니다.

*   `dst_offset` 속성은 지원 되지 않으며 항상 0을 반환 합니다.

*   패턴은 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

### 윈도우 특수

*   `formatLength` 옵션 `short` 하 고 `full` 값만 지원합니다.

*   `date and time` 패턴에 대 한 `pattern` 전체 datetime 형식만을 반환합니다.

*   `timezone` 전체 시간 영역 이름을 반환합니다.

*   `dst_offset` 속성은 지원 되지 않으며 항상 0을 반환 합니다.

*   패턴은 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

## navigator.globalization.getFirstDayOfWeek

클라이언트의 사용자 환경 설정 및 일정에 따라 일주일의 첫 날을 반환합니다.

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### 설명

주일의 일 1 일요일으로 간주 됩니다 1에서 시작 하는 번호가 지정 됩니다. 매개 변수로 `properties` 개체와 `successCallback`를 날짜를 반환합니다. 해당 개체 `숫자` 값으로 `value` 속성이 있어야 합니다.

오류 패턴을 얻는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.PATTERN_ERROR`.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

이 텍스트와 유사한 팝업 대화 상자를 표시 하는 브라우저는 `en_US` 로케일으로 설정 되어, `하루: 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

### 윈도우 특수

*   윈도우 8.0 또는 8.1에 값 사용자에 따라 달라 집니다 ' 캘린더 환경 설정. Windows Phone 8.1에 가치는 현재 로케일에 따라 다릅니다.

## navigator.globalization.getNumberPattern

포맷 하 고 클라이언트의 사용자 환경 설정에 따라 숫자를 구문 분석할 패턴 문자열을 반환 합니다.

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### 설명

매개 변수로 `properties` 개체와 `successCallback`에 패턴을 반환합니다. 해당 개체에는 다음 속성이 포함 되어 있습니다.

*   **pattern**: 포맷 하 고 숫자를 구문 분석할 숫자 패턴. 패턴에 따라 [유니코드 기술 표준 #35][1]. *(문자열)*

*   **symbol**: 때 서식 지정 및 구문 분석, % 또는 통화 기호 등을 사용 하 여 기호. *(문자열)*

*   **fraction**: 구문 분석 하 고 통화 서식을 사용 하 여 소수 자릿수의 수. *(수)*

*   **rounding**: 라운딩 때 구문 분석 및 서식 지정을 사용 하 여 증가 합니다. *(수)*

*   **positive**: 양수 때 구문 분석 및 서식 지정에 사용할 기호. *(문자열)*

*   **negative**: 음수 때 구문 분석 및 서식 지정에 사용할 기호. *(문자열)*

*   **decimal**: 구문 분석 및 서식 지정에 사용할 소수점 기호가. *(문자열)*

*   **grouping**: 구문 분석 및 서식 지정에 사용할 그룹화 기호. *(문자열)*

오류 패턴을 얻는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.PATTERN_ERROR`.

`options` 매개 변수는 선택적 이며 그것의 기본 값은:

    {type:'decimal'}
    

`Options.type` `decimal`, `percent` 또는 `currency` 수 있습니다..

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

브라우저는 `en_US` 로케일으로 설정 되어,이 수행 결과를 유사한 텍스트와 팝업 대화 상자가 표시 되어야 합니다.

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
    

결과:

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 단점

*   `pattern` 속성은 지원 되지 않으며 빈 문자열을 반환 합니다.

*   `fraction` 속성은 지원 되지 않으며 0을 반환 합니다.

### 윈도우 특수

*   `pattern` 속성은 지원 되지 않으며 빈 문자열을 반환 합니다.

## navigator.globalization.isDayLightSavingsTime

일광 절약 시간이 클라이언트의 표준 시간대 및 달력을 사용 하 여 특정된 날짜에 대 한 효과 인지 표시 합니다.

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### 설명

매개 변수로 `속성` 개체와 `successCallback`에 일광 절약 시간이 적용 됩니다 여부를 나타냅니다. 해당 개체는 `dst` 속성을 `Boolean` 값으로 있어야 합니다. 값이 `true 이면` 지정 된 날짜에 대 한 적용 되는 일광 절약 시간 `false` 하지 않음을 나타냅니다 나타냅니다.

인바운드 매개 변수 `date` 형식 `Date`의 이어야 한다.

날짜 읽기 오류가 있는 경우에, `errorCallback` 실행 합니다. 오류의 예상된 코드는 `GlobalizationError.UNKNOWN_ERROR`.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

여름 동안에, 브라우저 DST 설정 표준 시간대로 설정 되어 있으면이 텍스트 비슷한 팝업 대화 상자를 표시 해야 하는 고 `dst: 진정한`:

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

클라이언트의 사용자 환경 설정에 따라 문자열 형식으로 숫자를 반환 합니다.

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### 설명

서식이 지정 된 숫자 문자열을 매개 변수로 `properties` 개체와 `successCallback`에 돌아갑니다. 해당 개체 `값` 속성을 `문자열` 값으로 있어야 합니다.

숫자 서식을 오류가 있는 경우에, 다음 `errorCallback` 실행 `GlobalizationError` 개체와 매개 변수로. 오류의 예상된 코드는 `GlobalizationError.FORMATTING_ERROR`.

`options` 매개 변수는 선택적 이며 그것의 기본 값은:

    {type:'decimal'}
    

`options.type`는 'decimal', 'percent' 또는 'currency' 될 수 있습니다.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

이 텍스트와 유사한 팝업 대화 상자를 표시 하는 브라우저는 `en_US` 로케일으로 설정 되어, `번호: 3.142`:

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### 윈도우 특수

*   Windows 8.0 숫자 반올림을 지원 하지 않습니다, 그리고 따라서 값 하지 반올림 됩니다 자동으로.

*   윈도 즈 8.1와 Windows Phone 8.1 소수 부분이 되 고 잘린다 대신 `percent` 숫자 유형에 따라서 소수 자릿수의 경우 반올림에 0으로 설정 됩니다.

*   그룹화 하는 경우 stringToNumber에서 구문 분석할 수 없는 `percent` 숫자 그룹화 하지는.

## navigator.globalization.stringToDate

클라이언트의 사용자 환경 설정 및 달력 클라이언트의 표준 시간대를 사용 하 여 문자열 형식으로 날짜를 구문 분석 하 고 해당 하는 date 개체를 반환 합니다.

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### 설명

매개 변수로 `properties` 개체와 성공 콜백 하는 날짜를 반환합니다. 해당 개체는 다음 속성이 있어야 합니다.

*   **year**: 4 자리 연도. *(수)*

*   **month**: 달 (0-11). *(수)*

*   **day**: (1-31)에서 하루. *(수)*

*   **hour**: 1 시간 (0-23). *(수)*

*   **minute**: 분 (0-59)에서. *(수)*

*   **Second**: (0-59)에서 두 번째. *(수)*

*   **milisecond**: 모든 플랫폼에서 사용할 수 없습니다 (0-999)에서 밀리초. *(수)*

인바운드 `dateString` 매개 변수 형식이 `String` 이어야 합니다..

`options` 매개 변수는 선택적 이며 기본값은 다음 값:

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` `short`, `medium`, `long` 또는 `full` 수 있습니다. `options.selector` `date`, `time` 또는 `date and time` 수 있습니다..

날짜 문자열을 구문 분석 오류가 있는 경우에, 다음 `errorCallback` 실행 된 `GlobalizationError` 개체를 매개 변수로 합니다. 오류의 예상된 코드는 `GlobalizationError.PARSING_ERROR`.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

브라우저 `en_US` 로케일으로 설정 하면 텍스트가 `달: 8 날: 25 년: 2012`와 유사한 팝업 대화 상자가 표시 됩니다. 유의 정수는 한 달 미만의 문자열, 달 정수로 나타내는 배열 인덱스.

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 단점

*   `formatLength` 옵션 `short` 하 고 `full` 값만 지원합니다.

*   'date and time' 선택기에 대 한 패턴은 항상 전체 날짜/시간 형식입니다.

*   인바운드 `dateString` 매개 변수 getDatePattern에 의해 반환 된 패턴에 따라 형성 되어야 한다. 이 패턴 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

### 윈도우 특수

*   `formatLength` 옵션 `short` 하 고 `full` 값만 지원합니다.

*   'date and time' 선택기에 대 한 패턴은 항상 전체 날짜/시간 형식입니다.

*   인바운드 `dateString` 매개 변수 getDatePattern에 의해 반환 된 패턴에 따라 형성 되어야 한다. 이 패턴 사용자 로캘에 따라 ICU와 완전히 정렬 수 있습니다.

## navigator.globalization.stringToNumber

클라이언트의 사용자 환경 설정에 따라 문자열 형식으로 번호를 구문 분석 하 고 해당 번호를 반환 합니다.

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### 설명

매개 변수로 `속성` 개체와 `successCallback`을 수를 반환합니다. 해당 개체 `Number` 값으로 `value` 속성이 있어야 합니다.

숫자 문자열을 구문 분석 오류가 있는 경우에, 다음 `errorCallback` 실행 된 `GlobalizationError` 개체를 매개 변수로 합니다. 오류의 예상된 코드는 `GlobalizationError.PARSING_ERROR`.

`options` 매개 변수는 선택적 이며 기본값은 다음 값:

    {type:'decimal'}
    

`Options.type` `decimal`, `percent` 또는 `currency` 수 있습니다..

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

브라우저 `en_US` 로케일으로 설정 되어,이 텍스트와 유사한 팝업 대화 상자가 표시 되어야 합니다 `번호: 1234.56`:

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 단점

*   `percent` 타입의 경우 반환 되는 값 없는 100로 나눕니다.

### 윈도우 특수

*   문자열 로캘 형식 엄격 하 게 준수 해야 합니다. 예를 들어, 백분율 기호 형식 매개 변수 '%' 일 경우 ' en-US ' 로케일에 대 한 공간에 의해 분리 되어야 한다.

*   `percent` 번호 올바르게 구문 분석 하지 그룹화 해야 합니다.

## GlobalizationError

세계화 API에서 오류를 나타내는 개체입니다.

### 속성

*   **code**: 오류 형식을 나타내는 다음 코드 중 하나 *(수)* 
    *   GlobalizationError.UNKNOWN_ERROR: 0
    *   GlobalizationError.FORMATTING_ERROR: 1
    *   GlobalizationError.PARSING_ERROR: 2
    *   GlobalizationError.PATTERN_ERROR: 3
*   **message**: 오류 설명을 포함 및/또는 *(문자열)를* 자세히 설명 하는 텍스트 메시지

### 설명

이 개체와 코르도바, 의해 만들어지고 오류 경우 콜백 반환.

### 지원 되는 플랫폼

*   아마존 화재 운영 체제
*   안 드 로이드
*   블랙베리 10
*   Firefox 운영 체제
*   iOS
*   Windows Phone 8
*   윈도우

### 예를 들어

유사한 텍스트와 팝업 대화 상자가 표시 됩니다 다음 오류 콜백 실행 되 면 `코드: 3` 및 `메시지:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };
