/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
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

var Compass = {
    getHeading: function(success, error) {
        var orient = {};
        var heading = (Math.round((Math.random() * 360) * 100) / 100);

        orient.trueHeading = heading;
        orient.magneticHeading = heading;
        orient.headingAccuracy = 0;
        orient.timestamp = new Date().getTime();

        success(orient);
    }
};

module.exports = Compass;
require('cordova/exec/proxy').add('Compass', Compass);
