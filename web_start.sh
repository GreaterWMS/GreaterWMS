#!/bin/bash
cd /GreaterWMS/templates
yarn install --force
quasar build
quasar d
