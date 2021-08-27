FROM registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms_web_build:v1.0
RUN mkdir -p /GreaterWMS/templates
WORKDIR /GreaterWMS/templates
COPY templates .
RUN yarn install
RUN quasar -d
