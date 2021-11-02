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

Ce plugin obtienne des informations et effectue des opérations spécifiques aux paramètres régionaux de l'utilisateur, la langue et fuseau horaire. Notez la différence entre les paramètres régionaux et linguistiques : contrôles de paramètres régionaux comment nombres, les dates et les heures sont affichées pour une région, tandis que la langue détermine quel texte apparaît sous la forme, indépendamment des paramètres régionaux. Souvent les développeurs utilisent des paramètres régionaux pour définir ces deux paramètres, mais il n'y a aucune raison, qu'un utilisateur ne pouvait pas régler sa langue sur « English », mais en paramètres régionaux « Français », afin que le texte s'affiche en anglais mais dates, heures, etc., s'affichent comme ils sont en France. Malheureusement, les plateformes mobiles plus actuellement ne font pas une distinction entre ces paramètres.

Ce plugin définit global `navigator.globalization` objet.

Bien que dans la portée globale, il n'est pas disponible jusqu'après la `deviceready` événement.

    document.addEventListener (« deviceready », onDeviceReady, false) ;
    function onDeviceReady() {console.log(navigator.globalization);}
    

## Installation

    cordova plugin add cordova-plugin-globalization
    

## Objets

  * GlobalizationError

## Méthodes

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

Obtenir la balise de langue BCP 47 pour la langue du client actuel.

    navigator.globalization.getPreferredLanguage (successCallback, errorCallback) ;
    

### Description

Retourne la balise d'identificateur de langage compatible BCP-47 à la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit avoir une `value` propriété avec une `String` valeur.

S'il y a une erreur d'obtention de la langue, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.UNKNOWN_ERROR`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour le `en-US` langue, cela devrait afficher une boîte de dialogue contextuelle avec le texte `language: en-US` :

    navigator.globalization.getPreferredLanguage (fonction (langue) {alert ("langue:" + language.value + « \n »);}, function () {alert ('erreur d'obtention language\n');}) ;
    

### Quirks Android

  * Retourne le code de langue à deux lettres 639-1 ISO, majuscules du code ISO 3166-1 country et variante séparés par des tirets. Exemples: « fr », « en-US », « US »

### Notes au sujet de Windows Phone 8

  * Code renvoie l'ISO 639-1 deux lettres de la langue et indicatif ISO 3166-1 de la variante régionale correspondant à la « langue » définissant, séparés par un tiret.
  * Notez que la variante régionale est une propriété du paramètre « Langue » et pas déterminé par le paramètre « Pays/région » sans rapport avec Windows Phone.

### Bizarreries de Windows

  * Code renvoie l'ISO 639-1 deux lettres de la langue et indicatif ISO 3166-1 de la variante régionale correspondant à la « langue » définissant, séparés par un tiret.

### Bizarreries navigateur

  * Falls back on getLocaleName

## navigator.globalization.getLocaleName

Retourne la balise conforme BCP 47 pour paramètre de langue actuel du client.

    navigator.globalization.getLocaleName (successCallback, errorCallback) ;
    

### Description

Retourne la chaîne d'identificateur de paramètres régionaux compatibles BCP 47 à la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit avoir une `value` propriété avec une `String` valeur. La balise locale comprendra un code de deux lettres minuscules langue, code de pays à deux lettres majuscules et code de variante (non précisé), séparés par un tiret.

S'il y a une erreur d'obtenir les paramètres régionaux, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.UNKNOWN_ERROR`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en-US` locale, ceci pour afficher une fenêtre popup avec le texte`locale: en-US`.

    navigator.globalization.getLocaleName (fonction (paramètres régionaux) {alert ('locale: "+ locale.value + « \n »);}, function () {alert ('erreur d'obtention locale\n');}) ;
    

### Quirks Android

  * Java ne distingue pas entre un set « langue » et le set « locale », donc cette méthode est essentiellement identique à`navigator.globalizatin.getPreferredLanguage()`.

### Notes au sujet de Windows Phone 8

  * Code renvoie l'ISO 639-1 deux lettres de la langue et indicatif ISO 3166-1 de la variante régionale correspondant au paramètre de Format « régional », séparé par un trait d'Union.

### Bizarreries de Windows

  * Paramètres régionaux peuvent être changés dans le panneau-> horloge, langue et région-> région-> Formats-> Format et dans les milieux-> région-> Format régional sur Windows Phone 8.1.

### Bizarreries navigateur

  * IE retourne les paramètres régionaux du système d'exploitation. Chrome et Firefox retournent la balise de langue de navigateur.

## navigator.globalization.dateToString

Renvoie une date mise en forme comme une chaîne selon les paramètres régionaux du client et de fuseau horaire.

    navigator.globalization.dateToString (date, successCallback, errorCallback, options) ;
    

### Description

Retourne la date de mise en forme `String` par une `value` propriété accessible à partir de l'objet passé comme paramètre à la`successCallback`.

L'entrantes `date` paramètre doit être de type`Date`.

S'il y a une erreur de mise en forme la date, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.FORMATTING_ERROR`.

Le `options` paramètre est facultatif, et ses valeurs par défaut sont :

    {formatLength:'short', selector:'date and time'}
    

Le `options.formatLength` peut être `short` , `medium` , `long` , ou`full`.

Le `options.selector` peut être `date` , `time` ou`date and time`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Si le navigateur est configuré pour la `en_US` locale, cela permet d'afficher une boîte de dialogue contextuelle avec un texte semblable à `date: 9/25/2012 4:21PM` en utilisant les options par défaut :

    navigator.globalization.dateToString (new Date(), fonction (date) {alert ("date:" + date.value + « \n »);}, function () {alert ('erreur d'obtention dateString\n');}, { formatLength: 'short', selector: 'date and time' }) ;
    

### Quirks Android

  * `formatLength`les options sont un sous-ensemble d'Unicode [UTS #35](http://unicode.org/reports/tr35/tr35-4.html). L'option par défaut `short` dépend d'un format de date sélectionnée utilisateur dans `Settings -> System -> Date & time -> Choose date format` , qui fournissent un `year` modèle seulement avec 4 chiffres, pas de 2 chiffres. Cela signifie qu'il n'est pas complètement aligné avec [l'ICU](http://demo.icu-project.org/icu-bin/locexp?d_=en_US&_=en_US).

### Notes au sujet de Windows Phone 8

  * Le `formatLength` prend en charge uniquement l'option `short` et `full` valeurs.

  * Le modèle pour sélecteur « date et heure » est toujours un format datetime complet.

  * La valeur retournée peut être pas complètement alignée avec l'ICU selon les paramètres régionaux utilisateur.

### Bizarreries de Windows

  * Le `formatLength` prend en charge uniquement l'option `short` et `full` valeurs.

  * Le modèle pour sélecteur « date et heure » est toujours un format datetime complet.

  * La valeur retournée peut être pas complètement alignée avec l'ICU selon les paramètres régionaux utilisateur.

### Bizarreries navigateur

  * Seulement 79 paramètres régionaux est pris en charge car moment.js est utilisé dans cette méthode.

  * La valeur retournée peut être pas complètement alignée avec l'ICU selon les paramètres régionaux utilisateur.

  * sélecteur de `time` prend en charge `full` et `short` formatLength seulement.

### Firefox OS Quirks

  * `formatLength`n'est pas distinguer `long` et`full` 
  * une seule méthode d'affichage de date (aucun `long` ou `full` version)

## navigator.globalization.getCurrencyPattern

Retourne une chaîne de modèles pour formater et analyser les valeurs de monnaie selon les préférences de l'utilisateur et du code de devise ISO 4217 du client.

     navigator.globalization.getCurrencyPattern (currencyCode, successCallback, errorCallback) ;
    

### Description

Retourne le modèle de la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit contenir les propriétés suivantes :

  * **modèle**: le modèle de la monnaie de formater et d'analyser les valeurs de devise. Les modèles suivent [Unicode Technical Standard #35](http://unicode.org/reports/tr35/tr35-4.html). *(String)*

  * **code**: code de devise de l'ISO 4217 pour le modèle. *(String)*

  * **fraction**: le nombre de chiffres fractionnaires à utiliser lors de l'analyse et de formatage de devises. *(Nombre)*

  * **arrondissement**: l'arrondi incrémenter pour utiliser lors de l'analyse et de mise en forme. *(Nombre)*

  * **décimal**: le symbole décimal à utiliser pour l'analyse et de mise en forme. *(String)*

  * **regroupement**: le symbole de groupe à utiliser pour l'analyse et de mise en forme. *(String)*

L'entrantes `currencyCode` paramètre doit être un `String` de l'un des codes de devise ISO 4217, par exemple « USD ».

S'il y a une erreur, obtenir le modèle, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.FORMATTING_ERROR`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows 8
  * Windows

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale et la devise sélectionnée est Dollars des États-Unis, cet exemple pour afficher une fenêtre popup avec un texte semblable aux résultats qui suivent :

    navigator.globalization.getCurrencyPattern (« USD », function (modèle) {alert (' modèle: ' + pattern.pattern + « \n » + ' code: ' + pattern.code + « \n » + ' fraction: ' + pattern.fraction + « \n » + ' arrondi: ' + pattern.rounding + « \n » + ' décimal: ' + pattern.decimal + « \n » + ' groupement: ' + pattern.grouping) ;
        }, function () {alert ('erreur d'obtention pattern\n');}) ;
    

Résultat escompté :

    modèle : $#,##0.##;($#,##0.##) code : fraction USD: 2 arrondi: 0 décimales:.
    regroupement:,
    

### Bizarreries de Windows

  * Uniquement des propriétés « code » et « fraction » sont pris en charge

## navigator.globalization.getDateNames

Retourne un tableau des noms des mois ou jours de la semaine, selon le calendrier et les préférences de l'utilisateur du client.

    navigator.globalization.getDateNames (successCallback, errorCallback, options) ;
    

### Description

Retourne le tableau de noms à la `successCallback` avec un `properties` objet comme paramètre. Cet objet contient une `value` propriété avec un `Array` de `String` valeurs. Les noms de fonctionnalités de tableau à partir de soit le premier mois de l'année ou le premier jour de la semaine, selon l'option choisie.

S'il y a une erreur d'obtention des noms, puis les `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.UNKNOWN_ERROR`.

Le `options` paramètre est facultatif, et ses valeurs par défaut sont :

    {type:'wide', item:'months'}
    

La valeur de `options.type` peut être `narrow` ou`wide`.

La valeur de `options.item` peut être `months` ou`days`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cet exemple affiche une série de douze fenêtres popup, un par mois, avec un texte semblable à `month: January` :

    navigator.globalization.getDateNames (fonction (nom) {pour (var j'ai = 0; j'ai < names.value.length; i ++) {alert (' mois: "+ names.value[i] + « \n ») ;
            }}, function () {alert ('erreur d'obtention names\n');}, { type: 'wide', item: 'months' }) ;
    

### Firefox OS Quirks

  * `options.type`prend en charge une `genitive` valeur, important pour certaines langues

### Notes au sujet de Windows Phone 8

  * Le tableau du mois contient 13 éléments.
  * Le tableau retourné peut être pas complètement aligné sur ICU selon les paramètres régionaux utilisateur.

### Bizarreries de Windows

  * Le tableau du mois contient 12 éléments.
  * Le tableau retourné peut être pas complètement aligné sur ICU selon les paramètres régionaux utilisateur.

### Bizarreries navigateur

  * Les noms de date ne sont pas alignés avec l'ICU
  * Le tableau du mois contient 12 éléments.

## navigator.globalization.getDatePattern

Retourne une chaîne de modèles pour formater et d'analyser les dates selon les préférences de l'utilisateur du client.

    navigator.globalization.getDatePattern (successCallback, errorCallback, options) ;
    

### Description

Retourne le modèle de la `successCallback` . L'objet passé comme paramètre contient les propriétés suivantes :

  * **modèle**: le modèle de date et d'heure pour formater et analyser des dates. Les modèles suivent [Unicode Technical Standard #35](http://unicode.org/reports/tr35/tr35-4.html). *(String)*

  * **fuseau horaire**: l'abréviation du fuseau horaire sur le client. *(String)*

  * **utc_offset**: la différence actuelle en secondes entre le temps universel coordonné et du fuseau horaire du client. *(Nombre)*

  * **DST_OFFSET**: l'offset d'heure actuel en secondes entre non-heure le client du fuseau horaire et l'heure du client sauver du fuseau horaire. *(Nombre)*

S'il y a une erreur, obtenir le modèle, le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.PATTERN_ERROR`.

Le `options` paramètre est facultatif et par défaut les valeurs suivantes :

    {formatLength:'short', selector:'date and time'}
    

Le `options.formatLength` peut être `short` , `medium` , `long` , ou `full` . Le `options.selector` peut être `date` , `time` ou`date and
time`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cet exemple pour afficher une fenêtre popup avec texte comme `pattern: M/d/yyyy h:mm a` :

    function checkDatePattern() {navigator.globalization.getDatePattern (fonction (date) {alert (' modèle: "+ date.pattern + « \n »);}, function () {alert ('erreur d'obtention pattern\n');}, { formatLength: 'short', selector: 'date and time' });}
    

### Notes au sujet de Windows Phone 8

  * Le `formatLength` prend uniquement en charge `short` et `full` valeurs.

  * Le `pattern` pour `date and time` modèle retourne uniquement datetime plein format.

  * Le `timezone` retourne le nom de zone à temps plein.

  * La `dst_offset` propriété n'est pas prise en charge, et toujours retourne zéro.

  * Le modèle peut être pas complètement aligné sur ICU selon les paramètres régionaux utilisateur.

### Bizarreries de Windows

  * Le `formatLength` prend uniquement en charge `short` et `full` valeurs.

  * Le `pattern` pour `date and time` modèle retourne uniquement datetime plein format.

  * Le `timezone` retourne le nom de zone à temps plein.

  * La `dst_offset` propriété n'est pas prise en charge, et toujours retourne zéro.

  * Le modèle peut être pas complètement aligné sur ICU selon les paramètres régionaux utilisateur.

### Bizarreries navigateur

  * La propriété « pattern » n'est pas prise en charge et retourne une chaîne vide.

  * Seulement Chrome retourne « timezone » propriété. Son format est « Partie de la world/{City} ». Autres navigateurs retournent une chaîne vide.

## navigator.globalization.getFirstDayOfWeek

Retourne le premier jour de la semaine selon le calendrier et les préférences de l'utilisateur du client.

    navigator.globalization.getFirstDayOfWeek (successCallback, errorCallback) ;
    

### Description

Les jours de la semaine sont numérotés à partir de 1, où 1 est supposé pour être le dimanche. Retourne le jour de la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit avoir une `value` propriété avec une `Number` valeur.

S'il y a une erreur, obtenir le modèle, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.UNKNOWN_ERROR`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cela permet d'afficher une boîte de dialogue contextuelle avec un texte semblable à`day: 1`.

    navigator.globalization.getFirstDayOfWeek (fonction (jour) {alert (' jour: ' + day.value + « \n »);}, function () {alert ('erreur d'obtention day\n');}) ;
    

### Bizarreries de Windows

  * Sur Windows 8.0/8.1 la valeur dépend de l'utilisateur ' calendrier des préférences. Sur Windows Phone 8.1 la valeur dépend des paramètres régionaux en cours.

### Bizarreries navigateur

  * Seulement 79 paramètres régionaux est pris en charge car moment.js est utilisé dans cette méthode.

## navigator.globalization.getNumberPattern

Retourne une chaîne de modèles pour formater et d'analyser les chiffres selon les préférences de l'utilisateur du client.

    navigator.globalization.getNumberPattern (successCallback, errorCallback, options) ;
    

### Description

Retourne le modèle de la `successCallback` avec un `properties` objet comme paramètre. Cet objet contient les propriétés suivantes :

  * **modèle**: le modèle de numéro de formater et d'analyser les chiffres. Les modèles suivent [Unicode Technical Standard #35](http://unicode.org/reports/tr35/tr35-4.html). *(String)*

  * **symbole**: le symbole à utiliser lors de la mise en forme et l'analyse, comme un symbole de pourcentage ou de la monnaie. *(String)*

  * **fraction**: le nombre de chiffres fractionnaires à utiliser lors de l'analyse et de mise en forme des nombres. *(Nombre)*

  * **arrondissement**: l'arrondi incrémenter pour utiliser lors de l'analyse et de mise en forme. *(Nombre)*

  * **positif**: le symbole à utiliser pour les nombres positifs lors de l'analyse et de mise en forme. *(String)*

  * **négatif**: le symbole à utiliser pour les nombres négatifs lors de l'analyse et de mise en forme. *(String)*

  * **décimal**: le symbole décimal à utiliser pour l'analyse et de mise en forme. *(String)*

  * **regroupement**: le symbole de groupe à utiliser pour l'analyse et de mise en forme. *(String)*

S'il y a une erreur, obtenir le modèle, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.PATTERN_ERROR`.

Le `options` paramètre est facultatif, et les valeurs par défaut sont :

    {type:'decimal'}
    

Le `options.type` peut être `decimal` , `percent` , ou`currency`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cela doit afficher une boîte de dialogue contextuelle avec un texte semblable aux résultats qui suivent :

    navigator.globalization.getNumberPattern (fonction (modèle) {alert (' modèle: ' + pattern.pattern + « \n » + ' symbole: ' + pattern.symbol + « \n » + ' fraction: ' + pattern.fraction + « \n » + ' arrondi: ' + pattern.rounding + « \n » + ' positif: ' + pattern.positive + « \n » + ' négatif: ' + pattern.negative + « \n » + ' décimal: ' + pattern.decimal + « \n » + ' regroupant: ' + pattern.grouping);}, function () {alert ('erreur d'obtention pattern\n');}, {type:'decimal'}) ;
    

Résultats :

    modèle: #, ## 0. ### symbole:.
    fraction : arrondi 0: 0 positif : négatif: - décimal:.
    regroupement:,
    

### Notes au sujet de Windows Phone 8

  * La `pattern` propriété n'est pas pris en charge et retourne une chaîne vide.

  * La `fraction` propriété n'est pas prise en charge et retourne zéro.

### Bizarreries de Windows

  * La `pattern` propriété n'est pas pris en charge et retourne une chaîne vide.

### Bizarreries navigateur

  * getNumberPattern est pris en charge dans Chrome seulement ; la seule propriété définie est `pattern`.

## navigator.globalization.isDayLightSavingsTime

Indique si l'heure avancée est en vigueur pour une date donnée en utilisant le calendrier et le fuseau horaire du client.

    navigator.globalization.isDayLightSavingsTime (date, successCallback, errorCallback) ;
    

### Description

Indique si l'heure avancée est en vigueur à la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit avoir une `dst` propriété avec une `Boolean` valeur. A `true` valeur indique que l'heure avancée est en vigueur à la date donnée, et `false` indique qu'il ne l'est pas.

Le paramètre entrant `date` doit être de type`Date`.

S'il y a une erreur de lecture de la date, puis le `errorCallback` s'exécute. Code attendu de l'erreur est`GlobalizationError.UNKNOWN_ERROR`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Au cours de l'été, et si le navigateur est défini sur un fuseau horaire la DST-activé, il doit afficher une boîte de dialogue contextuelle avec un texte semblable à `dst: true` :

    navigator.globalization.isDayLightSavingsTime (new Date(), fonction (date) {alert ('dst: "+ date.dst + « \n »);}, function () {alert ('erreur d'obtention names\n');}) ;
    

## navigator.globalization.numberToString

Renvoie un nombre mis en forme comme une chaîne selon les préférences de l'utilisateur du client.

    navigator.globalization.numberToString (nombre, successCallback, errorCallback, options) ;
    

### Description

Retourne la chaîne mise en forme de nombre à la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit avoir une `value` propriété avec une `String` valeur.

S'il y a une erreur de mise en forme le nombre, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.FORMATTING_ERROR`.

Le `options` paramètre est facultatif, et ses valeurs par défaut sont :

    {type:'decimal'}
    

Le `options.type` peut être « decimal », « % » ou « monnaie ».

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cela permet d'afficher une boîte de dialogue contextuelle avec un texte semblable à `number: 3.142` :

    navigator.globalization.numberToString (3.1415926, fonction (nombre) {alert (' nombre: "+ number.value + « \n »);}, function () {alert ('erreur d'obtention number\n');}, {type:'decimal'}) ;
    

### Bizarreries de Windows

  * Windows 8.0 ne supporte pas le nombre arrondi, donc les valeurs ne seront pas arrondis automatiquement.

  * Sur la partie fractionnaire de 8.1 de Windows et Windows Phone 8.1 sont tronqués au lieu d'arrondi en cas de `percent` type number donc le nombre de chiffres fractionnaires est défini sur 0.

  * `percent`les numéros ne sont pas regroupés qu'ils ne peuvent pas être analysés dans stringToNumber si regroupés.

### Bizarreries navigateur

  * type de `currency` n'est pas pris en charge.

## navigator.globalization.stringToDate

Analyse une date mise en forme sous forme de chaîne, selon les préférences de l'utilisateur et du calendrier en utilisant le fuseau horaire du client, du client et retourne l'objet date correspondante.

    navigator.globalization.stringToDate (dateString, successCallback, errorCallback, options) ;
    

### Description

Retourne la date du rappel de succès avec un `properties` objet comme paramètre. Cet objet doit avoir les propriétés suivantes :

  * **année**: l'année à quatre chiffres. *(Nombre)*

  * **mois**: le mois de (0-11). *(Nombre)*

  * **jour**: le jour de (1-31). *(Nombre)*

  * **heure**: l'heure du (0-23). *(Nombre)*

  * **minute**: la minute (0-59). *(Nombre)*

  * **deuxième**: la seconde de (0 à 59). *(Nombre)*

  * **milliseconde**: les millisecondes (entre 0 et 999), non disponibles sur toutes les plateformes. *(Nombre)*

L'entrantes `dateString` paramètre doit être de type`String`.

Le `options` paramètre est facultatif et par défaut les valeurs suivantes :

    {formatLength:'short', selector:'date and time'}
    

Le `options.formatLength` peut être `short` , `medium` , `long` , ou `full` . Le `options.selector` peut être `date` , `time` ou`date and
time`.

S'il y a une erreur d'analyse de la chaîne de date, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.PARSING_ERROR`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows
  * Navigateur

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cela permet d'afficher une boîte de dialogue contextuelle avec un texte semblable à `month:8 day:25 year:2012` . Notez que le mois entier est l'un de moins que la chaîne, comme le nombre entier de mois représente un index de tableau.

    navigator.globalization.stringToDate (' 25/09/2012', function (date) {alert (' mois:' + date.month + ' jour:' + date.day + ' année: "+ date.year +"\n");}, function () {alert ('erreur d'obtention date\n');}, {selector: 'date'}) ;
    

### Notes au sujet de Windows Phone 8

  * Le `formatLength` prend en charge uniquement l'option `short` et `full` valeurs.

  * Le modèle pour sélecteur « date et heure » est toujours un format datetime complet.

  * L'entrantes `dateString` paramètre devrait être formé en conformité avec un modèle retourné par getDatePattern. Ce modèle peut être pas complètement aligné sur ICU selon les paramètres régionaux utilisateur.

### Bizarreries de Windows

  * Le `formatLength` prend en charge uniquement l'option `short` et `full` valeurs.

  * Le modèle pour sélecteur « date et heure » est toujours un format datetime complet.

  * L'entrantes `dateString` paramètre devrait être formé en conformité avec un modèle retourné par getDatePattern. Ce modèle peut être pas complètement aligné sur ICU selon les paramètres régionaux utilisateur.

### Bizarreries navigateur

  * Seulement 79 paramètres régionaux est pris en charge car moment.js est utilisé dans cette méthode.

  * Chaîne entrante doit être alignée avec le format de sortie `dateToString` et mai pas alignés avec l'ICU selon les paramètres régionaux utilisateur.

  * sélecteur de `time` prend en charge `full` et `short` formatLength seulement.

## navigator.globalization.stringToNumber

Analyse un nombre mis en forme comme une chaîne selon les préférences de l'utilisateur du client et renvoie le numéro du correspondant.

    navigator.globalization.stringToNumber (chaîne, successCallback, errorCallback, options) ;
    

### Description

Retourne le nombre de la `successCallback` avec un `properties` objet comme paramètre. Cet objet doit avoir une `value` propriété avec une `Number` valeur.

S'il y a une erreur d'analyse de la chaîne de numéro, puis le `errorCallback` s'exécute avec un `GlobalizationError` objet comme paramètre. Code attendu de l'erreur est`GlobalizationError.PARSING_ERROR`.

Le `options` paramètre est facultatif et par défaut les valeurs suivantes :

    {type:'decimal'}
    

Le `options.type` peut être `decimal` , `percent` , ou`currency`.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows

### Exemple

Lorsque le navigateur est configuré pour la `en_US` locale, cela doit afficher une boîte de dialogue contextuelle avec un texte semblable à `number: 1234.56` :

    navigator.globalization.stringToNumber (« 1234.56 », int (nombre) {alert (' nombre: "+ number.value + « \n »);}, function () {alert ('erreur d'obtention number\n');}, {type:'decimal'}) ;
    

### Notes au sujet de Windows Phone 8

  * En cas de `percent` type de la valeur retournée n'est pas divisée par 100.

### Bizarreries de Windows

  * La chaîne doit se conformer strictement au format de paramètres régionaux. Par exemple, symbole de pourcentage doit être séparé par l'espace pour les paramètres régionaux « en-US » si le paramètre de type est « % ».

  * `percent`numéros ne doivent pas être groupés pour être analysé correctement.

## GlobalizationError

Un objet qui représente une erreur de l'API de la mondialisation.

### Propriétés

  * **code**: Un des codes suivants qui représente le type d'erreur *(Nombre)* 
      * GlobalizationError.UNKNOWN_ERROR: 0
      * GlobalizationError.FORMATTING_ERROR: 1
      * GlobalizationError.PARSING_ERROR: 2
      * GlobalizationError.PATTERN_ERROR: 3
  * **message**: un message texte qui comprend l'explication de l'erreur et/ou de détails *(String)*

### Description

Cet objet est créé et peuplé de Cordova et retourné à un rappel en cas d'erreur.

### Plates-formes supportées

  * Amazon Fire OS
  * Android
  * BlackBerry 10
  * Firefox OS
  * iOS
  * Windows Phone 8
  * Windows 8
  * Windows

### Exemple

Lorsque le rappel d'erreur suivant s'exécute, il affiche une fenêtre popup avec le texte semblable à `code: 3` et`message:`

    function errorCallback(error) {alert ('code: ' + error.code + « \n » + "message: ' + error.message + « \n »);} ;