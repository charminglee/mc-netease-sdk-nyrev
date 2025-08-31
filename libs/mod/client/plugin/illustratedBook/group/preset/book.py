
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.group.pageGroup import PageGroup
from mod.client.plugin.illustratedBook.group.preset.category import Category
from typing import List
from typing import Dict
from typing import Tuple


class Book(PageGroup):

    def GetSons(self):
        # type: () -> List[Category]
        """
            获取子页组（其子页组就是Category对象）
        """
        pass

    def GetProgressValue(self):
        # type: () -> float
        """
            获取子页组解锁的进度，常用于进度条显示
        """ 
        pass

