# GreaterWMS--Open Source Warehouse Management System

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/GreaterWMS/blob/master/templates/public/statics/icons/logo.png?raw=true"/></div></p>

---

[中文文档](https://github.com/Singosgu/GreaterWMS/blob/master/README_zh_Hans.md)

## Production Introduce:

Fully open source warehouse management system follows Apache License 2.0 and front-back stage decoupling method. API uses restful protocol to facilitate for add-on functions development. The html & js code is constructed with quasar(base on Vue.js v2.6.0+). According to API, it can support business models such as multi warehouse, wave shipment, combined picking and milk-run and so on.

- Software Copyright Procedures: 2018SR517685
- GitHub Link: [GitHub](https://github.com/Singosgu/GreaterWMS)

- Demo Link: [DEMO](https://www.56yhz.com/)
- QQ Caboodle ：463562933

---

## Our Original Intention:

I have 15 years old experience focus on supply chain . I find that in this professional field . No freedom customize software can support our business deeply . Any software are closed-source and hardly to customize or dynamic with our suppliers & customers . So I design GreaterWMS , in order to give business highest freedom way to support trade development .

-  Our Vision: If you work in a non IT industry and you love your industry, please using technology to change it.

---

## Production Life Cycle:

- V 1.0.0 -- 2019.07 ~ 2020.12(Due to version 1.0.0 is more complex for re-development, so we rewrite the V 2.0)
- V 2.0.0 -- 2020.12 ~ 2021.03(Rewrite business process, native API development documents, add real-time communication, facilitate enterprise users to communicate with each other)
- V 2.1.0 -- 2021.03 ~ 2021.06(The real-time interaction between customers and enterprises is added to enhance the business relationship between enterprises and customers, and realize VMI business)
- V 2.2.0 -- 2020.06 ~ 2021.09(The real-time interaction between suppliers and enterprises is added to enhance the business relationship between enterprises and suppliers, and realize milk-run and look-proof pulling）
- V 2.3.0 -- 2021.09 ~ 2021.12(The rudiment of inventory management, the neural network is initially added, and the inventory changes are Deep learning)
- V 3.0.0 -- 2021.12 ~ 2022.03(Fully implanted neural network, so that upstream and downstream enterprises can operate the whole business at the lowest cost)
- V 3.1.0 -- 2022.03 ~ 2022.06(Regional warehouse business layout, through in-depth learning, to achieve multi warehouse operation, cost minimization)

---

## Development Environment:

- Python Version 3.8.0 +

- Django Version 3.1.0 +(This version of Django only supports asynchronous real-time communication)

- Django-rest-framework Version  3.12.2 + (Highest versions of Django-rest-framework are more compatible with Django3)

- Django-silk Version  4.1.0 (If you are deploying production, please turn off silk, which is only used for debugging API interface speed, which may leak users' information)

- Quasar Version 1.7.2 + (You can view the official website of quasar to edit the webside code of greater WMS: [Quasar](http://www.quasarchs.com/))

- Vue Version  2.6.0 +（Try not to use vue3, because the development environment does not use vue3, I don't know what will happened）
- API，Follow RESTful

---

## Build Command:

- Git Clone:

~~~shell
git clone https://github.com/Singosgu/GreaterWMS.git
~~~

- Install Python Library：

~~~python
pip install -r requirements.txt
~~~

Atention: `Installation requires Twisted library, this library sometimes cannot be installed, you need to download it and install it locally`

- Download Link：[TWISTED](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)

~~~python
pip install Twisted{Version Name Which You Download}
~~~

Atention:  `Local installation needs to pay attention to the path`

- Makemigrations the Database：

~~~python
python manage.py makemigrations
~~~

- Migrate Database：

~~~python
python manage.py migrate
~~~

Create a database. Django uses sqlite3 as the default database. If you need other database, please configure DATABASE in django_wms/settings.py

### Run Development Server:

- Dev Run：

~~~python
daphne -p 8008 django_wms.asgi:application
~~~

### Run Production Server:

- supervisor Daemon:

~~~shell
pip install supervisor
~~~

Use supervisor to guard the Django process, and then use Nginx as a reverse proxy. As for supervisors, there are many tutorials, so I won’t explain them here.

- Nginx Support：

It is recommended to use Nginx for deployment. You need to specify the WebSocket link when deploying. If you do not specify it, the real-time communication function will report an error.

Also need to modify ws_url in axios_request.js

~~~shell
## Example changes before
const baseurl = 'http://127.0.0.1:8008/'
const wsurl = 'ws://127.0.0.1:8008/'

## Example changes after
const baseurl = 'https://Your Production Server/'
const wsurl = 'wss://Your Production Server/websocket/'
~~~

If the server has SSL enabled, please use https and wss, if SSL is not enabled, use http and ws

The front-end code needs to be rebuilt after modification

---

## Development Extension:

Because the front and back ends are separated, more software applications can be developed through API

### Logistics AI AGV

- The AGV project has also been open sourced. Due to the limited space, only intelligent delivery, fixed-point return to the warehouse, tracking sensors, ultrasonic obstacle avoidance sensors, and infrared obstacle avoidance sensors are used. All instructions are transmitted through the network and are tied to the AGV. Specify the MAC address and IP address to ensure security, provided that you need a Raspberry Pi.

### Invoicing System

- It can be directly used as an invoicing system to simplify operations such as warehouse location setting.

### APP And Mini Programe

- Quasar can be directly packaged into IOS APP and Android APP
- The development of mini programs can be developed through API for secondary development, but small programs do not support put requests, so you need to write another request interface yourself.

- The combination of API can reach 1 million, so that we can obtain real-time reports and data monitoring according to query requests

### Supply Chain Management System

- The number of products, creation time, and last update time are all recorded, so it is convenient to analyze the inventory of the purchase plan and the allocation plan
- V 2.3.0 and later versions will come with deep learning analysis, so you can directly use the analysis results as a supply chain management system tool

### Multi-warehouse Management

- OPENID is the unique identification of the user's data, and the data group is uniformly identified as the APPID, so it is very convenient to realize multi-warehouse management

### Wave Picking And Shipping

- You can set a fixed time to send a request to the server to achieve the function of wave picking

- You can also use task work directly, through API query and analysis results to achieve, it is recommended to use [APScheduler](https://pypi.org/project/APScheduler/)

  ~~~python
  pip install apscheduler
  ~~~

### Milk-Run

- V 2.2.0 and above will natively support this function
- If you need this business now, you can call inventory consumption according to API to achieve this function

### VMI

- V 2.1.0 and above, will natively support this function
- If you need this business now, you can call inventory consumption according to API to achieve this function

### Picking Route Optimization

- The current picking route is sorted by bin location
- This feature will be natively supported after V 2.3.0
- If you need this business now, you can call the API to implement this function according to the daily picking details

---

## Development Guide:

### Baseurl

- It is the basic URL for initiating the request. If it is for local debugging, the default is http://127.0.0.1:8008/. If it is deployed on the server, you need to change it to your website access URL

- The modification method is to modify axios_request.js. Attention: `The modification of websocket has been mentioned `

### Django-Silk

- Django-Silk is a debugging tool during development. It can count the response speed of each interface. If you need to deploy to a production environment, please delete the Django-silk related configuration, because there is a risk of leaking user information, or directly modify the Django-silk library , So that users can only see their request data

### Database Storage

- Data migration and other issues are considered during database design, so only the user_id in users and the user_id that comes with Django are foreign keys, and all the other fields do not use foreign keys, which is convenient for data backup and database migration.
  - The database is a 4-stage design

  1. Verify data user ownership
  2. Verify data security
  3. Verify that the data can be stored in the database
  4. Save it in the database and return Response

### About Data Request

- The token value needs to be added to all request headers. This value is the unique identifier OPENID of the user’s data
- All data transmission needs to set content-type to application/json

### OPENID

- OPENID is the unique identifier of registered user data. When the administrator registers directly, there will be developer=1 as the administrator ID.
- You can do custom secondary development based on the developer label

### APPID

- APPID is the unique identifier of the user data group
- If you need multi company operation or multi warehouse operation, you can make unified link through appid to realize multi company and multi warehouse operation

### User Jurisdiction

- There are not too many restrictions on user authorization. Please limit the secondary development according to your own business needs

---

## Business Process:

- This content is not updated at this time