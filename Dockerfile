#总镜像
FROM silence2022/greaterwms:v2.0.25
#配置工作目录 复制所有文件到工作目录
WORKDIR /GreaterWMS
EXPOSE 8008
CMD ["daphne","-b","0.0.0.0","-p","8008","greaterwms.asgi:application"]
