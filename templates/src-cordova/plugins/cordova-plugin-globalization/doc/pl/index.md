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

Ten plugin uzyskuje informacje i wykonuje operacje specyficzne dla użytkownika ustawienia regionalne, język i strefa czasowa. Zwróć uwagę na różnicę między ustawień regionalnych i językowych: regionalny kontroli jak liczby, daty i godziny są wyświetlane dla regionu, podczas gdy język określa, jaki tekst w języku pojawia się jako, niezależnie od ustawień regionalnych. Często Deweloperzy używają regionalny do zarówno ustawienia, ale nie ma żadnego powodu, które użytkownik nie mógł ustawić jej język "Polski" regionalny "Francuski", tak, że tekst jest wyświetlany w angielski, ale daty, godziny, itp., są wyświetlane są one we Francji. Niestety najbardziej mobilnych platform obecnie nie wprowadzają rozróżnienia tych ustawień.

Ten plugin określa globalne `navigator.globalization` obiektu.

Chociaż w globalnym zasięgu, to nie dostępne dopiero po `deviceready` imprezie.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## Instalacja

    cordova plugin add cordova-plugin-globalization
    

## Obiekty

*   GlobalizationError

## Metody

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

Znacznik języka BCP 47 uzyskać bieżący język klienta.

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### Opis

Zwraca BCP 47 język zgodny Identyfikator tagu do `successCallback` z `properties` obiektu jako parametr. Obiekt powinien mieć `wartość` Właściwość `ciąg`.

Jeśli tu jest błąd w języku, następnie `errorCallback` wykonuje z `GlobalizationError` obiektu jako parametr. Oczekiwany kod błędu to `GlobalizationError.UNKNOWN_ERROR`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiony język `En US`, to należy wyświetlić wyskakujące okno z tekstem `Język: en US`:

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### Dziwactwa Androida

*   Zwraca ISO 639-1 języka dwuliterowy kod, wielkie litery ISO 3166-1 kraj kod i wariant oddzielonych myślnikami. Przykłady: "pl", "pl", "US"

### Windows Phone 8 dziwactwa

*   Zwraca ISO 639-1 dwuliterowy kod języka i kod ISO 3166-1 kraju regionalne wariant odpowiadający "Język" ustawienie, oddzielone myślnikiem.
*   Należy zauważyć, że regionalne wariant jest Właściwość ustawieniem "Language" i nie określona przez ustawienie "Kraj" niepowiązanych na Windows Phone.

### Windows dziwactwa

*   Zwraca ISO 639-1 dwuliterowy kod języka i kod ISO 3166-1 kraju regionalne wariant odpowiadający "Język" ustawienie, oddzielone myślnikiem.

## navigator.globalization.getLocaleName

Zwraca znacznik zgodny z BCP 47 dla klienta bieżące ustawienia regionalne.

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### Opis

Zwraca ciąg identyfikatora regionalny zgodny z BCP 47 `successCallback` z `properties` obiektu jako parametr. Obiekt powinien mieć `wartość` Właściwość `ciąg`. Tag regionalnych będzie się składać z ma³e dwuliterowy kod języka, dwie litery wielkie litery kodu kraju i (nieokreślone) kod wariantu, oddzielone myślnikiem.

Jeśli tu jest błąd ustawienia regionalne, a następnie `errorCallback` wykonuje z `GlobalizationError` obiektu jako parametr. Oczekiwany kod błędu to `GlobalizationError.UNKNOWN_ERROR`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `Pl pl` regionalne, wyświetla okno popup z tekstem `regionalny: en US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Dziwactwa Androida

*   Java nie rozróżnia się między zestaw "language" i ustaw "locale", więc ta metoda jest zasadniczo taka sama, jak `navigator.globalizatin.getPreferredLanguage()`.

### Windows Phone 8 dziwactwa

*   Zwraca ISO 639-1 dwuliterowy kod języka i kod ISO 3166-1 kraju regionalne wariant odpowiednie ustawienie "Format regionalny", oddzielone myślnikiem.

### Windows dziwactwa

*   Regionalny można zmienić w panelu sterowania-> zegar, język i Region-> w regionie-> formaty-> Format i w ustawieniach-> w regionie-> Format regionalny na Windows Phone 8.1.

## navigator.globalization.dateToString

Zwraca daty sformatowane jako ciąg regionalny klient i strefa czasowa.

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### Opis

Zwraca datę sformatowany `ciąg` poprzez `wartość` Właściwość dostępne od obiektu przekazane jako parametr do `successCallback`.

Parametr przychodzący `date` powinny być typu `Date`.

Jeśli występuje błąd formatowania daty, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.FORMATTING_ERROR`.

`Opcje` parametr jest opcjonalny, a jego wartości domyślne są:

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` może być `short`, `medium`, `long` lub `full`.

`options.selector` może być `date`, `time` lub `date and time`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Jeśli przeglądarka jest ustawiona na `pl` regionalne, to wyświetla okno dialogowe popup z tekst podobny do `Data: 9/25/2012 4:21 PM` przy użyciu opcji domyślnych:

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Dziwactwa Androida

*   `formatLength` opcje są podzbiorem Unicode [UTS #35][1]. Domyślnie opcja `Krótki` zależy od użytkownika format daty wybranej w `Ustawienia -> System -> Data i czas -> Wybierz format daty`, które zapewniają wzór `roku` tylko z 4 cyfr, nie 2 cyfry. Oznacza to, że nie jest to całkowicie dostosowane do [ICU][2].

 [1]: http://unicode.org/reports/tr35/tr35-4.html
 [2]: http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US

### Windows Phone 8 dziwactwa

*   Opcja `formatLength` obsługuje tylko `short` i `full` wartości.

*   Wzór dla selektora "date and time" jest zawsze pełna datetime format.

*   Zwracana wartość może być nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

### Windows dziwactwa

*   Opcja `formatLength` obsługuje tylko `short` i `full` wartości.

*   Wzór dla selektora "date and time" jest zawsze pełna datetime format.

*   Zwracana wartość może być nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

### Firefox OS dziwactwa

*   `formatLength` nie jest rozróżnienie, `long` i `full` 
*   tylko jedna metoda wyświetlania daty (nie `long` lub `full` wersja)

## navigator.globalization.getCurrencyPattern

Zwraca ciąg wzór do formatu i analizy wartości walut według preferencji użytkownika klienta i kod waluty ISO 4217.

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### Opis

Zwraca wzór do `successCallback` z `properties` obiektu jako parametr. Obiekt powinien zawierać następujące właściwości:

*   **pattern**: wzór waluty wobec układ graficzny i analizy wartości waluty. Wzory wykonaj [techniczny Standard Unicode #35][1]. *(String)*

*   **code**: kod waluty The ISO 4217 dla wzorca. *(String)*

*   **fraction**: liczba cyfr ułamkowych podczas analizowania i Formatowanie walutowe. *(Liczba)*

*   **rounding**: Zaokrąglenie przyrost podczas analizowania i formatowanie. *(Liczba)*

*   **decimal**: symbolu dziesiętnego używać do analizowania i formatowanie. *(String)*

*   **grouping**: symbol grupowania dla analizy i formatowanie. *(String)*

Parametr przychodzący `currencyCode` powinna być `ciągiem` jednego z kodów ISO 4217 waluty, na przykład "USD".

Jeśli występuje błąd uzyskania wzorzec, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.FORMATTING_ERROR`.

### Obsługiwane platformy

*   Amazon ogień OS
*   Android
*   Jeżyna 10
*   iOS
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne i wybranej waluty dolarów amerykańskich, w tym przykładzie wyświetla wyskakujące okno z tekstem podobne do wyników, które należy wykonać:

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
    

Oczekiwany wynik:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### Windows dziwactwa

*   Obsługiwane są tylko właściwości "code" i "fraction"

## navigator.globalization.getDateNames

Zwraca tablicę nazwy miesięcy i dni tygodnia, w zależności od preferencji użytkownika klienta i kalendarz.

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### Opis

Zwraca tablicę nazw do `successCallback` z `properties` obiektu jako parametr. Ten obiekt zawiera właściwość `wartość` z `tablicy` wartości `ciąg`. Nazwy funkcji Tablica albo od pierwszego miesiąca w roku lub pierwszego dnia tygodnia, w zależności od wybranej opcji.

Jeśli występuje błąd uzyskiwania nazwy, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.UNKNOWN_ERROR`.

`options` parametr jest opcjonalny, a jego wartości domyślne są:

    {type:'wide', item:'months'}
    

Wartość `options.type` może być `narrow` lub `wide`.

Wartość `options.item` może być `months` lub `days`.

### Obsługiwane platformy

*   Amazon ogień OS
*   Android
*   Jeżyna 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl_PL` ustawień regionalnych, w tym przykładzie wyświetla serię dwunastu lud dialogi, jeden raz na miesiąc, tekst podobny do `miesiąca: stycznia`:

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### Firefox OS dziwactwa

*   `options.type` obsługuje wartość `genitive`, ważne dla niektórych języków

### Windows Phone 8 dziwactwa

*   Szereg miesięcy zawiera 13 elementów.
*   Zwróconej tablicy może nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

### Windows dziwactwa

*   Szereg miesięcy zawiera 12 elementów.
*   Zwróconej tablicy może nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

## navigator.globalization.getDatePattern

Zwraca ciąg wzór do formatu i analizy dat według preferencji użytkownika klienta.

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### Opis

Zwraca wzór do `successCallback`. Obiekt przekazywana jako parametr zawiera następujące właściwości:

*   **pattern**: data i godzina wzór do formatu i analizować daty. Wzory wykonaj [techniczny Standard Unicode #35][1]. *(String)*

*   **timezone**: skróconą nazwę strefy czasowej na klienta. *(String)*

*   **utc_offset**: aktualna różnica w sekundach między klienta strefy czasowej i skoordynowanego czasu uniwersalnego. *(Liczba)*

*   **dst_offset**: bieżącego przesunięcie czasu w sekundach między klienta nie uwzględniaj w strefę czasową i klienta światło dzienne oszczędności w strefa czasowa. *(Liczba)*

Jeśli występuje błąd uzyskiwania wzór, `errorCallback` wykonuje się z obiektem `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.PATTERN_ERROR`.

Parametr `options` jest opcjonalne i domyślnie następujące wartości:

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` może być `short`, `medium`, `long` lub `full`. `options.selector` może być `date`, `time` lub `date and time`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne, w tym przykładzie wyświetla lud dialog z tekstu takie jak `wzór: za/rrrr g: mm`:

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 dziwactwa

*   Opcja `formatLength` obsługuje tylko `short` i `full` wartości.

*   `pattern` dla `date and time` wzór zwraca tylko pełne datetime format.

*   `timezone` zwraca nazwę strefy w pełnym wymiarze czasu.

*   Właściwość `dst_offset` nie jest obsługiwany, a zawsze zwraca zero.

*   Wzór może nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

### Windows dziwactwa

*   Opcja `formatLength` obsługuje tylko `short` i `full` wartości.

*   `pattern` dla `date and time` wzór zwraca tylko pełne datetime format.

*   `timezone` zwraca nazwę strefy w pełnym wymiarze czasu.

*   Właściwość `dst_offset` nie jest obsługiwany, a zawsze zwraca zero.

*   Wzór może nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

## navigator.globalization.getFirstDayOfWeek

Zwraca pierwszy dzień tygodnia według kalendarza i preferencje użytkownika klienta.

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### Opis

Dni tygodnia są numerowane począwszy od 1, gdzie 1 zakłada się niedziela. Zwraca dzień do `successCallback` z `properties` obiektu jako parametr. Obiekt powinien mieć `wartość` Właściwość z wartością `liczby`.

Jeśli występuje błąd uzyskania wzorzec, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.UNKNOWN_ERROR`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne, wyświetla okno popup z tekst podobny do `dzień: 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

### Windows dziwactwa

*   Na Windows 8.0/8.1 wartości zależy od użytkownika "Kalendarz preferencje. Na Windows Phone 8.1 wartości zależy od bieżących ustawień regionalnych.

## navigator.globalization.getNumberPattern

Zwraca ciąg wzór do formatu i analizować liczby preferencji użytkownika klienta.

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### Opis

Zwraca wzór do `successCallback` z `Właściwości` obiektu jako parametr. Ten obiekt zawiera następujące właściwości:

*   **pattern**: wzorzec numeru do formatu i analizowania liczb. Wzory wykonaj [techniczny Standard Unicode #35][1]. *(String)*

*   **symbol**: symbolem podczas formatowania i analizy, takie jak procent lub waluta symbol. *(String)*

*   **fraction**: liczba cyfr ułamkowych podczas analizowania i Formatowanie walutowe. *(Liczba)*

*   **rounding**: Zaokrąglenie przyrost podczas analizowania i formatowanie. *(Liczba)*

*   **positive**: symbol dla liczb dodatnich, gdy formatowanie i analizy. *(String)*

*   **negative**: symbol liczb ujemnych podczas analizowania i formatowanie. *(String)*

*   **decimal**: symbolu dziesiętnego używać do analizowania i formatowanie. *(String)*

*   **grouping**: symbol grupowania dla analizy i formatowanie. *(String)*

Jeśli występuje błąd uzyskania wzorzec, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.PATTERN_ERROR`.

`options` parametr jest opcjonalny, a wartości domyślne są:

    {type:'decimal'}
    

`Options.type` może być `decimal`, `percent` lub `currency`.

### Obsługiwane platformy

*   Amazon ogień OS
*   Android
*   Jeżyna 10
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne, to należy wyświetlić wyskakujące okno z tekstem podobne do wyników, które należy wykonać:

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
    

Wyniki:

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 dziwactwa

*   Właściwość `pattern` nie jest obsługiwane i zwraca pusty ciąg.

*   `fraction` Właściwość nie jest obsługiwany i zwraca zero.

### Windows dziwactwa

*   Właściwość `pattern` nie jest obsługiwane i zwraca pusty ciąg.

## navigator.globalization.isDayLightSavingsTime

Wskazuje, czy czas letni jest obowiązująca dla danej daty za pomocą klienta strefy czasowej i kalendarz.

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### Opis

Wskazuje, czy czas letni jest w efekcie do `successCallback` z `properties` obiektu jako parametr. Obiekt powinien mieć wartość `Boolean` Właściwość `dst`. Wartość `true` wskazuje, że czas letni jest obowiązującą w danym dniu, a `wartość false` wskazuje, że to nie jest.

Przychodzące parametr `date` powinny być typu `Date`.

Jeśli występuje błąd odczytu daty, a następnie wykonuje `errorCallback`. Oczekiwany kod błędu to `GlobalizationError.UNKNOWN_ERROR`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

W okresie letnim i jeśli przeglądarka jest ustawiona na timezone DST-włączone, to należy wyświetlić wyskakujące okno z tekstem podobne do `dst: prawdziwe`:

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

Zwraca liczby sformatowane jako ciąg preferencji użytkownika klienta.

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### Opis

Zwraca sformatowany ciąg liczb do `successCallback` z `properties` obiektu jako parametr. Obiekt powinien mieć `wartość` Właściwość `ciąg`.

Jeśli występuje błąd formatowanie numeru, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.FORMATTING_ERROR`.

`options` parametr jest opcjonalny, a jego wartości domyślne są:

    {type:'decimal'}
    

`options.type` może być "decimal", "percent" lub "currency".

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne, wyświetla okno popup z tekst podobny do `numer: 3.142`:

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows dziwactwa

*   8.0 systemu Windows nie obsługuje zaokrąglania liczb, więc wartości nie będzie być zaokrąglane automatycznie.

*   Windows 8.1 i Windows Phone 8.1 część ułamkowa jest obcinany zamiast zaokrąglone w przypadku `procent` liczby typu dlatego ułamkowe cyfr licznika jest równa 0.

*   `percent` liczby nie są pogrupowane, jak nie można analizować w stringToNumber, jeśli zgrupowane.

## navigator.globalization.stringToDate

Analizuje daty sformatowane jako ciąg, według preferencji użytkownika i strefa czasowa klient, kalendarz klienta i zwraca odpowiedni obiekt date.

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### Opis

Zwraca datę do sukcesu wywołanie zwrotne z `Właściwości` obiektu jako parametr. Obiekt powinien mieć następujące właściwości:

*   **year**: rok czterocyfrowy. *(Liczba)*

*   **month**: miesiąc od (0-11). *(Liczba)*

*   **day**: dzień z (1-31). *(Liczba)*

*   **hour**: godzina od (0-23). *(Liczba)*

*   **minute**: odległości od (0-59). *(Liczba)*

*   **second**: drugi od (0-59). *(Liczba)*

*   **milisecond**: milisekund (od 0-999), nie jest dostępna na wszystkich platformach. *(Liczba)*

Parametr przychodzący `dateString` powinny być typu `String`.

Parametr `options` jest opcjonalne i domyślnie następujące wartości:

    {formatLength:'short', selector:'date and time'}
    

`options.formatLength` może być `short`, `medium`, `long` lub `full`. `options.selector` może być `date`, `time` lub `date and time`.

Jeśli występuje błąd podczas analizowania ciągu daty, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.PARSING_ERROR`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne, to wyświetla wyskakujące okno z tekstem podobne do `miesiąca: 8 dzień: 25 rok: 2012`. Należy zauważyć, że miesiąc, liczba całkowita jest jeden mniej niż ciąg, jako miesiąc liczba całkowita reprezentuje indeks tablicy.

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 dziwactwa

*   Opcja `formatLength` obsługuje tylko `short` i `full` wartości.

*   Wzór dla selektora "date and time" jest zawsze pełna datetime format.

*   Parametr przychodzący `dateString` powinna zostać utworzona zgodnie z wzorcem, zwrócony przez getDatePattern. Ten wzór może być nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

### Windows dziwactwa

*   Opcja `formatLength` obsługuje tylko `short` i `full` wartości.

*   Wzór dla selektora "date and time" jest zawsze pełna datetime format.

*   Parametr przychodzący `dateString` powinna zostać utworzona zgodnie z wzorcem, zwrócony przez getDatePattern. Ten wzór może być nie całkowicie dostosowane z ICU w zależności od ustawienia regionalne użytkownika.

## navigator.globalization.stringToNumber

Analizuje liczby sformatowane jako ciąg preferencji użytkownika klienta i zwraca odpowiedni numer.

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### Opis

Zwraca liczbę do `successCallback` z `properties` obiektu jako parametr. Obiekt powinien mieć `wartość` Właściwość z wartością `liczby`.

Jeśli występuje błąd podczas analizowania ciągu liczb, a następnie `errorCallback` wykonuje z obiektu `GlobalizationError` jako parametr. Oczekiwany kod błędu to `GlobalizationError.PARSING_ERROR`.

Parametr `options` jest opcjonalne i domyślnie następujące wartości:

    {type:'decimal'}
    

`Options.type` może być `decimal`, `percent` lub `currency`.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy przeglądarka jest ustawiona na `pl` regionalne, to należy wyświetlić wyskakujące okno z tekstem podobne do `numer: 1234.56`:

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 dziwactwa

*   W przypadku `percent` typ zwracanej wartości jest nie dzielony przez 100.

### Windows dziwactwa

*   Ciąg musi ściśle odpowiadać format ustawień regionalnych. Na przykład symbol procentu powinny być oddzielone przez miejsce na "en US" ustawienia regionalne, jeśli typ parametru jest "procent".

*   `percent` liczby nie muszą być zgrupowane do być analizowany poprawnie.

## GlobalizationError

Obiekt reprezentujący błąd z API globalizacji.

### Właściwości

*   **code**: Jeden z następujących kodów oznaczających typ błędu *(Liczba)* 
    *   GlobalizationError.UNKNOWN_ERROR: 0
    *   GlobalizationError.FORMATTING_ERROR: 1
    *   GlobalizationError.PARSING_ERROR: 2
    *   GlobalizationError.PATTERN_ERROR: 3
*   **message**: komunikatu tekstowego, który zawiera wyjaśnienie błędu lub szczegóły *(String)*

### Opis

Ten obiekt jest tworzona i wypełniane przez Cordova i wrócił do wywołania zwrotnego w przypadku błędu.

### Obsługiwane platformy

*   Amazon Fire OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Przykład

Gdy błąd wywołania zwrotnego następujące wykonuje, wyświetla okno popup z tekst podobny do `kod: 3` i `wiadomość:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };
