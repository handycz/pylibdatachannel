import glob

import pybind11
from setuptools import Extension, setup

setup(
    name="pylibdatachannel",
    ext_modules=[
        Extension(
            "_pylibdatachannel",
            sources=[*glob.glob("cpp/*.cpp")],
            py_limited_api=True,
            include_dirs=[
                "foreign/libdatachannel/include",
                pybind11.get_include(),
            ],
            extra_compile_args=[
                "-frtti",
            ],
            runtime_library_dirs=[
                "$ORIGIN",
            ],
            libraries=[
                "ssl",
                "crypto",
                "datachannel",
            ],
            language="c++",
        ),
    ],
    zip_safe=False,
)
