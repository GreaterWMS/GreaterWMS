<div align="center">
  <img src="static/img/logo.png" alt="GreaterWMS logo" width="200" height="auto" />
  <h1>GreaterWMS</h1>
  <p>完全开源的仓库管理系统</p>

<!-- Badges -->
![License: APLv2](https://img.shields.io/github/license/GreaterWMS/GreaterWMS)
![Release Version (latest Version)](https://img.shields.io/github/v/release/GreaterWMS/GreaterWMS?color=orange&include_prereleases)
![QR Code Support](https://img.shields.io/badge/QR--Code-Support-orange.svg)
![Docker Support](https://img.shields.io/badge/Docker-Support-orange.svg)
![i18n Support](https://img.shields.io/badge/i18n-Support-orange.svg)

![repo size](https://img.shields.io/github/repo-size/GreaterWMS/GreaterWMS)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/GreaterWMS/GreaterWMS)
![Contributors](https://img.shields.io/github/contributors/GreaterWMS/GreaterWMS?color=blue)

![GitHub Org's stars](https://img.shields.io/github/stars/GreaterWMS?style=social)
![GitHub Follows](https://img.shields.io/github/followers/Singosgu?style=social)
![GitHub Forks](https://img.shields.io/github/forks/GreaterWMS/GreaterWMS?style=social)
![GitHub Watch](https://img.shields.io/github/watchers/GreaterWMS/GreaterWMS?style=social)

![Python](https://img.shields.io/badge/Python-3.8.10-yellowgreen)
![Django](https://img.shields.io/badge/Django-4.1.2-yellowgreen)
![Quasar Cli](https://img.shields.io/badge/Quasar/cli-1.2.1-yellowgreen)
![Vue](https://img.shields.io/badge/Vue-2.6.0-yellowgreen)
![NodeJS](https://img.shields.io/badge/NodeJS-14.19.3-yellowgreen)

[![BiliBili](https://img.shields.io/badge/BiliBili-4987-red)](https://space.bilibili.com/407321291/channel/seriesdetail?sid=776320)
</div>

## :rocket: 找到我们
<h4>
    <a href="https://www.56yhz.com/">官网首页</a>
</h4>
<h4>
    <a href="https://production.56yhz.com/">演示地址</a>
</h4>
<h4>
  <a href="https://space.bilibili.com/407321291?spm_id_from=333.1007.0.0">教程视频</a>
</h4>
<h4>
  <a href="https://github.com/GreaterWMS/GreaterwMS/issues/new?template=bug_report.md&title=[BUG]">提交一个Bug</a>
</h4>
<h4>   
  <a href="https://github.com/GreaterWMS/GreaterWMS/issues/new?template=feature_request.md&title=[FR]">提交一个建议</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/greaterwms.html">英文文档</a>
</h4>

QQ技术交流群：289548524

[//]: # (About the Project)
### :star2: 关于此项目

该库存管理系统是，目前福特亚太区售后物流仓储供应链流程。
离开福特后，我开始了这个项目。 为了帮助一些有需要的人。
OneAPP 理念。 支持扫描设备PDA、手机APP、桌面exe、网站等。

[//]: # (Function)
## :dart: 模块

* [x] 多仓
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

[//]: # (Install)
## :compass: 安装
python安装
- [python 3.8.10](https://www.python.org/downloads/release/python-3810/)

nodejs安装
- [nodejs 14.19.3](https://nodejs.org/download/release/v14.19.3/)

Twisted安装
- Twisted在某些情况下安装很困难，请自行百度安装方法

克隆代码
~~~shell
git clone https://gitee.com/Singosgu/GreaterWMS.git
~~~

### docker(可选择)
~~~shell
cd GreaterWMS/
docker-compose up -d
# 修改请求地址
# baseurl GreaterWMS/templates/public/statics/baseurl.txt
docker-compose restart
~~~

<h4>
  <a href="https://www.56yhz.com/zh/win_10.html">Windows X64</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh/centos_7.html">Centos 7</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh/ubuntu_20.html">Ubuntu 20</a>
</h4>

[//]: # (development)
## :hammer_and_wrench: 怎么启动开发环境:

- 启动后端环境:
~~~shell
cd GreaterWMS
daphne -p 8008 greaterwms.asgi:application
or
daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application # 局域网
~~~

- 启动前端环境:
~~~shell
cd templates
quasar d # http://localhost:8080
or
quasar dev # http://localhost:8080
~~~

- 请求地址修改
~~~shell
templates/public/statics/baseurl.txt
~~~

- API文档

~~~shell
baseurl + '/docs/'
~~~

### 配套的手机APP

- App源码编译

~~~shell
npm install cordova -g

cd app
yarn install
## 开发环境
quasar d -m cordova -T [android, ios]
## 构建打包
quasar build -m [android, ios]
~~~

- 你不想编译也可以直接使用

[IOS](https://apps.apple.com/cn/app/%E6%99%BA%E8%83%BD%E4%BB%93%E5%82%A8%E8%BD%AF%E4%BB%B6gwms/id6444078526)

[Android](https://production.56yhz.com/media/GWMS.apks)

GreaterWMS有配套的APP，支持手机扫描，和PDA扫描，配置下服务器请求地址即可

## 下载apks安装工具

!!! info "Android"
    
    应用商店搜索

    Split APKs Installer 

## 或直接下载apks安装工具

[Sai](https://po.56yhz.com/media/sai.apk)

- 打开Sai APP，选择下载的GWMS.apks，即可完成安装

[//]: # (publish)
## :trumpet: 怎么构建你的app:

- 网页版构建:

~~~shell
cd templates
quasar build # /templates/dist/spa
~~~

[//]: # (deploy)
## :computer: 怎么部署到服务器:

<h4>
  <a href="https://www.56yhz.com/zh/supervisor_process_guarded.html">Supervisor教程</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/zh/nginx_config.html">Nginx配置</a>
</h4>

记得启用ssl的话，需要额外配置
在前端代码中进行编辑

## Show
<div align="left">
    <img src="static/img/GreaterWMS.png" alt="GreaterWMS home" width="" height="400" />
</div>
<div align="left">
    <img src="static/img/mobile_splash.jpg" alt="GreaterWMS splash" width="200" height="400" />
    <img src="static/img/mobile_dn.jpg" alt="GreaterWMS dn" width="200" height="400" />
    <img src="static/img/mobile_equ.jpg" alt="GreaterWMS goods" width="200" height="400" />
</div>

<!-- ABOUT AUTHOR -->
## :bowing_man: 关于作者

[Elvis.Shi](https://gitee.com/GreaterWMS/GreaterWMS/wikis/%E6%88%91%E6%98%AF%E5%A6%82%E4%BD%95%E4%BB%8E%E4%B8%80%E4%B8%AA%E7%89%A9%E6%B5%81%E8%8F%9C%E9%B8%9F%EF%BC%8C%E4%B8%80%E7%9B%B4%E5%81%9A%E5%88%B0500%E5%BC%BA%E4%BA%9A%E5%A4%AA%E5%8C%BAChina%20PDC%20Manager%E7%9A%84)
