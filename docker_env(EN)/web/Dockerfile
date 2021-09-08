FROM silence2022/greaterwms_backend_build:v1.0
USER root
WORKDIR /GreaterWMS/
COPY . .
RUN cd /GreaterWMS/templates
RUN npm install -g yarn
RUN npm install -g @quasar/cli
RUN yarn install
EXPOSE 8080
