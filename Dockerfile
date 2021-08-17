FROM ubuntu:20.04

ENV TZ=Asia/Shanghai

WORKDIR /usr/src/app/

# 配置镜像源
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list

RUN apt-get clean

RUN apt update

RUN apt upgrade -y

# 安装 python 3.8
RUN apt-get install -y python3.8 python3-distutils \
    && ln -s  /usr/bin/python3.8 /usr/bin/python

# 安装 python3-pip daphne
RUN apt-get install python3-pip daphne -y

# 复制项目
COPY . /usr/src/app/

# 适配项目
RUN cp -f -r docker/workdir/* /usr/src/app/

# 安装依赖
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 数据库生成
RUN python3 manage.py makemigrations

# 数据库迁移
RUN python3 manage.py migrate

CMD daphne -p 80 -b 0.0.0.0 greaterwms.asgi:application

EXPOSE 80