/*
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

var cordova = require('cordova');
var proxy = require('cordova/exec/proxy');
var Connection = require('./Connection');

var type = navigator.onLine ? Connection.UNKNOWN : Connection.NONE;

// Subscribe to 'native' online/offline events
function onStatusChange (evt) {
    type = navigator.onLine ? Connection.UNKNOWN : Connection.NONE;
    // force async
    setTimeout(function () {
        cordova.fireDocumentEvent(evt.type);
    }, 0);
}

window.addEventListener('online', onStatusChange);
window.addEventListener('offline', onStatusChange);

proxy.add('NetworkStatus', {
    getConnectionInfo: function (cbSuccess) {
        // force async
        setTimeout(function () {
            cbSuccess(type);
        }, 0);
    }
});
