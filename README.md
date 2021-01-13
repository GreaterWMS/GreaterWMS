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

- Quasar Version 1.7.2 + (You can view the official website of quasar to edit the webside code of greater WMS: [Quasar](https://quasar.dev/))

- Vue Version  2.6.0 +（Try not to use vue3, because the development environment does not use vue3, I don't know what will happened）
- API，Follow RESTful

---

## Build Command:

- Git Clone:

~~~shell
git clone https://github.com/Singosgu/GreaterWMS.git
~~~

- Install Python Library:

~~~python
pip install -r requirements.txt
~~~

Atention: `Installation requires Twisted library, this library sometimes cannot be installed, you need to download it and install it locally`

- Download Link：[TWISTED](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)

~~~python
pip install Twisted{Version Name Which You Download}
~~~

Atention:  `Local installation needs to pay attention to the path`

- Makemigrations the Database:

~~~python
python manage.py makemigrations
~~~

- Migrate Database:

~~~python
python manage.py migrate
~~~

Create a database. Django uses sqlite3 as the default database. If you need other database, please configure DATABASE in greaterwms/settings.py

### Run Development Server:

- Dev Run：

~~~python
daphne -p 8008 greaterwms.asgi:application
~~~

### Run Production Server:

- supervisor Daemon:

~~~shell
pip install supervisor
~~~

Use supervisor to guard the Django process, and then use Nginx as a reverse proxy. As for supervisors, there are many tutorials, so I won’t explain them here.

- Nginx Support:

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

### 管理员

- Click Register, you can register as an administrator account, so as to realize the initialization program settings
- After registration, you will get two IDs and one developer label. openid is the unique ID of the user data group. All data under this openid is bound through openid. Appid is the unique ID of the user group data. Multi company and multi warehouse functions are realized through appid. The developer ID is a Boolean value, and true represents an administrator account
- There are two way for user login:
  1. Login directly with openid and staff name
  2. Administrator login with account and password
- After login, the web will localstorage login information
- you can view the openid of user data group by view my openid
- If multi company and multi warehouse operation is required, pay attention to change openid
- More administrator authrization, please develop by yourself

### Staff

- After registering as an administrator, create a new staff first
- Staff has two fields, staff_ Name (for employee login), staff_ Type (employee type to control employee permissions)
- The system does not have any restrictions on employee permissions. If you need employee permissions, please modify them according to the enterprise business model Templates
- Click Edit to modify the employee information
- Click Delete to delete the staff information. The system will set is_delete to true
- Click Contact:
  1. You can directly chat with employees in real time, but you can't chat with yourself
  2. You can create a new notebook employee, which is actually used as a notebook
  3. In the personal center, you can view recent contacts
  4. The message flag will remind you how many unread messages you have

### Driver

- Driver management is only used in the shipping process
- You need to know which driver picked up the goods

### Warehouse Set

- Warehouse
  1. You can create only one warehouse. Now you can create multiple warehouses, but only the first one will work
  2. If multi warehouse processing is needed, secondary development can be carried out through appid, or an administrator account can be created directly
  3. The city of the warehouse must be filled in, which is used to calculate the freight
- Bin_Property
  1. The bin property determines the property of the goods in the warehouse
  2. Four property: damage, holding, inspection, normal
  3. In the beta version, property can be modified and deleted, but the release version can not
  4. All shipping process will only match the goods in the normal bin
  5. When goods are received and moved to another bin, the inventory quantity will be directly modified according to the bin property, and the inventory quantity of the warehouse will not be negative
- Bin_Size
  1. The size of bin is to help the operator to check whether the goods can be put into the bin
  2. The current version does not check the dimensions of bin, and automatic inspection will be added in the future
- Bin_Set
  1. Bin setting is necessary. Generally, bin setting is horizontal, vertical and horizontal, such as A010101, i.e. A horizontal, 01 vertical, 01 horizontal and 01 vertical
  2. The setting of bin needs to set the bin property and size. The property is very important, which determines whether the goods in this bin are normal goods

### Basic Info

- Company
  1. The creation of basic company information can only create one company. Now you can create multiple companies, but only the first one will work
  2. If multi company processing is needed, secondary development can be carried out through appid, or an administrator account can be created directly
  3. The city of the company must be filled in, which is used to show on the receipt-proof
- Supplier
  1. Basic information of suppliers
  2. The city of the supplier must be filled in, which is used to display on the receipt-proof, and also to calculate the freight automatically
- Customer
  1. Basic information of customers
  2. The customer's city must be filled in, which is used to display on the invoice, and also to automatically calculate the freight

### Godds

- Unit
  1. Goods units, the system will initialize to create some, but you can add and modify
- Class
  1. Goods Class, you can add and modify
- Color
  1. Goods color, the system will initialize to create some, but you can add and modify
- Brand
  1. Goods brand, you can add and modify
- Shape
  1. Goods Shape, the system will initialize to create some, but you can add and modify
- Specs
  1. Goods specs, you can add and modify
- Origin
  1. Goods Origin, where initial product goods, you can add and modify
- Goods List
  1. Goods list

### Capital

- Capital
  1. The creation of fixed assets, not too much expansion, just record the use
  2. Can be statistical pallets accounts

### Stock Management

- Stock List
  1. 在库的货物总的库存数据量
  2. Onhand_stock现有的库存数量
  3. Can Order，可以用于下单发货的库存数量，因为有些货物已经被下了订单，虽然有现有库存，但是不可以再被订货
  4. Ordered Stock，已经被下单的货物数量
  5. ASN Stock，已经下了到货通知书，但还没有确认到货通知书的货物数量
  6. DN Stock，已被下单，但是还没有确认订单数量
  7. Pre Load，预计到货货物数量
  8. Pre Sort，已经到货，卸货完成，等待分拣的货物数量
  9. Sorted Stock，货物分拣完成，等待上架的货物数量
  10. Pick Stock，发货单生成了拣货单，等待拣货的货物数量
  11. Picked Stock，已经拣货完成，等待和司机交接的货物数量
  12. Back Order Stock，欠货订单数量
- Bin Stock
  1. Total Stock，这个库位该产品的所有库存数量
  2. Pick Stock，这个库位需要拣货的数量
  3. Picked Stock，这个库位拣货完成的数量
  4. Move To Bin， 移库，移库后，会根据库位属性，直接更新库存数量，如果库位全部移空，则该库位会更新为空库位
- Empty Bin
  1. 空库位明细
- Occupied Bin
  1. 非空库位明细

### 收获管理

- ASN到货通知书状态
  1. ASN Status = 1, ASN到货通知书创建完成，状态1是唯一可以删除和修改ASN信息的状态，他会显示在Pre Delivery中，即有了到货通知书，但是还没有到货，点击Confirm Delivery，即确认货物已经到达，ASN Status更新到2，此时已经无法再修改ASN信息
  2. ASN Status = 2, 拓展开发为司机到货排队，如果我们有很多司机到货，这可以做成一个排队系统，同时也可以让采购和销售看到到货信息，减少不必要的邮件和电话沟通，点击Finish Loading，即确认货物已经卸货完成，ASN Status更新到3,货物信息会出现在Sorting，此时的ASN状态表示，货物已卸到仓库，等待分拣
  3. ASN Status = 3, 货物分拣是必须的一个流程，没有货物分拣，货物是无法上架的，上架的原则就是货物整理好，摆放到相对应的库位上，点击Confirm Sorted，ASN Status更新到4，即确认分拣完成，等待上架
  4. 此时移动Sorted页面，会出现需要上架的货物明细，点击Move To Bin，上架完成，当然，系统会根据上架后的库位属性，自动更新商品库存数量信息

### 发货管理

- DN发货单状态
  1. DN Status = 1, DN发货单创建完成，此时订单还是可以修改状态，且系统中的库存数量不会发生任何改变，点击Confirm Order，DN Status更新到2，即订单已经被确认，且无法更改，同时系统中的货物库存数量会自动更新，比如Can Order数量和Ordered数量
  2. DN Status = 2, 这是订单被确认等待生成拣货单的过程，你可以点击单条订单Order Release来生成一个订单的拣货单，你也可以点击Release All Order，来将所有订单生成拣货单，如果是所有订单Release，那么会根据时间的先后进行库存匹配，库存不足时，会生成Back Order，即欠货订单，在这个过程中，DN单号是会发生改变的，如一家客户的多张订单，会被统一到一张订单中进行拣货，如客户订单无法满足，会将未满足部分生成欠货订单，欠货订单如果仍未得到匹配库存满足，将不再生成新的订单，DN Status会更新到3，即等待拣货的过程，已确认的订单和欠货订单都时Status为2的状态
  3. DN Status = 3, 直接拣货，此功能会出现在Beta5更新中，暂时未更新
  4. DN Status = 4, 发货交接，此功能会出现在Beta6更新中，暂时未更新
  5. DN Status = 5, 客户签收，此功能会出现在Beta7更新中，暂时未更新
  6. DN Status = 6, 对账结束，订单关闭，此功能会出现在Beta7更新中，暂时未更新

### 退货管理

- RO退货订单
  此功能将会出现在正式版中

### 运费管理

- Transportation Fee
  API已经完成，前端暂未更新入口，如果想要使用，可以直接调用Payment下的Transportation Fee API进行使用，运费自动计算模块已经做进收发货流程中