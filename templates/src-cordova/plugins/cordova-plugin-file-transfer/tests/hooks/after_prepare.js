#!/usr/bin/env node

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

var path = require('path');
var fs = require('fs');

module.exports = function(context) {
    function main() {
        // get the file transfer server address from the specified variables
        var fileTransferServerAddress = getFileTransferServerAddress(context) || getDefaultFileTransferServerAddress(context);
        console.log('Tests will use the following file transfer server address: ' + fileTransferServerAddress);
        console.log('If you\'re using cordova@6.3.1 and the above address is wrong at "platform add", don\'t worry, it\'ll fix itself on "cordova run" or "cordova prepare".');

        // pass it to the tests
        writeFileTransferOptions(fileTransferServerAddress, context);
    }

    function getDefaultFileTransferServerAddress(context) {
        var address = null;
        var configNodes = context.opts.plugin.pluginInfo._et._root._children;

        for (var node in configNodes) {
            if (configNodes[node].attrib.name == 'FILETRANSFER_SERVER_ADDRESS') {
                address = configNodes[node].attrib.default;
            }
        }

        return address;
    }

    function getFileTransferServerAddress(context) {
        var platformJsonFile = path.join(context.opts.projectRoot, 'platforms', context.opts.platforms[0], context.opts.platforms[0] + '.json');
        var platformJson = JSON.parse(fs.readFileSync(platformJsonFile, 'utf8'));

        if (platformJson && platformJson.installed_plugins && platformJson.installed_plugins['cordova-plugin-file-transfer-tests'] && platformJson.installed_plugins['cordova-plugin-file-transfer-tests'].FILETRANSFER_SERVER_ADDRESS) {
            return platformJson.installed_plugins['cordova-plugin-file-transfer-tests'].FILETRANSFER_SERVER_ADDRESS;
        } else {
            return null;
        }
    }

    function writeFileTransferOptions(address, context) {
        for (var p in context.opts.paths) {
            var ftOpts = {
                serverAddress: address
            };
            var ftOptsString = JSON.stringify(ftOpts);
            var ftOptsFile = path.join(context.opts.paths[p], 'fileTransferOpts.json');
            fs.writeFileSync(ftOptsFile, ftOptsString, 'utf8');
        }
    }

    main();

};
