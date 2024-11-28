#!/bin/bash

if [ -e /etc/centos-release ]; then
  yum install -y openssl-devel-1.1.*
elif [ -e /etc/alpine-release ]; then
  apk add libssl3 libcrypto3 openssl-dev
fi

scripts/build-libdatachannel-cmake.sh
