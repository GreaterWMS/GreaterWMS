var exec = require('cordova/exec');
var cordova = require('cordova');


//先定义Scanreceiver，在QRScanreceiver里面addWindowEventHandler，监听getqrdata
var SeuicScanner = function(){
    this.data = null;
    cordova.addWindowEventHandler('getcodedata').onHasSubscribersChange = SeuicScanner.onHasSubscribersChange;
}

//指定回调，当插件初始化时响应
SeuicScanner.onHasSubscribersChange = function(){
    exec(scanreceiver._listen,scanreceiver._error,"SeuicScanner","start",[]);
}

//有二维码数据来时，激发getqrdata事件
SeuicScanner.prototype._listen = function(info){
    if(info){
        cordova.fireWindowEvent('getcodedata',info);
        scanreceiver.data = info.data;
    }
}
//插件初始化失败的回调
SeuicScanner.prototype._error = function(e){
    console.log('插件初始化错误，详情: ' + e);
}

var scanreceiver = new SeuicScanner();

module.exports = scanreceiver;