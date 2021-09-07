FROM silence2022/greaterwms_backend_build:v1.0
WORKDIR /GreaterWMS/
COPY . .
RUN cd /GreaterWMS/templates
RUN npm install -g yarn --registry=https://registry.npm.taobao.org
RUN npm install -g @quasar/cli --registry=https://registry.npm.taobao.org
RUN yarn install --registry=https://registry.npm.taobao.org
EXPOSE 8080
