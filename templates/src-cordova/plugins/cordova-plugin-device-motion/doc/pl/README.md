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

Ten plugin umożliwia dostęp do akcelerometru. Akcelerometr jest czujnikiem ruchu, który wykrywa zmiany (*delta*) w ruchu względem bieżącej orientacji urządzenia, w trzech wymiarach na osi *x*, *y*i *z* .

Dostęp odbywa się za pomocą obiektu globalnego `navigator.accelerometer`.

Mimo, że obiekt jest dołączony do globalnego zakresu `navigator`, to nie dostępne dopiero po zdarzeniu `deviceready`.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.accelerometer);
    }
    

## Instalacja

    cordova plugin add cordova-plugin-device-motion
    

## Obsługiwane platformy

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Przeglądarka
  * Firefox OS
  * iOS
  * Tizen
  * Windows Phone 8
  * Windows

## Metody

  * navigator.accelerometer.getCurrentAcceleration
  * navigator.accelerometer.watchAcceleration
  * navigator.accelerometer.clearWatch

## Obiekty

  * Acceleration

## navigator.accelerometer.getCurrentAcceleration

Uzyskać aktualne przyspieszenie wzdłuż osi *x*, *y* i *z*.

Te wartości przyspieszenia są zwracane do funkcji wywołania zwrotnego `accelerometerSuccess`.

    navigator.accelerometer.getCurrentAcceleration(accelerometerSuccess, accelerometerError);
    

### Przykład

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
    

### Quirks przeglądarki

Wartości dla osi X, Y, Z ruchu są losowo generowane w celu symulacji akcelerometr.

### Dziwactwa iOS

  * W iOS nie wprowadzono możliwości zmierzenia aktualnego przyspieszenia w dowolnym punkcie.

  * Musisz obserwować przyspieszenie i odbierać wyniki w określonych odstępach czasu.

  * Podsumowując, funkcja `getCurrentAcceleration` zwraca ostatnią wartość zgłoszoną przez wywołanie `watchAccelerometer`.

## navigator.accelerometer.watchAcceleration

Pobiera bieżącego urządzenia `Acceleration` w regularnych odstępach czasu, wykonywanie funkcji wywołania zwrotnego `accelerometerSuccess` każdorazowe. Określ interwał w milisekundach przez parametr obiektu `acceleratorOptions` `frequency`.

Identyfikator zwrócony zegarek odwołuje akcelerometr zegarek interwał i może być używany z `navigator.accelerometer.clearWatch`, aby zatrzymać obejrzeniu akcelerometru.

    var watchID = navigator.accelerometer.watchAcceleration(accelerometerSuccess,
                                                           accelerometerError,
                                                           accelerometerOptions);
    

  * **accelerometerOptions**: Obiekt z następującymi opcjonalnymi kluczami: 
      * **okres**: żądany okres wzywa do accelerometerSuccess z danych przyspieszenia w milisekundach. *(Liczba)* (Domyślnie: 10000)

### Przykład

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
    

### Dziwactwa iOS

Interfejs API wymaga sukcesu funkcji wywołania zwrotnego w interwał żądana, ale ogranicza zakres żądania do urządzenia między 40ms i 1000ms. Na przykład jeśli poprosisz o odstępie 3 sekundy (3000ms), interfejs API żądania danych z urządzenia co 1 sekundę, ale tylko wykonuje wywołanie zwrotne sukces co 3 sekundy.

## navigator.accelerometer.clearWatch

Przestać oglądać `Acceleration` określany przez parametr `watchID`.

    navigator.accelerometer.clearWatch(watchID);
    

  * **watchID**: Identyfikator zwrócony przez `navigator.accelerometer.watchAcceleration`.

### Przykład

    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.accelerometer.clearWatch(watchID);
    

## Acceleration

Zawiera `Accelerometer` dane przechwycone w określonym czasie. Wartości przyśpieszenia to efekt grawitacji (9.81 m/s ^ 2), tak, że kiedy urządzenie znajduje się płaska i górę, *x*, *y*, i *z* wartości zwracane powinno być ``, `` i `9.81`.

### Właściwości

  * **x**: Wartość przyśpieszenia na osi x. (w m/s^2) *(Liczba)*
  * **y**: Wartość przyśpieszenia na osi y. (w m/s^2) *(Liczba)*
  * **z**: Wartość przyśpieszenia na osi z. (w m/s^2) *(Liczba)*
  * **timestamp**: Znacznik czasu w milisekundach. *(DOMTimeStamp)*