<!--
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

# cordova-plugin-globalization

[![Build Status](https://travis-ci.org/apache/cordova-plugin-globalization.svg)](https://travis-ci.org/apache/cordova-plugin-globalization)

Este plugin obtiene información y realiza operaciones específicas de la configuración regional del usuario, idioma y zona horaria. Tenga en cuenta la diferencia entre la configuración regional e idioma: controles locale como números, fechas y tiempos se muestran para una región, mientras que el lenguaje determina qué texto aparece como, independientemente de la configuración local. A menudo los desarrolladores utilizan locale para fijar ambos ajustes, pero no hay razón que el usuario no pudo establecer su idioma a "Inglés" locale "Francés", para que se muestre el texto en inglés, pero las fechas, tiempos, etc., se muestran como son en Francia. Desafortunadamente, las plataformas móviles más actualmente no hacen una distinción entre estos ajustes.

Este plugin define global `navigator.globalization` objeto.

Aunque en el ámbito global, no estará disponible hasta después de la `deviceready` evento.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## Instalación

    cordova plugin add cordova-plugin-globalization
    

## Objetos

  * GlobalizationError

## Métodos

  * navigator.globalization.getPreferredLanguage
  * navigator.globalization.getLocaleName
  * navigator.globalization.dateToString
  * navigator.globalization.stringToDate
  * navigator.globalization.getDatePattern
  * navigator.globalization.getDateNames
  * navigator.globalization.isDayLightSavingsTime
  * navigator.globalization.getFirstDayOfWeek
  * navigator.globalization.numberToString
  * navigator.globalization.stringToNumber
  * navigator.globalization.getNumberPattern
  * navigator.globalization.getCurrencyPattern

## navigator.globalization.getPreferredLanguage

Busque la etiqueta de idioma BCP 47 el idioma actual del cliente.

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### Descripción

Devuelve la etiqueta de identificador de idioma compatible con BCP-47 a la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe tener un `value` propiedad con un `String` valor.

Si hay un error al obtener el idioma, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.UNKNOWN_ERROR`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador está configurado la `en-US` lengua, ésta debe mostrar un cuadro de diálogo emergente con el texto `language: en-US` :

    navigator.globalization.getPreferredLanguage (función (lengua) {alert (' idioma: ' + language.value + '\n');}, function () {alert ('Error al obtener language\n');});
    

### Rarezas Android

  * Devuelve el código de idioma de dos letras 639-1 ISO, mayúsculas código ISO 3166-1 y la variante separada por guiones. Ejemplos: "at", "en-US", "US"

### Windows Phone 8 rarezas

  * Código de idioma devuelve el ISO 639-1 dos letras y código de la ISO 3166-1 de la variante regional correspondiente a la "lengua" ajuste, separados por un guión.
  * Tenga en cuenta que la variante regional es una característica de la configuración del "Idioma" y no determinado por el ajuste de "País o región" sin relación en Windows Phone.

### Windows rarezas

  * Código de idioma devuelve el ISO 639-1 dos letras y código de la ISO 3166-1 de la variante regional correspondiente a la "lengua" ajuste, separados por un guión.

### Navegador rarezas

  * Falls back on getLocaleName

## navigator.globalization.getLocaleName

Devuelve la etiqueta compatible con BCP 47 para la configuración regional actual del cliente.

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### Descripción

Devuelve el identificador BCP 47 local conforme a la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe tener un `value` propiedad con un `String` valor. La etiqueta de configuración regional consistirá en un código de idioma de dos letras minúsculas, código de país de dos letras mayúsculas y códigos de la variante (no especificados), separados por un guión.

Si hay un error al obtener la configuración regional, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.UNKNOWN_ERROR`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador se establece en el `en-US` local, muestra un cuadro de diálogo emergente con el texto`locale: en-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Rarezas Android

  * Java no distingue entre un conjunto "idioma" y establecer "locale", así que este método es esencialmente el mismo que`navigator.globalizatin.getPreferredLanguage()`.

### Windows Phone 8 rarezas

  * Código de idioma devuelve el ISO 639-1 dos letras y código de la ISO 3166-1 de la variante regional correspondiente a la posición "Formato Regional", separada por un guión.

### Windows rarezas

  * Puede cambiar configuración regional del Panel de Control-> reloj, idioma y región-> región-> formatos-> formato y en configuración de-> región-> formato Regional en Windows Phone 8.1.

### Navegador rarezas

  * IE devuelve la configuración regional del sistema operativo. Chrome y Firefox volver etiqueta de idioma del navegador.

## navigator.globalization.dateToString

Devuelve una fecha con formato como una cadena según la configuración regional del cliente y zona horaria.

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### Descripción

Devuelve la fecha con formato `String` vía un `value` propiedad accesible desde el objeto pasado como parámetro para el`successCallback`.

Los entrantes `date` parámetro debe ser del tipo`Date`.

Si hay un error de formato de la fecha, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.FORMATTING_ERROR`.

El `options` parámetro es opcional, y sus valores por defecto son:

    {formatLength:'short', selector:'date and time'}
    

El `options.formatLength` puede ser `short` , `medium` , `long` , o`full`.

El `options.selector` puede ser `date` , `time` o`date and time`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Si el navegador está configurado la `en_US` local, muestra un cuadro de diálogo emergente con texto similar a `date: 9/25/2012 4:21PM` utilizando las opciones predeterminadas:

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Rarezas Android

  * `formatLength`las opciones son un subconjunto de Unicode [UTS #35](http://unicode.org/reports/tr35/tr35-4.html). La opción predeterminada `short` depende de un formato de fecha seleccionada usuario dentro de `Settings -> System -> Date & time -> Choose date format` , que proporcionan un `year` patrón solamente con 4 dígitos, no de 2 dígitos. Esto significa que no está completamente alineado con [ICU](http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US).

### Windows Phone 8 rarezas

  * El `formatLength` los soportes de la opción `short` y `full` los valores.

  * El patrón de selector 'fecha y hora' es siempre un formato datetime completo.

  * El valor devuelto puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

### Windows rarezas

  * El `formatLength` los soportes de la opción `short` y `full` los valores.

  * El patrón de selector 'fecha y hora' es siempre un formato datetime completo.

  * El valor devuelto puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

### Navegador rarezas

  * 79 locales son compatibles porque moment.js se utiliza en este método.

  * El valor devuelto puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

  * selector de `time` apoya sólo formatLength `full` y `short` .

### Firefox OS rarezas

  * `formatLength`No es distinguir `long` y`full` 
  * Sólo un método de visualización de fecha (no `long` o `full` versión)

## navigator.globalization.getCurrencyPattern

Devuelve una cadena de patrón para analizar valores de divisas según las preferencias del usuario y código de moneda ISO 4217 del cliente y el formato.

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### Descripción

Devuelve el patrón a la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe contener las siguientes propiedades:

  * **patrón**: el patrón de la moneda para analizar los valores de la moneda y el formato. Los patrones siguen [Unicode técnica estándar #35](http://unicode.org/reports/tr35/tr35-4.html). *(String)*

  * **código**: código de divisa de la ISO 4217 para el patrón. *(String)*

  * **fracción**: el número de dígitos fraccionarios a utilizar al análisis sintáctico y el formato de moneda. *(Número)*

  * **redondeo**: el redondeo incremento para utilizar al análisis sintáctico y formato. *(Número)*

  * **decimal**: el símbolo decimal para analizar y dar formato. *(String)*

  * **agrupación**: el símbolo de la agrupación para analizar y dar formato. *(String)*

Los entrantes `currencyCode` parámetro debe ser un `String` de uno de los códigos de moneda ISO 4217, por ejemplo 'USD'.

Si hay un error obteniendo el patrón, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.FORMATTING_ERROR`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows 8
  * Windows

### Ejemplo

Cuando el navegador está configurado la `en_US` local y la moneda seleccionada dólares de Estados Unidos, este ejemplo muestra un cuadro de diálogo emergente con texto similar a los resultados que siguen:

    navigator.globalization.getCurrencyPattern(
        'USD',
        function (pattern) {
            alert('pattern: '  + pattern.pattern  + '\n' +
                  'code: '     + pattern.code     + '\n' +
                  'fraction: ' + pattern.fraction + '\n' +
                  'rounding: ' + pattern.rounding + '\n' +
                  'decimal: '  + pattern.decimal  + '\n' +
                  'grouping: ' + pattern.grouping);
        },
        function () { alert('Error getting pattern\n'); }
    );
    

Resultado esperado:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### Windows rarezas

  * Se admiten las propiedades únicas de 'código' y la 'fracción'

## navigator.globalization.getDateNames

Devuelve una matriz de los nombres de los meses o días de la semana, dependiendo de las preferencias del usuario y el calendario del cliente.

    navigator.globalization.getDateNames (successCallback, errorCallback, opciones);
    

### Descripción

Devuelve la matriz de nombres de la `successCallback` con un `properties` objeto como parámetro. Ese objeto contiene un `value` propiedad con un `Array` de `String` valores. Los nombres de funciones de matriz a partir desde el primer mes en el año o el primer día de la semana, dependiendo de la opción seleccionada.

Si hay un error obteniendo los nombres, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.UNKNOWN_ERROR`.

El `options` parámetro es opcional, y sus valores por defecto son:

    {type:'wide', item:'months'}
    

El valor de `options.type` puede ser `narrow` o`wide`.

El valor de `options.item` puede ser `months` o`days`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador se establece en el `en_US` local, este ejemplo muestra una serie de doce diálogos emergente, uno por mes, con un texto similar a `month: January` :

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### Firefox OS rarezas

  * `options.type`apoya un `genitive` valor, importante para algunos idiomas

### Windows Phone 8 rarezas

  * La matriz de meses contiene 13 elementos.
  * La matriz devuelta puede ser no totalmente alineada con ICU dependiendo de una configuración regional del usuario.

### Windows rarezas

  * La matriz de meses contiene 12 elementos.
  * La matriz devuelta puede ser no totalmente alineada con ICU dependiendo de una configuración regional del usuario.

### Navegador rarezas

  * Nombres fecha no están completamente alineados con ICU
  * La matriz de meses contiene 12 elementos.

## navigator.globalization.getDatePattern

Devuelve una cadena de patrón para analizar las fechas según las preferencias del cliente usuario y el formato.

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### Descripción

Devuelve el patrón a la `successCallback` . El objeto se pasa como parámetro contiene las siguientes propiedades:

  * **patrón**: el patrón para analizar las fechas y el formato de fecha y hora. Los patrones siguen [Unicode técnica estándar #35](http://unicode.org/reports/tr35/tr35-4.html). *(String)*

  * **zona horaria**: el nombre abreviado de la zona horaria en el cliente. *(String)*

  * **utc_offset**: la actual diferencia de segundos entre la zona horaria del cliente y el tiempo universal coordinado. *(Número)*

  * **dst_offset**: el desplazamiento horario actual en segundos entre no-horario del cliente de huso horario y día del cliente ahorro de zona horaria. *(Número)*

Si hay un error obteniendo el patrón, el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.PATTERN_ERROR`.

El `options` parámetro es opcional y por defecto los siguientes valores:

    {formatLength:'short', selector:'date and time'}
    

El `options.formatLength` puede ser `short` , `medium` , `long` , o `full` . El `options.selector` puede ser `date` , `time` o`date and
time`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador se establece en el `en_US` local, este ejemplo muestra un cuadro de diálogo emergente con el texto como `pattern: M/d/yyyy h:mm a` :

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 rarezas

  * El `formatLength` sólo es compatible con `short` y `full` los valores.

  * El `pattern` para `date and time` patrón devuelve sólo formato datetime completo.

  * El `timezone` devuelve el nombre de zona de tiempo completo.

  * El `dst_offset` no se admite la propiedad, y siempre devuelve cero.

  * El patrón puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

### Windows rarezas

  * El `formatLength` sólo es compatible con `short` y `full` los valores.

  * El `pattern` para `date and time` patrón devuelve sólo formato datetime completo.

  * El `timezone` devuelve el nombre de zona de tiempo completo.

  * El `dst_offset` no se admite la propiedad, y siempre devuelve cero.

  * El patrón puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

### Navegador rarezas

  * La propiedad 'pattern' no admite y devuelve la cadena vacía.

  * Sólo cromo devuelve 'zona horaria' propiedad. Su formato es "Parte del mundo/{City}". Otros navegadores volver cadena vacía.

## navigator.globalization.getFirstDayOfWeek

Devuelve el primer día de la semana según las preferencias del usuario y el calendario del cliente.

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### Descripción

Los días de la semana están contados a partir de la 1, donde 1 se supone que es el domingo. Devuelve el día de la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe tener un `value` propiedad con un `Number` valor.

Si hay un error obteniendo el patrón, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.UNKNOWN_ERROR`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador se establece en el `en_US` local, muestra un cuadro de diálogo emergente con texto similar a`day: 1`.

    navigator.globalization.getFirstDayOfWeek (función (día) {alert (' día: ' + day.value + '\n');}, function () {alert ('Error al obtener day\n');});
    

### Windows rarezas

  * En Windows 8.0/8.1 el valor depende de usuario ' preferencias del calendario. Windows Phone 8.1 el valor depende de configuración regional actual.

### Navegador rarezas

  * 79 locales son compatibles porque moment.js se utiliza en este método.

## navigator.globalization.getNumberPattern

Devuelve una cadena de patrón para analizar números según las preferencias del cliente usuario y el formato.

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### Descripción

Devuelve el patrón a la `successCallback` con un `properties` objeto como parámetro. Ese objeto contiene las siguientes propiedades:

  * **patrón**: el patrón del número a analizar números y el formato. Los patrones siguen [Unicode técnica estándar #35](http://unicode.org/reports/tr35/tr35-4.html). *(String)*

  * **símbolo**: el símbolo a usar cuando formateo y análisis, como un símbolo por ciento o moneda. *(String)*

  * **fracción**: el número de dígitos fraccionarios a utilizar al análisis sintáctico y el formato de números. *(Número)*

  * **redondeo**: el redondeo incremento para utilizar al análisis sintáctico y formato. *(Número)*

  * **positivo**: el símbolo para números positivos al análisis sintáctico y formato. *(String)*

  * **negativo**: el símbolo para números negativos al análisis sintáctico y formato. *(String)*

  * **decimal**: el símbolo decimal para analizar y dar formato. *(String)*

  * **agrupación**: el símbolo de la agrupación para analizar y dar formato. *(String)*

Si hay un error obteniendo el patrón, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.PATTERN_ERROR`.

El `options` parámetro es opcional, y los valores por defecto son:

    {type:'decimal'}
    

El `options.type` puede ser `decimal` , `percent` , o`currency`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador está configurado el `en_US` locale, esto debería mostrar un cuadro de diálogo emergente con texto similar a los resultados que siguen:

    navigator.globalization.getNumberPattern(
        function (pattern) {alert('pattern: '  + pattern.pattern  + '\n' +
                                  'symbol: '   + pattern.symbol   + '\n' +
                                  'fraction: ' + pattern.fraction + '\n' +
                                  'rounding: ' + pattern.rounding + '\n' +
                                  'positive: ' + pattern.positive + '\n' +
                                  'negative: ' + pattern.negative + '\n' +
                                  'decimal: '  + pattern.decimal  + '\n' +
                                  'grouping: ' + pattern.grouping);},
        function () {alert('Error getting pattern\n');},
        {type:'decimal'}
    );
    

Resultados:

    patrón: #, ## 0. ### símbolo:.
    fracción: redondeo 0: 0 positivo: negativo: - decimal:.
    agrupación:,
    

### Windows Phone 8 rarezas

  * El `pattern` no admite la propiedad y devuelve una cadena vacía.

  * El `fraction` no se admite la propiedad, y devuelve cero.

### Windows rarezas

  * El `pattern` no admite la propiedad y devuelve una cadena vacía.

### Navegador rarezas

  * getNumberPattern es compatible con Chrome la única propiedad definida es `patrón`.

## navigator.globalization.isDayLightSavingsTime

Indica si el horario de verano es en efecto para una fecha determinada usando la zona horaria y el calendario del cliente.

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### Descripción

Indica si es o no horario de verano en efecto a la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe tener un `dst` propiedad con un `Boolean` valor. A `true` valor indica que el horario de verano es en efecto para la fecha determinada, y `false` indica que no es.

El parámetro entrantes `date` debe ser de tipo`Date`.

Si hay un error de lectura de la fecha, entonces el `errorCallback` se ejecuta. Código esperado del error es`GlobalizationError.UNKNOWN_ERROR`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Durante el verano, y si el navegador está configurado para una zona horaria DST habilitado, esto debería mostrar un cuadro de diálogo emergente con texto similar a `dst: true` :

    navigator.globalization.isDayLightSavingsTime (new Date(), función (fecha) {alert ('dst: ' + date.dst + '\n');}, function () {alert ('Error al obtener names\n');});
    

## navigator.globalization.numberToString

Devuelve un número con formato como una cadena según las preferencias del cliente usuario.

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### Descripción

Devuelve la cadena con formato de número a la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe tener un `value` propiedad con un `String` valor.

Si hay un error de formato del número, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.FORMATTING_ERROR`.

El `options` parámetro es opcional, y sus valores por defecto son:

    {type:'decimal'}
    

El `options.type` puede ser 'decimal', '%' o 'moneda'.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador se establece en el `en_US` local, muestra un cuadro de diálogo emergente con texto similar a `number: 3.142` :

    navigator.globalization.numberToString (3.1415926, función (número) {alert (' número: ' + number.value + '\n');}, function () {alert ('Error al obtener number\n');}, {type:'decimal'});
    

### Windows rarezas

  * Windows 8.0 no soporta redondeo de número, por lo tanto los valores serán no redondeados automáticamente.

  * 8.1 de Windows y Windows Phone 8.1 parte fraccional es ser truncado en vez de redondeados en caso de `percent` tipo de número por lo tanto dígitos fraccionarios Conde se establece en 0.

  * `percent`números no se agrupan como que no se puede analizar en stringToNumber si agrupados.

### Navegador rarezas

  * no se admite el tipo de `currency` .

## navigator.globalization.stringToDate

Analiza una fecha con formato como una cadena, según las preferencias del usuario y calendario usando la zona horaria del cliente, el cliente y devuelve el objeto correspondiente fecha.

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### Descripción

Devuelve la fecha para la devolución de llamada con éxito un `properties` objeto como parámetro. Ese objeto debe tener las siguientes propiedades:

  * **año**: el año de cuatro dígitos. *(Número)*

  * **mes**: mes de (0-11). *(Número)*

  * **día**: el día de (1-31). *(Número)*

  * **hora**: la hora de (0-23). *(Número)*

  * **minuto**: el minuto de (0-59). *(Número)*

  * **segundo**: el segundo de (0-59). *(Número)*

  * **milisegundo**: los milisegundos (de 0-999), no está disponibles en todas las plataformas. *(Número)*

Los entrantes `dateString` parámetro debe ser del tipo`String`.

El `options` parámetro es opcional y por defecto los siguientes valores:

    {formatLength:'short', selector:'date and time'}
    

El `options.formatLength` puede ser `short` , `medium` , `long` , o `full` . El `options.selector` puede ser `date` , `time` o`date and
time`.

Si hay un error al analizar la cadena de fecha, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.PARSING_ERROR`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Explorador

### Ejemplo

Cuando el navegador se establece en el `en_US` local, muestra un cuadro de diálogo emergente con texto similar a `month:8 day:25 year:2012` . Tenga en cuenta que el mes entero es uno menos de la cadena, como el entero mes representa un índice de matriz.

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 rarezas

  * El `formatLength` los soportes de la opción `short` y `full` los valores.

  * El patrón de selector 'fecha y hora' es siempre un formato datetime completo.

  * Los entrantes `dateString` parámetro debe ser formado en cumplimiento de un patrón devuelto por getDatePattern. Este patrón puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

### Windows rarezas

  * El `formatLength` los soportes de la opción `short` y `full` los valores.

  * El patrón de selector 'fecha y hora' es siempre un formato datetime completo.

  * Los entrantes `dateString` parámetro debe ser formado en cumplimiento de un patrón devuelto por getDatePattern. Este patrón puede ser no totalmente alineado con ICU dependiendo de una configuración regional del usuario.

### Navegador rarezas

  * 79 locales son compatibles porque moment.js se utiliza en este método.

  * Entrantes de la cadena debe estar alineada con el formato de salida de `dateToString` y mayo no totalmente alineado con ICU según una configuración regional del usuario.

  * selector de `time` apoya sólo formatLength `full` y `short` .

## navigator.globalization.stringToNumber

Analiza un número con formato como una cadena según las preferencias del cliente usuario y devuelve el número correspondiente.

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### Descripción

Devuelve el número de la `successCallback` con un `properties` objeto como parámetro. Ese objeto debe tener un `value` propiedad con un `Number` valor.

Si hay un error al analizar la cadena de número, entonces el `errorCallback` se ejecuta con un `GlobalizationError` objeto como parámetro. Código esperado del error es`GlobalizationError.PARSING_ERROR`.

El `options` parámetro es opcional y por defecto los siguientes valores:

    {type:'decimal'}
    

El `options.type` puede ser `decimal` , `percent` , o`currency`.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows

### Ejemplo

Cuando el navegador está configurado el `en_US` locale, esto debería mostrar un cuadro de diálogo emergente con texto similar a `number: 1234.56` :

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 rarezas

  * En caso de `percent` tipo del valor devuelto no está dividido por 100.

### Windows rarezas

  * La cadena debe cumplir estrictamente con el formato de la localidad. Por ejemplo, el símbolo de porcentaje debe ser separado por espacio de configuración 'en-US' si el parámetro de tipo es '%'.

  * `percent`números no deben estar agrupados para ser analizado correctamente.

## GlobalizationError

Un objeto que representa un error de la API de la globalización.

### Propiedades

  * **Código**: Uno de los siguientes códigos que representa el tipo de error *(Número)* 
      * GlobalizationError.UNKNOWN_ERROR: 0
      * GlobalizationError.FORMATTING_ERROR: 1
      * GlobalizationError.PARSING_ERROR: 2
      * GlobalizationError.PATTERN_ERROR: 3
  * **mensaje**: un mensaje de texto que incluye la explicación de los errores o detalles *(String)*

### Descripción

Este objeto es creado y poblada por Córdoba y regresó a una devolución de llamada en caso de error.

### Plataformas soportadas

  * Amazon fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows

### Ejemplo

Cuando se ejecuta el callback de error siguiente, se muestra un cuadro de diálogo emergente con el texto similar a `code: 3` y`message:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };