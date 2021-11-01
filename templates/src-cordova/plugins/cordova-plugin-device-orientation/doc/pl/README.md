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

Ten plugin umożliwia dostęp do urządzenia kompas. Kompas jest czujnik, który wykrywa kierunek lub pozycji, że urządzenie jest wskazywany, zazwyczaj z górnej części urządzenia. Mierzy on nagłówek w stopniach od 0 do 359.99, gdzie 0 jest północ.

Dostęp odbywa się za pomocą obiektu globalnego `navigator.compass`.

Mimo, że obiekt jest dołączony do globalnego zakresu `navigator`, to nie dostępne dopiero po zdarzeniu `deviceready`.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.compass);
    }
    

## Instalacja

    cordova plugin add cordova-plugin-device-orientation
    

## Obsługiwane platformy

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Przeglądarka
  * Firefox OS
  * iOS
  * Tizen
  * Windows Phone 7 i 8 (jeśli jest dostępny w sprzęcie)
  * Windows 8

## Metody

  * navigator.compass.getCurrentHeading
  * navigator.compass.watchHeading
  * navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

Uzyskać bieżącej pozycji kompas. Kompas pozycji jest zwracana za pośrednictwem obiektu `CompassHeading` za pomocą funkcji wywołania zwrotnego `compassSuccess`.

    navigator.compass.getCurrentHeading(compassSuccess, compassError);
    

### Przykład

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

Pobiera bieżący nagłówek urządzenia w regularnych odstępach czasu. Każdym razem, gdy nagłówek jest źródło, funkcja wywołania zwrotnego `headingSuccess` jest wykonywany.

Identyfikator zwrócony zegarek odwołuje interwał kompas zegarek. Oglądaj identyfikator może być używany z `navigator.compass.clearWatch`, aby przestać oglądać navigator.compass.

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions` może zawierać następujące klucze:

  * **częstotliwość**: jak często pobrać kompas pozycji w milisekundach. *(Liczba)* (Domyślnie: 100)
  * **Filtr**: zmiana stopni wymagane zainicjować wywołania zwrotnego watchHeading sukces. Gdy ta wartość jest ustawiona, **częstotliwość** jest ignorowana. *(Liczba)*

### Przykład

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
    

### Quirks przeglądarki

Wartości dla bieżącej pozycji są losowo generowane w celu symulacji kompas.

### Dziwactwa iOS

Tylko jeden `watchHeading` może być efekt w tym samym czasie w iOS. Jeśli `watchHeading` używa filtru, `getCurrentHeading` lub `watchHeading` używa istniejących wartości filtru określić zmiany pozycji. Obserwując zmiany pozycji z filtrem jest bardziej efektywne niż z odstępach czasu.

### Amazon ogień OS dziwactwa

  * `filter`nie jest obsługiwane.

### Dziwactwa Androida

  * Brak wsparcia dla`filter`.

### Firefox OS dziwactwa

  * Brak wsparcia dla`filter`.

### Dziwactwa Tizen

  * Brak wsparcia dla`filter`.

### Windows Phone 7 i 8 dziwactwa

  * Brak wsparcia dla`filter`.

## navigator.compass.clearWatch

Przestać oglądać określany przez parametr ID Zegarek kompas.

    navigator.compass.clearWatch(watchID);
    

  * **watchID**: Identyfikator zwrócony przez`navigator.compass.watchHeading`.

### Przykład

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

Obiekt `CompassHeading` jest zwracany do funkcji wywołania zwrotnego `compassSuccess`.

### Właściwości

  * **magneticHeading**: pozycja w stopniach od 0-359.99 w jednym momencie. *(Liczba)*

  * **trueHeading**: nagłówek do geograficznego Bieguna Północnego w stopniu 0-359.99 w jednym momencie. Wartość ujemna wskazuje, że prawda pozycji nie może być ustalona. *(Liczba)*

  * **headingAccuracy**: odchylenie w stopniach między zgłoszonych pozycji i pozycji prawda. *(Liczba)*

  * **sygnatura czasowa**: czas, w którym pozycja ta została ustalona. *(w milisekundach)*

### Amazon ogień OS dziwactwa

  * `trueHeading`nie jest obsługiwane, ale raporty taką samą wartość jak`magneticHeading`

  * `headingAccuracy`jest zawsze 0, ponieważ nie ma żadnej różnicy między `magneticHeading` i`trueHeading`

### Dziwactwa Androida

  * `trueHeading`Właściwość nie jest obsługiwany, ale raporty taką samą wartość jak`magneticHeading`.

  * `headingAccuracy`Właściwość jest zawsze 0, ponieważ nie ma żadnej różnicy między `magneticHeading` i`trueHeading`.

### Firefox OS dziwactwa

  * `trueHeading`Właściwość nie jest obsługiwany, ale raporty taką samą wartość jak`magneticHeading`.

  * `headingAccuracy`Właściwość jest zawsze 0, ponieważ nie ma żadnej różnicy między `magneticHeading` i`trueHeading`.

### Dziwactwa iOS

  * `trueHeading`Właściwość jest zwracana tylko dla lokalizacji usług włączone za pomocą`navigator.geolocation.watchLocation()`.

## CompassError

Gdy wystąpi błąd, funkcja wywołania zwrotnego `compassError` zwracany jest obiekt `CompassError`.

### Właściwości

  * **Kod**: jeden z kodów błędów wstępnie zdefiniowanych poniżej.

### Stałe

  * `CompassError.COMPASS_INTERNAL_ERR`
  * `CompassError.COMPASS_NOT_SUPPORTED`