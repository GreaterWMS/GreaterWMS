cordova.define("cordova-plugin-ubx.Uplugin", function(require, exports, module) {
var exec = require('cordova/exec');

exports.getDeviceID = function (arg0, success, error) {
    exec(success, error, 'Uplugin', 'getDeviceID', [arg0]);
};

exports.getBarcode = function (arg0, success, error) {
    exec(success, error, 'Uplugin', 'getBarcode', [arg0]);
};

});
