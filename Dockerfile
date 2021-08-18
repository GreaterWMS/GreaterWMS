#基础镜像（这里的base_app_image就是之前制作的基础镜像，项目镜像是在基础镜像的基础上进行制作的，这个一定要理解清楚）
FROM python:3.9.6-slim
#将项目目录文件复制到镜像中,CODE_DIR是在基础镜像中定义的
RUN mkdir -p /src/GreaterWMS/templates
COPY .  /src/GreaterWMS
#配置工作目录
WORKDIR /src/GreaterWMS
#安装supervisor
#更换apt-get为阿里云的源
RUN sed -i s/deb.debian.org/mirrors.aliyun.com/g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update && apt-get install supervisor -y
RUN apt-get install build-essential -y
RUN python3 -m pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
#安装Twisted依赖
run tar -xjvf Twisted-18.4.0.tar.bz2
run cd Twisted-18.4.0 && python3 setup.py install
run cd /src/GreaterWMS
#安装项目依赖包
RUN pip install supervisor -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
RUN pip install -U 'Twisted[tls,http2]' -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
RUN apt install -y libmariadbd-dev
RUN pip install mysqlclient -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
#前端环境
RUN tar xf node-v14.17.5-linux-x64.tar.xz -C /opt
ENV PATH=$PATH:/opt/node-v14.17.5-linux-x64/bin
RUN node -v
RUN npm install npm -g
RUN npm install yarn -g
RUN npm install -g @quasar/cli
RUN cd /src/GreaterWMS/templates
RUN yarn
EXPOSE 8000
EXPOSE 8080
