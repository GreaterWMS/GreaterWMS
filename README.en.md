<div align="center">
  <img src="static/img/logo.png" alt="GreaterWMS logo" width="200" height="auto" />
  <h1>GreaterWMS</h1>
  <p>Open Source Inventory Management System </p>

<!-- Badges -->
[![License: APLv2](https://img.shields.io/github/license/GreaterWMS/GreaterWMS)](https://opensource.org/licenses/Apache-2.0/)
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

![Python](https://img.shields.io/badge/Python-3.9.5-yellowgreen)
![Django](https://img.shields.io/badge/Django-3.1.14-yellowgreen)
![Quasar Cli](https://img.shields.io/badge/Quasar/cli-1.2.1-yellowgreen)
![Vue](https://img.shields.io/badge/Vue-2.6.0-yellowgreen)
![NodeJS](https://img.shields.io/badge/NodeJS-14.19.3-yellowgreen)

[![YouTube](https://img.shields.io/youtube/channel/subscribers/UCPW1wciGMIEh7CYOdLnsloA?color=red&label=YouTube&logo=youtube&style=for-the-badge)](https://www.youtube.com/channel/UCPW1wciGMIEh7CYOdLnsloA)
</div>

[//]: # (Some Link)
## :rocket: Link US
<h4>
    <a href="https://www.56yhz.com/">Home Page</a>
</h4>
<h4>
  <a href="https://www.youtube.com/channel/UCPW1wciGMIEh7CYOdLnsloA">Video Tutorials</a>
</h4>
<h4>
  <a href="https://github.com/GreaterWMS/GreaterwMS/issues/new?template=bug_report.md&title=[BUG]">Report Bug</a>
</h4>
<h4>   
  <a href="https://github.com/GreaterWMS/GreaterWMS/issues/new?template=feature_request.md&title=[FR]">Request Feature</a>
</h4>
<h4>
  <a href="https://gitee.com/GreaterwMS/GreaterWMS/blob/master/README.zh-CN.md">中文文档</a>
</h4>

[//]: # (About the Project)
## :star2: About the Project

This Inventory management system is the currently Ford Asia Pacific after-sales logistics warehousing supply chain process .
After I leave Ford , I start this project . In order to help some who need it . 
OneAPP Type . Support scanner PDA, mobile APP, desktop exe, website as well .

[//]: # (Function)
## :dart: Function

* [x] Supplier Management
* [x] Customer Management
* [x] Scanner PDA
* [x] Cycle Count
* [x] Order Management
* [x] Stock Control
* [x] Safety Stock Show
* [x] API Documents
* [x] IOS APP Support
* [x] Android APP Support
* [x] Electron APP Support
* [x] Auto Update
* [x] i18n Support
* [x] API Documents

[//]: # (development)
## :eyes: Where is APIs Documents:

- After installed you can find APIs Documents from url /docs/

~~~shell
example: http://127.0.0.1:8008/docs/
~~~

[//]: # (Install)
## :compass: Install
~~~shell
git clone https://github.com/GreaterWMS/GreaterWMS.git
~~~

### docker
~~~shell
cd GreaterWMS/
docker-compose up -d
# Change Front Request Baseurl
# baseurl GreaterWMS/templates/public/statics/baseurl.js
# change the baseurl and wsurl
docker-compose restart
~~~

<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/3/">Windows X64</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/4/">Centos 7</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/5/">Ubuntu 20</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/6/">IOS Environment</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/7/">Android Environment</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/8/">Android APK Signed</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/11/">Electron Environment</a>
</h4>

[//]: # (development)
## :hammer_and_wrench: How To Run Development Server:

- Webside Dev Run:

~~~shell
cd templates
quasar d # http://localhost:8080
or
quasar dev # http://localhost:8080
~~~

- Electron APP Dev Run

~~~shell
cd templates
quasar d -m electron
or
quasar dev -m electron
~~~

- Mobile APP Dev Run

You should connect your mobile . Sometime it need you choose the ip , the ip is your PC's internal ip . 
The Android APP installed on the mobile phone is the mobile page, and the installation on the scanning device is the scanning page.

~~~shell
cd templates/src-cordova
cordova platform add [ios or android]
cd .. # back to templates
quasar d -m cordova -T [ios or android]
~~~

[//]: # (publish)
## :trumpet: How To Publish Your APP:

- Webside Build:

~~~shell
cd templates
quasar build # /templates/dist/spa
~~~

- Electron APP Build:

~~~shell
quasar build -m electron -P always # /templates/dist/electron
~~~

- Mobile APP Build:

~~~shell
quasar build -m cordova -T [ios or android] # /templates/dist/cordova
~~~

[//]: # (deploy)
## :computer: How To Deploy Server:

<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/9/">Supervisor Process Guarded</a>
</h4>
<h4>
  <a href="https://www.56yhz.com/en-us/docs/2/10/">Nginx Config</a>
</h4>

If the server has SSL enabled, please use https and wss, if SSL is not enabled, use http and ws

The front-end code needs to be rebuilt after modification

<!-- Sponsor -->
## :money_with_wings: Sponsor

If you use GreaterWMS and find it to be useful, please consider making a donation toward its continued development.

[Donate via PayPal](https://paypal.me/singosgu)

<!-- License -->
## :warning: License

Distributed under the [APL v2](https://opensource.org/licenses/Apache-2.0/) License. See [LICENSE.txt](https://github.com/GreaterWMS/GreaterWMS/blob/master/LICENSE) for more information.

<!-- COMMERCIAL LICENSE -->
## :old_key: Commercial License

- Don't worry about Commercial License. You will get Free Commercial License while you download the source code .
