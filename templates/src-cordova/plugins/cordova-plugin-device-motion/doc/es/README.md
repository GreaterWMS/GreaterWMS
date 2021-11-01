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

Este plugin proporciona acceso a acelerómetro del dispositivo. El acelerómetro es un sensor de movimiento que detecta el cambio (*delta*) en movimiento con respecto a la orientación actual del dispositivo, en tres dimensiones sobre el eje *x*, *y*y *z* .

El acceso es por un global `navigator.accelerometer` objeto.

Aunque el objeto está unido al ámbito global `navigator` , no estará disponible hasta después de la `deviceready` evento.

    document.addEventListener ("deviceready", onDeviceReady, false);
    function onDeviceReady() {console.log(navigator.accelerometer)};
    

## Instalación

    cordova plugin add cordova-plugin-device-motion
    

## Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Explorador
  * Firefox OS
  * iOS
  * Tizen
  * Windows Phone 8
  * Windows

## Métodos

  * navigator.accelerometer.getCurrentAcceleration
  * navigator.accelerometer.watchAcceleration
  * navigator.accelerometer.clearWatch

## Objetos

  * Acceleration

## navigator.accelerometer.getCurrentAcceleration

Tienes la aceleración actual a lo largo de los ejes *x*, *y*y *z* .

Estos valores de aceleración son devueltos a la `accelerometerSuccess` función de callback.

    navigator.accelerometer.getCurrentAcceleration(accelerometerSuccess, accelerometerError);
    

### Ejemplo

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
    

### Navegador rarezas

Los valores para X, Y, movimiento Z son todo generada aleatoriamente en orden para simular el acelerómetro.

### iOS rarezas

  * iOS no reconoce el concepto de conseguir la aceleración actual en cualquier momento dado.

  * Debes ver la aceleración y capturar los datos en determinados intervalos de tiempo.

  * Así, la función de `getCurrentAcceleration` rinde el último valor informado de una llamada de `watchAccelerometer`.

## navigator.accelerometer.watchAcceleration

Recupera el dispositivo actual de `Acceleration` a intervalos regulares, ejecutar el `accelerometerSuccess` función callback cada vez. Especificar el intervalo en milisegundos mediante la `acceleratorOptions` del objeto `frequency` parámetro.

El vuelto ver referencias ID intervalo del acelerómetro reloj y puede ser utilizado con `navigator.accelerometer.clearWatch` para dejar de ver el acelerómetro.

    var watchID = navigator.accelerometer.watchAcceleration (accelerometerSuccess, accelerometerError, accelerometerOptions);
    

  * **accelerometerOptions**: Un objeto con las llaves opcionales siguientes: 
      * **periodo**: periodo solicitado de llamadas a accelerometerSuccess con los datos de aceleración en milisegundos. *(Número)* (Por defecto: 10000)

### Ejemplo

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
    

### iOS rarezas

La API llama a la función de devolución de llamada de éxito en el intervalo solicitado, pero restringe la gama de solicitudes que el dispositivo entre 40ms y 1000ms. Por ejemplo, si usted solicita un intervalo de 3 segundos, (3000ms), la API solicita datos desde el dispositivo cada 1 segundo, pero sólo ejecuta el callback de éxito cada 3 segundos.

## navigator.accelerometer.clearWatch

Dejar de mirar el `Acceleration` referenciado por el `watchID` parámetro.

    navigator.accelerometer.clearWatch(watchID);
    

  * **watchID**: el identificador devuelto por`navigator.accelerometer.watchAcceleration`.

### Ejemplo

    var watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    
    // ... later on ...
    
    navigator.accelerometer.clearWatch(watchID);
    

## Acceleration

Contiene `Accelerometer` datos capturados en un punto específico en el tiempo. Valores de aceleración incluyen el efecto de la gravedad (9,81 m/s ^ 2), de modo que cuando se encuentra un dispositivo plano y hacia arriba, *x*, *y*, y *z* valores devueltos deben ser `` , `` , y`9.81`.

### Propiedades

  * **x**: Cantidad de aceleración en el eje X. (en m/s^2) *(Number)*
  * **y**: Cantidad de aceleración en el eje Y. (en m/s^2) *(Number)*
  * **z**: Cantidad de aceleración en el eje Z. (en m/s^2) *(Number)*
  * **timestamp**: Momento de la captura en milisegundos.*(DOMTimeStamp)*