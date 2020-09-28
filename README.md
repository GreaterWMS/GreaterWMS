# Django_WMS--Open source warehouse management software

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/logo.png?raw=true"/></div></p>

<hr>
<p>虽然本开源项目使用前后端分离设计，但是，前后端分离就是一个垃圾产物，会增加很多前端人员和后端人员，而你的开发效率提升仅仅是20%的速度提升，原因就在于你们会浪费非常多的时间，发邮件，发聊天，发截图，相互扯淡，一旦一处代码改动，整个团队都要加班改动</p>
<p>项目2.0版本，将全部改版为异步通信，同步数据，并加入实时聊天功能</p>
<p><h2><a href="https://github.com/Singosgu/Elvis_WMS/blob/master/README_zh_Hans.md" target="_blank">中文文档</a></h2></p>
<p><h3>Project Description:</h3></p>
<p>Open source warehouse management software follows MIT protocol and front-back stage decoupling method. API uses restful protocol to facilitate for add-on functions development. The html & js code is constructed with quasar(base on Vue.js v2.6.0+). According to API, it can support business models such as multi warehouse, wave shipment, combined picking and milk-run and so on.</p>

<p>Software copyright Code：<a>China: 2018SR517685</a></p>
<p>Gitee Link:<a href="https://gitee.com/Singosgu/Elvis_WMS" target="_blank">Gitee</a></p>

<p>Technical QQ community：<a>1051907485</a></p>
<hr>
<p><h3>Development Environment:</h3></p>
<p>* Python v3.7.0 +</p>
<p>* Django v2.2.14(Django v2.2.14 can support Django-rest-swagger better. If you don't need Django-rest-swagger to debug api, you can pip install higher version Django)</p>
<p>* Django-rest-framework v3.9.2(Django-rest-framework v3.9.2 can support Django-rest-swagger better，If you don't need Django-rest-swagger to debug api, you can pip install higher version Django-rest-framework)</p>
<p>* Django-rest-swagger v2.2.0</p>
<p>* Django-silk v4.0.1(In production environment，please close silk，silk will leak user infomation)</p>
<p>* Quasar v1.7.2+</p>
<p>* Vue v2.6.0+</p>
<p>* API，follow restful protocol</p>
<hr>
<p><h3>Server deployment:</h3></p>
<p>$ pip install -r requirements.txt</p>
<p>Install Python Library</p>
<p>$ python manage.py makemigrations</p>
<p>Run Django database migrate file.</p>
<p>$ python manage.py migrate</p>
<p>Confirm migrate database. Django Primordial support sqlite3 database. If you wanna change database to others. Please editor singosgu/settings.py.</p>
<p><h4>Run Server:</h4></p>
<p>Local Server</p>
<p>$ python manage.py runserver</p>
<p>Local Server Port Customize</p>
<p>$ python manage.py runserver 0.0.0.0:8001</p>
<p>If you customize the Port. The user in local area network can use 'server IP:Port' to browse the software</p>
<p><h4>Production Server Run:</h4></p>
<p>Nginx Config：</p>
<p>Only example for Nginx. You can get example nginx.conf in project files. Exchange you server nginx.conf is ok. Take attention the project path & domin name in nginx.conf must be real.</p>
<p>Install uwsgi:</p>
<p>$ pip install uwsgi</p>
<p>If you use virtual environment. You must install uwsgi in Production Environment once, then install uwsgi in virtual environment once again.</p>
<p>Run uwsgi:</p>
<p>$ uwsgi -x /path/to/***your project path***/mysite.xml</p>
<p>If you don't want the project refresh while the code changed . You can set py-autoreload as 0(zero)</p>
<p>uwsgi reload:</p>
<p>$ uwsgi --reload /path/to/***your project path***/mysite.pid</p>
<p>Uwsgi recorded a pid file. Each time you want to reload the uwsgi . Reload this pid is ok</p>
<hr>
<p><h3>Develop Extend:</h3></p>
<p>According to front-back stage decoupling method. It support you to develop more extend software</p>
<p><h4>Logistic_AI_ROBOT_AGV</h4></p>
<p>* The project of AGV has been open-source. It use Tracking sensor,Ultrasonic obstacle avoidance sensor, Infrared obstacle avoidance sensor. Base on HTTP protocol & WEB Web Framework. In order to ensure safety, data interchange must bind AGV's MAC address and IP address . </p>
<p><h4>Sales Management System</h4></p>
<p>* Don't use warehouse modular, API can support fast develop a sales management system.</p>
<p><h4>APP & WX Mini Program</h4></p>
<p>* API can support you develop a real time data monitoring system.</p>
<p><h4>SCM</h4></p>
<p>* Goods' QTY, Create_time, Last_update_time be detailed record. So you can analyst the inventory cleary and develop a SCM system.</p>
<p><h4>Multi Warehouse Management</h4></p>
<p>* Openid is user's unique identification. Data unique identification is appid. Data-line unique identification is t_code. So it facilitate support Multi Warehouse Management</p>
<p><h4>Wave Picking, Shipping</h4></p>
<p>* Can set Cyclical-Requests to realize Wave picking & shipping.</p>
<p><h4>Milk-Run</h4></p>
<p>* Can edit supplier & customer's authorization. Let them know the goods demand & consumption</p>
<p><h4>VMI</h4></p>
<p>* Ditto</p>
<p><h4>Picking Route Optimization</h4></p>
<p>* You can set picking route rule to imporve picking productiveness.</p>
<hr>
<p><h3>Develop Guide:</h3></p>
<p><h4>baseurl</h4></p>
<p>* statics/baseurl.js是发起请求的基本网址，如果是本地调试，则默认为http://127.0.0.1:8000/ ，如果部署在服务器，则需要将其改为你的网站访问url</p>
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
<p><h3>WMS Project Show:</h3></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/home.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/inbound.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/outbound.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/stocklist.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/goodslist.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/staff.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/notbook.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/api.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/silk.png?raw=true"/></div></p>
