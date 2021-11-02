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

Questo plugin consente di accedere alla bussola del dispositivo. La bussola è un sensore che rileva la direzione o la voce che il dispositivo è puntato, in genere dalla parte superiore del dispositivo. Esso misura la rotta in gradi da 0 a 359.99, dove 0 è a nord.

L'accesso avviene tramite un oggetto globale `navigator.compass`.

Anche se l'oggetto è associato con ambito globale del `navigator`, non è disponibile fino a dopo l'evento `deviceready`.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.compass);
    }
    

## Installazione

    cordova plugin add cordova-plugin-device-orientation
    

## Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Browser
*   Firefox OS
*   iOS
*   Tizen
*   Windows Phone 7 e 8 (se disponibili nell'hardware)
*   Windows 8

## Metodi

*   navigator.compass.getCurrentHeading
*   navigator.compass.watchHeading
*   navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

Ottenere la corrente della bussola. La bussola viene restituita tramite un oggetto `CompassHeading` utilizzando la funzione di callback `compassSuccess`.

    navigator.compass.getCurrentHeading(compassSuccess, compassError);
    

### Esempio

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

Ottiene il titolo attuale del dispositivo a intervalli regolari. Ogni volta che viene recuperato il titolo, viene eseguita la funzione di callback `headingSuccess`.

L'orologio restituito ID fa riferimento l'intervallo orologio bussola. L'ID di orologio utilizzabile con `navigator.compass.clearWatch` a smettere di guardare la navigator.compass.

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions` può contenere i seguenti tasti:

*   **frequency**: la frequenza di recuperare la bussola in millisecondi. *(Numero)* (Default: 100)
*   **filter**: il cambiamento in gradi necessari per avviare un callback di successo watchHeading. Quando questo valore è impostato, la **frequency** viene ignorata. *(Numero)*

### Esempio

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
    

### Stranezze browser

I valori per la rubrica attuale sono generati casualmente al fine di simulare la bussola.

### iOS stranezze

Solo un `watchHeading` può essere in effetti una volta in iOS. Se un `watchHeading` utilizza un filtro, chiamata `getCurrentHeading` o `watchHeading` utilizza il valore di filtro esistenti per specificare le modifiche intestazione. Guardando i cambiamenti di direzione con un filtro è più efficiente con intervalli di tempo.

### Amazon fuoco OS stranezze

*   `filter`non è supportato.

### Stranezze Android

*   Nessun supporto per`filter`.

### Firefox OS stranezze

*   Nessun supporto per`filter`.

### Tizen stranezze

*   Nessun supporto per`filter`.

### Windows Phone 7 e 8 stranezze

*   Nessun supporto per`filter`.

## navigator.compass.clearWatch

Smettere di guardare la bussola a cui fa riferimento il parametro ID orologio.

    navigator.compass.clearWatch(watchID);
    

*   **watchID**: l'ID restituito da`navigator.compass.watchHeading`.

### Esempio

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

Alla funzione di callback `compassSuccess` viene restituito un oggetto `CompassHeading`.

### Proprietà

*   **magneticHeading**: la rotta in gradi da 0-359.99 in un unico momento. *(Numero)*

*   **trueHeading**: la voce rispetto al Polo Nord geografico in gradi 0-359.99 in un unico momento. Un valore negativo indica che non è possibile determinare la vera voce. *(Numero)*

*   **headingAccuracy**: lo scostamento in gradi tra il titolo segnalato e la vera voce. *(Numero)*

*   **timestamp**: il tempo in cui questa voce è stata determinata. *(millisecondi)*

### Amazon fuoco OS stranezze

*   `trueHeading`non è supportato, ma riporta lo stesso valore`magneticHeading`

*   `headingAccuracy`è sempre 0 perché non non c'è alcuna differenza tra la `magneticHeading` e`trueHeading`

### Stranezze Android

*   La `trueHeading` proprietà non è supportata, ma riporta lo stesso valore`magneticHeading`.

*   La `headingAccuracy` proprietà è sempre 0 perché non non c'è alcuna differenza tra la `magneticHeading` e`trueHeading`.

### Firefox OS stranezze

*   La `trueHeading` proprietà non è supportata, ma riporta lo stesso valore`magneticHeading`.

*   La `headingAccuracy` proprietà è sempre 0 perché non non c'è alcuna differenza tra la `magneticHeading` e`trueHeading`.

### iOS stranezze

*   La `trueHeading` proprietà viene restituito solo per servizi di localizzazione attivate tramite`navigator.geolocation.watchLocation()`.

## CompassError

Un oggetto `CompassError` viene restituito alla funzione di callback `compassError` quando si verifica un errore.

### Proprietà

*   **codice**: uno dei codici di errore predefiniti elencati di seguito.

### Costanti

*   `CompassError.COMPASS_INTERNAL_ERR`
*   `CompassError.COMPASS_NOT_SUPPORTED`
