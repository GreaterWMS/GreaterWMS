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

Este plugin proporciona acceso al compás del dispositivo. La brújula es un sensor que detecta la dirección o rumbo que el dispositivo está apuntado, normalmente desde la parte superior del dispositivo. Mide el rumbo en grados de 0 a 359.99, donde 0 es el norte.

El acceso es por un global `navigator.compass` objeto.

Aunque el objeto está unido al ámbito global `navigator` , no estará disponible hasta después de la `deviceready` evento.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.compass);
    }
    

## Instalación

    cordova plugin add cordova-plugin-device-orientation
    

## Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Explorador
  * Firefox OS
  * iOS
  * Tizen
  * Windows Phone 7 y 8 (si está disponible en el hardware)
  * Windows 8

## Métodos

  * navigator.compass.getCurrentHeading
  * navigator.compass.watchHeading
  * navigator.compass.clearWatch

## navigator.compass.getCurrentHeading

Conseguir el actual rumbo de la brújula. El rumbo de la brújula es devuelto vía un `CompassHeading` objeto usando la `compassSuccess` función de callback.

    navigator.compass.getCurrentHeading(compassSuccess, compassError);
    

### Ejemplo

    function onSuccess(heading) {
        alert('Heading: ' + heading.magneticHeading);
    };
    
    function onError(error) {
        alert('CompassError: ' + error.code);
    };
    
    navigator.compass.getCurrentHeading(onSuccess, onError);
    

## navigator.compass.watchHeading

Obtiene el título actual del dispositivo a intervalos regulares. Cada vez que se recupera el título, el `headingSuccess` se ejecuta la función callback.

El identificador devuelto reloj referencias el intervalo reloj brújula. El reloj ID puede utilizarse con `navigator.compass.clearWatch` para dejar de ver la navigator.compass.

    var watchID = navigator.compass.watchHeading(compassSuccess, compassError, [compassOptions]);
    

`compassOptions`puede contener las siguientes claves:

  * **frecuencia**: frecuencia con la que recuperar el rumbo de la brújula en milisegundos. *(Número)* (Por defecto: 100)
  * **filtro**: el cambio de grados necesarios para iniciar una devolución de llamada de éxito watchHeading. Cuando se establece este valor, **frecuencia** es ignorado. *(Número)*

### Ejemplo

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
    

### Navegador rarezas

Los valores de partida actual son generados al azar para simular la brújula.

### iOS rarezas

Solamente un `watchHeading` puede ser en efecto a la vez en iOS. Si un `watchHeading` utiliza un filtro, llamando a `getCurrentHeading` o `watchHeading` utiliza el valor existente del filtro para especificar los cambios de rumbo. Observando los cambios de rumbo con un filtro es más eficiente que con intervalos de tiempo.

### Amazon fuego OS rarezas

  * `filter`No se admite.

### Rarezas Android

  * No hay soporte para`filter`.

### Firefox OS rarezas

  * No hay soporte para`filter`.

### Rarezas Tizen

  * No hay soporte para`filter`.

### Windows Phone 7 y 8 rarezas

  * No hay soporte para`filter`.

## navigator.compass.clearWatch

Deja de mirar la brújula al que hace referencia el parámetro ID de reloj.

    navigator.compass.clearWatch(watchID);
    

  * **watchID**: el identificador devuelto por`navigator.compass.watchHeading`.

### Ejemplo

    var watchID = navigator.compass.watchHeading(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.compass.clearWatch(watchID);
    

## CompassHeading

A `CompassHeading` objeto es devuelto a la `compassSuccess` función de callback.

### Propiedades

  * **magneticHeading**: el rumbo en grados de 0-359.99 en un solo momento. *(Número)*

  * **trueHeading**: el título en relación con el polo norte geográfico en grados 0-359.99 en un solo momento. Un valor negativo indica que no se puede determinar el rumbo verdadero. *(Número)*

  * **headingAccuracy**: la desviación en grados entre el rumbo divulgado y el rumbo verdadero. *(Número)*

  * **timestamp**: el momento en el cual se determinó esta partida. *(milisegundos)*

### Amazon fuego OS rarezas

  * `trueHeading`No es compatible, pero el mismo valor que los informes`magneticHeading`

  * `headingAccuracy`es siempre 0 porque no hay ninguna diferencia entre el `magneticHeading` y`trueHeading`

### Rarezas Android

  * El `trueHeading` propiedad no es compatible, pero el mismo valor que los informes`magneticHeading`.

  * El `headingAccuracy` propiedad es siempre 0 porque no hay ninguna diferencia entre el `magneticHeading` y`trueHeading`.

### Firefox OS rarezas

  * El `trueHeading` propiedad no es compatible, pero el mismo valor que los informes`magneticHeading`.

  * El `headingAccuracy` propiedad es siempre 0 porque no hay ninguna diferencia entre el `magneticHeading` y`trueHeading`.

### iOS rarezas

  * El `trueHeading` propiedad es devuelto sólo para servicios de localización habilitados mediante`navigator.geolocation.watchLocation()`.

## CompassError

A `CompassError` objeto es devuelto a la `compassError` función de devolución de llamada cuando se produce un error.

### Propiedades

  * **code**: uno de los códigos de error predefinido enumerados a continuación.

### Constantes

  * `CompassError.COMPASS_INTERNAL_ERR`
  * `CompassError.COMPASS_NOT_SUPPORTED`