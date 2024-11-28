#!/bin/bash

set -e

mkdir -p build
cmake \
  -B build \
  -DNO_SERVER=1 \
  -DUSE_NICE=0 \
  -DNO_MEDIA=1 \
  -DNO_WEBSOCKET=1 \
  -DNO_EXAMPLES=1 \
  -DNO_TESTS=1 \
  -DCMAKE_INSTALL_LIBDIR=/lib64 \
  foreign/libdatachannel

cmake --build build --target install
