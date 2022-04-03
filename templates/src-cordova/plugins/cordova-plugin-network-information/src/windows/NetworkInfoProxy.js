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

/* global Windows:true */

var Connection = require('./Connection');

var winNetConn = Windows.Networking.Connectivity;
var networkInfo = winNetConn.NetworkInformation;

function getCurrrentConnectionType () {
    var profile = networkInfo.getInternetConnectionProfile();

    if (!profile) {
        return Connection.NONE;
    }

    var conLevel = profile.getNetworkConnectivityLevel();
    var interfaceType = profile.networkAdapter.ianaInterfaceType;

    // since we use this to detect whether we are online or offline we do check agains InternetAccess
    // localAccess (airplane mode as an example) or constrainedInternetAccess mean there is no access to the internet available
    // https://msdn.microsoft.com/library/windows/apps/windows.networking.connectivity.networkconnectivitylevel.aspx
    if (conLevel !== Windows.Networking.Connectivity.NetworkConnectivityLevel.internetAccess) {
        return Connection.NONE;
    }

    var connectionType;

    switch (interfaceType) {
    case 71:
        connectionType = Connection.WIFI;
        break;
    case 6:
        connectionType = Connection.ETHERNET;
        break;
    case 243: // (3GPP WWAN) // Fallthrough is intentional
    case 244: // (3GPP2 WWAN)
        connectionType = Connection.CELL_3G;
        break;
    default:
        connectionType = Connection.UNKNOWN;
        break;
    }

    return connectionType;
}

module.exports = {

    getConnectionInfo: function (win, fail, args) {
        var reportConnectionInfoOnce = function () {
            win(getCurrrentConnectionType(), { keepCallback: true });
        };

        // report current connection  type
        setTimeout(reportConnectionInfoOnce, 0);
        // start traking future changes
        networkInfo.addEventListener('networkstatuschanged', reportConnectionInfoOnce);
    }
};

require('cordova/exec/proxy').add('NetworkStatus', module.exports);
