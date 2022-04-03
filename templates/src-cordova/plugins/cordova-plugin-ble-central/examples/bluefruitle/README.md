## Adafruit UART

This example will connect to hardware running the Nordic UART service. Many of the Bluetooth LE products from Adafruit run the Nordic UART service. This example will also connect to the [Adafruit Bluefruit LE Friend](https://www.adafruit.com/products/2267), [puck.js](http://puckjs.com), or [BBC Micro:bit](http://microbit.org/) running [Espruino](http://www.espruino.com/).

## Android

	cordova platform add android
	cordova run android --device

NOTE: Some Android devices have trouble filtering by UUID when scanning. If your Android phone can't find your Bluetooth peripheral, try removing the service filter.

Change 

	ble.scan([bluefruit.serviceUUID], 5, app.onDiscoverDevice, app.onError);

To 

	ble.scan([], 5, app.onDiscoverDevice, app.onError);

## iOS

	cordova platform add ios
	cordova run ios --device
	
Note: Sometimes Xcode can't deploy from the command line. If that happens, open BluefruitLE.xcworkspace and deploy to your phone using Xcode.

    open platforms/ios/BluefruitLE.xcworkspace

## Building a Peripheral

If you have an Arduino Uno and [Adafruit's Bluefruit LE](http://www.adafruit.com/products/1697) breakout board. You can run the [callbackEcho sketch](https://github.com/adafruit/Adafruit_nRF8001/blob/master/examples/callbackEcho/callbackEcho.ino) and see [Adafruit's tutorial](https://learn.adafruit.com/getting-started-with-the-nrf8001-bluefruit-le-breakout/software-uart-service) for setting up the hardware and Arduino code.

Hardware

 * [Arduino](http://www.adafruit.com/products/50)
 * [BluefruitLE](http://www.adafruit.com/products/1697)

