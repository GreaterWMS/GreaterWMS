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

# cordova-plugin-device-motion

Этот плагин обеспечивает доступ к акселерометру устройства. Акселерометр является датчиком движения, который обнаруживает изменение (*дельта*) в движении относительно текущей ориентации устройства, в трех измерениях вдоль осей *x*, *y* и *z* .

## Установка

    cordova plugin add cordova-plugin-device-motion
    

## Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   Обозреватель
*   Firefox OS
*   iOS
*   Tizen
*   Windows Phone 7 и 8
*   Windows 8

## Методы

*   navigator.accelerometer.getCurrentAcceleration
*   navigator.accelerometer.watchAcceleration
*   navigator.accelerometer.clearWatch

## Объекты

*   Acceleration

## navigator.accelerometer.getCurrentAcceleration

Возвращает текущее ускорение вдоль осей *x*, *y* и *z*.

Значения ускорения передаются функции обратного вызова `accelerometerSuccess`.

    navigator.accelerometer.getCurrentAcceleration(accelerometerSuccess, accelerometerError);
    

### Пример

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
    

### Браузер причуды

Значения X, Y, Z движения являются все случайным в целях моделирования акселерометра.

### Особенности iOS

*   iOS не поддерживает автоматическое обновление значений для ускорения.

*   Вы должны самостоятельно отслеживать изменение ускорения и считывать данные через определенные интервалы времени.

*   Таким образом функция `getCurrentAcceleration` возвращает последнее значение, полученное при вызове `watchAccelerometer`.

## navigator.accelerometer.watchAcceleration

Извлекает текущая устройство `Acceleration` с постоянным интервалом, выполнение `accelerometerSuccess` функция обратного вызова каждый раз. Задайте интервал в миллисекундах, через `acceleratorOptions` объекта `frequency` параметр.

Возвращаемый смотреть ссылки ID акселерометр часы интервал и может быть использован с `navigator.accelerometer.clearWatch` чтобы остановить просмотр акселерометр.

    var watchID = navigator.accelerometer.watchAcceleration(accelerometerSuccess,
                                                           accelerometerError,
                                                           accelerometerOptions);
    

*   **accelerometerOptions**: Объект с следующие необязательные свойствами: 
    *   **период**: запрошенный период звонков на accelerometerSuccess с ускорение данных в миллисекундах. *(Число)* (По умолчанию: 10000)

### Пример

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
    

### Особенности iOS

API вызывает функцию обратного вызова с указанным интервалом, но имеет ограничение по частоте запросов к устройству от 40 мс и до 1000 мс. Например если вы запрашиваете интервал 3 секунды, (3000 мс), API запрашивает данные от устройства каждую секунду, но функция обратного вызова будет срабатывать только каждые 3 секунды.

## navigator.accelerometer.clearWatch

Останавливает отслеживание изменений объекта `Acceleration`, на который ссылается параметр `watchID`.

    navigator.accelerometer.clearWatch(watchID);
    

*   **watchID**: идентификатор, возвращенный`navigator.accelerometer.watchAcceleration`.

### Пример

    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.accelerometer.clearWatch(watchID);
    

## Acceleration

Содержит данные полученные от акселерометра на определенный момент времени. Ускорение значения включают эффект гравитации (9,81 м/с ^ 2), так что когда устройство лежит плоская и вверх, *x*, *y*, и *z* значения, возвращаемые должны быть `` , `` , и`9.81`.

### Параметры

*   **x**: величина ускорение по оси x. (в м/с ^ 2) *(Число)*
*   **y**: величина ускорение по оси y. (в м/с ^ 2) *(Число)*
*   **z**: величина ускорение по оси z. (в м/с ^ 2) *(Число)*
*   **timestamp**: временая метка в миллисекундах. *(DOMTimeStamp)*
