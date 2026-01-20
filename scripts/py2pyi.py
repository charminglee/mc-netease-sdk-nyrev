# -*- coding: utf-8 -*-
# =================================================
#  ⠀
#   Copyright (c) 2026 Nuoyan
#  ⠀
#   Author: Nuoyan <https://github.com/charminglee>
#   Email : 1279735247@qq.com
#   Date  : 2026-01-14
#  ⠀
# =================================================


import os


def py2pyi(path):
    if not os.path.exists(path):
        return
    for root, dirs, files in os.walk(path):
        for fn in files:
            if fn != "__init__.py" and fn.endswith('.py'):
                old_path = os.path.join(root, fn)
                new_path = os.path.join(root, fn[:fn.rindex(".")] + '.pyi')
                os.rename(old_path, new_path)


if __name__ == "__main__":
    py2pyi(r"..\libs\mod")
