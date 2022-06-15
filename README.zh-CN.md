<div align="center">
  <img src="static/img/logo.png" alt="GreaterWMS logo" width="200" height="auto" />
  <h1>GreaterWMS</h1>
  <p>完全开源的仓库管理系统</p>

<!-- Badges -->
[![License: GPLv3](https://img.shields.io/github/license/Singosgu/GreaterWMS)](https://www.gnu.org/licenses/gpl-3.0.html)
![Release Version (latest Version)](https://img.shields.io/github/v/release/Singosgu/GreaterWMS?color=orange&include_prereleases)
![QR Code Support](https://img.shields.io/badge/QR--Code-Support-orange.svg)
![Docker Support](https://img.shields.io/badge/Docker-Support-orange.svg)
![i18n Support](https://img.shields.io/badge/i18n-Support-orange.svg)

![repo size](https://img.shields.io/github/repo-size/Singosgu/GreaterWMS)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Singosgu/GreaterWMS)
![Contributors](https://img.shields.io/github/contributors/Singosgu/GreaterWMS?color=blue)

![GitHub Org's stars](https://img.shields.io/github/stars/Singosgu?style=social)
![GitHub Follows](https://img.shields.io/github/followers/Singosgu?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Singosgu/GreaterWMS?style=social)
![GitHub Watch](https://img.shields.io/github/watchers/Singosgu/GreaterWMS?style=social)

![Python](https://img.shields.io/badge/Python-3.9.5-yellowgreen)
![Django](https://img.shields.io/badge/Django-3.1.14-yellowgreen)
![Quasar Cli](https://img.shields.io/badge/Quasar/cli-1.2.1-yellowgreen)
![Vue](https://img.shields.io/badge/Vue-2.6.0-yellowgreen)
![NodeJS](https://img.shields.io/badge/NodeJS-14.19.3-yellowgreen)

[![BiliBili](https://img.shields.io/badge/BiliBili-4987-red)](https://space.bilibili.com/407321291/channel/seriesdetail?sid=776320)
</div>

[//]: # (Some Link)
## :rocket: 找到我们
<h4>
    <a href="https://www.56yhz.com/">官网首页</a>
</h4>
<h4>
  <a href="https://space.bilibili.com/407321291/channel/seriesdetail?sid=776320">相关视频</a>
</h4>
<h4>
  <a href="https://github.com/Singosgu/GreaterwMS/issues/new?template=bug_report.md&title=[BUG]">提交一个Bug</a>
</h4>
<h4>   
  <a href="https://github.com/Singosgu/GreaterWMS/issues/new?template=feature_request.md&title=[FR]">提交一个建议</a>
</h4>
<h4>
  <a href="https://gitee.com/GreaterWMS/GreaterWMS/blob/master/README.en.md">英文文档</a>
</h4>

[//]: # (About the Project)
### :star2: 关于此项目

该库存管理系统是，目前福特亚太区售后物流仓储供应链流程。
离开福特后，我开始了这个项目。 为了帮助一些有需要的人。
OneAPP 理念。 支持扫描设备PDA、手机APP、桌面exe、网站等。

[//]: # (Function)
## :dart: 模块

* [x] 供应商管理
* [x] 客户管理
* [x] 扫描设备PDA
* [x] 盘点
* [x] 订单管理
* [x] 库存管理
* [x] 安全库存
* [x] API文档
* [x] IOS APP支持
* [x] Android APP支持
* [x] Electron APP支持
* [x] 自动更新
* [x] i18n国际化

[//]: # (development)
## :eyes: API文档在哪里:

- 当你安装完成后，可以通过此链接找到API文档 /docs/

~~~shell
例子: http://127.0.0.1:8008/docs/
~~~

[//]: # (Install)
## :compass: 安装
~~~shell
git clone https://github.com/Singosgu/GreaterWMS.git
~~~
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/3/">Windows X64</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/4/">Centos 7</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/5/">Ubuntu 20</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/6/">IOS 环境</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/7/">Android 环境</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/8/">Android APK 签名</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/12/">Electron 环境</a>
</h4>

[//]: # (development)
## :hammer_and_wrench: 怎么启动开发环境:

- 启动网页开发环境:

~~~shell
cd templates
quasar d # http://localhost:8080
or
quasar dev # http://localhost:8080
~~~

- 启动Electron开发环境

~~~shell
cd templates
quasar d -m electron
or
quasar dev -m electron
~~~

- 启动手机开发环境

你需要链接你的手机，打开usb调试，有时候需要选择ip地址，记得要选择你的电脑的局域网ip. 
Android APP安装到手机就是手机页面，安装到扫描设备，就是扫描页面。

~~~shell
cd templates/src-cordova
cordova platform add [ios or android]
cd .. # back to templates
quasar d -m cordova -T [ios or android]
~~~

[//]: # (publish)
## :trumpet: 怎么构建你的app:

- 网页版构建:

~~~shell
cd templates
quasar build # /templates/dist/spa
~~~

- Electron APP构建

~~~shell
quasar build -m electron -P always # /templates/dist/electron
~~~

- 移动APP构建

~~~shell
quasar build -m cordova -T [ios or android] # /templates/dist/cordova
~~~

[//]: # (deploy)
## :computer: 怎么部署到服务器:

<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/9/">Supervisor教程</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh-hans/docs/39/10/">Nginx配置</a>
</h4>

记得启用ssl的话，需要额外配置
在前端代码中进行编辑

<!-- Sponsor -->
## :money_with_wings: 打赏

如果你觉得我们的项目对你有所帮助，可以请我们喝杯咖啡，我们会更好的维护这个项目。

<div align="left">
    <img src="static/img/wechat.jpg" alt="GreaterWMS wechat" width="" height="300" />
    <img src="static/img/alipay.jpg" alt="GreaterWMS alipay" width="" height="300" />
</div>

<!-- License -->
## :warning: License

该项目使用的是 [GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) 协议. 详情查阅[LICENSE.txt](https://gitee.com/GreaterWMS/GreaterWMS/blob/master/LICENSE).必须遵守此协议。
