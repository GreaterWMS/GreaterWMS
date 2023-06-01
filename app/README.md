yarn install

cordova platform add android

cordova platform add ios

quasar d -m cordova -T android

quasar build -m android

bundletool.jar build-apks --bundle=app-release.aab --output=GWMS.apks

bundletool.jar install-apks --apks=GWMS.apks
