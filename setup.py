# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="mc-netease-sdk-nyrev",
    version="1.0.4",
    description="网易我的世界ModSDK补全库修正版 by Nuoyan",
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













