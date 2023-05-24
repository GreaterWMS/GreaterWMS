#!/bin/bash
cd /GreaterWMS/templates
#安装yarn,首次运行启用
yarn install --force
#前端静态文件打包
quasar build
#运行前端
quasar d
