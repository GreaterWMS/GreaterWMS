# 聚商汇--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://www.56yhz.com/statics/icons/logo.png"/></div></p>

---

## 项目介绍：

完全开源仓储管理软件，遵循Apache License 2.0协议，前后端分离，且完全开源，API使用restful协议，方便二次开发，前端代码使用quasar进行构建，后端使用Python Django3.1，利用API，可以支持多仓，波次发货，合并拣货，Milk-Run等业务模型。

- 软件著作权编号：2018SR517685
- GitHub地址：[GitHub](https://github.com/Singosgu/GreaterWMS)

- 码云地址：[码云](https://gitee.com/Singosgu/GreaterWMS)

- Demo地址：[DEMO](https://www.56yhz.com/)
- 技术交流QQ群：463562933

---

## 项目初衷：

我在供应链行业工作了15年，发现在我们这个专业的领域，没有一款高自由度、高自定义化的软件，来深度支持我们企业的业务。大多数软件都是闭源的，而且很难去做二次开发，即使开发，周期也是非常长，开发失败的案例也是比比皆是。由于企业选择了一款软件后，其二次开发也会被开发公司绑定，至于二次开发费用，只能说呵呵。所以，我设立了这个聚商汇WMS，为的是做到一款高自由度，高自定义开发的仓库管理软件，来深度支持企业的业务。

- 愿景：如果你从事着非IT行业的工作，而你又热爱你的行业，那就用科技去改变他。

---

## 生命周期

- V 1.0.0 -- 2019年7月 ~~2020年12月（由于1.0.0版本的二次开发设计较为复杂，故2.0重新编写）
- V 2.0.0 -- 2020年12月 ~~2021年3月（重新编写业务逻辑，原生自带API开发文档，加入实时通信，方便企业用户互相沟通）
- V 2.1.0 -- 2021年3月 ~~2021年6月（加入了客户与企业之间的实时互动，增进企业与客户之间的业务联系，实现VMI）
- V 2.2.0 -- 2020年6月 ~~2021年9月（加入了供应商与企业之间的实时互动，增进企业与供应商之间的业务联系，实现Milk-Run和看板拉动）
- V 2.3.0 -- 2021年9月 ~~2021年12月（库存管理雏形，初步加入神经网络，深度学习库存变化）
- V 3.0.0 -- 2021年9月 ~~2021年12月（完全植入神经网络，让上下游企业可以以最低的成本运营整体的业务）
- V 3.1.0 -- 2021年12月 ~~2022年3月（区域仓库业务布局，通过深度学习，实现多仓运营，成本最低化）

---

## 开发环境：

- Python 版本为 V 3.8.0 +

- Django 版本为 V 3.1.0 +(该版本Django才原生支持异步实时通信)

- Django-rest-framework 版本为 V 3.12.2 + (更高版本的Django-rest-Framework对Django3的兼容比较好)

- Django-silk 版本为 V 4.1.0 (如果是部署上线，请关闭silk，silk仅为调试API接口速度用，有可能会泄露用户信息)

- Quasar 版本为 V1.7.2 + (可以查看Quasar官网，来编辑GreaterWMS前端代码：[Quasar官网](http://www.quasarchs.com/))

- Vue 版本为 V 2.6.0 +（尽量不要使用Vue3，因为开发环境没有使用Vue3，不知道会出现什么问题）
- API，遵循 RESTful 架构

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

推荐使用Nginx进行部署，部署的时候需要指定WebSocket链接，如果不知道，实时通信功能将报错

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
- 小程序的开发可以通过API开做二次开发，但小程序不知道put请求，所以需要自己再写一个请求接口。

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

#### 拣货路线优化

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

### 数据库设计

- 数据库设计时考虑到数据迁移等问题，所以只有users里面的user_id和Django自带的user_id做了外键，其余所有字段全部没有使用外键，方便数据备份和数据库迁移
- 数据库是3段式设计
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

- APPID是用户数据组唯一标识
- 如果需要多公司运营，或者多仓运营，可以通过APPID做统一链接，来实现多公司，多仓操作

### 用户权限

- 未对用户权限做过多限制，请根据自身的业务需要，做二次开发限制

---

## 业务流程：

- 暂时未更新此内容