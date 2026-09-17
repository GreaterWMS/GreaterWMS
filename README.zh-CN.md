<div align="center">
  <img src="static/img/logo.png" alt="GreaterWMS logo" width="200" height="auto" />
  <h1>GreaterWMS</h1>
  <h3>完全开源的仓库管理系统 —— 为你的业务而定制</h3>
</div>

> ## 🎉 GreaterWMS 3.0 已发布 · 基于 Bomiot 重构
>
> GreaterWMS 3.0 已正式发布，核心已使用 [Bomiot](https://gitee.com/Bomiot/Bomiot) 完整重构。基于 Rust 的插件化架构与应用市场，让定制开发和功能扩展更高效。
>
> 👉 **[前往 Bomiot 了解更多](https://gitee.com/Bomiot/Bomiot)**



## 🎬 开源版本功能视频介绍

想快速了解 GreaterWMS 能做什么？我们录制了完整的开源版本功能演示，涵盖入库、出库、库存管理、PDA 扫描等核心操作流程。

👉 **[点击观看 GreaterWMS 开源版本功能视频](https://www.bilibili.com/video/BV1r1Em6QE5v/?vd_source=e27ed0e4cbc69fce7cb662cddc3ceae1)**

## 🔓 为什么选择 GreaterWMS

传统的商业 WMS 软件往往闭源且难以二次开发，企业一旦选择某款软件，二次开发就会被开发公司绑定，费用高昂且周期漫长。GreaterWMS 的诞生正是为了解决这个问题——作者在供应链行业工作 15 年，深知行业内缺乏一款**高自由度、高自定义化**的软件来深度支持企业业务。GreaterWMS 的设计初衷就是**为定制而生**：无论你是仅构建进销存、仓库管理，还是需要对接物联网、ERP 和分销系统，GreaterWMS 都能作为你的基础平台。

**Bomiot 底层框架赋能**

GreaterWMS 3.0 已正式发布，核心已使用 [Bomiot](https://gitee.com/Bomiot/Bomiot) **完整重构**。Bomiot 核心用 Rust 编写，提供插件化架构、应用市场（pip 安装即可扩展）、信号机制等能力，让**定制开发和功能扩展变得更加高效**。它构建了以 CLI 为基础的新软件模式，无需手动配置环境，让交付更直接高效。

👉 **[前往 Bomiot 探索插件市场与开发者文档](https://gitee.com/Bomiot/Bomiot)**

**开发者文档**

所有开发者文档已迁移到 [Bomiot](https://gitee.com/Bomiot/Bomiot) 中，执行以下指令安装：

```shell
pip install bomiot
```

## 🎯 定制化能力

**前后端分离架构**

系统采用 Django REST Framework 后端 + Quasar (Vue.js) 前端的分离架构，API 遵循 RESTful 协议。这种设计使得**添加功能或修改业务逻辑**非常方便，前后端可以独立演进。

**模块化业务设计**

系统按模块组织业务逻辑（ASN 收货、DN 发货、库存、库位等），每个模块职责清晰。你可以**只修改或扩展需要的模块**，而不影响其他功能。

**多端统一与灵活扩展**

OneAPP 理念让同一套后端可以服务于 PDA、手机 APP、桌面端和网站等多种终端。前端基于 Quasar 框架，代码可编译为 Web、Android、PDA 程序，甚至微信小程序。

## 📦 实际定制场景

GreaterWMS 已经在多个行业被成功定制落地：

**三方物流、云仓（3PL）**：基于原生代码扩展多仓集群管控、一车多仓串装卸、冷链 IoT 温控、批次效期管控、多货主租户隔离等功能。原生 Milk-Run 能力可改造为干线车辆依次停靠多仓装卸货。

**医药流通**：定制批次管理模块实现药品有效期自动预警，对接 IoT 设备监控温湿度，满足 GSP 合规要求。某医药分销企业上线后库存周转天数从 45 天降至 28 天。

**冷链仓储**：在标准 WMS 基础上增加温度记录与预警功能，实现冷库+冷藏车的全链路温控追溯。

**跨境电商**：开发国际物流与报关集成接口，适配跨境业务的特殊流程需求。

**制造业**：通过批次管理和 FIFO 控制满足零部件追溯需求，与 MES 系统集成实现物料拉动式管理。某汽车零部件企业应用后库存周转率提升 25%。

## 🧭 快速开始

### 获取代码

```bash
git clone https://github.com/GreaterWMS/GreaterWMS.git
cd GreaterWMS
```

### 后端启动

```bash
pip install -r requirements.txt
daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
```

### 前端开发

```bash
cd templates
npm install
quasar dev
```

**请求地址配置**：`templates/public/statics/baseurl.txt`

### 技术栈

- **后端**：Python 3.8+ / Django 3.1+ / Django REST Framework
- **前端**：Quasar 1.7.2+ / Vue 2.6+
- **数据库**：SQLite（默认）/ MySQL / PostgreSQL

## 📬 联系方式

**项目官网**：[https://www.bomiot.com/](https://www.bomiot.com/)

**邮箱**：dawnup888@163.com

**微信**：ts-Wlm

如有定制化需求、商业合作意向，或希望咨询二次开发相关问题，欢迎通过以上方式联系我们。

## License

Apache 2.0
