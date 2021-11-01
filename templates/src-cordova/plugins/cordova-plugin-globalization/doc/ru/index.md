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

# cordova-plugin-globalization

Этот модуль получает информацию и выполняет операции, специфичные для языка, язык и часовой пояс пользователя. Обратите внимание на разницу между и языка: язык элементов, как числа, даты и время отображаются для региона, в то время как язык определяет, какой язык текст отображается в виде, независимо от локали. Часто разработчики используют языковой стандарт для установки обоих параметров, но нет никаких причин, которые пользователь не мог установить ее язык «Английский язык», но языка «Французский», так что текст отображается на английском языке, но даты, время, и т.п., отображаются как они во Франции. К сожалению большинство мобильных платформ в настоящее время не проводится различие между этими параметрами.

## Установка

    cordova plugin add cordova-plugin-globalization
    

## Объекты

*   GlobalizationError

## Методы

*   navigator.globalization.getPreferredLanguage
*   navigator.globalization.getLocaleName
*   navigator.globalization.dateToString
*   navigator.globalization.stringToDate
*   navigator.globalization.getDatePattern
*   navigator.globalization.getDateNames
*   navigator.globalization.isDayLightSavingsTime
*   navigator.globalization.getFirstDayOfWeek
*   navigator.globalization.numberToString
*   navigator.globalization.stringToNumber
*   navigator.globalization.getNumberPattern
*   navigator.globalization.getCurrencyPattern

## navigator.globalization.getPreferredLanguage

Получите тег языка BCP 47 для клиента текущего языка.

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### Описание

Возвращает метку идентификатор совместимого языка BCP-47 к `successCallback` с `properties` объект в качестве параметра. Этот объект должен иметь `value` собственности с `String` значение.

Если есть ошибка, как язык, то `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.UNKNOWN_ERROR`.

### Поддерживаемые платформы

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en-US` языке, это должно отображать всплывающее диалоговое окно с текстом `language: en-US` :

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### Особенности Android

*   Возвращает ISO 639-двухбуквенный код языка 1, верхний регистр ISO 3166-1 код и вариант, разделенных дефисами. Примеры: «en», «en US», «США»

### Особенности Windows Phone 8

*   Код языка возвращает двухбуквенный ISO 639-1 и ISO 3166-1 код региональный вариант, соответствующий «Язык» установка, разделенных дефисом.
*   Обратите внимание, что региональный вариант является свойством параметра «Язык» и не определяется параметром отношения "Страна/регион" на Windows Phone.

## navigator.globalization.getLocaleName

Возвращает в BCP 47 совместимый тег для текущей локали клиента.

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### Описание

Возвращает строку идентификатор совместимого языка BCP 47 `successCallback` с `properties` объект в качестве параметра. Этот объект должен иметь `value` собственности с `String` значение. Тег языка будет состоять из двух букв нижнего регистра кода языка, код страны две буквы заглавные и (неопределенные) код варианта, разделенных дефисом.

Если есть ошибка получения локали, то `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.UNKNOWN_ERROR`.

### Поддерживаемые платформы

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en-US` языка, это выводит всплывающее диалоговое окно с текстом`locale: en-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Особенности Android

*   Java не различает набор «langauge» и установить «локаль», поэтому этот метод является по существу таким же, как`navigator.globalizatin.getPreferredLanguage()`.

### Особенности Windows Phone 8

*   Возвращает ISO 639-1 двухбуквенный код языка и код ISO 3166-1 страны региональный вариант соответствующего параметра «Региональный формат», разделенных дефисом.

## navigator.globalization.dateToString

Возвращает дату в формате строки согласно локали клиента и часовой пояс.

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### Описание

Возвращает отформатированную дату `String` через `value` свойств, доступных из объекта, переданного в качестве параметра для`successCallback`.

Входящий `date` параметр должен иметь тип`Date`.

Если есть ошибка форматирования даты, то `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.FORMATTING_ERROR`.

`options`Параметр является необязательным, и его значения по умолчанию являются:

    {formatLength: «короткая», селектор: «Дата и время»}
    

`options.formatLength`Может быть `short` , `medium` , `long` , или`full`.

`options.selector`Может быть `date` , `time` или`date and time`.

### Поддерживаемые платформы

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

Если браузер настроен `en_US` языка, это выводит всплывающее диалоговое окно с текстом, похож на `date: 9/25/2012 4:21PM` с использованием параметров по умолчанию:

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Windows Phone 8 причуды

*   `formatLength`Вариант поддерживает только `short` и `full` значения.

### Firefox OS причуды

*   `formatLength`не различать `long` и`full` 
*   только один метод отображения даты (не `long` или `full` версия)

## navigator.globalization.getCurrencyPattern

Возвращает строку шаблона для форматирования и анализа значений валют согласно ISO 4217 код валюты предпочтения пользователя и клиента.

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### Описание

Возвращает шаблон для `successCallback` с `properties` объект в качестве параметра. Этот объект должен содержать следующие свойства:

*   **шаблон**: валюты шаблон для форматирования и синтаксического анализа значения валюты. Шаблоны следуют [технического стандарта Unicode #35][1]. *(Строка)*

*   **код**: код валюты ISO 4217 для шаблона. *(Строка)*

*   **фракция**: количество дробных разрядов для использования когда синтаксический анализ и форматирование валюты. *(Число)*

*   **округления**: округление увеличивается для использования при синтаксического анализа и форматирования. *(Число)*

*   **десятичное**: десятичный символ использовать для синтаксического анализа и форматирования. *(Строка)*

*   **Группировка**: группировка символ использовать для синтаксического анализа и форматирования. *(Строка)*

 [1]: http://unicode.org/reports/tr35/tr35-4.html

Входящий `currencyCode` параметр должен быть `String` одного из кодов ISO 4217 валют, например «USD».

Если есть ошибка получения шаблона, то свойство `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.FORMATTING_ERROR`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   iOS

### Пример

Когда браузер настроен `en_US` языка и выбранной валюты это доллары США, этот пример отображает всплывающее диалоговое окно с текстом аналогичные результаты, которые следуют:

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
    

Ожидаемый результат:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

## navigator.globalization.getDateNames

Возвращает массив, содержащий названия месяцев или дней недели, в зависимости от предпочтений пользователя и календарь клиента.

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### Описание

Возвращает массив имен для `successCallback` с `properties` объект в качестве параметра. Этот объект содержит `value` собственности с `Array` из `String` значения. Имена функций массива, начиная с либо в первый месяц, в год или в первый день недели, в зависимости от выбранного варианта.

Если есть ошибка получения имена, а затем `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.UNKNOWN_ERROR`.

`options`Параметр является необязательным, и его значения по умолчанию являются:

    {type:'wide', item:'months'}
    

Значение `options.type` может быть `narrow` или`wide`.

Значение `options.item` может быть `months` или`days`.

### Поддерживаемые платформы

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, в этом примере отображается ряд двенадцати всплывающих диалоговых окон, один в месяц, с текстом, похож на `month: January` :

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### Firefox OS причуды

*   `options.type`поддерживает `genitive` значения, важные для некоторых языков

## navigator.globalization.getDatePattern

Возвращает строку шаблона для форматирования и разбора даты согласно предпочтениям пользователя клиента.

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### Описание

Возвращает шаблон для `successCallback` . Объект, переданный в качестве параметра содержит следующие свойства:

*   **шаблон**: Дата и время шаблон для форматирования и разбора дат. Шаблоны следуют [технического стандарта Unicode #35][1]. *(Строка)*

*   **Часовой пояс**: сокращенное название часового пояса на клиентском компьютере. *(Строка)*

*   **utc_offset**: текущий разница в секундах между часовой пояс и время клиента. *(Число)*

*   **dst_offset**: текущее смещение в летнее время в секундах между клиента не летнее часовой пояс и летнее клиента сохранение в часовой пояс. *(Число)*

Если есть ошибка получения шаблон, `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.PATTERN_ERROR`.

`options`Параметр является необязательным и по умолчанию имеет следующие значения:

    {formatLength: «короткая», селектор: «Дата и время»}
    

`options.formatLength` может быть `short`, `medium`, `long` или `full`. `options.selector`Может быть `date` , `time` или`date and
time`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, этот пример отображает всплывающее диалоговое окно с текстом, такие как `pattern: M/d/yyyy h:mm a` :

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 причуды

*   `formatLength`Поддерживает только `short` и `full` значения.

*   `pattern`Для `date and time` модель возвращает только полное datetime формат.

*   `timezone`Возвращает имя зоны полный рабочий день.

*   `dst_offset`Свойство не поддерживается, и всегда возвращает нуль.

## navigator.globalization.getFirstDayOfWeek

Возвращает первый день недели согласно календаря предпочтения пользователя и клиента.

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### Описание

Дни недели нумеруются, начиная с 1, где 1 считается воскресенье. Возвращает день в `successCallback` с `properties` объект в качестве параметра. Этот объект должен иметь `value` собственности с `Number` значение.

Если есть ошибка получения шаблона, то свойство `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.UNKNOWN_ERROR`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, это выводит всплывающее диалоговое окно с текстом похож на`day: 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

## navigator.globalization.getNumberPattern

Возвращает строку шаблона для форматирования и разбора номера согласно предпочтениям пользователя клиента.

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### Описание

Возвращает шаблон для `successCallback` с `properties` объект в качестве параметра. Этот объект содержит следующие свойства:

*   **шаблон**: шаблон номера для форматирования и синтаксического анализа чисел. Шаблоны следуют [технического стандарта Unicode #35][1]. *(Строка)*

*   **символ**: символ для использования при форматировании и синтаксическом разборе, например символ валюты и процентов. *(Строка)*

*   **фракция**: количество дробных разрядов для использования при синтаксического анализа и форматирования чисел. *(Число)*

*   **округления**: округление увеличивается для использования при синтаксического анализа и форматирования. *(Число)*

*   **положительные**: символ для положительных чисел, когда синтаксический анализ и форматирование. *(Строка)*

*   **отрицательные**: символ для отрицательных чисел, когда синтаксический анализ и форматирование. *(Строка)*

*   **десятичное**: десятичный символ использовать для синтаксического анализа и форматирования. *(Строка)*

*   **Группировка**: группировка символ использовать для синтаксического анализа и форматирования. *(Строка)*

Если есть ошибка получения шаблона, то свойство `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.PATTERN_ERROR`.

`options`Параметр является необязательным, и значения по умолчанию являются:

    {Тип: «десятичных»}
    

`options.type` может быть `decimal`, `percent` или `currency`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, это должно отображать всплывающее диалоговое окно с текстом аналогичные результаты, которые следуют:

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
    

Результаты:

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 причуды

*   `pattern`Свойство не поддерживается и retuens является пустой строкой.

*   `fraction`Свойство не поддерживается, и возвращает ноль.

## navigator.globalization.isDayLightSavingsTime

Указывает, является ли летнее время в силе для заданной даты, с использованием клиента часовой пояс и календаря.

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### Описание

Указывает, является ли или не летнее время в силе до `successCallback` с `properties` объект в качестве параметра. Этот объект должен иметь `dst` свойство с `Boolean` значение. A `true` значение указывает, что летнее время в силе для заданной даты и `false` показывает, что это не.

Входящий параметр `date` должен иметь тип`Date`.

Если есть ошибка чтения даты, то `errorCallback` выполняет. Ожидаемый код ошибки`GlobalizationError.UNKNOWN_ERROR`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

В течение лета и если браузер настроен на часовой пояс, летнее время с поддержкой, это должно отображать всплывающее диалоговое окно с текстом похож на `dst: true` :

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

Возвращает число, которое форматируется как строка согласно предпочтениям пользователя клиента.

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### Описание

Возвращает форматируемую строку номер для `successCallback` с `properties` объект в качестве параметра. Этот объект должен иметь `value` собственности с `String` значение.

Если есть ошибка форматирования числа, то `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.FORMATTING_ERROR`.

`options`Параметр является необязательным, и его значения по умолчанию являются:

    {Тип: «десятичных»}
    

`options.type` может быть 'decimal', 'percent' или 'currency'.

### Поддерживаемые платформы

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, это выводит всплывающее диалоговое окно с текстом, похож на `number: 3.142` :

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

## navigator.globalization.stringToDate

Анализирует дату форматированы в виде строки, по словам клиента предпочтения пользователя и календарь с помощью часовой пояс клиента и возвращает соответствующий объект date.

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### Описание

Возвращает дату в успех обратного вызова с `properties` объект в качестве параметра. Этот объект должен иметь следующие свойства:

*   **год**: год четыре цифры. *(Число)*

*   **месяц**: на месяц от (0-11). *(Число)*

*   **день**: день с (1-31). *(Число)*

*   **час**: час (0-23). *(Число)*

*   **минута**: минута (0-59). *(Число)*

*   **второй**: второй от (0-59). *(Число)*

*   **МС**: миллисекунд (от 0-999), не доступны на всех платформах. *(Число)*

Входящий `dateString` параметр должен иметь тип`String`.

`options`Параметр является необязательным и по умолчанию имеет следующие значения:

    {formatLength: «короткая», селектор: «Дата и время»}
    

`options.formatLength` может быть `short`, `medium`, `long` или `full`. `options.selector`Может быть `date` , `time` или`date and
time`.

Если есть ошибка при разборе строки даты, то `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.PARSING_ERROR`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, это выводит всплывающее диалоговое окно с текстом, похож на `month:8 day:25 year:2012` . Обратите внимание, что целое число является один месяц меньше, чем строка, как целое число месяца представляет индекс массива.

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 причуды

*   `formatLength`Вариант поддерживает только `short` и `full` значения.

## navigator.globalization.stringToNumber

Анализирует число, которое форматируется как строка согласно предпочтениям пользователя клиента и возвращает соответствующий номер.

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### Описание

Возвращает номер для `successCallback` с `properties` объект в качестве параметра. Этот объект должен иметь `value` свойство с `Number` значение.

Если есть ошибка при разборе номер строки, а затем `errorCallback` выполняет с `GlobalizationError` объект в качестве параметра. Ожидаемый код ошибки`GlobalizationError.PARSING_ERROR`.

`options`Параметр является необязательным и по умолчанию имеет следующие значения:

    {Тип: «десятичных»}
    

`options.type` может быть `decimal`, `percent` или `currency`.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8

### Пример

Когда браузер настроен `en_US` языка, это должно отображать всплывающее диалоговое окно с текстом, похож на `number: 1234.56` :

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

## GlobalizationError

Объект, представляющий ошибку от глобализации API.

### Свойства

*   **код**: Один из следующих кодов, представляющих тип ошибки *(Число)* 
    *   GlobalizationError.UNKNOWN_ERROR: 0
    *   GlobalizationError.FORMATTING_ERROR: 1
    *   GlobalizationError.PARSING_ERROR: 2
    *   GlobalizationError.PATTERN_ERROR: 3
*   **сообщение**: текстовое сообщение, которое включает в себя объяснение ошибки и/или детали *(String)*

### Описание

Этот объект создается и населенная Cordova и возвращается обратный вызов в случае ошибки.

### Поддерживаемые платформы

*   Amazon Fire ОС
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS

### Пример

Когда следующий ошибка обратного вызова выполняется, он отображает всплывающее диалоговое окно с текстом похож на `code: 3` и`message:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };
