var exec = require('cordova/exec');
var cordova = require('cordova');


//先定义QRScanreceiver，在QRScanreceiver里面addWindowEventHandler，监听getqrdata
var QRScanreceiver = function(){
    this.data = null;
    cordova.addWindowEventHandler('getqrdata').onHasSubscribersChange = QRScanreceiver.onHasSubscribersChange;
}

//指定回调，当插件初始化时响应
QRScanreceiver.onHasSubscribersChange = function(){
    exec(qrscanreceiver._listen,qrscanreceiver._error,"qrscanreceiver","start",[]);
}

//有二维码数据来时，激发getqrdata事件
QRScanreceiver.prototype._listen = function(info){
    if(info){
        cordova.fireWindowEvent('getqrdata',info);
        qrscanreceiver.data = info.data;
    }
}
//插件初始化失败的回调
QRScanreceiver.prototype._error = function(e){
    console.log('插件初始化错误，详情: ' + e);
}

var qrscanreceiver = new QRScanreceiver();

module.exports = qrscanreceiver;