/*
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

#ifndef ACCELEROMETER_H
#define ACCELEROMETER_H

#include <cplugin.h>
#include <QAccelerometer>
#include <QtCore>

class DeviceMotion: public CPlugin {
    Q_OBJECT
public:
    explicit DeviceMotion(Cordova *cordova);

    virtual const QString fullName() override {
        return DeviceMotion::fullID();
    }

    virtual const QString shortName() override {
        return "Accelerometer";
    }

    static const QString fullID() {
        return "Accelerometer";
    }

public slots:
    void start(int scId, int ecId);
    void stop(int scId, int ecId);

protected slots:
    void updateSensor();

private:
    int _scId, _ecId;
    bool _sensorAvaliable;
    QSharedPointer<QAccelerometer> _accelerometerSource;
};

#endif
