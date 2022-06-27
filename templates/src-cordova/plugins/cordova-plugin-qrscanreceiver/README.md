# cordvoa-plugin-qrscanreceiver

通过BroadcastReceiver监听二维码识别获取二维码信息的cordova插件



注意，只对部分设备有效，主要还是推荐我写的另一个插件[cordova-plugin-pdascanner](https://github.com/plat10510/cordova-plugin-pdascanner.git)，感觉那个插件支持的设备会多一些。

## 安装(Installation)

`cordova plugin add cordova-plugin-qrscanreceiver`

如果是ionic项目则在cordova前加上ionic

`ionic cordova plugin add cordova-plugin-qrscanreceiver`

## 用法(Usage)

### cordova/phonegap项目(in cordova/phonegap)

```
window.addEventListener("getqrdata", getQRData, false);

function getQRData(data){
  console.log(data.data);
}
```

### ionic3+
`npm i qrscanreceiver`

添加至module.ts(Add to your app's module)
```
import { QRscanreceiver } from 'qrscanreceiver';

...
providers: [
    ...
    QRscanreceiver,
    ...
  ]
...
```

```

constructor(public navCtrl: NavController,public qrreceiver:QRscanreceiver) {


    qrreceiver.onReceiver().subscribe((data:any)=>{
      console.log(data.data);
    });

  }
```
