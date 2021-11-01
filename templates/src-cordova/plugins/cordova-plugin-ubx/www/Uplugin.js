var exec = require('cordova/exec');

exports.getDeviceID = function (arg0, success, error) {
    exec(success, error, 'Uplugin', 'getDeviceID', [arg0]);
};

exports.getBarcode = function (arg0, success, error) {
    exec(success, error, 'Uplugin', 'getBarcode', [arg0]);
};
