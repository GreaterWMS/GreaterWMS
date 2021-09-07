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

6. 适用于长期保存数据(需要在用户服务器上存放代码)

```
//拉取代码
git clone https://github.com/Singosgu/GreaterWMS.git
//进入项目目录，利用docker-compose up -d来运行项目
//运行项目前需要修改baseurl.js的内容
vim templates/dist/spa/statics/baseurl.js //将127.0.0.1修改为服务器的IP地址
docker-compose up -d
//查看镜像运行日志
docker logs -f greaterwms:v2.0.25
<<<<<<< Updated upstream
=======
//备注：backend_start.sh功能说明
  //用于数据库迁移的操作，当初始化完成时用户可以手动注释掉前面两段代码
  //daphne -p 8008 greaterwms.asgi:application为运行后端程序的命令
>>>>>>> Stashed changes
```

7. 适用于二次开发

```
# 后端基础镜像只有在 requirements.txt 变化后重新编译，其他情况无需变化
#构建后端基础镜像（国内用户）,这里的版本号是指内部调试时使用的版本号，非正式版，每次更新后面的版本号建议都增加
docker build -f ./docker_env\(CN\)/backend/DockerfileBuild -t registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms_backend_build:v1.0 .
#构建后端基础镜像（全球用户）
docker build -f ./docker_env\(EN\)/backend/DockerfileBuild -t registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms_backend_build:v1.0 .
#构建成功以后需要在再构建总镜像并上传到仓库，建议用户可以直接使用我的总镜像,这里的版本号指正式发布的版本号
docker build -t greaterwms:v2.0.25 . 
docker push 仓库地址
#建议用户用自己的仓库作为打包的镜像存放地址，docker-compose.yml中的地址是仅作为对外展示，不接收用户修改后再上传
```

