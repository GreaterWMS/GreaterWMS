#基础镜像 用docker_env/backend/Dockerfile的文件制作的基础镜像
FROM silence2022/greaterwms:v2.0.24
#配置工作目录 复制所有文件到工作目录
WORKDIR /GreaterWMS
EXPOSE 8008
CMD ["daphne","-b","0.0.0.0","-p","8008","greaterwms.asgi:application"]
