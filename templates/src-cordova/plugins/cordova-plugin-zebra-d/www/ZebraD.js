var exec = require('cordova/exec');
var ZebraD = {
  getSerialNumber: (success, error) => {
    exec(success, error, "ZebraD", 'getSerialNumber', []);
  },
  getIMEINumber: (success, error) => {
    exec(success, error, "ZebraD", 'getIMEINumber', []);
  },
}
module.exports = ZebraD;
