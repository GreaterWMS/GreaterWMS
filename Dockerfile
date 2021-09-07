#总镜像
FROM registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms_backend_build:v1.0
#配置工作目录 复制所有文件到工作目录
WORKDIR /GreaterWMS
EXPOSE 8008
CMD ["daphne","-p","8008","greaterwms.asgi:application"]
