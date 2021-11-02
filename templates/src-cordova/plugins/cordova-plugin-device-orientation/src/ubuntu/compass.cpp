/*
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

#include "compass.h"

DeviceOrientation::DeviceOrientation(Cordova *cordova): CPlugin(cordova), _validData(false) {
    _compass.connectToBackend();
    connect(&_compass, SIGNAL(readingChanged()), SLOT(updateSensor()));
    connect(&_compass, SIGNAL(sensorError(int)), SLOT(sensorError(int)));
}

void DeviceOrientation::getHeading(int scId, int ecId, QVariantMap options) {
    Q_UNUSED(options);
    if (_compass.isConnectedToBackend() || !_compass.start()) {
        this->callback(ecId, "CompassError.COMPASS_NOT_SUPPORTED");
        return;
    }

    _successCallbacks << scId;
    _errorCallbacks << ecId;

    if (_validData) {
        reportResult();
        return;
    }
}

void DeviceOrientation::sensorError(int error) {
    Q_UNUSED(error);

    for (int ecId: _errorCallbacks) {
        this->callback(ecId, "CompassError.COMPASS_INTERNAL_ERR");
    }

    _errorCallbacks.clear();
    _successCallbacks.clear();
    _validData = false;
}

void DeviceOrientation::reportResult() {
    QVariantMap obj;

    obj.insert("magneticHeading", _azymuth);
    obj.insert("trueHeading", _azymuth);
    obj.insert("headingAccuracy", _accuracy);
    obj.insert("timestamp", _timestamp);

    for (int scId: _successCallbacks) {
        this->cb(scId, obj);
    }

    _errorCallbacks.clear();
    _successCallbacks.clear();
}

void DeviceOrientation::updateSensor(){
    QCompassReading *heading = _compass.reading();
    _azymuth = heading->azimuth();
    _accuracy = heading->calibrationLevel();
    _timestamp = QDateTime::currentDateTime().toMSecsSinceEpoch();

    _validData = true;
    reportResult();
}
