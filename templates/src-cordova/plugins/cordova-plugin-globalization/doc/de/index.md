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

Dieses Plugin Ruft Informationen und führt durch spezifisch für des Benutzers Gebietsschema, Sprache und Zeitzone. Beachten Sie den Unterschied zwischen Sprache und Gebietsschema: Gebietsschema Steuerelemente wie Zahlen, Datumsangaben und Zeiten werden angezeigt für eine Region, während die Sprache bestimmt, welcher Text in Sprache erscheint als, unabhängig von den Einstellungen des Gebietsschemas. Häufig Entwickler verwenden Gebietsschema verwenden, setzen Sie beide Einstellungen aber es gibt keinen Grund, die ein Benutzer ihre Sprache auf "Englisch" eingestellt konnte nicht aber Gebietsschema "Französisch", damit Text angezeigt wird, in Englisch, aber Termine, Zeiten, usw. werden angezeigt wie in Frankreich. Leider machen die meisten mobile Plattformen derzeit keine Unterscheidung zwischen diesen Einstellungen.

Dieses Plugin wird global `navigator.globalization`-Objekt definiert.

Obwohl im globalen Gültigkeitsbereich, steht es nicht bis nach dem `deviceready`-Ereignis.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## Installation

    cordova plugin add cordova-plugin-globalization
    

## Objekte

*   GlobalizationError

## Methoden

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

Erhalten Sie das BCP 47-Sprachtag für aktuelle Sprache des Clients.

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### Beschreibung

Gibt das BCP-47-kompatiblen Sprache Bezeichner-Tag an der `successCallback` mit einem `properties`-Objekt als Parameter zurück. Das Objekt sollte eine `Value`-Eigenschaft mit einem `String`-Wert haben.

Wenn ein Fehler, der immer der Sprache vorliegt, führt die `errorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.UNKNOWN_ERROR`.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf die `En-US`-Sprache festgelegt ist, sollte dies einen Popup-Dialog mit dem Text anzeigen `Sprache: En-US`:

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### Android Eigenarten

*   Gibt zurück, der ISO 639-1 zwei Buchstaben bestehenden Sprachcode, Großbuchstaben ISO 3166-1-Ländercode und Variante, die durch Bindestriche getrennt sind. Beispiele: "de", "En-US", "US"

### Windows Phone 8 Macken

*   Gibt die ISO 639-1 zweistelligen Sprachcode und ISO 3166-1-Ländercode der regionalen Variante der "Sprache" festlegen, durch einen Bindestrich getrennt.
*   Beachten Sie, dass die regionale Variante eine Eigenschaft des "Spracheinstellung ist" und nicht durch die unabhängige "Land/Region" Einstellung auf Windows Phone bestimmt.

### Windows-Eigenheiten

*   Gibt die ISO 639-1 zweistelligen Sprachcode und ISO 3166-1-Ländercode der regionalen Variante der "Sprache" festlegen, durch einen Bindestrich getrennt.

## navigator.globalization.getLocaleName

Gibt das BCP 47 kompatible Tag für aktuelle Gebietsschema-Einstellung des Clients zurück.

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### Beschreibung

Gibt die BCP 47 kompatible Gebietsschemabezeichner-Zeichenfolge an die `SuccessCallback` mit einem `Eigenschaften`-Objekt als Parameter zurück. Das Objekt sollte eine `Value`-Eigenschaft mit einem `String`-Wert haben. Das Gebietsschema-Tag besteht aus ein Sprachcode zwei Buchstaben in Kleinbuchstaben und Großbuchstaben Zweibuchstaben-Ländercode (nicht spezifiziert) Variantencode, durch einen Bindestrich getrennt.

Wenn ein Fehler, der immer des Gebietsschemas vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.UNKNOWN_ERROR`.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En-US`-Gebietsschema festgelegt ist, zeigt dies einen Popup-Dialog mit dem Text `Locale: En-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Android Eigenarten

*   Java unterscheidet nicht zwischen einem Set "lancuage" und Set "Locale", so ist diese Methode im Wesentlichen das gleiche wie `navigator.globalizatin.getPreferredLanguage()`.

### Windows Phone 8 Macken

*   Gibt die ISO 639-1 zweistelligen Sprachcode und ISO 3166-1-Ländercode der regionalen Variante entsprechenden auf die "Regionales Format"-Einstellung, die durch einen Bindestrich getrennt.

### Windows-Eigenheiten

*   Locale-Einstellung kann in der Systemsteuerung-> Zeit, Sprache und Region-> Region-> Formate-> Format und in-> Region-> Regionales Format auf Windows Phone 8.1-Einstellungen geändert werden.

## navigator.globalization.dateToString

Gibt ein Datum formatiert als Zeichenfolge gemäß der Client Gebietsschema und Zeitzone.

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### Beschreibung

Gibt das formatierte Datum `String` über eine `Value`-Eigenschaft aus dem Objekt als Parameter übergeben, um die `SuccessCallback` zu erreichen.

Der eingehende `date`-Parameter muss vom Typ `Date` sein.

Wenn ein Fehler, die Formatierung des Datums vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.FORMATTING_ERROR`.

Der `options`-Parameter ist optional, und die Standardwerte sind:

    {formatLength:'short', selector:'date and time'}
    

Die `options.formatLength` kann `short`, `medium`, `long` oder `full` sein.

Die `options.selector` können `date`, `time` oder `date and time` werden.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, zeigt dies einen Popup-Dialog mit Text ähnlich `Datum: 25.09.2012 16:21` mit den Standardoptionen:

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Android Eigenarten

*   `formatLength`-Optionen sind eine Teilmenge der Unicode [UTS #35][1]. Die standardmäßige Option `kurze` hängt von einem Benutzer ausgewählten Datumsformat in `Einstellungen -> System -> Datum & Zeit-Datumsformat auswählen >`, die liefern einer `Jahr`-Musters nur mit 4 Ziffern, nicht 2 Ziffern. Dies bedeutet, dass es nicht völlig [ICU][2] ausgerichtet ist.

 [1]: http://unicode.org/reports/tr35/tr35-4.html
 [2]: http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US

### Windows Phone 8 Macken

*   Die `FormatLength`-Option unterstützt nur `short` und `full` Werte.

*   Das Muster für "date and time" Selektor ist immer eine volle Datetime-Format.

*   Der zurückgegebene Wert möglicherweise nicht vollständig mit ICU je nach ein Benutzergebietsschema ausgerichtet werden.

### Windows-Eigenheiten

*   Die `FormatLength`-Option unterstützt nur `short` und `full` Werte.

*   Das Muster für "date and time" Selektor ist immer eine volle Datetime-Format.

*   Der zurückgegebene Wert möglicherweise nicht vollständig mit ICU je nach ein Benutzergebietsschema ausgerichtet werden.

### Firefox OS Macken

*   `formatLength` ist `long` und `full` unterscheiden. 
*   nur eine Methode der Anzeige von Datum (keine `long` oder `full`-Version)

## navigator.globalization.getCurrencyPattern

Gibt eine Musterzeichenfolge zum Formatieren und Analysieren von Währungsangaben nach Benutzereinstellungen und ISO 4217 Währungscode des Kunden.

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### Beschreibung

Gibt das Muster auf der `successCallback` mit einem `properties`-Objekt als Parameter. Das Objekt sollte die folgenden Eigenschaften enthalten:

*   **pattern**: das Währung-Muster zur Formatierung und zum Analysieren von Währungswerten. Die Muster folgen [Unicode Technical Standard #35][1]. *(String)*

*   **code**: der ISO-4217-Währungscode für das Muster. *(String)*

*   **fraction**: die Anzahl von Bruchziffern zum analysieren und Formatieren einer Währung verwendet. *(Anzahl)*

*   **rounding**: die Rundung erhöhen wenn analysieren und formatieren verwenden. *(Anzahl)*

*   **decimal**: das Dezimaltrennzeichen für analysieren und formatieren. *(String)*

*   **grouping**: das Symbol für Zifferngruppierung zum analysieren und formatieren verwenden. *(String)*

Der eingehende `currencyCode`-Parameter muss eine `String` eines der ISO 4217 Währungscodes, z. B. 'USD' sein.

Wenn ein Fehler, erhalten das Muster vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.FORMATTING_ERROR`.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist und die ausgewählte Währung US-Dollar, zeigt in diesem Beispiel wird einen Popup-Dialog mit Text ähnlich wie die Ergebnisse, die Folgen:

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
    

Erwartete Ergebnis:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### Windows-Eigenheiten

*   Nur 'code' und 'fraction' Eigenschaften werden unterstützt

## navigator.globalization.getDateNames

Gibt ein Array der Namen der Monate oder Tage der Woche, abhängig von dem Client Benutzereinstellungen und Kalender.

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### Beschreibung

Gibt das Array von Namen zu den `successCallback` mit einem `properties`-Objekt als Parameter. Dieses Objekt enthält eine `Value`-Eigenschaft mit einem `Array` von `Zeichenfolgen`. Die Namen von Array-Funktionen, entweder der erste Monat im Jahr oder der erste Tag der Woche, je nach der ausgewählten Option ab.

Wenn ein Fehler, erhalten die Namen vorliegt, führt dann `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.UNKNOWN_ERROR`.

Der `options`-Parameter ist optional, und die Standardwerte sind:

    {type:'wide', item:'months'}
    

Der Wert des `options.type` kann `narrow` oder `wide` sein.

Der Wert des `options.item` kann `month` oder `days` sein.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, in diesem Beispiel wird eine Reihe von zwölf Popup-Dialoge, eine pro Monat, mit Text ähnlich `Monat: Januar`:

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### Firefox OS Macken

*   `pptions.type` unterstützt einen `genitive` Wert, wichtig für einige Sprachen

### Windows Phone 8 Macken

*   Das Array von Monaten enthält 13 Elemente.
*   Das zurückgegebene Array kann nicht vollständig mit ICU je nach ein Benutzergebietsschema ausgerichtet werden.

### Windows-Eigenheiten

*   Das Array von Monaten enthält 12 Elemente.
*   Das zurückgegebene Array kann nicht vollständig mit ICU je nach ein Benutzergebietsschema ausgerichtet werden.

## navigator.globalization.getDatePattern

Gibt eine Musterzeichenfolge zum Formatieren und Analysieren von Daten entsprechend der Client-Benutzer-Einstellungen.

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### Beschreibung

Gibt das Muster auf der `successCallback`. Das als Parameter übergebene Objekt enthält die folgenden Eigenschaften:

*   **pattern**: das Datum und die Uhrzeit-Muster zur Formatierung und zum Analysieren von Daten. Die Muster folgen [Unicode Technical Standard #35][1]. *(String)*

*   **timezone**: der abgekürzte Name der Zeitzone auf dem Client. *(String)*

*   **utc_offset**: die aktuelle Differenz in Sekunden zwischen dem Client Zeitzone und koordinierte Weltzeit. *(Anzahl)*

*   **dst_offset**: der aktuelle Sommerzeit-Offset in Sekunden zwischen der Client-Sommerzeit der Zeitzone und der Client Tageslicht Speichern der Zeitzone. *(Anzahl)*

Wenn ein Fehler, erhalten das Muster vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.PATTERN_ERROR`.

Der `options`-Parameter ist optional und wird standardmäßig auf folgende Werte:

    {formatLength:'short', selector:'date and time'}
    

Die `options.formatLength` kann `short`, `medium`, `long` oder `full` sein. Die `options.selector` können `date`, `time` oder `date and time` werden.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, in diesem Beispiel wird einen Popup-Dialog mit Text wie z. B. `Muster: t.m.JJJJ h: mm ein`:

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 Macken

*   Die `FormatLength`-Option unterstützt nur `short` und `full` Werte.

*   Das `pattern` für `date and time`-Muster gibt nur volle Datetime-Format zurück.

*   Die `timezone` gibt den Namen der Vollzeit-Zone zurück.

*   Die `dst_offset`-Eigenschaft wird nicht unterstützt und gibt immer 0 (null).

*   Das Muster kann je nach ein Benutzergebietsschema nicht vollständig mit ICU ausgerichtet werden.

### Windows-Eigenheiten

*   Die `FormatLength`-Option unterstützt nur `short` und `full` Werte.

*   Das `pattern` für `date and time`-Muster gibt nur volle Datetime-Format zurück.

*   Die `timezone` gibt den Namen der Vollzeit-Zone zurück.

*   Die `dst_offset`-Eigenschaft wird nicht unterstützt und gibt immer 0 (null).

*   Das Muster kann je nach ein Benutzergebietsschema nicht vollständig mit ICU ausgerichtet werden.

## navigator.globalization.getFirstDayOfWeek

Den ersten Tag der Woche laut dem Client Benutzereinstellungen und Kalender gibt.

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### Beschreibung

Die Tage der Woche sind nummeriert, beginnend mit 1, wo wird 1 Sonntag angenommen. Gibt den Tag an der `successCallback` mit einem `properties`-Objekt als Parameter zurück. Das Objekt sollte eine `Value`-Eigenschaft mit einem `String`-Wert haben.

Wenn ein Fehler, erhalten das Muster vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.UNKNOWN_ERROR`.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, zeigt dies einen Popup-Dialog mit Text ähnlich `Tag: 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

### Windows-Eigenheiten

*   Für Windows 8.0/8.1 der Wert hängt vom Benutzer "Kalender" Einstellungen ". Auf Windows Phone 8.1 hängt der Wert von aktuellen Gebietsschema.

## navigator.globalization.getNumberPattern

Gibt eine Musterzeichenfolge zum Formatieren und Analysieren von Zahlen nach der Client-Benutzer-Einstellungen.

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### Beschreibung

Gibt das Muster auf der `successCallback` mit einem `properties`-Objekt als Parameter. Dieses Objekt enthält die folgenden Eigenschaften:

*   **pattern**: die Muster zur Formatierung und zum Analysieren von Zahlen. Die Muster folgen [Unicode Technical Standard #35][1]. *(String)*

*   **symbol**: das Symbol beim Formatieren und analysieren, wie ein Prozentsatz oder Symbol verwendet. *(String)*

*   **fraction**: die Anzahl von Bruchziffern zum analysieren und Formatieren von Zahlen verwendet. *(Anzahl)*

*   **rounding**: die Rundung erhöhen wenn analysieren und formatieren verwenden. *(Anzahl)*

*   **positive**: das Symbol für positive Zahlen beim Analysieren und formatieren verwenden. *(String)*

*   **negative**: das Symbol für negative Zahlen beim Analysieren und formatieren verwenden. *(String)*

*   **decimal**: das Dezimaltrennzeichen für analysieren und formatieren. *(String)*

*   **grouping**: das Symbol für Zifferngruppierung zum analysieren und formatieren verwenden. *(String)*

Wenn ein Fehler, erhalten das Muster vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.PATTERN_ERROR`.

Der `options`-Parameter ist optional, und die Standardwerte sind:

    {type:'decimal'}
    

Die `options.type` können `decimal`, `percent` oder `currency` sein.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, sollte dies einen Popup-Dialog mit Text ähnlich wie die Ergebnisse angezeigt werden, die Folgen:

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
    

Ergebnisse:

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 Macken

*   Die `pattern`-Eigenschaft wird nicht unterstützt, und gibt eine leere Zeichenfolge zurück.

*   Die `fraction`-Eigenschaft wird nicht unterstützt und gibt NULL zurück.

### Windows-Eigenheiten

*   Die `pattern`-Eigenschaft wird nicht unterstützt, und gibt eine leere Zeichenfolge zurück.

## navigator.globalization.isDayLightSavingsTime

Gibt an, ob die Sommerzeit ist in der Tat für ein bestimmtes Datum unter Verwendung des Auftraggebers Zeitzone und Kalender.

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### Beschreibung

Gibt an, ob Sommerzeit in Kraft, die `successCallback` mit einem `properties`-Objekt als Parameter ist. Das Objekt sollte eine `dst`-Eigenschaft mit einem `Boolean` Wert aufweisen. Ein Wert von `true` gibt an, dass die Sommerzeit ist in der Tat für das angegebene Datum, und `false` gibt an, dass es nicht.

Die eingehenden Parameter `date` sollte vom Typ `Date` werden.

Wenn gibt es einen Lesefehler das Datum führt dann die `ErrorCallback`. Die erwarteten Fehlercode ist `GlobalizationError.UNKNOWN_ERROR`.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Im Sommer und wenn der Browser auf eine DST-fähigen Zeitzone festgelegt ist, sollte dies einen Popup-Dialog mit Text ähnlich anzeigen `dst: echte`:

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

Gibt eine Zahl, die als Zeichenfolge nach dem Client-Benutzer-Einstellungen formatiert.

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### Beschreibung

Gibt die formatierte Zeichenfolge an die `SuccessCallback` mit einem `Eigenschaften`-Objekt als Parameter zurück. Das Objekt sollte eine `Value`-Eigenschaft mit einem `String`-Wert haben.

Wenn ein Fehler, die Formatierung der Zahl vorliegt, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.FORMATTING_ERROR`.

Der `options`-Parameter ist optional, und die Standardwerte sind:

    {type:'decimal'}
    

Die `options.type` kann "decimal", "percent" oder "currency" sein.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, zeigt dies einen Popup-Dialog mit Text ähnlich `Zahl: 3,142`:

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows-Eigenheiten

*   Windows 8.0 unterstützt nicht die Zahl gerundet, daher Werte werden nicht automatisch gerundet werden.

*   Auf Windows 8.1 und Windows Phone 8.1 Kommastellen statt abgeschnitten ist, bei `percent` Zahl Typ daher Nachkommastellen gerundet wird Graf auf 0 festgelegt.

*   `percent` Zahlen werden nicht gruppiert, wie sie in StringToNumber analysiert werden können, wenn gruppiert.

## navigator.globalization.stringToDate

Analysiert ein Datum formatiert als Zeichenfolge, nach der Client Benutzereinstellungen und Kalender mit der Zeitzone des Clients, und gibt das entsprechende Datumsobjekt zurück.

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### Beschreibung

Gibt das Datum an den Erfolg-Rückruf mit einem `properties`-Objekt als Parameter. Das Objekt sollte folgenden Eigenschaften aufweisen:

*   **year**: die vier Digit Year. *(Anzahl)*

*   **month**: der Monat ab (0-11). *(Anzahl)*

*   **day**: der Tag von (1-31). *(Anzahl)*

*   **hour**: die Stunde (0-23). *(Anzahl)*

*   **minute**: die Minute (0-59). *(Anzahl)*

*   **second**: die zweite von (0-59). *(Anzahl)*

*   **millisecond**: die Millisekunden (von 0-999), nicht auf allen Plattformen verfügbar. *(Anzahl)*

Der eingehende `dateString`-Parameter muss vom Typ `String` sein.

Der `options`-Parameter ist optional und wird standardmäßig auf folgende Werte:

    {formatLength:'short', selector:'date and time'}
    

Die `options.formatLength` kann `short`, `medium`, `long` oder `full` sein. Die `options.selector` können `date`, `time` oder `date and time` werden.

Wenn es ein Fehler beim Analysieren der Datumszeichenfolge ist, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.PARSING_ERROR`.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, wird einen Popup-Dialog mit Text `Monat: 8 Tag: 25 Jahr: 2012` ähnlich angezeigt. Beachten Sie, dass im Monat ganze Zahl ist kleiner als die Zeichenfolge AsInteger Monat stellt einen Array-Index.

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 Macken

*   Die `FormatLength`-Option unterstützt nur `short` und `full` Werte.

*   Das Muster für "date and time" Selektor ist immer eine volle Datetime-Format.

*   Parameters eingehenden `dateString` sollte in Übereinstimmung mit einem Muster von GetDatePattern zurückgegebenen gebildet werden. Dieses Muster kann nicht vollständig mit ICU je nach ein Benutzergebietsschema ausgerichtet werden.

### Windows-Eigenheiten

*   Die `FormatLength`-Option unterstützt nur `short` und `full` Werte.

*   Das Muster für "date and time" Selektor ist immer eine volle Datetime-Format.

*   Parameters eingehenden `dateString` sollte in Übereinstimmung mit einem Muster von GetDatePattern zurückgegebenen gebildet werden. Dieses Muster kann nicht vollständig mit ICU je nach ein Benutzergebietsschema ausgerichtet werden.

## navigator.globalization.stringToNumber

Analysiert eine Zahl als Zeichenfolge nach dem Client-Benutzer-Einstellungen formatiert und gibt die entsprechende Nummer zurück.

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### Beschreibung

Gibt die Anzahl der `successCallback` mit einem `properties`-Objekt als Parameter zurück. Das Objekt sollte eine `Value`-Eigenschaft mit `Number` haben.

Ist ein Fehler beim Analysieren der Zeichenfolge, führt die `ErrorCallback` mit einem `GlobalizationError`-Objekt als Parameter. Die erwarteten Fehlercode ist `GlobalizationError.PARSING_ERROR`.

Der `options`-Parameter ist optional und wird standardmäßig auf folgende Werte:

    {type:'decimal'}
    

Die `options.type` können `decimal`, `percent` oder `currency` sein.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn der Browser auf das `En_US` Gebietsschema festgelegt ist, sollte dies einen Popup-Dialog mit Text ähnlich anzeigen `Zahl: 1234,56`:

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 Macken

*   Bei `percent` Typ wird der zurückgegebene Wert nicht durch 100 dividiert.

### Windows-Eigenheiten

*   Die Zeichenfolge muss streng auf das Gebietsschema-Format entsprechen. Beispielsweise sollten Prozentzeichen werden durch Leerzeichen getrennt für Gebietsschema "En-US" ist der Typparameter 'percent'.

*   `percent` zahlen müssen nicht gruppiert werden, um ordnungsgemäß analysiert werden.

## GlobalizationError

Ein Objekt, das einen Fehler von der Globalisierung-API darstellt.

### Eigenschaften

*   **code**: Einen der folgenden Codes, der den Fehlertyp *(Anzahl)* 
    *   GlobalizationError.UNKNOWN_ERROR: 0
    *   GlobalizationError.FORMATTING_ERROR: 1
    *   GlobalizationError.PARSING_ERROR: 2
    *   GlobalizationError.PATTERN_ERROR: 3
*   **message**: eine SMS-Nachricht, die enthält den Fehler Erklärung und/oder details *(String)*

### Beschreibung

Dieses Objekt ist erstellt und bevölkert von Cordova und kehrte nach einem Rückruf im Fehlerfall.

### Unterstützte Plattformen

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Beispiel

Wenn die folgenden Fehler-Callback ausgeführt wird, zeigt es einen Popup-Dialog mit dem Text ähnlich `Code: 3` und `message:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };
