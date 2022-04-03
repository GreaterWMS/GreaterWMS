## RFduino LED Button

Requires an [RFduino](http://rfudino.com) running the [LED Button sketch](https://github.com/RFduino/RFduino/blob/cfe1a448524f2dafc25f62cccd900484925bba8a/libraries/RFduinoBLE/examples/LedButton/LedButton.ino).

Hardware

 * [RFduino](http://www.rfduino.com/product/rfd22102-rfduino-dip/)
 * [Button Shield](http://www.rfduino.com/product/rfd22122-rgb-button-shield-for-rfduino/)
 * [USB Shield](http://www.rfduino.com/product/rfd22124-pcb-usb-shield-for-rfduino/)


Install

    $ cordova platform add android ios
    $ cordova plugin add cordova-plugin-ble-central
    $ cordova run
