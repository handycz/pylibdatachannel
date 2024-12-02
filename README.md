# pylibdatachannel
Minimal Python wrapper for [libdatachannel](https://github.com/paullouisageneau/libdatachannel) (C++ WebRTC network library) using [pybind11](https://pybind11.readthedocs.io). 

The library currently only supports minimal API needed by my use case, but contributions to extend the API are welcome.

**Disclaimer**: This project is an independent Python wrapper for the `libdatachannel` library and is not affiliated with, endorsed by, or maintained by the original `libdatachannel` project.

## Wheels
Python wheels are published to [Pypi repository](https://pypi.org/project/pylibdatachannel). Only Linux `x86_64` and `aarch64` are currently built.

## Versions
The library uses Semver that does not match the version of *libdatachannel*. The table below shows relation between the wrapper and library versions.

| Wrapper version   | Library version   |
| ----------------- | ----------------- |
| 0.1.0             | 0.22.2            |

