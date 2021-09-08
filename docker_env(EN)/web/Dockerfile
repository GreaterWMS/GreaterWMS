FROM silence2022/greaterwms_backend_build:v1.0
USER root
WORKDIR /GreaterWMS/
COPY . .
RUN cd /GreaterWMS/templates --force
RUN npm install -g yarn --force
RUN npm install -g @quasar/cli --force
RUN yarn install --force
EXPOSE 8080
