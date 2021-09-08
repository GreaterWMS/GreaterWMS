FROM registry.cn-hangzhou.aliyuncs.com/cow11023/greaterwms_web_build:v1.0
USER root
WORKDIR /GreaterWMS/
COPY . .
RUN cd /GreaterWMS/templates
RUN npm install -g yarn --registry=https://registry.npm.taobao.org
RUN npm install -g @quasar/cli --registry=https://registry.npm.taobao.org
RUN yarn install --registry=https://registry.npm.taobao.org
EXPOSE 8080
