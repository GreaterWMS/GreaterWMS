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

#include <ctime> //TODO: switch to QTimeZone (QT 5.1)
#include <unicode/decimfmt.h>
#include <unicode/timezone.h>

#include "globalization.h"

Globalization::Globalization(Cordova *cordova):
    CPlugin(cordova) {
}

void Globalization::getPreferredLanguage(int scId, int ecId) {
    Q_UNUSED(ecId)

    QLocale locale;
    QString lang = QLocale::languageToString(locale.language());
    QVariantMap obj;
    obj.insert("value", lang);
    this->cb(scId, obj);
}

void Globalization::getLocaleName(int scId, int ecId) {
    Q_UNUSED(ecId)

    QVariantMap obj;
    obj.insert("value", QLocale().name());
    this->cb(scId, obj);
}

void Globalization::getFirstDayOfWeek(int scId, int ecId) {
    Q_UNUSED(ecId)

    QLocale locale;

    int res;
    if (locale.firstDayOfWeek() == Qt::Sunday) {
        res = 1;
    } else {
        res = (2 - Qt::Monday) + locale.firstDayOfWeek();
    }

    QVariantMap obj;
    obj.insert("value", res);
    this->cb(scId, obj);
}

void Globalization::isDayLightSavingsTime(int scId, int ecId, const QVariantMap &options) {
    time_t time = options.find("time_t")->toLongLong() / 1000;
    const tm *desc = std::localtime(&time);
    if (desc->tm_isdst < 0) {
        this->callback(ecId, QString("new GlobalizationError(%1, 'information is not available');").arg(Globalization::UNKNOWN_ERROR));
        return;
    }
    this->callback(scId, QString("{dst:%1}").arg(desc->tm_isdst > 0 ? "true" : "false"));
}

QLocale::FormatType translateFormat(Globalization::Format formatLength) {
    QLocale::FormatType format = QLocale::ShortFormat;
    switch (formatLength) {
    case Globalization::FORMAT_FULL:
    case Globalization::FORMAT_LONG:
        format = QLocale::ShortFormat; // TODO: Qt cant parse string produced with QLocale::LongFormat;
        break;
    case Globalization::FORMAT_MEDIUM:
        format = QLocale::ShortFormat;
        break;
    case Globalization::FORMAT_SHORT:
        format = QLocale::NarrowFormat;
        break;
    }
    return format;
}

void Globalization::dateToString(int scId, int ecId, const QVariantMap &options) {
    time_t time = options.find("time_t")->toLongLong() / 1000;

    Globalization::Format formatLength = static_cast<Globalization::Format>(options.find("formatLength")->toInt());
    Globalization::Selector selector = static_cast<Globalization::Selector>(options.find("selector")->toInt());

    QLocale::FormatType format = translateFormat(formatLength);
    if (time < 0) {
        this->callback(ecId, QString("new GlobalizationError(%1, 'unsupported operation');").arg(Globalization::FORMATTING_ERROR));
        return;
    }

    QLocale locale;
    QString res;
    QDateTime dateTime = QDateTime::fromTime_t((uint)time);
    switch (selector) {
    case SELECTOR_ALL:
        res = locale.toString(dateTime,format);
        break;
    case SELECTOR_TIME:
        res = locale.toString(dateTime.time(), format);
        break;
    case SELECTOR_DATE:
        res = locale.toString(dateTime.date(), format);
        break;
    }
    QVariantMap obj;
    obj.insert("value", res);
    this->cb(scId, obj);
}

void Globalization::stringToDate(int scId, int ecId, const QVariantMap &options) {
    QString dateString = options.find("dateString")->toString();
    Globalization::Format formatLength = static_cast<Globalization::Format>(options.find("formatLength")->toInt());
    Globalization::Selector selector = static_cast<Globalization::Selector>(options.find("selector")->toInt());

    QLocale::FormatType format = translateFormat(formatLength);
    QLocale locale;
    bool valid(true);
    int year(0), month(0), day(0), hour(0), minute(0), second(0), millisecond(0);
    switch (selector) {
    case SELECTOR_ALL:
        {
            QDateTime dateTime = locale.toDateTime(dateString, format);
            valid = dateTime.isValid();
            QTime time = dateTime.time();
            hour = time.hour(); minute = time.minute(); second = time.second(); millisecond = time.msec();
            QDate date = dateTime.date();
            year = date.year(); month = date.month(); day = date.day();
        }
        break;
    case SELECTOR_TIME:
        {
            QTime time = locale.toTime(dateString, format);
            valid = time.isValid();
            hour = time.hour(); minute = time.minute(); second = time.second(); millisecond = time.msec();
        }
        break;
    case SELECTOR_DATE:
        {
            QDate date = locale.toDate(dateString, format);
            valid = date.isValid();
            year = date.year(); month = date.month(); day = date.day();
        }
        break;
    }
    if ((format == QLocale::NarrowFormat || format == QLocale::ShortFormat) && year < 2000 && year > 1900) {
        year += 100;
    }
    if (!valid) {
        this->callback(ecId, QString("new GlobalizationError(%1, 'parsing error')").arg(Globalization::PARSING_ERROR));
    } else {
        QVariantMap obj;
        obj.insert("year", year);
        obj.insert("month", month - 1);
        obj.insert("day", day);
        obj.insert("hour", hour);
        obj.insert("minute", minute);
        obj.insert("second", second);
        obj.insert("millisecond", millisecond);
        this->cb(scId, obj);
    }
}

void Globalization::getDateNames(int scId, int ecId, const QVariantMap &options) {
    Q_UNUSED(ecId)

    int type = options.find("type")->toInt();
    int item = options.find("item")->toInt();

    QLocale::FormatType format;
    if (type == FORMAT_SHORT)
        format = QLocale::ShortFormat;
    else
        format = QLocale::LongFormat;
    QLocale locale;
    QList<QString> res;
    if (item == REQUEST_DAY_NAMES) {
        for (int i = 1; i <= 7; i++) {
            res.append(locale.dayName(i, format));
        }
    } else { //REQUEST_MONTH_NAMES
        for (int i = 1; i <= 12; i++) {
            res.append(locale.monthName(i, format));
        }
    }

    QString result;
    for (QList<QString>::iterator it = res.begin(); it != res.end(); it++) {
        result += QString("'%1',").arg(*it);
    }
    this->callback(scId, QString("{ value: [ %1 ]}").arg(result));
}

template<class T>
static QString format(T number, Globalization::NumberType type) {
    QString res;
    QLocale locale;
    switch (type) {
    case Globalization::DECIMAL:
        res = locale.toString(number);
        break;
    case Globalization::PERCENT:
        res = locale.toString(number) + locale.percent();
        break;
    case Globalization::CURRENCY:
        res = locale.toCurrencyString(number);
        break;
    };
    return res;
}

void Globalization::numberToString(int scId, int ecId, const QVariantMap &options) {
    Q_UNUSED(ecId)

    bool isInt = options.find("isInt")->toBool();
    NumberType type = static_cast<NumberType>(options.find("type")->toBool());

    QString res;
    if (isInt) {
        long long number = options.find("number")->toLongLong();
        res = format(number, type);
    } else {
        double number = options.find("number")->toDouble();
        res = format(number, type);
    }
    this->callback(scId, QString("{ value: '%1' }").arg(res));
}

void Globalization::stringToNumber(int scId, int ecId, int type, QString string) {
    switch ((NumberType)type) {
    case Globalization::DECIMAL:
        string = string.remove(QLocale().groupSeparator());
        break;
    case Globalization::PERCENT:
        string = string.remove(QLocale().percent()).remove(QLocale().groupSeparator());
        break;
    case Globalization::CURRENCY:
        string = string.remove(QLocale().currencySymbol()).remove(QLocale().groupSeparator());
        break;
    };
    bool ok;
    double res = QLocale().toDouble(string, &ok);
    if (ok)
        this->callback(scId, QString("{ value: %1 }").arg(res));
    else
        this->callback(ecId, QString("new GlobalizationError(%1, 'parsing error')").arg(Globalization::PARSING_ERROR));
}

static QString ustr2qstr(UnicodeString &ustr) {
    std::string res;
    ustr.toUTF8String(res);

    return QString(res.c_str());
}

void Globalization::getNumberPattern(int scId, int ecId, int type) {
    Q_UNUSED(ecId);
    UErrorCode status = U_ZERO_ERROR;
    icu::DecimalFormat icu(status);

    icu::UnicodeString pattern;
    icu.toPattern(pattern);

    QLocale locale;
    QVariantMap obj;

    obj.insert("pattern", ustr2qstr(pattern));

    switch ((NumberType)type) {
    case Globalization::DECIMAL:
        obj.insert("symbol", "");
        break;
    case Globalization::PERCENT:
        obj.insert("symbol", QString(locale.percent()));
        break;
    case Globalization::CURRENCY:
        obj.insert("symbol", QString(locale.currencySymbol()));
        break;
    };

    obj.insert("fraction", icu.getMaximumFractionDigits());
    obj.insert("rounding", icu.getRoundingIncrement());
    obj.insert("positive", QString(locale.positiveSign()));
    obj.insert("negative", QString(locale.negativeSign()));
    obj.insert("decimal", QString(locale.decimalPoint()));
    obj.insert("grouping", QString(locale.groupSeparator()));

    this->cb(scId, obj);
}

static bool inDayLightSavingsTime() {
    time_t now;

    time(&now);

    const tm *desc = std::localtime(&now);

    return desc->tm_isdst > 0;
}

void Globalization::getDatePattern(int scId, int ecId, int formatLength, int selector) {
    Q_UNUSED(ecId);

    QLocale locale;
    QVariantMap res;
    QLocale::FormatType format = translateFormat((Format)formatLength);

    switch ((Selector)selector) {
    case Selector::SELECTOR_TIME:
        res.insert("pattern", locale.timeFormat(format));
        break;
    case Selector::SELECTOR_DATE:
        res.insert("pattern", locale.dateFormat(format));
        break;
    case Selector::SELECTOR_ALL:
        res.insert("pattern", locale.dateTimeFormat(format));
        break;
    };

    UnicodeString result;
    QSharedPointer<TimeZone> timezone = QSharedPointer<TimeZone>(TimeZone::createDefault());
    timezone->getDisplayName(inDayLightSavingsTime(), TimeZone::SHORT, result);

    res.insert("timezone", ustr2qstr(result));
    res.insert("utc_offset", timezone->getRawOffset() / 1000 + timezone->getDSTSavings() / 1000);
    res.insert("dst_offset", timezone->getDSTSavings() / 1000);

    this->cb(scId, res);
}

