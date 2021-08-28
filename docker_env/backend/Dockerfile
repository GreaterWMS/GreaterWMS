#FROM registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms_backend_build:v1.0
FROM silence2022/greaterwms_backend_build:v1.0
WORKDIR /GreaterWMS/
COPY . .
RUN chmod -R 777 /GreaterWMS/backend_start.sh
CMD ["/GreaterWMS/backend_start.sh"]