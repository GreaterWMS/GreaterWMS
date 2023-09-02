var exec = require('cordova/exec');
var cordova = require('cordova');

var iDataScanner = function(){
    this.data = null;
    cordova.addWindowEventHandler('idatadata').onHasSubscribersChange = iDataScanner.onHasSubscribersChange;
}

iDataScanner.onHasSubscribersChange = function(){
    exec(scanreceiver._listen,scanreceiver._error,"iDataScanner","start",[]);
}

iDataScanner.prototype._listen = function(info){
    if(info){
        cordova.fireWindowEvent('idatadata',info);
        scanreceiver.data = info.data;
    }
}

iDataScanner.prototype._error = function(e){
    console.log('插件初始化错误，详情: ' + e);
}


var scanreceiver = new iDataScanner();

module.exports = scanreceiver;
