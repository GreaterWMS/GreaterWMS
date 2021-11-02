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

Questo plugin ottiene informazioni ed esegue operazioni specifiche impostazioni locali dell'utente, lingua e fuso orario. Si noti la differenza tra lingua e impostazioni internazionali: controlli delle impostazioni internazionali, numeri, date e tempi di visualizzazione per una regione, mentre la lingua determina quale testo di lingua appare come, indipendentemente dalle impostazioni locali. Spesso gli sviluppatori utilizzano impostazioni locali per impostare entrambe le impostazioni, ma non non c'è alcun motivo per che un utente non poteva impostare la lingua "Inglese" ma locale alla "Francese", così che il testo viene visualizzato in inglese ma le date, tempi, ecc., vengono visualizzati come sono in Francia. Purtroppo, piattaforme mobili più attualmente non fanno una distinzione tra queste impostazioni.

Questo plugin definisce oggetto global `navigator.globalization`.

Anche se in ambito globale, non è disponibile fino a dopo l'evento `deviceready`.

    document.addEventListener("deviceready", onDeviceReady, false);
    function onDeviceReady() {
        console.log(navigator.globalization);
    }
    

## Installazione

    cordova plugin add cordova-plugin-globalization
    

## Oggetti

*   GlobalizationError

## Metodi

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

Ottenere il tag di lingua BCP 47 per la lingua corrente del client.

    navigator.globalization.getPreferredLanguage(successCallback, errorCallback);
    

### Descrizione

Restituisce l'etichetta di identificatore di linguaggio compatibile con BCP-47 per il `successCallback` con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere una `value` di proprietà con un valore di `String`.

Se c'è un errore nell'acquisizione della lingua, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.UNKNOWN_ERROR`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per la lingua `En-US`, questo dovrebbe visualizzare una finestra di dialogo pop-up con il testo `lingua: en-US`:

    navigator.globalization.getPreferredLanguage(
        function (language) {alert('language: ' + language.value + '\n');},
        function () {alert('Error getting language\n');}
    );
    

### Stranezze Android

*   Restituisce il codice di due lettere della lingua 639-1 ISO, maiuscolo ISO 3166-1 prefisso e variante separati da trattini. Esempi: "en", "en-US", "US"

### Windows Phone 8 stranezze

*   Codice restituisce l'ISO 639-1 due lettere della lingua e il codice ISO 3166-1 paese della variante regionale corrispondente alla "Lingua" impostazione, separati da un trattino.
*   Si noti che la variante regionale è una proprietà di impostazione "Language" e non determinato dall'impostazione del "Paese" indipendente su Windows Phone.

### Stranezze di Windows

*   Codice restituisce l'ISO 639-1 due lettere della lingua e il codice ISO 3166-1 paese della variante regionale corrispondente alla "Lingua" impostazione, separati da un trattino.

## navigator.globalization.getLocaleName

Restituisce il tag compatibile con BCP 47 per impostazione locale corrente del client.

    navigator.globalization.getLocaleName(successCallback, errorCallback);
    

### Descrizione

Restituisce la stringa dell'identificatore locale conforme BCP 47 il `successCallback` con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere una `Value` di proprietà con un valore di `String`. L'etichetta locale sarà costituito da un codice di due lettere minuscole lingua, codice paese di due lettere maiuscole e codice variante (non specificato), separati da un trattino.

Se c'è un errore nell'acquisizione della lingua, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.UNKNOWN_ERROR`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni internazionali `En-US`, questa viene visualizzata una finestra popup con il testo `impostazioni internazionali: en-US`.

    navigator.globalization.getLocaleName(
        function (locale) {alert('locale: ' + locale.value + '\n');},
        function () {alert('Error getting locale\n');}
    );
    

### Stranezze Android

*   Java non fa distinzione tra un set "language" e impostare "locale", quindi questo metodo è essenzialmente lo stesso di `navigator.globalization.getPreferredLanguage()`.

### Windows Phone 8 stranezze

*   Codice restituisce l'ISO 639-1 due lettere della lingua e il codice ISO 3166-1 paese della variante regionale corrispondente all'impostazione "Formato regionale", separato da un trattino.

### Stranezze di Windows

*   Impostazioni locali possono essere modificata nel pannello di controllo-> orologio, lingua e regione-> regione-> formati-> formato e nelle impostazioni-> regione-> formato regionale su Windows Phone 8.1.

## navigator.globalization.dateToString

Restituisce una data formattata come stringa secondo le impostazioni locali del client e fuso orario.

    navigator.globalization.dateToString(date, successCallback, errorCallback, options);
    

### Descrizione

Restituisce la data formattata `String` tramite una proprietà di `value` accessibile dall'oggetto passato come parametro per la `successCallback`.

Il parametro in ingresso `date` dovrebbe essere di tipo `Date`.

Se c'è un errore nell'acquisizione della lingua, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.FORMATTING_ERROR`.

Il parametro `options` è opzionale, e valori predefiniti sono:

    {formatLength:'short', selector:'date and time'}
    

Il `options.formatLength` può essere `breve`, `medium`, `long` o `full`.

Il `options.selector` può essere `date`, `time` o `date e time`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Se il browser è impostato per le impostazioni locali `en_US`, questa viene visualizzata una finestra di popup con testo simile a `Data: 25/09/2012 16:21` utilizzando le opzioni di default:

    navigator.globalization.dateToString(
        new Date(),
        function (date) { alert('date: ' + date.value + '\n'); },
        function () { alert('Error getting dateString\n'); },
        { formatLength: 'short', selector: 'date and time' }
    );
    

### Stranezze Android

*   `formatLength` opzioni sono un sottoinsieme di Unicode [UTS #35][1]. Il `short` predefinito opzione dipende dal formato di data selezionata un utente all'interno `Impostazioni -> sistema -> Data & ora -> Scegli formato data`, che forniscono un modello `anno` solo con 4 cifre, non 2 cifre. Ciò significa che esso non è completamente allineato con [ICU][2].

 [1]: http://unicode.org/reports/tr35/tr35-4.html
 [2]: http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US

### Windows Phone 8 stranezze

*   L'opzione `formatLength` supporta solo valori `short` e `full`.

*   Il modello per selettore 'data e ora' è sempre un formato datetime completo.

*   Il valore restituito può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

### Stranezze di Windows

*   L'opzione `formatLength` supporta solo valori `short` e `full`.

*   Il modello per selettore 'data e ora' è sempre un formato datetime completo.

*   Il valore restituito può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

### Firefox OS stranezze

*   `formatLength` non è distinguere `long` e `full` 
*   solo un metodo di visualizzazione data (nessuna versione `long` o `full`)

## navigator.globalization.getCurrencyPattern

Restituisce una stringa per formattare e analizzare i valori di valuta secondo le preferenze dell'utente e il codice ISO 4217 del client.

     navigator.globalization.getCurrencyPattern(currencyCode, successCallback, errorCallback);
    

### Descrizione

Restituisce il modello per la `successCallback` con un oggetto di `properties` come parametro. Tale oggetto deve contenere le seguenti proprietà:

*   **pattern**: il modello valuta per formattare e analizzare i valori di valuta. I modelli seguono [Unicode Technical Standard #35][1]. *(String)*

*   **code**: codice per il modello The ISO 4217. *(String)*

*   **fraction**: il numero di cifre da utilizzare durante l'analisi e la formattazione valuta. *(Numero)*

*   **rounding**: l'arrotondamento incrementare per utilizzare quando l'analisi e la formattazione. *(Numero)*

*   **decimal**: il simbolo decimale da utilizzare per l'analisi e la formattazione. *(String)*

*   **grouping**: il raggruppamento simbolo da utilizzare per l'analisi e la formattazione. *(String)*

Il parametro in ingresso `currencyCode` deve essere una `String` di uno dei codici valuta ISO 4217, ad esempio 'USD'.

Se c'è un errore nell'acquisizione della lingua, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.FORMATTING_ERROR`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US` e la valuta selezionata è dollari degli Stati Uniti, in questo esempio viene visualizzata una finestra di popup con testo simile ai risultati che seguono:

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
    

Risultato atteso:

    pattern: $#,##0.##;($#,##0.##)
    code: USD
    fraction: 2
    rounding: 0
    decimal: .
    grouping: ,
    

### Stranezze di Windows

*   Sono supportate solo le proprietà 'code' e 'fraction'

## navigator.globalization.getDateNames

Restituisce una matrice di nomi di mesi o giorni della settimana, a seconda delle preferenze dell'utente del client e calendario.

    navigator.globalization.getDateNames(successCallback, errorCallback, options);
    

### Descrizione

Restituisce la matrice di nomi per la `successCallback` con un oggetto di `properties` come parametro. Tale oggetto contiene una `value` di proprietà con una `Array` di valori `String`. I nomi di funzioni matrice a partire da entrambi il primo mese dell'anno o il primo giorno della settimana, a seconda dell'opzione selezionata.

Se c'è un errore nell'acquisizione della lingua, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.UNKNOWN_ERROR`.

Il parametro `options` è opzionale, e valori predefiniti sono:

    {type:'wide', item:'months'}
    

Il valore di `options.type` può essere `narrow` o `wide`.

Il valore di `options.item` può essere di `months` o `days`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, questo esempio visualizza una serie di dodici finestre pop-up, uno al mese, con un testo simile a `mese: gennaio`:

    navigator.globalization.getDateNames(
        function (names) {
            for (var i = 0; i < names.value.length; i++) {
                alert('month: ' + names.value[i] + '\n');
            }
        },
        function () { alert('Error getting names\n'); },
        { type: 'wide', item: 'months' }
    );
    

### Firefox OS stranezze

*   `options.Type` supporta un valore di `genitive`, importante per alcune lingue

### Windows Phone 8 stranezze

*   La matrice di mesi contiene 13 elementi.
*   Il valore restituito può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

### Stranezze di Windows

*   La matrice di mesi contiene 12 elementi.
*   La matrice restituita può essere non completamente allineata con ICU a seconda delle impostazioni locali dell'utente.

## navigator.globalization.getDatePattern

Restituisce una stringa per formattare e analizzare i dati secondo le preferenze dell'utente del client.

    navigator.globalization.getDatePattern(successCallback, errorCallback, options);
    

### Descrizione

Restituisce il modello di `successCallback`. L'oggetto passato come parametro contiene le seguenti proprietà:

*   **pattern**: il modello di data e ora per formattare e analizzare i dati. I modelli seguono [Unicode Technical Standard #35][1]. *(String)*

*   **timezone**: il nome abbreviato del fuso orario sul client. *(String)*

*   **utc_offset**: l'attuale differenza in secondi tra del client fuso orario e tempo universale coordinato. *(Numero)*

*   **dst_offset**: l'offset corrente ora legale in secondi tra non-legale del client di fuso orario e ora legale del cliente risparmio di fuso orario. *(Numero)*

Se c'è un errore per ottenere il modello, il `errorCallback` viene eseguito con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.PATTERN_ERROR`.

Il parametro `options` è facoltativo e di default per i seguenti valori:

    {formatLength:'short', selector:'date and time'}
    

Il `options.formatLength` può essere `short`, `medium`, `long` o `full`. Il `options.selector` può essere `date`, `time` o `date e time`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, in questo esempio viene visualizzata una finestra di popup con il testo come `modello: gg/mm/aaaa h:mm un`:

    function checkDatePattern() {
        navigator.globalization.getDatePattern(
            function (date) { alert('pattern: ' + date.pattern + '\n'); },
            function () { alert('Error getting pattern\n'); },
            { formatLength: 'short', selector: 'date and time' }
        );
    }
    

### Windows Phone 8 stranezze

*   L'opzione `formatLength` supporta solo valori `short` e `full`.

*   Il `pattern` per modello di `date e time` restituisce solo il formato datetime completo.

*   Il `timezone` restituisce il nome della zona a tempo pieno.

*   La proprietà `dst_offset` non è supportata e restituisce sempre zero.

*   Il modello può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

### Stranezze di Windows

*   `FormatLength` supporta solo valori `brevi` e `completo`.

*   Il `pattern` per modello di `data e time` restituisce solo il formato datetime completo.

*   Il `timezone` restituisce il nome della zona a tempo pieno.

*   La proprietà `dst_offset` non è supportata e restituisce sempre zero.

*   Il modello può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

## navigator.globalization.getFirstDayOfWeek

Restituisce il primo giorno della settimana secondo le preferenze dell'utente del client e calendario.

    navigator.globalization.getFirstDayOfWeek(successCallback, errorCallback);
    

### Descrizione

I giorni della settimana sono numerati a partire da 1, dove 1 è presupposto per essere domenica. Restituisce il giorno del `successCallback` con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere una `valore` di proprietà con un valore di `Number`.

Se c'è un errore per ottenere il modello, quindi il `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.UNKNOWN_ERROR`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, questa viene visualizzata una finestra di popup con testo simile al `giorno: 1`.

    navigator.globalization.getFirstDayOfWeek(
        function (day) {alert('day: ' + day.value + '\n');},
        function () {alert('Error getting day\n');}
    );
    

### Stranezze di Windows

*   Su Windows 8.0/8.1 il valore dipende dall'utente ' preferenze di calendario. Su Windows Phone 8.1 il valore dipende dalle impostazioni locali correnti.

## navigator.globalization.getNumberPattern

Restituisce una stringa per formattare e analizzare i numeri secondo le preferenze dell'utente del client.

    navigator.globalization.getNumberPattern(successCallback, errorCallback, options);
    

### Descrizione

Restituisce il modello per la `successCallback` con un oggetto di `properties` come parametro. Tale oggetto contiene le seguenti proprietà:

*   **pattern**: il modello del numero per formattare e analizzare i numeri. I modelli seguono [Unicode Technical Standard #35][1]. *(String)*

*   **symbol**: il simbolo da utilizzare durante la formattazione e l'analisi, come un simbolo di percentuale o valuta. *(String)*

*   **fraction**: il numero di cifre da utilizzare durante l'analisi e la formattazione valuta. *(Numero)*

*   **rounding**: l'arrotondamento incrementare per utilizzare quando l'analisi e la formattazione. *(Numero)*

*   **positive**: il simbolo da utilizzare per i numeri positivi quando l'analisi e la formattazione. *(String)*

*   **negative**: il simbolo da utilizzare per i numeri negativi quando l'analisi e la formattazione. *(String)*

*   **decimal**: il simbolo decimale da utilizzare per l'analisi e la formattazione. *(String)*

*   **grouping**: il raggruppamento simbolo da utilizzare per l'analisi e la formattazione. *(String)*

Se c'è un errore nell'acquisizione della lingua, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.PATTERN_ERROR`.

Il parametro `options` è opzionale, e i valori predefiniti sono:

    {type:'decimal'}
    

Il `options.type` può essere `decimal`, `percent` o `currency`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, questo dovrebbe visualizzare una finestra di popup con testo simile ai risultati che seguono:

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
    

Risultati:

    pattern: #,##0.###
    symbol: .
    fraction: 0
    rounding: 0
    positive:
    negative: -
    decimal: .
    grouping: ,
    

### Windows Phone 8 stranezze

*   La proprietà `pattern` non è supportata e restituisce una stringa vuota.

*   La `fraction` di proprietà non è supportata e restituisce zero.

### Stranezze di Windows

*   La proprietà `pattern` non è supportata e restituisce una stringa vuota.

## navigator.globalization.isDayLightSavingsTime

Indica se l'ora legale è in vigore per una data specifica utilizzando del client fuso orario e calendario.

    navigator.globalization.isDayLightSavingsTime(date, successCallback, errorCallback);
    

### Descrizione

Indica se è o meno dell'ora legale in vigore per il `successCallback` con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere una proprietà di `dst` con un valore `Boolean`. Un valore `true` indica che l'ora legale è in vigore per la data specificata, e `false` indica che non è.

Il parametro in ingresso `Date` dovrebbe essere di tipo `Date`.

Se c'è un errore di lettura della data, quindi esegue il `errorCallback`. Previsto codice dell'errore è `GlobalizationError.UNKNOWN_ERROR`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Durante l'estate, e se il browser è impostato su un fuso orario abilitato DST, questo dovrebbe visualizzare una finestra di popup con testo simile a `dst: true`:

    navigator.globalization.isDayLightSavingsTime(
        new Date(),
        function (date) {alert('dst: ' + date.dst + '\n');},
        function () {alert('Error getting names\n');}
    );
    

## navigator.globalization.numberToString

Restituisce un numero formattato come una stringa secondo le preferenze dell'utente del client.

    navigator.globalization.numberToString(number, successCallback, errorCallback, options);
    

### Descrizione

Restituisce la stringa di numeri formattata per la `successCallback` con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere una `value` di proprietà con un valore di `String`.

Se c'è un errore di formattazione del numero, quindi il `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.FORMATTING_ERROR`.

Il parametro `options` è opzionale, e valori predefiniti sono:

    {type:'decimal'}
    

Il `options.type` può essere 'decimal', 'percent' o 'currency'.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, questa viene visualizzata una finestra di popup con testo simile a `numero: 3.142`:

    navigator.globalization.numberToString(
        3.1415926,
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Stranezze di Windows

*   8.0 Windows non supporta l'arrotondamento del numero, quindi i valori non è arrotondati automaticamente.

*   8.1 di Windows e Windows Phone 8.1 parte frazionaria è troncamento anziché arrotondato le cifre numero tipo pertanto frazionarie `percento` in caso di conteggio è impostato su 0.

*   `percent` non raggruppare i numeri come non può essere analizzati in stringToNumber se raggruppati.

## navigator.globalization.stringToDate

Analizza una data formattata come stringa, secondo le preferenze dell'utente e calendario utilizzando il fuso orario del cliente, il cliente e restituisce l'oggetto data corrispondente.

    navigator.globalization.stringToDate(dateString, successCallback, errorCallback, options);
    

### Descrizione

Restituisce la data per il callback di successo con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere le seguenti proprietà:

*   **year**: l'anno a quattro cifre. *(Numero)*

*   **month**: mese da (0-11). *(Numero)*

*   **day**: il giorno da (1-31). *(Numero)*

*   **hour**: l'ora (0-23). *(Numero)*

*   **minute**: il minuto da (0-59). *(Numero)*

*   **second**: il secondo da (0-59). *(Numero)*

*   **millisecond**: I millisecondi (da 0-999), non disponibili su tutte le piattaforme. *(Numero)*

Il parametro in ingresso `dateString` deve essere di tipo `String`.

Il parametro `options` è facoltativo e di default per i seguenti valori:

    {formatLength:'short', selector:'date and time'}
    

Il `options.formatLength` può essere `short`, `medium`, `long` o `full`. Il `options.selector` può essere `date`, `time` o `date e time`.

Se c'è un errore di parsing della stringa data, quindi la `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.PARSING_ERROR`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, questa viene visualizzata una finestra di popup con testo simile al `mese: 8 giorno: 25 anno: 2012`. Si noti che il mese intero è uno minore di stringa, come l'intero mese rappresenta un indice di matrice.

    navigator.globalization.stringToDate(
        '9/25/2012',
        function (date) {alert('month:' + date.month +
                               ' day:'  + date.day   +
                               ' year:' + date.year  + '\n');},
        function () {alert('Error getting date\n');},
        {selector: 'date'}
    );
    

### Windows Phone 8 stranezze

*   L'opzione `formatLength` supporta solo valori `short` e `full`.

*   Il modello per selettore 'data e ora' è sempre un formato datetime completo.

*   Il parametro in ingresso `dateString` dovrebbe essere formato nel rispetto di un modello restituito da getDatePattern. Questo modello può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

### Stranezze di Windows

*   L'opzione `formatLength` supporta solo valori `short` e `full`.

*   Il modello per selettore 'data e ora' è sempre un formato datetime completo.

*   Il parametro in ingresso `dateString` dovrebbe essere formato nel rispetto di un modello restituito da getDatePattern. Questo modello può essere non completamente allineato con ICU a seconda delle impostazioni locali dell'utente.

## navigator.globalization.stringToNumber

Analizza un numero formattato come una stringa secondo le preferenze dell'utente del client e restituisce il numero corrispondente.

    navigator.globalization.stringToNumber(string, successCallback, errorCallback, options);
    

### Descrizione

Restituisce il numero del `successCallback` con un oggetto di `properties` come parametro. Tale oggetto dovrebbe avere una `valore` di proprietà con un valore di `numero`.

Se c'è un errore di parsing della stringa di numeri, quindi il `errorCallback` viene eseguita con un oggetto `GlobalizationError` come parametro. Previsto codice dell'errore è `GlobalizationError.PARSING_ERROR`.

Il parametro `options` è facoltativo e di default per i seguenti valori:

    {type:'decimal'}
    

Il `options.type` può essere `decimal`, `percent` o `currency`.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando il browser è impostato per le impostazioni locali `en_US`, questo dovrebbe visualizzare una finestra di popup con testo simile a `numero: 1234.56`:

    navigator.globalization.stringToNumber(
        '1234.56',
        function (number) {alert('number: ' + number.value + '\n');},
        function () {alert('Error getting number\n');},
        {type:'decimal'}
    );
    

### Windows Phone 8 stranezze

*   In caso di tipo `percent` il valore restituito non è diviso per 100.

### Stranezze di Windows

*   La stringa deve essere conforme rigorosamente nel formato delle impostazioni locali. Ad esempio, simbolo di percentuale dovrebbe essere separato da spazio per impostazioni locali 'en-US' se il parametro di tipo è 'percent'.

*   numeri `percent` non devono essere raggruppati per essere analizzato correttamente.

## GlobalizationError

Un oggetto che rappresenta un errore dall'API di globalizzazione.

### Proprietà

*   **code**: Uno dei seguenti codici che rappresenta il tipo di errore *(Numero)* 
    *   GlobalizationError.UNKNOWN_ERROR: 0
    *   GlobalizationError.FORMATTING_ERROR: 1
    *   GlobalizationError.PARSING_ERROR: 2
    *   GlobalizationError.PATTERN_ERROR: 3
*   **message**: un messaggio di testo che include la spiegazione dell'errore e/o dettagli *(String)*

### Descrizione

Questo oggetto è creato e popolato da Cordova e restituito una richiamata in caso di errore.

### Piattaforme supportate

*   Amazon fuoco OS
*   Android
*   BlackBerry 10
*   Firefox OS
*   iOS
*   Windows Phone 8
*   Windows

### Esempio

Quando si esegue il callback di errore seguenti, esso viene visualizzata una finestra popup con il testo simile a `code: 3` e `message:`

    function errorCallback(error) {
        alert('code: ' + error.code + '\n' +
              'message: ' + error.message + '\n');
    };
