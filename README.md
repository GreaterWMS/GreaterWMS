<div align="center">
  <img src="static/img/logo.png" alt="GreaterWMS logo" width="200" height="auto" />
  <h1>GreaterWMS</h1>
  <p>Open Source Inventory Management System </p>

<!-- Badges -->
[![License: GPLv3](https://img.shields.io/github/license/Singosgu/GreaterWMS)](https://www.gnu.org/licenses/gpl-3.0.html)
![Release Version (latest Version)](https://img.shields.io/github/v/release/Singosgu/GreaterWMS?color=orange&include_prereleases)
![QR Code Support](https://img.shields.io/badge/QR--Code-Support-orange.svg)
![Docker Support](https://img.shields.io/badge/Docker-Support-orange.svg)
![i18n Support](https://img.shields.io/badge/i18n-Support-orange.svg)

![repo size](https://img.shields.io/github/repo-size/Singosgu/GreaterWMS)
![Lines of code](https://img.shields.io/tokei/lines/github/Singosgu/GreaterWMS)
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
  <a href="https://github.com/Singosgu/GreaterwMS/issues/new?template=bug_report.md&title=[BUG]">Report Bug</a>
</h4>
<h4>   
  <a href="https://github.com/Singosgu/GreaterWMS/issues/new?template=feature_request.md&title=[FR]">Request Feature</a>
</h4>
<h4>
  <a href="https://github.com/Singosgu/GreaterWMS/blob/master/README_zh_Hans.md">中文文档</a>
</h4>

[//]: # (About the Project)
## :star2: About the Project

I have 15 years old experience focus on supply chain . I find that in this professional field . No freedom customize software can support our business deeply . Any software are closed-source and hardly to customize or dynamic with our suppliers & customers . So I design GreaterWMS , in order to give business highest freedom way to support trade development .

- Our Vision: If you work in a non IT industry and you love your industry, please using technology to change it.

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

[//]: # (Install)
## :compass: Install

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
### :hammer_and_wrench: How To Run Development Server:

- Webside Dev Run:

~~~shell
cd templates
quasar d # http://localhost:8081
or
quasar dev # http://localhost:8081
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

~~~shell
cd templates/src-cordova
cordova platform add [ios or android]
cd .. # back to templates
quasar d -m cordova -T [ios or android]
~~~

[//]: # (publish)
### How To Publish Your APP:

- Webside Dev Run:

~~~shell
cd templates
quasar build # http://localhost:8081
~~~

- Electron APP Dev Run

~~~shell
quasar build -m electron -P always
~~~

- Mobile APP Dev Run

~~~shell
quasar build -m cordova -T [ios or android]
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

Distributed under the [GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) License. See [LICENSE.txt](https://github.com/Singosgu/GreaterWMS/blob/master/LICENSE) for more information.
