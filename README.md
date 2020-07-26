# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/logo.png?raw=true"/></div></p>

<hr>
<p><h3>项目介绍：</h3></p>
<p>开源仓储管理软件，遵循MIT协议，前后端分离，api使用restful协议，方便二次开发，前端代码使用quasar进行构建，利用API，可以支持多仓，波次发货，合并拣货，Milk-Run等业务模型</p>
<p>演示地址：<a href="https://www.56yhz.com" target="_blank">https://www.56yhz.com</a></p>
<p>软件著作权编号：<a>2018SR517685</a></p>
<p>码云地址：<a href="https://gitee.com/Singosgu/Elvis_WMS" target="_blank">码云</a></p>
<p>GitHub地址：<a href="https://www.56yhz.com" target="_blank">GitHub</a></p>
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
<p>uwsgi安装：</p>
<p>$ pip install uwsgi</p>
<p>如果你使用了虚拟环境，那uwsgi的安装需要正式环境安装一遍，再在虚拟环境中安装一遍</p>
<p>uwsgi挂载：</p>
<p>uwsgi -x /path/to/***你的项目路径***/mysite.xml</p>
<p>如果不希望代码更改后，自动刷新挂载，可以把py-autoreload设置为0</p>
<p>uwsgi重新挂载：</p>
<p>uwsgi --reload /path/to/***你的项目路径***/mysite.pid</p>
<p>uwsgi已经记录了pid文件，每次重新挂载只需要reload这个pid就可以了</p>
<hr>
<p><h3>开发扩展：</h3></p>
<p>因为使用的前后端分离的设计，所以可以通过API，开发更多的软件应用</p>
<p><h4>物流智能AGV</h4></p>
<p>* AGV的项目也已经开源，由于场地受限，仅实现智能发货，定点回库，使用的循迹感应器，超声波避障感应器，红外避障感应器</p>
<p><h4>进销存</h4></p>
<p>* 不使用仓库设置模块，直接使用商品设置和供应商及客户设置，可以快速搭建一个进销存系统</p>
<p><h4>APP和小程序</h4></p>
<p>* API的组合可以达到1万种，这样我们可以根据查询请求，来获得实时报表和数据监控</p>
<p><h4>供应链管理系统</h4></p>
<p>* 产品的数量，创建时间，最后使用时间是各方面统计的，所以可以方便采购计划和调拨计划进行库存的分析</p>
<p><h4>多仓管理</h4></p>
<p>* openid为用户的唯一标识，数据统一标识为appid，数据t_code为数据在服务器的唯一标识，所以很方便可以实现多仓管理</p>
<p><h4>波次拣货，发货</h4></p>
<p>* 可以设置固定时间向服务器发出请求，从而达到波次拣货的功能</p>
<p><h4>Milk-Run</h4></p>
<p>* 可以给供应商或者客户设置权限，让他们可以查询到固定产品的库存消耗</p>
<p><h4>VMI</h4></p>
<p>* 同上</p>
<p><h4>拣货路线优化</h4></p>
<p>* 库位的设置决定了拣货的效率</p>
<hr>
<p><h3>开发指南：</h3></p>
<hr>
<p><h3>项目展示：</h3></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/home.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/inbound.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/outbound.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/stocklist.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/goodslist.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/staff.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/notbook.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/api.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/silk.png?raw=true"/></div></p>
