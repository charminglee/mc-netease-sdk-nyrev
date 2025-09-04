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


import os
import build
from twine.commands import upload
import glob


dist_dir = "dist"
for fn in os.listdir(dist_dir):
    path = os.path.join(dist_dir, fn)
    os.remove(path)


builder = build.ProjectBuilder(".")
builder.build("sdist", "dist")
builder.build("wheel", "dist")


with open(".token") as f:
    token = f.read()
dists = glob.glob("dist/*")
args = [
    "--username", "__token__",
    "--password", token,
]
args.extend(dists)
upload.main(args)













