# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/scm/scm.png?raw=true"/></div></p>

<hr>
<p><h3>项目介绍：</h3></p>
<p>开源仓储管理软件，遵循MIT协议，前后端分离，api使用restful协议，方便二次开发，前端代码使用quasar进行构建，利用API，可以支持多仓，波次发货，合并拣货，Milk-Run等业务模型</p>
<p>演示地址：<a href="https://www.56yhz.com" targret="_blank">https://www.56yhz.com</a></p>
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
