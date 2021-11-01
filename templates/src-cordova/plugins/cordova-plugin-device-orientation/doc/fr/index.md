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

Ce plugin permet d'accéder à la boussole de l'appareil. La boussole est un capteur qui détecte la direction ou la position que l'appareil est pointé, généralement par le haut de l'appareil. Il mesure la position en degrés de 0 à 359.99, où 0 est vers le Nord.

Accès se fait par un global `navigator.compass` objet.

Bien que l'objet est attaché à la portée globale `navigator` , il n'est pas disponible jusqu'après la `deviceready` événement.

    document.addEventListener (« deviceready », onDeviceReady, false) ;
    function onDeviceReady() {console.log(navigator.compass);}
    

## Installation

    Cordova plugin ajouter cordova-plugin-device-orientation
    

## Plates-formes prises en charge

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Navigateur
*   Firefox OS
*   iOS
*   Paciarelli
*   Windows Phone 7 et 8 (s'il est disponible dans le matériel)
*   Windows 8

## Méthodes

*   navigator.compass.getCurrentHeading
*   navigator.compass.watchHeading
*   navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

Téléchargez la cours de la boussole. La boussole est renvoyé via un `CompassHeading` s'opposer à l'aide de la `compassSuccess` fonction de rappel.

    navigator.compass.getCurrentHeading (compassSuccess, compassError) ;
    

### Exemple

    function onSuccess(heading) {alert (' intitulé: "+ heading.magneticHeading);} ;
    
    function onError(error) {alert ('CompassError: ' + error.code);} ;
    
    navigator.compass.getCurrentHeading (onSuccess, onError) ;
    

## navigator.compass.watchHeading

Obtient la position actuelle de l'appareil à intervalle régulier. Chaque fois que le titre est récupéré, la `headingSuccess` fonction de rappel est exécutée.

Le code retourné montre fait référence à l'intervalle montre boussole. La montre ID peut être utilisé avec `navigator.compass.clearWatch` d'arrêter de regarder le navigator.compass.

    var watchID = navigator.compass.watchHeading (compassSuccess, compassError, [compassOptions]) ;
    

`compassOptions`peut contenir les clés suivantes :

*   **fréquence** : la fréquence de récupération de la boussole en millisecondes. *(Nombre)* (Par défaut : 100)
*   **filtre**: le changement en degrés nécessaires pour lancer un rappel de succès watchHeading. Lorsque cette valeur est définie, la **fréquence** est ignoré. *(Nombre)*

### Exemple

    function onSuccess(heading) {var element = document.getElementById('heading') ;
        element.innerHTML = "intitulé:" + heading.magneticHeading ;
    };
    
    function onError(compassError) {alert (' erreur de boussole: "+ compassError.code);} ;
    
    options de var = {
        frequency: 3000
    } ; Mise à jour chaque 3 secondes var watchID = navigator.compass.watchHeading (onSuccess, onError, options) ;
    

### Bizarreries navigateur

Valeurs pour la rubrique actuelle sont générés au hasard afin de simuler la boussole.

### iOS Quirks

Seul `watchHeading` peut être en effet à un moment donné dans l'iOS. Si un `watchHeading` utilise un filtre, appeler `getCurrentHeading` ou `watchHeading` utilise la valeur existante de filtre pour spécifier des changements de position. En regardant les changements de position avec un filtre est plus efficace qu'avec des intervalles de temps.

### Amazon Fire OS Quirks

*   `filter`n'est pas pris en charge.

### Quirks Android

*   Pas de support pour`filter`.

### Firefox OS Quirks

*   Pas de support pour`filter`.

### Bizarreries de paciarelli

*   Pas de support pour`filter`.

### Windows Phone 7 et 8 Quirks

*   Pas de support pour`filter`.

## navigator.compass.clearWatch

Arrêter de regarder la boussole référencée par le paramètre ID de montre.

    navigator.compass.clearWatch(watchID) ;
    

*   **watchID**: l'ID retourné par`navigator.compass.watchHeading`.

### Exemple

    var watchID = navigator.compass.watchHeading (onSuccess, onError, options) ;
    
    ... plus tard... navigator.compass.clearWatch(watchID) ;
    

## CompassHeading

A `CompassHeading` objet est retourné à la `compassSuccess` fonction de rappel.

### Propriétés

*   **magneticHeading**: la position en degrés de 0-359,99 à un instant donné. *(Nombre)*

*   **trueHeading**: la position par rapport au pôle Nord géographique en degrés 0-359,99 à un instant donné. Une valeur négative indique que le cap vrai ne peut être déterminée. *(Nombre)*

*   **headingAccuracy**: la déviation en degrés entre la direction signalée et la véritable direction. *(Nombre)*

*   **horodatage**: l'heure à laquelle cette direction a été déterminée. *(millisecondes)*

### Amazon Fire OS Quirks

*   `trueHeading`n'est pas pris en charge, mais la même valeur que les rapports`magneticHeading`

*   `headingAccuracy`est toujours 0 car il n'y a pas de différence entre la `magneticHeading` et`trueHeading`

### Quirks Android

*   La `trueHeading` propriété n'est pas pris en charge, mais la même valeur que des rapports`magneticHeading`.

*   La `headingAccuracy` propriété est toujours 0 car il n'y a pas de différence entre la `magneticHeading` et`trueHeading`.

### Firefox OS Quirks

*   La `trueHeading` propriété n'est pas pris en charge, mais la même valeur que des rapports`magneticHeading`.

*   La `headingAccuracy` propriété est toujours 0 car il n'y a pas de différence entre la `magneticHeading` et`trueHeading`.

### iOS Quirks

*   La `trueHeading` propriété est retournée uniquement pour les services de localisation activées via`navigator.geolocation.watchLocation()`.

## CompassError

A `CompassError` objet est retourné à la `compassError` fonction de rappel lorsqu'une erreur survient.

### Propriétés

*   **code**: l'un des codes d'erreur prédéfinis énumérés ci-dessous.

### Constantes

*   `CompassError.COMPASS_INTERNAL_ERR`
*   `CompassError.COMPASS_NOT_SUPPORTED`
