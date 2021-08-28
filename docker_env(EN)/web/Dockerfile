FROM silence2022/greaterwms_backend_build:v1.0
RUN mkdir -p /GreaterWMS/templates
WORKDIR /GreaterWMS
COPY templates/ .
RUN yarn install
RUN quasar -d
