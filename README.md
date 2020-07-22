# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/scm/scm.png?raw=true"/></div></p>

<hr>
<p><h3>项目介绍：</h3></p>
<p>现行的WMS项目分2类，一类是传统的线下软件，这类软件一般是高度封装，客户如果想要定制化一些功能，会非常复杂和耗时；第二类是saas的wms，线上WMS存在致命的问题，就是很难和线下的ERP或者TMS软件做API对接，如果涉及到定制开发，也很难得到支持。</p>
<p>该开源项目，做了前后端分离，后端全部为分离的api，api技术使用的是Django-rest-framework，遵循restful协议；前端为vue页面，用axios进行封装，后端路由使用的是Django的路由机制，前端路由使用vue-router，并且数据传输做了安全控制，防sql注入和js,css攻击</p>
<hr>
<p><h3>开发环境：</h3></p>
<p>* Node.JS版本为v12.16.3</p>
<p>* Quasar/CLI版本为v1.0.7</p>
<p>* Vue.JS是基础开发语言</p>
<p>* axios版本为v0.19.2</p>
<p>* API，使用restful协议</p>
<hr>
<p><h3>构建命令：</h3></p>
<p><h4>开发：</h4></p>
<p>运行开发服务器(使用默认主题)：</p>
<p>$ quasar dev</p>
<p>运行在特定端口：</p>
<p>$ quasar dev -p 9090</p>
<p>SSR：</p>
<p>$ quasar dev -m ssr</p>
<p>PWA：</p>
<p>$ quasar dev -m pwa</p>
<p>手机应用：</p>
<p>$ quasar dev -m cordova -T [android|ios]</p>
<p>或更短的格式：</p>
<p>$ quasar dev -m [android|ios]</p>
<p>Electron应用：</p>
<p>$ quasar dev -m electron</p>
<p>将额外的参数和/或选项传递给</p>
<p>底层“cordova”或“electron”可执行文件：</p>
<p>$ quasar dev -m ios -- some params --and options --here</p>
<p>$ quasar dev -m electron -- --no-sandbox --disable-setuid-sandbox</p>
<p><h4>生产版本：</h4></p>
<p>运行开发服务器(使用默认主题)：</p>
<p>$ quasar build</p>
<p>SSR：</p>
<p>$ quasar build -m ssr</p>
<p>PWA：</p>
<p>$ quasar build -m pwa</p>
<p>手机应用：</p>
<p>$ quasar build -m cordova -T [android|ios]</p>
<p>或更短的格式：</p>
<p>$ quasar build -m [android|ios]</p>
<p>Electron应用：</p>
<p>$ quasar build -m electron</p>
<p>将额外的参数和/或选项传递给</p>
<p>底层“cordova”或“electron”可执行文件：</p>
<p>$ quasar build -m ios -- some params --and options --here</p>
<p><h4>Electron应用构建发布版本：</h4></p>
<p>quasar build --mode electron --publish always</p>
<hr>
<p><h3>使用教程：</h3></p>
