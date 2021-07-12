~~~shell
如何配置Cordova环境，请参考
http://www.quasarchs.com/quasar-cli/developing-cordova-apps/preparation

# 进入templates目录，创建src-cordova
quasar mode add cordova
# 进入src-cordova目录
cd src-cordova
# 部署安卓客户端
cordova platform add android
输入app名称为org.greaterwms.app
# 返回templates目录，先启动一次项目来创建gradle文件夹
quasar d -m cordova -T andorid
Ctrl + c退出
# 修改gradle版本下载distributionUrl，文件在tempates/src-cordova/platforms/android/gradle/wrapper/gradle-wrapper.properties
distributionUrl=https://mirrors.cloud.tencent.com/gradle/gradle-4.10.3-all.zip
# 进入src-cordova目录来安装所需要的插件
cd src-cordova
# 按顺序安装插件
cordova plugin add cordova-plugin-device
cordova plugin add cordova-plugin-battery-status
cordova plugin add cordova-plugin-camera
cordova plugin add com-darryncampbell-cordova-plugin-intent
# 修改适配问题的文件，templates\src-cordova\platforms\android\app\src\main\java\org\apache\cordova\camera\FileProvider.java
第21行的android.support.v4.content.FileProvider，修改为androidx.core.content.FileProvider
# 修改适配问题的文件，templates\src-cordova\platforms\android\app\src\main\java\org\apache\cordova\camera\CameraLauncher.java
第42行的android.support.v4.content.FileProvider，修改为androidx.core.content.FileProvider
# 回到templates，再次启动项目
quasar d -m cordova -T andorid

现在只支持Zebra扫描枪，Zebra扫描枪需要打开广播


# 打包apk
quasar build -m android

接下来在dist/cordova/android/apk/release下面可以找到一个未签名的apk，关于怎么签名，自行百度
~~~