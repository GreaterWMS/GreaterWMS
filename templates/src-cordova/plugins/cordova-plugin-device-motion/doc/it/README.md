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

Questo plugin consente di accedere all'accelerometro del dispositivo. L'accelerometro è un sensore di movimento che rileva il cambiamento (*delta*) nel movimento relativo l'orientamento corrente del dispositivo, in tre dimensioni lungo l'asse *x*, *y*e *z* .

L'accesso avviene tramite un oggetto globale `navigator.accelerometer`.

Anche se l'oggetto è associato con ambito globale del `navigator`, non è disponibile fino a dopo l'evento `deviceready`.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.accelerometer);
    }
    

## Installazione

    cordova plugin add cordova-plugin-device-motion
    

## Piattaforme supportate

  * Amazon fuoco OS
  * Android
  * BlackBerry 10
  * Browser
  * Firefox OS
  * iOS
  * Tizen
  * Windows Phone 8
  * Windows

## Metodi

  * navigator.accelerometer.getCurrentAcceleration
  * navigator.accelerometer.watchAcceleration
  * navigator.accelerometer.clearWatch

## Oggetti

  * Accelerazione

## navigator.accelerometer.getCurrentAcceleration

Ottenere l'attuale accelerazione lungo gli assi *x*, *y* e *z*.

I valori di accelerazione vengono restituiti alla funzione di callback `accelerometerSuccess`.

    navigator.accelerometer.getCurrentAcceleration(accelerometerSuccess, accelerometerError);
    

### Esempio

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
    

### Stranezze browser

I valori per X, Y, movimento Z sono tutti generati casualmente in ordine per simulare l'accelerometro.

### iOS stranezze

  * iOS non riconosce il concetto di ottenere l'accelerazione della corrente in un dato punto.

  * Si deve guardare l'accelerazione e acquisire i dati di intervalli di tempo dato.

  * Così, il `getCurrentAcceleration` funzione restituisce l'ultimo valore segnalato da un `watchAccelerometer` chiamare.

## navigator.accelerometer.watchAcceleration

Recupera corrente del dispositivo `Acceleration` a intervalli regolari, l'esecuzione della funzione di callback `accelerometerSuccess` ogni volta. Specificare l'intervallo in millisecondi tramite parametro `frequency` dell'oggetto `acceleratorOptions`.

L'orologio restituito ID fa riferimento intervallo orologio di accelerometro e può essere utilizzato con `navigator.accelerometer.clearWatch` a smettere di guardare l'accelerometro.

    var watchID = navigator.accelerometer.watchAcceleration(accelerometerSuccess,
                                                           accelerometerError,
                                                           accelerometerOptions);
    

  * **accelerometerOptions**: Un oggetto con le seguenti chiavi opzionali: 
      * **periodo**: periodo richiesto di chiamate a accelerometerSuccess con i dati di accelerazione in millisecondi. *(Numero)* (Default: 10000)

### Esempio

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
    

### iOS stranezze

L'API chiama la funzione di callback di successo nell'intervallo richiesto, ma limita la gamma di richieste alla periferica tra 40ms e 1000ms. Ad esempio, se si richiede un intervallo di 3 secondi, (3000ms), l'API richiede i dati dal dispositivo ogni secondo, ma esegue solo il callback di successo ogni 3 secondi.

## navigator.accelerometer.clearWatch

Smettere di guardare l' `Acceleration` a cui fa riferimento il parametro `watchID`.

    navigator.accelerometer.clearWatch(watchID);
    

  * **watchID**: l'ID restituito da`navigator.accelerometer.watchAcceleration`.

### Esempio

    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.accelerometer.clearWatch(watchID);
    

## Accelerazione

Contiene i dati dell'`Accelerometer` catturati in un punto specifico nel tempo. I valori di accelerazione includono l'effetto della gravità (9,81 m/s ^ 2), in modo che quando un dispositivo si trova piatta e rivolto in su, *x*, *y*, e *z* valori restituiti dovrebbero essere ``, `` e `9,81`.

### Proprietà

  * **x**: quantità di accelerazione sull'asse x. (in m/s ^ 2) *(Numero)*
  * **y**: quantità di accelerazione sull'asse y. (in m/s ^ 2) *(Numero)*
  * **z**: quantità di accelerazione sull'asse z. (in m/s ^ 2) *(Numero)*
  * **timestamp**: creazione timestamp in millisecondi. *(DOMTimeStamp)*