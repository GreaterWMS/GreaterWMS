# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/Elvis_WMS/tree/master/statics/icons/logo.png?raw=true"/></div></p>

<hr>
<p><h3>项目介绍：</h3></p>
<p>开源仓储管理软件，遵循MIT协议，前后端分离，api使用restful协议，方便二次开发，前端代码使用quasar进行构建，利用API，可以支持多仓，波次发货，合并拣货，Milk-Run等业务模型</p>
<p>演示地址：<a href="https://www.56yhz.com" target="_blank">https://www.56yhz.com</a></p>
<p>技术交流QQ群：<a>1051907485</a></p>
<hr>
<p><h3>开发环境：</h3></p>
<p>* python 版本为v3.7.0 +</p>
<p>* django版本为v2.2.14(该版本django和django-rest-swagger兼容比较好，如果不需要使用django-rest-swagger，可以使用更高版本的django)</p>
<p>* django-rest-framework 版本为3.9.2(该版本django和django-rest-swagger兼容比较好，如果不需要使用django-rest-swagger，可以使用更高版本的django)</p>
<p>* django-rest-swagger 版本为v2.2.0</p>
<p>* django-silk 版本为v4.0.1(如果是部署上线，请关闭silk，silk有可能会泄露用户信息)</p>
<p>* quasar 版本为v1.7.2+</p>
<p>* vue 版本为v2.6.0+</p>
<p>* API，使用restful协议</p>
<hr>
<p><h3>构建命令：</h3></p>
<p>$ pip install -r requirements.txt</p>
<p>安装python库</p>
<p>$ python manage.py makemigrations</p>
<p>运行数据库迁移文件</p>
<p>$ python manage.py migrate</p>
<p>创建数据库，django默认使用sqlite3作为数据库，如果需要mysql数据库，请在singosgu/settings.py里面进行配置</p>
<p><h4>开发服务器运行：</h4></p>
<p>运行开发服务器：</p>
<p>$ python manage.py runserver</p>
<p>运行在特定端口：</p>
<p>$ python manage.py runserver 0.0.0.0:8001</p>
<p>如果运行特定端口，局域网的电脑，只需要访问，运行电脑的ip+端口，即可以访问运行页面</p>
<p><h4>生产服务器运行：</h4></p>
<p>Nginx配置：</p>
<p>这里仅以Nginx配置为例，将项目下的nginx.conf替换服务器端的nginx.conf即可，注意更改nginx.conf里面的项目地址和域名</p>
<p>wsgi挂载：</p>
<p>$ python manage.py runserver 0.0.0.0:8001</p>
<p>如果运行特定端口，局域网的电脑，只需要访问，运行电脑的ip+端口，即可以访问运行页面</p>
<hr>
<p><h3>开发指南：</h3></p>
