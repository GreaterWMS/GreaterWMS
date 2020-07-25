# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/scm/scm.png?raw=true"/></div></p>

<hr>
<p><h3>项目介绍：</h3></p>
<p>现行的WMS项目分2类，一类是传统的线下软件，这类软件一般是高度封装，客户如果想要定制化一些功能，会非常复杂和耗时；第二类是saas的wms，线上WMS存在致命的问题，就是很难和线下的ERP或者TMS软件做API对接，如果涉及到定制开发，也很难得到支持。</p>
<p>该开源项目，做了前后端分离，后端全部为分离的api，api技术使用的是Django-rest-framework，遵循restful协议；前端为vue页面，用axios进行封装，后端路由使用的是Django的路由机制，前端路由使用vue-router，并且数据传输做了安全控制，防sql注入和js,css攻击</p>
<hr>
<p><h3>开发环境：</h3></p>
<p>* python 版本为v3.7.0 +</p>
<p>* django版本为v2.2.14</p>
<p>* django-rest-framework 版本为3.9.2</p>
<p>* django-rest-swagger 版本为v2.2.0</p>
<p>* API，使用restful协议</p>
<hr>
<p><h3>构建命令：</h3></p>
<p>$ python manage.py makemigrations</p>
<p>运行数据库迁移文件</p>
<p>$ python manage.py migrate</p>
<p>创建数据库，django默认使用sqlite3作为数据库，如果需要mysql数据库，请在singosgu/settings.py里面进行配置</p>
<p><h4>开发：</h4></p>
<p>运行开发服务器：</p>
<p>$ python manage.py runserver</p>
<p>运行在特定端口：</p>
<p>$ python manage.py runserver 0.0.0.0:8001</p>
<p>如果运行特定端口，局域网的电脑，只需要访问，运行电脑的ip+端口，即可以访问运行结果</p>

<hr>
<p><h3>开发指南：</h3></p>
