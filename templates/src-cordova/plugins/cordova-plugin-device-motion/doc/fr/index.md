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

Ce plugin permet d'accéder à l'accéléromètre de l'appareil. L'accéléromètre est un capteur de mouvement qui détecte la modification (*delta*) en mouvement par rapport à l'orientation actuelle de l'appareil, en trois dimensions le long de l'axe *x*, *y*et *z* .

Accès se fait par un global `navigator.accelerometer` objet.

Bien que l'objet est attaché à la portée globale `navigator` , il n'est pas disponible jusqu'après la `deviceready` événement.

    document.addEventListener (« deviceready », onDeviceReady, false) ;
    function onDeviceReady() {console.log(navigator.accelerometer);}
    

## Installation

    Cordova plugin ajouter cordova-plugin-device-motion
    

## Plates-formes prises en charge

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Navigateur
*   Firefox OS
*   iOS
*   Paciarelli
*   Windows Phone 8
*   Windows

## Méthodes

*   navigator.accelerometer.getCurrentAcceleration
*   navigator.accelerometer.watchAcceleration
*   navigator.accelerometer.clearWatch

## Objets

*   Acceleration

## navigator.accelerometer.getCurrentAcceleration

Obtenir l'accélération courante le long des axes *x*, *y*et *z* .

Ces valeurs d'accélération sont retournés à la `accelerometerSuccess` fonction de rappel.

    navigator.accelerometer.getCurrentAcceleration (accelerometerSuccess, accelerometerError) ;
    

### Exemple

    function onSuccess(acceleration) {alert ("Accélération X:" + acceleration.x + « \n » + "Accélération Y:" + acceleration.y + « \n » + « Accélération Z: » + acceleration.z + « \n » + ' Timestamp: "+ acceleration.timestamp + « \n »);} ;
    
    fonction onError() {alert('onError!');} ;
    
    navigator.accelerometer.getCurrentAcceleration (onSuccess, onError) ;
    

### Bizarreries navigateur

Les valeurs x, Y, motion de Z sont tous ordre généré de manière aléatoire dans pour simuler l'accéléromètre.

### iOS Quirks

*   iOS ne permet pas d'obtenir l'accélération en cours à un instant donné.

*   Vous devez observer l'accélération et capturer ses données à un intervalle de temps donné.

*   De ce fait, la fonction `getCurrentAcceleration` renvoie la dernière valeur retournée par un appel à `watchAccelerometer`.

## navigator.accelerometer.watchAcceleration

Récupère le dispositif actuel de `Acceleration` à intervalle régulier, l'exécution de la `accelerometerSuccess` fonction de rappel chaque fois. Spécifiez l'intervalle, en millisecondes, via le `acceleratorOptions` de l'objet `frequency` paramètre.

Le retourné regarder ID références intervalle de surveillance de l'accéléromètre et peut être utilisé avec `navigator.accelerometer.clearWatch` d'arrêter de regarder l'accéléromètre.

    var watchID = navigator.accelerometer.watchAcceleration (accelerometerSuccess, accelerometerError, accelerometerOptions) ;
    

*   **accelerometerOptions**: Un objet avec les clés facultatives suivantes : 
    *   **période**: période demandée d'appels à accelerometerSuccess avec les données d'accélération en millisecondes. *(Nombre)* (Par défaut : 10000)

### Exemple

    function onSuccess(acceleration) {alert ("Accélération X:" + acceleration.x + « \n » + "Accélération Y:" + acceleration.y + « \n » + « Accélération Z: » + acceleration.z + « \n » + ' Timestamp: "+ acceleration.timestamp + « \n »);} ;
    
    fonction onError() {alert('onError!');} ;
    
    options de var = { frequency: 3000 } ;  Mise à jour chaque 3 secondes var watchID = navigator.accelerometer.watchAcceleration (onSuccess, onError, options) ;
    

### iOS Quirks

L'API appelle la fonction de rappel de succès à l'intervalle demandé, mais restreint l'éventail des demandes à l'appareil entre 40ms et 1000ms. Par exemple, si vous demandez un intervalle de 3 secondes, (3000ms), l'API demande des données de l'appareil toutes les 1 seconde, mais seulement exécute le rappel réussi toutes les 3 secondes.

## navigator.accelerometer.clearWatch

Arrêter de regarder le `Acceleration` référencé par le `watchID` paramètre.

    navigator.accelerometer.clearWatch(watchID) ;
    

*   **watchID**: l'ID retourné par`navigator.accelerometer.watchAcceleration`.

### Exemple

    var watchID = navigator.accelerometer.watchAcceleration (onSuccess, onError, options) ;
    
    ... plus tard... navigator.accelerometer.clearWatch(watchID) ;
    

## Accélération

Contient `Accelerometer` données capturées à un point précis dans le temps. Valeurs d'accélération comprennent l'effet de la pesanteur (9,81 m/s ^ 2), de sorte que lorsqu'un périphérique se trouve plat et face vers le haut, *x*, *y*, et *z* valeurs retournées doivent être `` , `` , et`9.81`.

### Propriétés

*   **x**: Valeur de l'accélération sur l'axe des x. (en m/s^2) *(Number)*
*   **y**: Valeur de l'accélération sur l'axe des y. (en m/s^2) *(Number)*
*   **y**: Valeur de l'accélération sur l'axe des z. (en m/s^2) *(Number)*
*   **timestamp**: Date de création en millisecondes. *(DOMTimeStamp)*
