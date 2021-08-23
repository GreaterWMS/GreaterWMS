# 关于windows系统配置GreaterWMS的Android环境

**@author:Briliant Wang**



参考网页：http://www.quasarchs.com/quasar-cli/developing-cordova-apps/preparation/

以下是该网页的图解

## 1.首先我们第一步是确保安装了Cordova CLI和必要的SDK，可以如下操作：

![1629436491(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629436491(1).jpg)



结果如图这样就表示装好了。

## 2.下载Andriod studio，配置其环境

#### a.下载链接：https://developer.android.google.cn/studio/

​	<span style ='color:red'>注意：这里是官网的链接  我们需要下载的是专业版，注意在下载的时候选择专业版</span>

#### b.下载好Android studio后还需要安装两个东西

##### ①*来自Oracle的JDK。（也就是JAVA的JDK，这里必须下载特定的版本为Java 8 ）

​	为了方便下载可以点击链接下载：

链接：https://pan.baidu.com/s/1sHntW1ZR8h4kw5uwBGON5w 
提取码：jdk8

下载好后双击安装jdk  安装时记好安装的路径

设置环境变量：

![1629443442(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629443442(1).jpg)



![1629446724(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629446724(1).jpg)

②*Gradle. 曾经可以在Android Studio中使用，但是现在您必须单独安装它。 Cordova需要一个非常特定的版本。

下载链接：https://downloads.gradle-dn.com/distributions/gradle-4.10.3-all.zip

下载后解压缩，同样记住好路径

配置环境变量：

![1629447101(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629447101(1).jpg)

接下来Android studio 下载安装后会自动下载SDK，具体操作如图所示：

##### ③.打开Android studio

![1629432616(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629432616(1).jpg)



##### ④.选择安装sdk的目录

![1629432945(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629432945(1).jpg)



##### *选择所需的SDK。 根据2019年12月的数据，Cordova需要android-28（Android 9.0-Pie），因此请确保将其包括在内。 点击“Apply”安装SDK。

![1629448158(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629448158(1).jpg)

最后这些sdk建议都勾选上

![1629448475(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629448475(1).jpg)

勾选后别忘了apply

#### c.

##### ①确保在安装Android SDK之后，您可以接受其许可证。 打开终端并转到安装SDK的文件夹，在tools/bin中调用`sdkmanager --licenses`。

![1629441809(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629441809(1).jpg)

##### ② 在运行的时候会出现手动的操作：

![1629441730(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629441730(1).jpg)

#### d.配置Android的环境变量

![无标题属性](C:\Users\Brilliant Wang\Pictures\Saved Pictures\无标题属性.png)

![1629443404(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629443404(1).jpg)





![1629444484(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629444484(1).jpg)



![1629443442(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629443442(1).jpg)



![1629443921(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629443921(1).jpg)



![1629443924(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629443924(1).jpg)



#### e.配置剩下的环境变量：



![1629447317(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629447317(1).jpg)





![1629447897(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629447897(1).jpg)

最后点击确定退出。

### 3.检查安装好的环境

进入项目的src-cordova运行终端



![1629448776(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629448776(1).jpg)

输入cordova requirements检查环境，如果成功的话如下所示：

![1629449040(1)](C:\Users\Brilliant Wang\Pictures\Saved Pictures\1629449040(1).jpg)

到此环境就装好了。
