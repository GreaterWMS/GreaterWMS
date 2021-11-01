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

Этот плагин обеспечивает доступ к устройства компас. Компас-это датчик, который определяет направление или заголовок, что устройство указывает, как правило в верхней части устройства. Он измеряет направление в градусах от 0 до 359,99 градусов, где 0 — север.

## Установка

    cordova plugin add cordova-plugin-device-orientation
    

## Поддерживаемые платформы

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Обозреватель
*   Firefox OS
*   iOS
*   Tizen
*   Windows Phone 7 и 8 (при наличии оборудования)
*   Windows 8

## Методы

*   navigator.compass.getCurrentHeading
*   navigator.compass.watchHeading
*   navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

Получите текущий курс. Курс возвращается через `CompassHeading` объекта с помощью `compassSuccess` функции обратного вызова.

    navigator.compass.getCurrentHeading (compassSuccess, compassError);
    

### Пример

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

Получает текущий заголовок устройства в регулярном интервале. Каждый раз, когда извлекаются заголовок, `headingSuccess` выполняется функция обратного вызова.

Идентификатор возвращаемой смотреть ссылки компас часы интервал. Часы, ID может быть использован с `navigator.compass.clearWatch` чтобы остановить просмотр navigator.compass.

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions`может содержать следующие разделы:

*   **Частота**: как часто получить курс в миллисекундах. *(Число)* (По умолчанию: 100)
*   **Фильтр**: изменения в градусах, требуемых для инициирования обратного вызова watchHeading успех. Если это значение задано, **Частота** учитывается. *(Число)*

### Пример

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
    

### Браузер причуды

Для того, чтобы имитировать компас генерируются случайным образом значения для текущего заголовка.

### Особенности iOS

Только один `watchHeading` может быть в одно время эффекта в iOS. Если `watchHeading` использует фильтр, вызов `getCurrentHeading` или `watchHeading` для указания изменения заголовка используется существующее значение фильтра. Наблюдая изменения заголовка с помощью фильтра является более эффективным, чем с интервалов времени.

### Особенности Amazon Fire OS

*   `filter`не поддерживается.

### Особенности Android

*   Поддержка отсутствует`filter`.

### Особенности Firefox OS

*   Поддержка отсутствует`filter`.

### Особенности Tizen

*   Поддержка отсутствует`filter`.

### Особенности Windows Phone 7 и 8

*   Поддержка отсутствует`filter`.

## navigator.compass.clearWatch

Перестать смотреть компас, на который ссылается параметр ID смотреть.

    navigator.compass.clearWatch(watchID);
    

*   **watchID**: идентификатор, возвращенный`navigator.compass.watchHeading`.

### Пример

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

A `CompassHeading` объект возвращается к `compassSuccess` функции обратного вызова.

### Параметры

*   **magneticHeading**: направление в градусах от 0-359,99 в один момент времени. *(Число)*

*   **trueHeading**: заголовок относительно географического Северного полюса в градусах 0-359,99 в один момент времени. Отрицательное значение указывает, что заголовок правда не может быть определено. *(Число)*

*   **headingAccuracy**: отклонение в градусах между сообщил заголовок и заголовок верно. *(Число)*

*   **отметка времени**: время, на котором был определен этот заголовок. *(в миллисекундах)*

### Особенности Amazon Fire OS

*   `trueHeading`не поддерживается, но сообщает то же значение`magneticHeading`

*   `headingAccuracy`Это всегда 0 потому, что нет никакой разницы между `magneticHeading` и`trueHeading`

### Особенности Android

*   `trueHeading`Свойство не поддерживается, но сообщает то же значение`magneticHeading`.

*   `headingAccuracy`Свойство всегда имеет 0 потому, что нет никакой разницы между `magneticHeading` и`trueHeading`.

### Особенности Firefox OS

*   `trueHeading`Свойство не поддерживается, но сообщает то же значение`magneticHeading`.

*   `headingAccuracy`Свойство всегда имеет 0 потому, что нет никакой разницы между `magneticHeading` и`trueHeading`.

### Особенности iOS

*   `trueHeading`Свойства возвращается только для служб определения местоположения включена через`navigator.geolocation.watchLocation()`.

## CompassError

A `CompassError` объект возвращается к `compassError` функцию обратного вызова при возникновении ошибки.

### Параметры

*   **code**: один из стандартных кодов ошибок, перечисленных ниже.

### Константы

*   `CompassError.COMPASS_INTERNAL_ERR`
*   `CompassError.COMPASS_NOT_SUPPORTED`
