
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.group.pageGroup import PageGroup
from typing import List
from typing import Dict
from typing import Tuple


class Category(PageGroup):

    def GetSons(self):
        # type: () -> List[PageGroup]
        """
            获取子页组（其子页组可以是Category对象，也可以是Entry对象，因为目录是允许嵌套的）
        """
        pass

    def GetParent(self):
        # type: () -> float
        """
            获取父页组（其父页组可以是Category对象，也可以是Entry对象，因为目录是允许嵌套的）
        """ 
        pass

    def isLocked(self):
        # type: () -> bool
        """
            返回该目录解锁状态
        """ 
        pass


    def Lock(self):
        # type: () -> None
        """
            将该目录上锁
        """ 
        pass

    def Unlock(self):
        # type: () -> None
        """
            将该目录解锁
        """
        pass

    def GetProgressValue(self):
        # type: () -> float
        """
            获取子页组解锁的进度，常用于进度条显示
        """
        pass

