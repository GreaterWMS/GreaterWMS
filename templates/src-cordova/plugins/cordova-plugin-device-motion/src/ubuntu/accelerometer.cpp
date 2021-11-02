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

#include <cassert>
#include "accelerometer.h"

DeviceMotion::DeviceMotion(Cordova *cordova): CPlugin(cordova), _scId(0), _ecId(0) {
    _accelerometerSource = QSharedPointer<QAccelerometer>(new QAccelerometer());
    _sensorAvaliable = _accelerometerSource->start();
    connect(_accelerometerSource.data(), SIGNAL(readingChanged()), SLOT(updateSensor()));
}

void DeviceMotion::start(int scId, int ecId) {
    assert(_ecId == 0);
    assert(_scId == 0);

    _ecId = ecId;
    _scId = scId;

    if (!_sensorAvaliable) {
        this->cb(ecId);
        return;
    }
}

void DeviceMotion::stop(int, int) {
    _scId = 0;
    _ecId = 0;
}

void DeviceMotion::updateSensor() {
    QAccelerometerReading *accelerometer = _accelerometerSource->reading();

    QVariantMap obj;
    obj.insert("x", accelerometer->x());
    obj.insert("y", accelerometer->y());
    obj.insert("z", accelerometer->z());
    // accelerometer->timestamp() is not sutiable.
    // Timestamps values are microseconds since _a_ fixed point(depend on backend).
    obj.insert("timestamp", QDateTime::currentDateTime().toMSecsSinceEpoch());

    if (_scId)
        this->callbackWithoutRemove(_scId, CordovaInternal::format(obj));
}
