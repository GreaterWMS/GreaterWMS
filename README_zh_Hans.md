# 聚商汇WMS--开源仓库管理系统

<p><div align=center><img width="150" height="150" src="https://github.com/Singosgu/picfile/blob/master/logo.png?raw=true"/></div></p>

---

## 项目介绍：

完全开源仓储管理软件，遵循Apache License 2.0协议，前后端分离，且完全开源，API使用restful协议，方便二次开发，前端代码使用quasar进行构建，后端使用Python Django3.1，利用API，可以支持多仓，波次发货，合并拣货，Milk-Run等业务模型。

- 软件著作权编号：2018SR517685
- GitHub地址：[GitHub](https://github.com/Singosgu/GreaterWMS)
- Gitee地址：[Gitee](https://gitee.com/Singosgu/GreaterWMS)
- 视频教程：[B站](https://space.bilibili.com/407321291/channel/detail?cid=152043)(所有的教程都会更新在这里)
- Demo地址：[DEMO](https://www.56yhz.com/)(注册会获得初始化Demo数据)
- 技术交流QQ群：463562933
- CIMO-ADMIN(vue-quasar-manage): [GitHub](https://github.com/972784674t/vue-quasar-manage) | [Gitee](https://gitee.com/incimo/vue-quasar-manage)

---

## 项目初衷：

我在供应链行业工作了15年，发现在我们这个专业的领域，没有一款高自由度、高自定义化的软件，来深度支持我们企业的业务。大多数软件都是闭源的，而且很难去做二次开发，即使开发，周期也是非常长，开发失败的案例也是比比皆是。由于企业选择了一款软件后，其二次开发也会被开发公司绑定，至于二次开发费用，只能说呵呵。所以，我设计了这个聚商汇WMS，为的是做到一款高自由度，高自定义开发的仓库管理软件，来深度支持企业的业务。

- 愿景：如果你从事着非IT行业的工作，而你又热爱你的行业，那就用科技去改变他。

---

## 生命周期

- V 1.0.0 -- 2019年7月 ~ 2020年12月（由于1.0.0版本的二次开发设计较为复杂，故2.0重新编写）
- V 2.0.0 -- 2020年12月 ~ 2021年3月（重新编写业务逻辑，原生自带API开发文档，加入实时通信，方便企业用户互相沟通）
- V 2.1.0 -- 2021年3月 ~ 2021年6月（加入了客户与企业之间的实时互动，增进企业与客户之间的业务联系，实现VMI）
- V 2.2.0 -- 2020年6月 ~ 2021年9月（加入了供应商与企业之间的实时互动，增进企业与供应商之间的业务联系，实现Milk-Run和看板拉动）
- V 2.3.0 -- 2021年9月 ~ 2021年12月（库存管理雏形，初步加入神经网络，深度学习库存变化）
- V 3.0.0 -- 2021年12月 ~ 2022年3月（完全植入神经网络，让上下游企业可以以最低的成本运营整体的业务）
- V 3.1.0 -- 2022年3月 ~ 2022年6月（区域仓库业务布局，通过深度学习，实现多仓运营，成本最低化）

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

创建数据库，Django默认使用sqlite3作为数据库，如果需要mysql数据库，请在greaterwms/settings.py里面配置DATABASE

### 开发服务器运行：

- 开发运行：

~~~python
daphne -p 8008 greaterwms.asgi:application
~~~

### 生产服务器运行：

- supervisor守护进程：

~~~shell
pip install supervisor
~~~

使用supervisor来守护Django进程，再使用Nginx做反向代理，至于superevisor的教程有很多，这里不做讲解

- Nginx支持：

推荐使用Nginx进行部署，部署的时候需要指定WebSocket链接，如果不指定，实时通信功能将报错

另需要修改从2.0.19版本以后，优化了请求地址修改方式，直接修改templates/dist/spa/statics/baseurl.js，中的baseurl和wsurl，就可以成功更改前端请求地址，不再需要做下面的quasar build打包工作。

如果需要修改前端内容，则还需要修改templates/public/statics/baseurl.js中的baseurl和wsurl，然后重新使用quasar build进行打包里的ws_url

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
- 你可以根据developer标识来做自定义二次开发

### APPID

- APPID是用户数据组唯一标识
- 如果需要多公司运营，或者多仓运营，可以通过APPID做统一链接，来实现多公司，多仓操作

### 用户权限

- 未对用户权限做过多限制，请根据自身的业务需要，做二次开发限制

---

## 业务流程：

### 管理员

- 点击注册，可以注册成为管理员账号，从而实现初始化程序设置
- 注册后会得到2个ID和1个开发者标识，OPENID是用户数据组唯一标识，通过OPENID绑定此OPENID下所有的数据，APPID是用户组数据唯一标识，通过APPID来实现多公司，多仓库功能，Developer标识是个布尔值，True代表这是个管理员账号
- 用户登入分2种：
  1. 使用OPENID和员工名称直接登入
  2. 管理员使用账号和密码登入
- 登入后前端会存储登入信息
- 可以通过查看我的OPENID来查看用户数据组的OPENID
- 如果需要多公司，多仓库操作，注意需要更改OPENID
- 更多管理员权限，请自行开发

### 员工管理
- 注册管理员后，新建一个员工
- 员工有2个字段，Staff_name（用于员工登入），Staff_type（员工类型来控制员工的权限）
- 系统没有对员工权限做任何限制，如果需要员工权限，请根据企业业务模型，自行修改Templates
- 点击Edit，可以修改员工信息
- 点击Delete，可以删除员工信息，系统后台会将Is_delete调成True
- 点击Contact：
  1. 可以直接和员工实时聊天，但是不可以和自己聊天
  2. 可以新建一个备忘录员工，这样做其实是当成备忘录使用
  3. 在个人中心，可以查看最近的联系人
  4. Message标识会提醒你现在有多少未读消息

### 司机管理
- 司机管理只会在发货流程中用到
- 你需要知道货物是哪个司机提货取走的

### 仓库设置
- Warehouse
  1. 仓库的创建只可以创建一个仓库，现在可以创建多个，但是只有第一个会起作用
  2. 如果需要多仓处理，可以通过APPID进行二次开发，也可以直接重新创建一个管理员账号
  3. 仓库的城市一定要填写，这是用来计算运费的
- Bin_Property
  1. 库位属性决定了仓库中货物属于什么属性的货物
  2. 4种属性：破损（Damage)，锁定（Holding），质检（Inspection），正常（Normal）
  3. Beta版中，属性可以修改和删除，正式版将无法删除和修改
  4. 所有的发货，都只会匹配Normal库位的货物
  5. 收货上架和移库，都会根据库位属性，直接修改库存数量，仓库的库存数量不会出现负数
- Bin_Size
  1. 库位的尺寸是帮助操作人员查看货物是否可以放入库位
  2. 现行的版本没有对上架和移库尺寸做检查，将来会加入自动检查
- Bin_Set
  1. 库位设置是必须的，通常库位设置是横纵横纵，比如A010101，即A横01纵01横01纵
  2. 库位的设置需要设置库位属性和尺寸，属性很重要，他决定了此库位的货物是否为正常货物

### 基础设置
- Company
  1. 公司基本信息的创建只可以创建一个公司，现在可以创建多个，但是只有第一个会起作用
  2. 如果需要多公司处理，可以通过APPID进行二次开发，也可以直接重新创建一个管理员账号
  3. 公司的城市一定要填写，这是用来显示在收发货单上的
- Supplier
  1. 供应商的基础信息
  2. 供应商的城市一定要填写，这是用来显示在收货单上的，并且也是要自动计算运费的
- Customer
  1. 客户的基础信息
  2. 客户的城市一定要填写，这是用来显示在发货单上的，并且也是要自动计算运费的

### 商品管理
- Unit
  1. 商品的单位，系统会初始化创建一些，但可以自己添加和修改
- Class
  1. 商品的类型，可以自己添加和修改
- Color
  1. 商品的颜色，系统会初始化创建一些，但可以自己添加和修改
- Brand
  1. 商品的品牌，可以自己添加和修改
- Shape
  1. 商品的形状，系统会初始化创建一些，但可以自己添加和修改
- Specs
  1. 商品的规格，可以自己添加和修改
- Origin
  1. 商品的产地，可以自己添加和修改
- Goods List
  1. 商品的列表

### 固定资产
- Capital
  1. 固定资产创建，没有做过多拓展，只是记录使用
  2. 可以统计托盘账目等

### 库存管理
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

### 收货管理
- ASN到货通知书状态
  1. ASN Status = 1, ASN到货通知书创建完成，状态1是唯一可以删除和修改ASN信息的状态，他会显示在Pre Delivery中，即有了到货通知书，但是还没有到货，点击Confirm Delivery，即确认货物已经到达，ASN Status更新到2，此时已经无法再修改ASN信息
  2. ASN Status = 2, 拓展开发为司机到货排队，如果我们有很多司机到货，这可以做成一个排队系统，同时也可以让采购和销售看到到货信息，减少不必要的邮件和电话沟通，点击Finish Loading，即确认货物已经卸货完成，ASN Status更新到3,货物信息会出现在Sorting，此时的ASN状态表示，货物已卸到仓库，等待分拣
  3. ASN Status = 3, 货物分拣是必须的一个流程，没有货物分拣，货物是无法上架的，上架的原则就是货物整理好，摆放到相对应的库位上，点击Confirm Sorted，ASN Status更新到4，即确认分拣完成，等待上架
  4. 此时移动Sorted页面，会出现需要上架的货物明细，点击Move To Bin，上架完成，当然，系统会根据上架后的库位属性，自动更新商品库存数量信息
### 发货管理
- DN发货单状态
  1. DN Status = 1, DN发货单创建完成，此时订单还是可以修改状态，且系统中的库存数量不会发生任何改变，点击Confirm Order，DN Status更新到2，即订单已经被确认，且无法更改，同时系统中的货物库存数量会自动更新，比如Can Order数量和Ordered数量
  2. DN Status = 2, 这是订单被确认等待生成拣货单的过程，你可以点击单条订单Order Release来生成一个订单的拣货单，你也可以点击Release All Order，来将所有订单生成拣货单，如果是所有订单Release，那么会根据时间的先后进行库存匹配，库存不足时，会生成Back Order，即欠货订单，在这个过程中，DN单号是会发生改变的，如一家客户的多张订单，会被统一到一张订单中进行拣货，如客户订单无法满足，会将未满足部分生成欠货订单，欠货订单如果仍未得到匹配库存满足，将不再生成新的订单，DN Status会更新到3，即等待拣货的过程，已确认的订单和欠货订单都时Status为2的状态
  3. DN Status = 3, 直接拣货，此功能会出现在Beta5更新
  4. DN Status = 4, 发货交接，此功能会出现在Beta6更新
  5. DN Status = 5, 客户签收，此功能会出现在Beta7更新
  6. DN Status = 6, 对账结束，订单关闭，此功能会出现在Beta7更新
### 退货管理
- RO退货订单
  此功能将会出现在正式版中
### 运费管理
- Transportation Fee
  API已经完成，前端暂未更新入口，如果想要使用，可以直接调用Payment下的Transportation Fee API进行使用，运费自动计算模块已经做进收发货流程中

### 界面截图

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/inbound.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/outbound.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/stock.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/finace.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/goods.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/baseinfo.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/warehouse.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/staff.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/driver.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/api.png?raw=true"/></div></p>

<p><div align=center><img width="100%" height="100%" src="https://github.com/Singosgu/picfile/blob/master/CN/chat.png?raw=true"/></div></p>
<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/CN/app1.png?raw=true"/></div></p>

<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/CN/app2.png?raw=true"/></div></p>

<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/CN/app3.png?raw=true"/></div></p>

<p><div align=center><img src="https://github.com/Singosgu/picfile/blob/master/CN/app4.png?raw=true"/></div></p>

