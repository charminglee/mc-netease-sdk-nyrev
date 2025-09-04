# -*- coding: utf-8 -*-
"""
| ==============================================
|
|   Copyright (c) 2025 Nuoyan
|
|   Author: Nuoyan
|   Email : 1279735247@qq.com
|   Gitee : https://gitee.com/charming-lee
|   Date  : 2025-09-05
|
| ==============================================
"""


from setuptools import setup, find_packages


setup(
    name="mc-netease-sdk-nyrev",
    version="1.0.5",
    description="Netease ModSDK completion library revised version by Nuoyan",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nuoyan",
    author_email="1279735247@qq.com",
    url="https://github.com/charminglee/mc-netease-sdk-nyrev",
    license="MIT",
    packages=find_packages(where="libs"),
    package_dir={"": "libs"},
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7, <4",
)













