# -*- coding: utf-8 -*-
# =================================================
#  ⠀
#   Copyright (c) 2025 Nuoyan
#  ⠀
#   Author: Nuoyan <https://github.com/charminglee>
#   Email : 1279735247@qq.com
#   Date  : 2025-12-20
#  ⠀
# =================================================


from setuptools import setup, find_packages


try:
    long_description = open("README.md").read()
except:
    try:
        long_description = open("README.md", encoding="utf-8").read()
    except:
        long_description = "Netease ModSDK completion library revised version by Nuoyan.\nSee https://github.com/charminglee/mc-netease-sdk-nyrev"


setup(
    name="mc-netease-sdk-nyrev",
    version="3.6.0.64490-4",
    description="Netease ModSDK completion library revised version by Nuoyan",
    long_description=long_description,
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

    packages=find_packages(where="libs"),
    include_package_data=True,
    package_data={'': ["*.pyi"]},
    package_dir={'': "libs"},

    python_requires=">=2.7, <4",
    install_requires=[
        'typing==3.10.0.0; python_version=="2.7"',
        'typing-extensions==3.10.0.2; python_version=="2.7"',
        'typing==3.7.4.3; python_version>="3"',
        'typing-extensions; python_version>="3"',
    ]
)













