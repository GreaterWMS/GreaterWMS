# GreaterWMS--Open Source Warehouse Management System

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/GreaterWMS/blob/master/templates/public/statics/icons/logo.png?raw=true"/></div></p>

---

[中文文档](https://github.com/Singosgu/GreaterWMS/blob/master/README_zh_Hans.md)

## Production Introduce：

Fully open source warehouse management system follows Apache License 2.0 and front-back stage decoupling method. API uses restful protocol to facilitate for add-on functions development. The html & js code is constructed with quasar(base on Vue.js v2.6.0+). According to API, it can support business models such as multi warehouse, wave shipment, combined picking and milk-run and so on.

- Software Copyright Procedures: 2018SR517685
- GitHub Link: [GitHub](https://github.com/Singosgu/GreaterWMS)

- Demo Link: [DEMO](https://www.56yhz.com/)
- QQ Caboodle ：463562933

---

## Our Original Intention：

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

## Development Environment：

- Python Version 3.8.0 +

- Django Version 3.1.0 +(This version of Django only supports asynchronous real-time communication)

- Django-rest-framework Version  3.12.2 + (Highest versions of Django-rest-framework are more compatible with Django3)

- Django-silk Version  4.1.0 (If you are deploying production, please turn off silk, which is only used for debugging API interface speed, which may leak users' information)

- Quasar Version 1.7.2 + (You can view the official website of quasar to edit the webside code of greater WMS: [Quasar官网](http://www.quasarchs.com/))

- Vue Version  2.6.0 +（Try not to use vue3, because the development environment does not use vue3, I don't know what will happened）
- API，Follow RESTful

---

## 构建命令：

- 下载代码：

~~~shell
git clone https://github.com/Singosgu/GreaterWMS.git
~~~

- 安装Python库：

~~~python
pip install -r requirements.txt
~~~

注意：`安装需要Twisted库，这个库有时候会安装不上，需要下载下来本地安装`

- 下载地址：[TWISTED](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)

~~~python
pip install Twisted{你下载下来的版本名称}
~~~

注意：`本地安装需要注意路径`

- 初始化数据库：

~~~python
python manage.py makemigrations
~~~

- 迁移数据库：

~~~python
python manage.py migrate
~~~

创建数据库，Django默认使用sqlite3作为数据库，如果需要mysql数据库，请在django_wms/settings.py里面配置DATABASE

### 开发服务器运行：

- 开发运行：

~~~python
daphne -p 8008 django_wms.asgi:application
~~~

### 生产服务器运行：

- supervisor守护进程：

~~~shell
pip install supervisor
~~~

使用supervisor来守护Django进程，再使用Nginx做反向代理，至于superevisor的教程有很多，这里不做讲解

- Nginx支持：

推荐使用Nginx进行部署，部署的时候需要指定WebSocket链接，如果不指定，实时通信功能将报错

另需要修改axios_request.js里的ws_url

~~~shell
## 示例更改前
const baseurl = 'http://127.0.0.1:8008/'
const wsurl = 'ws://127.0.0.1:8008/'

## 示例更改后
const baseurl = 'https://你的域名/'
const wsurl = 'wss://你的域名/websocket/'
~~~

如果服务器启用了SSL，请使用https和wss，如果没有启用SSL，则使用http和ws

修改后需要重新build前端代码

---

## 开发扩展：

因为使用的前后端分离的设计，所以可以通过API，开发更多的软件应用

### 物流智能AGV

- AGV的项目也已经开源，由于场地受限，仅实现智能发货，定点回库，使用的循迹感应器，超声波避障感应器，红外避障感应器，所有的指令通过网络传输，AGV绑定MAC地址和IP地址，保证了安全性，前提是，你需要有一个树莓派。

### 进销存

- 可以直接当一个进销存系统使用，简化仓库库位设置等操作即可。

### APP和小程序

- Quasar原生可以直接打包成IOS APP和Android APP
- 小程序的开发可以通过API开做二次开发，但小程序不支持put请求，所以需要自己再写一个请求接口。

- API的组合可以达到100万种，这样我们可以根据查询请求，来获得实时报表和数据监控

### 供应链管理系统

- 产品的数量，创建时间，最后使用时间是各方面统计的，所以可以方便采购计划和调拨计划进行库存的分析
- V 2.3.0及其以后的版本，将自带深度学习分析，所以可以直接使用分析结果作为供应链管理系统工具使用

### 多仓管理

- OPENID为用户的数据唯一标识，数据组统一标识为APPID，所以很方便可以实现多仓管理

### 波次拣货，发货

- 可以设置固定时间向服务器发出请求，从而达到波次拣货的功能

- 也可以直接使用任务工作，通过API查询分析结果来实现，推荐使用[APScheduler](https://pypi.org/project/APScheduler/)

  ~~~python
  pip install apscheduler
  ~~~

### Milk-Run

- V 2.2.0及其以上版本，将原生支持此功能
- 如果现在就需要这个业务，可以根据API调用库存消耗，来实现此功能

### VMI

- V 2.1.0及其以上版本，将原生支持此功能
- 如果现在就需要这个业务，可以根据API调用库存消耗，来实现此功能

### 拣货路线优化

- 现在的拣货路线是按照库位排序
- V 2.3.0以后版本将原生支持此功能
- 如果现在需要这个业务，可以根据每天的拣货明细，调用API来实现此功能

---

## 开发指南：

### baseurl

- 是发起请求的基本网址，如果是本地调试，则默认为http://127.0.0.1:8008/ ，如果部署在服务器，则需要将其改为你的网站访问url

- 修改方式为，修改axios_request.js，注意`websocket的修改之前已经提到了`

### Django-silk

- django-silk为开发时的调试工具，可以统计每个接口的响应速度，如果需要部署到生产环境，请删除Django-silk相关配置，因为会有泄露用户信息的风险，或者直接修改Django-silk库，让用户只能看到自己的请求数据

### 数据库存储

- 数据库设计时考虑到数据迁移等问题，所以只有users里面的user_id和Django自带的user_id做了外键，其余所有字段全部没有使用外键，方便数据备份和数据库迁移
- 数据库是4段式设计
  1. 验证数据用户归属
  2. 验证数据安全性
  3. 验证数据是否可以存入数据库
  4. 存入数据库，并返回Response

### 关于数据传输

- 需要在所有的请求头headers里面加入token值，这个值就是用户的数据唯一标识OPENID
- 所有的数据传输需要设定content-type为application/json

### OPENID

- OPENID是注册用户数据的唯一标识，当管理员直接注册时，会有developer=1这个管理员标识。
- 你可以根据developter标识来做自定义二次开发

### APPID

- APPID is the unique identifier of the user data group
- If you need multi company operation or multi warehouse operation, you can make unified link through appid to realize multi company and multi warehouse operation

### User Jurisdiction

- There are not too many restrictions on user authorization. Please limit the secondary development according to your own business needs

---

## Business Process：

- This content is not updated at this time