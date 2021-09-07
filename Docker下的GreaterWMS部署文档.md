Docker下使用GreaterWMS（本文档适用于具备Docker基础的用户使用）

1. 安装或升级Docker客户端

```
	curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
	//如果提示没有curl再执行sudo apt install curl 或 yum -y install curl
```

2. 配置加速器（国内）

```
	sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF' ##国内加速，全球用户则不需要配加速器
{
  "registry-mirrors": ["https://w61q8mf4.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl enable docker
sudo systemctl restart docker
```

3. 安装Docker-compose

```
	sudo curl -L "https://get.daocloud.io/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
```

4. 利用docker直接试运行项目（非二次开发，用户试用，无需从github上克隆项目）

```
//直接docker run 国内用户使用
docker run -itd --name greaterwms_v2.0.25 -p 8008:8008 -d registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms:v2.0.25
//直接docker run 全球用户使用
docker run -itd --name greaterwms_v2.0.25 -p 8008:8008 -d silence2022/greaterwms:v2.0.25
```

5. 安装git

```
//Ubuntu下安装git
apt-get install git
//CentOS下安装git
yum install git
```

6. 适用于长期保存数据(需要在用户服务器上存放代码) 和二次开发

```
//拉取代码
git clone https://github.com/Singosgu/GreaterWMS.git
//运行项目前需要修改baseurl.js的内容
vim templates/public/statics/baseurl.js //将127.0.0.1修改为服务器的IP地址
docker-compose up -d
//查看前端镜像运行日志
docker logs -f greaterwms_web_v2.0.25
//当打印的前端日志出现以下信息即表示前端启动成功
 N  App dir........... /GreaterWMS/templates
    App URL........... http://localhost:8080
    Dev mode.......... spa
    Pkg quasar........ v1.15.23
    Pkg @quasar/app... v2.2.10
    Transpiled JS..... yes (Babel)
  
｢wds｣: Project is running at http://0.0.0.0:8080/
｢wds｣: webpack output is served from 
//查看后端镜像运行日志
docker logs -f greaterwms_backend_v2.0.25
////当打印的后端日志出现以下信息即表示后端启动成功
2021-09-07 21:19:43,168 INFO     Starting server at tcp:port=8008:interface=0.0.0.0
2021-09-07 21:19:43,169 INFO     HTTP/2 support enabled
2021-09-07 21:19:43,169 INFO     Configuring endpoint tcp:port=8008:interface=0.0.0.0
2021-09-07 21:19:43,170 INFO     Listening on TCP address 0.0.0.0:8008

```

7. 发布前端代码

```
//进入前端容器
docker exec -it greaterwms_web_v2.0.25 /bin/bash
//容器内进入templates目录
cd templates
//编译前端代码
quasar d 
```

8. 访问入口

   前端：http://服务器IP:8080

   后端：http://服务器IP:8008
