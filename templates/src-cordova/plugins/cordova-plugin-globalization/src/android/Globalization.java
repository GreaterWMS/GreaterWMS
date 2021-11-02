/*
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
*/

package org.apache.cordova.globalization;

import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.Comparator;
import java.util.Currency;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TimeZone;

import org.apache.cordova.CallbackContext;
import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.PluginResult;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.annotation.TargetApi;
import android.text.format.Time;

/**
 *
 */
public class Globalization extends CordovaPlugin  {
    //GlobalizationCommand Plugin Actions
    public static final String GETLOCALENAME = "getLocaleName";
    public static final String DATETOSTRING = "dateToString";
    public static final String STRINGTODATE = "stringToDate";
    public static final String GETDATEPATTERN = "getDatePattern";
    public static final String GETDATENAMES = "getDateNames";
    public static final String ISDAYLIGHTSAVINGSTIME = "isDayLightSavingsTime";
    public static final String GETFIRSTDAYOFWEEK = "getFirstDayOfWeek";
    public static final String NUMBERTOSTRING = "numberToString";
    public static final String STRINGTONUMBER = "stringToNumber";
    public static final String GETNUMBERPATTERN = "getNumberPattern";
    public static final String GETCURRENCYPATTERN = "getCurrencyPattern";
    public static final String GETPREFERREDLANGUAGE = "getPreferredLanguage";

    //GlobalizationCommand Option Parameters
    public static final String OPTIONS = "options";
    public static final String FORMATLENGTH = "formatLength";
    //public static final String SHORT = "short"; //default for dateToString format
    public static final String MEDIUM = "medium";
    public static final String LONG = "long";
    public static final String FULL = "full";
    public static final String SELECTOR = "selector";
    //public static final String DATEANDTIME = "date and time"; //default for dateToString
    public static final String DATE = "date";
    public static final String TIME = "time";
    public static final String DATESTRING = "dateString";
    public static final String TYPE = "type";
    public static final String ITEM = "item";
    public static final String NARROW = "narrow";
    public static final String WIDE = "wide";
    public static final String MONTHS = "months";
    public static final String DAYS = "days";
    //public static final String DECMIAL = "wide"; //default for numberToString
    public static final String NUMBER = "number";
    public static final String NUMBERSTRING = "numberString";
    public static final String PERCENT = "percent";
    public static final String CURRENCY = "currency";
    public static final String CURRENCYCODE = "currencyCode";

    @Override
    public boolean execute(String action, JSONArray data, CallbackContext callbackContext) {
        JSONObject obj = new JSONObject();

        try{
            if (action.equals(GETLOCALENAME)){
                obj = getLocaleName();
            }else if (action.equals(GETPREFERREDLANGUAGE)){
                obj = getPreferredLanguage();
            } else if (action.equalsIgnoreCase(DATETOSTRING)) {
                obj = getDateToString(data);
            }else if(action.equalsIgnoreCase(STRINGTODATE)){
                obj = getStringtoDate(data);
            }else if(action.equalsIgnoreCase(GETDATEPATTERN)){
                obj = getDatePattern(data);
            }else if(action.equalsIgnoreCase(GETDATENAMES)){
                if (android.os.Build.VERSION.SDK_INT < android.os.Build.VERSION_CODES.GINGERBREAD) {
                    throw new GlobalizationError(GlobalizationError.UNKNOWN_ERROR);
                } else {
                    obj = getDateNames(data);
                }
            }else if(action.equalsIgnoreCase(ISDAYLIGHTSAVINGSTIME)){
                obj = getIsDayLightSavingsTime(data);
            }else if(action.equalsIgnoreCase(GETFIRSTDAYOFWEEK)){
                obj = getFirstDayOfWeek(data);
            }else if(action.equalsIgnoreCase(NUMBERTOSTRING)){
                obj = getNumberToString(data);
            }else if(action.equalsIgnoreCase(STRINGTONUMBER)){
                obj = getStringToNumber(data);
            }else if(action.equalsIgnoreCase(GETNUMBERPATTERN)){
                obj = getNumberPattern(data);
            }else if(action.equalsIgnoreCase(GETCURRENCYPATTERN)){
                obj = getCurrencyPattern(data);
            }else {
                return false;
            }

            callbackContext.success(obj);
        }catch (GlobalizationError ge){
            callbackContext.sendPluginResult(new PluginResult(PluginResult.Status.ERROR, ge.toJson()));
        }catch (Exception e){
            callbackContext.sendPluginResult(new PluginResult(PluginResult.Status.JSON_EXCEPTION));
        }
        return true;
    }
    /*
     * @Description: Returns a well-formed ITEF BCP 47 language tag representing
     * the locale identifier for the client's current locale 
     *
     * @Return: String: The BCP 47 language tag for the current locale
     */
    private String toBcp47Language(Locale loc){
        final char SEP = '-';       // we will use a dash as per BCP 47
        String language = loc.getLanguage();
        String region = loc.getCountry();
        String variant = loc.getVariant();

        // special case for Norwegian Nynorsk since "NY" cannot be a variant as per BCP 47
        // this goes before the string matching since "NY" wont pass the variant checks
        if( language.equals("no") && region.equals("NO") && variant.equals("NY")){
            language = "nn";
            region = "NO";
            variant = "";
        }

        if( language.isEmpty() || !language.matches("\\p{Alpha}{2,8}")){
            language = "und";       // Follow the Locale#toLanguageTag() implementation 
                                    // which says to return "und" for Undetermined
        }else if(language.equals("iw")){
            language = "he";        // correct deprecated "Hebrew"
        }else if(language.equals("in")){
            language = "id";        // correct deprecated "Indonesian"
        }else if(language.equals("ji")){
            language = "yi";        // correct deprecated "Yiddish"
        }

        // ensure valid country code, if not well formed, it's omitted
        if (!region.matches("\\p{Alpha}{2}|\\p{Digit}{3}")) {
            region = "";
        }

         // variant subtags that begin with a letter must be at least 5 characters long
        if (!variant.matches("\\p{Alnum}{5,8}|\\p{Digit}\\p{Alnum}{3}")) {
            variant = "";
        }

        StringBuilder bcp47Tag = new StringBuilder(language);
        if (!region.isEmpty()) {
            bcp47Tag.append(SEP).append(region);
        }
        if (!variant.isEmpty()) {
             bcp47Tag.append(SEP).append(variant);
        }

        return bcp47Tag.toString();
    }
    /*
     * @Description: Returns the BCP 47 Unicode locale identifier for current locale setting
     * The locale is defined by a language code, a country code, and a variant, separated
     * by a hyphen, for example, "en-US", "fr-CA", etc.,
     *
     * @Return: JSONObject
     *          Object.value {String}: The locale identifier
     *
     * @throws: GlobalizationError.UNKNOWN_ERROR
     */
    private JSONObject getLocaleName() throws GlobalizationError{
        JSONObject obj = new JSONObject();
        try{
            obj.put("value", toBcp47Language(Locale.getDefault()));
            return obj;
        }catch(Exception e){
            throw new GlobalizationError(GlobalizationError.UNKNOWN_ERROR);
        }
    }
    /*
     * @Description: Returns the BCP 47 language tag for the client's 
     * current language. Currently in Android this is the same as locale,
     * since Java does not distinguish between locale and language.
     *
     * @Return: JSONObject
     *          Object.value {String}: The language identifier
     *
     * @throws: GlobalizationError.UNKNOWN_ERROR
     */
    private JSONObject getPreferredLanguage() throws GlobalizationError {
        JSONObject obj = new JSONObject();
        try {
            obj.put("value", toBcp47Language(Locale.getDefault()));
            return obj;
        } catch (Exception e) {
            throw new GlobalizationError(GlobalizationError.UNKNOWN_ERROR);
        }
    }
    /*
     * @Description: Returns a date formatted as a string according to the client's user preferences and
     * calendar using the time zone of the client.
     *
     * @Return: JSONObject
     *          Object.value {String}: The localized date string
     *
     * @throws: GlobalizationError.FORMATTING_ERROR
     */
    private JSONObject getDateToString(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        try{
            Date date = new Date((Long)options.getJSONObject(0).get(DATE));

            //get formatting pattern from android device (Will only have device specific formatting for short form of date) or options supplied
            JSONObject datePattern = getDatePattern(options);
            SimpleDateFormat fmt = new SimpleDateFormat(datePattern.getString("pattern"));

            //return formatted date
            return obj.put("value",fmt.format(date));
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.FORMATTING_ERROR);
        }
    }

    /*
     * @Description: Parses a date formatted as a string according to the client's user
     * preferences and calendar using the time zone of the client and returns
     * the corresponding date object
     * @Return: JSONObject
     *          Object.year {Number}: The four digit year
     *          Object.month {Number}: The month from (0 - 11)
     *          Object.day {Number}: The day from (1 - 31)
     *          Object.hour {Number}: The hour from (0 - 23)
     *          Object.minute {Number}: The minute from (0 - 59)
     *          Object.second {Number}: The second from (0 - 59)
     *          Object.millisecond {Number}: The milliseconds (from 0 - 999), not available on all platforms
     *
     * @throws: GlobalizationError.PARSING_ERROR
    */
    private JSONObject getStringtoDate(JSONArray options)throws GlobalizationError{
        JSONObject obj = new JSONObject();
        Date date;
        try{
            //get format pattern from android device (Will only have device specific formatting for short form of date) or options supplied
            DateFormat fmt = new SimpleDateFormat(getDatePattern(options).getString("pattern"));

            //attempt parsing string based on user preferences
            date = fmt.parse(options.getJSONObject(0).get(DATESTRING).toString());

            //set Android Time object
            Time time = new Time();
            time.set(date.getTime());

            //return properties;
            obj.put("year", time.year);
            obj.put("month", time.month);
            obj.put("day", time.monthDay);
            obj.put("hour", time.hour);
            obj.put("minute", time.minute);
            obj.put("second", time.second);
            obj.put("millisecond", Long.valueOf(0));
            return obj;
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.PARSING_ERROR);
        }
    }

    /*
     * @Description: Returns a pattern string for formatting and parsing dates according to the client's
     * user preferences.
     * @Return: JSONObject
     *
     *          Object.pattern {String}: The date and time pattern for formatting and parsing dates.
     *                                  The patterns follow Unicode Technical Standard #35
     *                                  http://unicode.org/reports/tr35/tr35-4.html
     *          Object.timezone {String}: The abbreviated name of the time zone on the client
     *          Object.utc_offset {Number}: The current difference in seconds between the client's
     *                                      time zone and coordinated universal time.
     *          Object.dst_offset {Number}: The current daylight saving time offset in seconds
     *                                      between the client's non-daylight saving's time zone
     *                                      and the client's daylight saving's time zone.
     *
     * @throws: GlobalizationError.PATTERN_ERROR
    */
    private JSONObject getDatePattern(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();

        try{
            SimpleDateFormat fmtDate = (SimpleDateFormat)android.text.format.DateFormat.getDateFormat(this.cordova.getActivity()); //default user preference for date
            SimpleDateFormat fmtTime = (SimpleDateFormat)android.text.format.DateFormat.getTimeFormat(this.cordova.getActivity());  //default user preference for time

            String fmt = fmtDate.toLocalizedPattern() + " " + fmtTime.toLocalizedPattern(); //default SHORT date/time format. ex. dd/MM/yyyy h:mm a

            //get Date value + options (if available)
            if (options.getJSONObject(0).has(OPTIONS)){
                //options were included

                JSONObject innerOptions = options.getJSONObject(0).getJSONObject(OPTIONS);
                //get formatLength option
                if (!innerOptions.isNull(FORMATLENGTH)){
                    String fmtOpt = innerOptions.getString(FORMATLENGTH);
                    if (fmtOpt.equalsIgnoreCase(MEDIUM)){//medium
                        fmtDate = (SimpleDateFormat)android.text.format.DateFormat.getMediumDateFormat(this.cordova.getActivity());
                    }else if (fmtOpt.equalsIgnoreCase(LONG) || fmtOpt.equalsIgnoreCase(FULL)){ //long/full
                        fmtDate = (SimpleDateFormat)android.text.format.DateFormat.getLongDateFormat(this.cordova.getActivity());
                    }
                }

                //return pattern type
                fmt = fmtDate.toLocalizedPattern() + " " + fmtTime.toLocalizedPattern();
                if (!innerOptions.isNull(SELECTOR)){
                    String selOpt = innerOptions.getString(SELECTOR);
                    if (selOpt.equalsIgnoreCase(DATE)){
                        fmt =  fmtDate.toLocalizedPattern();
                    }else if (selOpt.equalsIgnoreCase(TIME)){
                        fmt = fmtTime.toLocalizedPattern();
                    }
                }
            }

            //TimeZone from users device
            //TimeZone tz = Calendar.getInstance(Locale.getDefault()).getTimeZone(); //substitute method
            TimeZone tz = TimeZone.getTimeZone(Time.getCurrentTimezone());

            obj.put("pattern", fmt);
            obj.put("timezone", tz.getDisplayName(tz.inDaylightTime(Calendar.getInstance().getTime()),TimeZone.SHORT));
            obj.put("iana_timezone", tz.getID());
            obj.put("utc_offset", tz.getRawOffset()/1000);
            obj.put("dst_offset", tz.getDSTSavings()/1000);
            return obj;

        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.PATTERN_ERROR);
        }
    }

    /*
     * @Description: Returns an array of either the names of the months or days of the week
     * according to the client's user preferences and calendar
     * @Return: JSONObject
     *          Object.value {Array{String}}: The array of names starting from either
     *                                      the first month in the year or the
     *                                      first day of the week.
     *
     * @throws: GlobalizationError.UNKNOWN_ERROR
    */
    @TargetApi(9)
    private JSONObject getDateNames(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        //String[] value;
        JSONArray value = new JSONArray();
        List<String> namesList = new ArrayList<String>();
        final Map<String,Integer> namesMap; // final needed for sorting with anonymous comparator
        try{
            int type = 0; //default wide
            int item = 0; //default months

            //get options if available
            if (options.getJSONObject(0).length() > 0){
                //get type if available
                if (!((JSONObject)options.getJSONObject(0).get(OPTIONS)).isNull(TYPE)){
                    String t = (String)((JSONObject)options.getJSONObject(0).get(OPTIONS)).get(TYPE);
                    if (t.equalsIgnoreCase(NARROW)){type++;} //DateUtils.LENGTH_MEDIUM
                }
                //get item if available
                if (!((JSONObject)options.getJSONObject(0).get(OPTIONS)).isNull(ITEM)){
                    String t = (String)((JSONObject)options.getJSONObject(0).get(OPTIONS)).get(ITEM);
                    if (t.equalsIgnoreCase(DAYS)){item += 10;} //Days of week start at 1
                }
            }
            //determine return value
            int method = item + type;
            if  (method == 1) { //months and narrow
                namesMap = Calendar.getInstance().getDisplayNames(Calendar.MONTH, Calendar.SHORT, Locale.getDefault());
            } else if (method == 10) { //days and wide
                namesMap = Calendar.getInstance().getDisplayNames(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.getDefault());
            } else if (method == 11) { //days and narrow
                namesMap = Calendar.getInstance().getDisplayNames(Calendar.DAY_OF_WEEK, Calendar.SHORT, Locale.getDefault());
            } else { //default: months and wide
                namesMap = Calendar.getInstance().getDisplayNames(Calendar.MONTH, Calendar.LONG, Locale.getDefault());
            }

            // save names as a list
            for(String name : namesMap.keySet()) {
                namesList.add(name);
            }

            // sort the list according to values in namesMap
            Collections.sort(namesList, new Comparator<String>() {
                public int compare(String arg0, String arg1) {
                    return namesMap.get(arg0).compareTo(namesMap.get(arg1));
                }
            });

            // convert nameList into JSONArray of String objects
            for (int i = 0; i < namesList.size(); i ++){
                value.put(namesList.get(i));
            }

            //return array of names
            return obj.put("value", value);
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.UNKNOWN_ERROR);
        }
    }

    /*
     * @Description: Returns whether daylight savings time is in effect for a given date using the client's
     * time zone and calendar.
     * @Return: JSONObject
     *          Object.dst {Boolean}: The value "true" indicates that daylight savings time is
     *                              in effect for the given date and "false" indicate that it is not.    *
     *
     * @throws: GlobalizationError.UNKNOWN_ERROR
    */
    private JSONObject getIsDayLightSavingsTime(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        boolean dst = false;
        try{
            Date date = new Date((Long)options.getJSONObject(0).get(DATE));
            //TimeZone tz = Calendar.getInstance(Locale.getDefault()).getTimeZone();
            TimeZone tz = TimeZone.getTimeZone(Time.getCurrentTimezone());
            dst = tz.inDaylightTime(date); //get daylight savings data from date object and user timezone settings

            return obj.put("dst",dst);
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.UNKNOWN_ERROR);
        }
    }

    /*
     * @Description: Returns the first day of the week according to the client's user preferences and calendar.
     * The days of the week are numbered starting from 1 where 1 is considered to be Sunday.
     * @Return: JSONObject
     *          Object.value {Number}: The number of the first day of the week.
     *
     * @throws: GlobalizationError.UNKNOWN_ERROR
    */
    private JSONObject getFirstDayOfWeek(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        try{
            int value = Calendar.getInstance(Locale.getDefault()).getFirstDayOfWeek(); //get first day of week based on user locale settings
            return obj.put("value", value);
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.UNKNOWN_ERROR);
        }
    }

    /*
     * @Description: Returns a number formatted as a string according to the client's user preferences.
     * @Return: JSONObject
     *          Object.value {String}: The formatted number string.
     *
     * @throws: GlobalizationError.FORMATTING_ERROR
    */
    private JSONObject getNumberToString(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        String value = "";
        try{
            DecimalFormat fmt = getNumberFormatInstance(options);//returns Decimal/Currency/Percent instance
            value = fmt.format(options.getJSONObject(0).get(NUMBER));
            return obj.put("value", value);
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.FORMATTING_ERROR);
        }
    }

    /*
     * @Description: Parses a number formatted as a string according to the client's user preferences and
     * returns the corresponding number.
     * @Return: JSONObject
     *          Object.value {Number}: The parsed number.
     *
     * @throws: GlobalizationError.PARSING_ERROR
    */
    private JSONObject getStringToNumber(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        Number value;
        try{
            DecimalFormat fmt = getNumberFormatInstance(options); //returns Decimal/Currency/Percent instance
            value = fmt.parse((String)options.getJSONObject(0).get(NUMBERSTRING));
            return obj.put("value", value);
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.PARSING_ERROR);
        }
    }

    /*
     * @Description: Returns a pattern string for formatting and parsing numbers according to the client's user
     * preferences.
     * @Return: JSONObject
     *          Object.pattern {String}: The number pattern for formatting and parsing numbers.
     *                                  The patterns follow Unicode Technical Standard #35.
     *                                  http://unicode.org/reports/tr35/tr35-4.html
     *          Object.symbol {String}: The symbol to be used when formatting and parsing
     *                                  e.g., percent or currency symbol.
     *          Object.fraction {Number}: The number of fractional digits to use when parsing and
     *                                  formatting numbers.
     *          Object.rounding {Number}: The rounding increment to use when parsing and formatting.
     *          Object.positive {String}: The symbol to use for positive numbers when parsing and formatting.
     *          Object.negative: {String}: The symbol to use for negative numbers when parsing and formatting.
     *          Object.decimal: {String}: The decimal symbol to use for parsing and formatting.
     *          Object.grouping: {String}: The grouping symbol to use for parsing and formatting.
     *
     * @throws: GlobalizationError.PATTERN_ERROR
    */
    private JSONObject getNumberPattern(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        try{
            //uses java.text.DecimalFormat to format value
            DecimalFormat fmt = (DecimalFormat) DecimalFormat.getInstance(Locale.getDefault()); //default format
            String symbol = String.valueOf(fmt.getDecimalFormatSymbols().getDecimalSeparator());
            //get Date value + options (if available)
            if (options.getJSONObject(0).length() > 0){
                //options were included
                if (!((JSONObject)options.getJSONObject(0).get(OPTIONS)).isNull(TYPE)){
                    String fmtOpt = (String)((JSONObject)options.getJSONObject(0).get(OPTIONS)).get(TYPE);
                    if (fmtOpt.equalsIgnoreCase(CURRENCY)){
                        fmt = (DecimalFormat) DecimalFormat.getCurrencyInstance(Locale.getDefault());
                        symbol = fmt.getDecimalFormatSymbols().getCurrencySymbol();
                    }else if(fmtOpt.equalsIgnoreCase(PERCENT)){
                        fmt = (DecimalFormat) DecimalFormat.getPercentInstance(Locale.getDefault());
                        symbol = String.valueOf(fmt.getDecimalFormatSymbols().getPercent());
                    }
                }
            }

            //return properties
            obj.put("pattern", fmt.toPattern());
            obj.put("symbol", symbol);
            obj.put("fraction", fmt.getMinimumFractionDigits());
            obj.put("rounding", Integer.valueOf(0));
            obj.put("positive", fmt.getPositivePrefix());
            obj.put("negative", fmt.getNegativePrefix());
            obj.put("decimal", String.valueOf(fmt.getDecimalFormatSymbols().getDecimalSeparator()));
            obj.put("grouping", String.valueOf(fmt.getDecimalFormatSymbols().getGroupingSeparator()));

            return obj;
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.PATTERN_ERROR);
        }
    }

    /*
     * @Description: Returns a pattern string for formatting and parsing currency values according to the client's
     * user preferences and ISO 4217 currency code.
     * @Return: JSONObject
     *          Object.pattern {String}: The currency pattern for formatting and parsing currency values.
     *                                  The patterns follow Unicode Technical Standard #35
     *                                  http://unicode.org/reports/tr35/tr35-4.html
     *          Object.code {String}: The ISO 4217 currency code for the pattern.
     *          Object.fraction {Number}: The number of fractional digits to use when parsing and
     *                                  formatting currency.
     *          Object.rounding {Number}: The rounding increment to use when parsing and formatting.
     *          Object.decimal: {String}: The decimal symbol to use for parsing and formatting.
     *          Object.grouping: {String}: The grouping symbol to use for parsing and formatting.
     *
     * @throws: GlobalizationError.FORMATTING_ERROR
    */
    private JSONObject getCurrencyPattern(JSONArray options) throws GlobalizationError{
        JSONObject obj = new JSONObject();
        try{
            //get ISO 4217 currency code
            String code = options.getJSONObject(0).getString(CURRENCYCODE);

            //uses java.text.DecimalFormat to format value
            DecimalFormat fmt = (DecimalFormat) DecimalFormat.getCurrencyInstance(Locale.getDefault());

            //set currency format
            Currency currency = Currency.getInstance(code);
            fmt.setCurrency(currency);

            //return properties
            obj.put("pattern", fmt.toPattern());
            obj.put("code", currency.getCurrencyCode());
            obj.put("fraction", fmt.getMinimumFractionDigits());
            obj.put("rounding", Integer.valueOf(0));
            obj.put("decimal", String.valueOf(fmt.getDecimalFormatSymbols().getDecimalSeparator()));
            obj.put("grouping", String.valueOf(fmt.getDecimalFormatSymbols().getGroupingSeparator()));

            return obj;
        }catch(Exception ge){
            throw new GlobalizationError(GlobalizationError.FORMATTING_ERROR);
        }
    }

    /*
     * @Description: Parses a JSONArray from user options and returns the correct Instance of Decimal/Percent/Currency.
     * @Return: DecimalFormat : The Instance to use.
     *
     * @throws: JSONException
    */
    private DecimalFormat getNumberFormatInstance(JSONArray options) throws JSONException{
        DecimalFormat fmt =  (DecimalFormat)DecimalFormat.getInstance(Locale.getDefault()); //default format
        try{
            if (options.getJSONObject(0).length() > 1){
                //options were included
                if (!((JSONObject)options.getJSONObject(0).get(OPTIONS)).isNull(TYPE)){
                    String fmtOpt = (String)((JSONObject)options.getJSONObject(0).get(OPTIONS)).get(TYPE);
                    if (fmtOpt.equalsIgnoreCase(CURRENCY)){
                        fmt = (DecimalFormat)DecimalFormat.getCurrencyInstance(Locale.getDefault());
                    }else if(fmtOpt.equalsIgnoreCase(PERCENT)){
                        fmt = (DecimalFormat)DecimalFormat.getPercentInstance(Locale.getDefault());
                    }
                }
            }

        }catch (JSONException je){}
        return fmt;
    }
}
