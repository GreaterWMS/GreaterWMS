/*
 *
 * Copyright 2013 Canonical Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
*/
#ifndef GLOBALIZATION_H_SVO2013
#define GLOBALIZATION_H_SVO2013

#include <QtCore>
#include <QLocale>

#include <cplugin.h>

class Globalization: public CPlugin {
    Q_OBJECT
    enum GlobalizationError {
        UNKNOWN_ERROR = 0,
        FORMATTING_ERROR = 1,
        PARSING_ERROR = 2,
        PATTERN_ERROR = 3
    };

    enum Selector {
        SELECTOR_DATE = 0,
        SELECTOR_TIME = 1,
        SELECTOR_ALL = 2
    };

    enum Format {
        FORMAT_SHORT = 0,
        FORMAT_MEDIUM = 1,
        FORMAT_LONG = 2,
        FORMAT_FULL = 3
    };

    enum {
        REQUEST_DAY_NAMES = 0,
        REQUEST_MONTH_NAMES = 1
    };

    enum NumberType {
        DECIMAL,
        PERCENT,
        CURRENCY
    };

public:
    explicit Globalization(Cordova *cordova);

    virtual const QString fullName() override {
        return Globalization::fullID();
    }

    virtual const QString shortName() override {
        return "Globalization";
    }

    static const QString fullID() {
        return "Globalization";
    }

public slots:
    void getPreferredLanguage(int scId, int ecId);
    void getLocaleName(int scId, int ecId);
    void getFirstDayOfWeek(int scId, int ecId);
    void isDayLightSavingsTime(int scId, int ecId, const QVariantMap &options);
    void dateToString(int scId, int ecId, const QVariantMap &options);
    void stringToDate(int scId, int ecId, const QVariantMap &options);

    void getDateNames(int scId, int ecId, const QVariantMap &options);
    void numberToString(int scId, int ecId, const QVariantMap &options);
    void stringToNumber(int scId, int ecId, int type, QString string);
    void getNumberPattern(int scId, int ecId, int type);
    void getDatePattern(int scId, int ecId, int formatLength, int selector);
private:
    friend QLocale::FormatType translateFormat(Globalization::Format formatLength);
    template<class T> friend QString format(T number, Globalization::NumberType type);
};

#endif
