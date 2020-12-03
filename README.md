# GreaterWMS--Open source warehouse management software
<p><div align=center><img width="100" height="25" src="https://visitor-badge.glitch.me/badge?page_id=<your_page_id>"/></div></p>
<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/logo.png?raw=true"/></div></p>
<p>
<div align=center>
  <img width="100" height="25" src="https://img.shields.io/hexpm/l/plug?style=plastic"/>
  <img src="https://img.shields.io/npm/v/quasar.svg?label=quasar"> <img src="https://img.shields.io/npm/v/%40quasar/app.svg?label=@quasar/app"> <img src="https://img.shields.io/npm/v/%40quasar/cli.svg?label=@quasar/cli"> <img src="https://img.shields.io/npm/v/%40quasar/extras.svg?label=@quasar/extras"> <img src="https://img.shields.io/npm/v/%40quasar/icongenie.svg?label=@quasar/icongenie">
</div>
</p>

<hr>
<p><h2><a href="https://github.com/Singosgu/GreaterWMS/blob/master/README_zh_Hans.md" target="_blank">中文文档</a></h2></p>
<p><h3>Project Description:</h3></p>
<p>Open source warehouse management software follows Apache License 2.0 protocol and front-back stage decoupling method. API uses restful protocol to facilitate for add-on functions development. The html & js code is constructed with quasar(base on Vue.js v2.6.0+). According to API, it can support business models such as multi warehouse, wave shipment, combined picking and milk-run and so on.</p>

<p>Software copyright Code：<a>China: 2018SR517685</a></p>
<p>Gitee Link:<a href="https://gitee.com/Singosgu/GreaterWMS" target="_blank">Gitee</a></p>

<p>Technical QQ community：<a>1051907485</a></p>
<hr>
<p><h3>Development Environment:</h3></p>
<p>* Python v3.8.0 +</p>
<p>* Django v3.1.3 +</p>
<p>* Django-silk v4.0.1 + (In production environment，please close silk，silk will leak user infomation)</p>
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
<p>$ daphne -p 8000 django_wms.asgi:application</p>
<p>Local Server Port Customize</p>
<p>$ daphne -b 0.0.0.0 -p 8000 django_wms.asgi:application</p>
<p>If you customize the Port. The user in local area network can use 'server IP:Port' to browse the software</p>
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
