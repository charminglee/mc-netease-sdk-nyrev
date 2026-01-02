# -*- coding: utf-8 -*-
# =================================================
#  ⠀
#   Copyright (c) 2025 Nuoyan
#  ⠀
#   Author: Nuoyan <https://github.com/charminglee>
#   Email : 1279735247@qq.com
#   Date  : 2025-12-29
#  ⠀
# =================================================


from setuptools import setup, find_packages


try:
    LONG_DESCR = open("README.md").read()
except:
    try:
        LONG_DESCR = open("README.md", encoding="utf-8").read()
    except:
        LONG_DESCR = "Netease ModSDK completion library revised version by Nuoyan.\nSee https://github.com/charminglee/mc-netease-sdk-nyrev"


MODSDK_VER = "3.7.0.70028"
LIB_ROOT = "libs"


setup(
    name="mc-netease-sdk-nyrev",
    version=MODSDK_VER,
    # version=MODSDK_VER + "-6",
    # version=MODSDK_VER + "a1",
    description="Netease ModSDK completion library revised version by Nuoyan",
    long_description=LONG_DESCR,
    long_description_content_type="text/markdown",
    author="Nuoyan",
    author_email="1279735247@qq.com",
    url="https://github.com/charminglee/mc-netease-sdk-nyrev",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    packages=find_packages(LIB_ROOT),
    package_dir={'': LIB_ROOT},
    include_package_data=True,
    package_data={'': ["*.pyi"]},
    py_modules=["mod_log"],

    python_requires=">=2.7, <4",
    install_requires=[
        'typing==3.10.0.0; python_version=="2.7"',
        'typing-extensions==3.10.0.2; python_version=="2.7"',
        'typing==3.7.4.3; python_version>="3"',
        'typing-extensions; python_version>="3"',
    ]
)













