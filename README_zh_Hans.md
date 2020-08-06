# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://www.56yhz.com/statics/icons/logo.png"/></div></p>

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
<p>$ uwsgi -x /path/to/***你的项目路径***/mysite.xml</p>
<p>如果不希望代码更改后，自动刷新挂载，可以把py-autoreload设置为0</p>
<p>uwsgi重新挂载：</p>
<p>$ uwsgi --reload /path/to/***你的项目路径***/mysite.pid</p>
<p>uwsgi已经记录了pid文件，每次重新挂载只需要reload这个pid就可以了</p>
<hr>
<p><h3>开发扩展：</h3></p>
<p>因为使用的前后端分离的设计，所以可以通过API，开发更多的软件应用</p>
<p><h4>物流智能AGV</h4></p>
<p>* AGV的项目也已经开源，由于场地受限，仅实现智能发货，定点回库，使用的循迹感应器，超声波避障感应器，红外避障感应器，所有的指令通过网络传输，AGV绑定MAC地址和IP地址，保证了安全性</p>
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
<p><h4>baseurl</h4></p>
<p>* 是发起请求的基本网址，如果是本地调试，则默认为http://127.0.0.1:8000/ ，如果部署在服务器，则需要将其改为你的网站访问url</p>
<p>* 修改方式为，发起一个post请求到https://www.56yhz.com/baseurl/ ，传输一个json数据data{'baseurl': 'http://*****', 'title': '你的项目名称', 'icp': '中国的icp备案信息'}</p>
<p><h4>django-silk</h4></p>
<p>* django-silk为开发时的调试工具，可以统计每个接口的响应速度，如果需要部署到生产环境，请删除django-silk相关配置，因为会有泄露用户信息的风险，或者直接修改django-silk，让用户只能看到自己的请求数据<p>
<p><h4>django-rest-swagger</h4></p>
<p>* swagger会生成软件的开发者文档，访问'baseurl' + '/docs/'，就可以看到具体的开发者文档，同时还可以对接口进行调试, 开发者文档使用的YML的格式，也可以自己在APIView里面修改，注意接口，get是修改get请求的API文档，post是修改post请求的API文档<p>
<p><h4>数据库设计</h4></p>
<p>* 数据库设计时考虑到数据迁移等问题，所以只有users里面的user_id和django自带的user_id做了外键，其余所有字段全部没有使用外键，方便数据备份和数据库迁移<p>
<p><h4>关于数据传输</h4></p>
<p>* post，patch，put请求会传输一个数据data，可以是一个json数据，也可以是一个json数据组，传输的data会被utils/datasolve处理，来判断是否有js文件或sql注入，从而保证了后台数据库的安全性，每个前端给后端发的请求，都会核对用户的唯一标识，以防止用户数据串流<p>
<p><h4>openid</h4></p>
<p>* openid是注册用户的唯一标识，当管理员直接注册时，会有developer=1这个管理员标识，管理员具备最高权限，而由管理员，或有新增用户权限的用户新建的用户，developer=0，developer作为管理员标识存在，每次向服务器发起请求，都需要url传值这个openid，服务器端会根据这个openid来判断是否为正常用户，从而保证数据不会被混乱访问，同时也可以根据openid来记录具体的访问用户，作为数据追溯依据，可以使用request.auth获得该条数据<p>
<p><h4>appid</h4></p>
<p>* appid是数据源唯一标识，每次新建用户(员工账号)时，用户的appid都会统一为管理员账号的appid，从而达到了所有数据的统一性，即新用户A在发起数据请求时，会带上自己的openid，服务器端根据这个openid去链接appid下的所有数据，防止访问到其他用户的数据，可以使用request.user.appid获得该条数据<p>
<p><h4>用户权限</h4></p>
<p>* 用户信息已经设计了权限管理，共45个，有字段aut1~~aut45，可自定义权限管理，先未对权限管理数据传输做任何限制，可自定义添加<p>
<p><h4>t_code</h4></p>
<p>* t_code是数据存在数据库里面的唯一标识，是具有唯一性的，所有的数据修改和删除，都是使用t_code来判断的，避免使用id判断时，会出现数据误操作，该条数据是由当时的时间戳+传入的一个string值，合并生成的MD5码<p>
<p><h4>get请求设计</h4></p>
<p>* get请求已经做好了分页设计，传值时：max_page参数为每页最大显示多少条内容，默认设计是1000条数据，因为如果数据过多，会造成数据较慢； page参数为请求第几页的数据，一般在返回的数据中，有一个totalpage参数，可以知道一共有多少页<p>
<p><h4>数据传输流程</h4></p>
<p>* 一般post,patch,put是4段式设计，1--审查用户权限，会return一个值'Y' or 'N'，2--审查数据的安全性， 3--审查数据是否可以存入数据库或修改数据库数据，4--新增或修改数据，并返回一个data给到前端，这样做可以避免数据增删改的时候出现误改的情况<p>
<p><h4>数据库设计</h4></p>
<p>* 数据库设计时考虑到数据迁移等问题，所以只有users里面的user_id和django自带的user_id做了外键，其余所有字段全部没有使用外键，方便数据备份和数据库迁移<p>
<p><h4>小程序开发</h4></p>
<p>* 由于小程序不支持patch请求，所以需要自信在django中设置一个views，来访问patch请求的数据<p>
<hr>
<p><h3>项目展示：</h3></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081359_00047e76_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081400_accf72f6_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081401_96be5429_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081359_c6a79408_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081400_bc1c201e_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081400_812d6c78_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081401_a90ce517_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081402_e23345dd_1199519.png"/></div></p>
<p><div align=center><img src="https://images.gitee.com/uploads/images/2020/0801/081403_77ce3a94_1199519.png"/></div></p>
