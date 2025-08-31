
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.group.pageGroup import PageGroup
from mod.client.plugin.illustratedBook.group.preset.category import Category
from typing import List
from typing import Dict
from typing import Tuple


class Entry(PageGroup):

    def GetParent(self):
        # type: () -> float
        """
            获取父页组（其父页组是Category对象）
        """ 
        pass
        

    def isLocked(self):
        # type: () -> bool
        """
            返回该章节解锁状态
        """ 
        pass


    def Lock(self):
        # type: () -> None
        """
            将该章节上锁
        """ 
        pass

    def Unlock(self):
        # type: () -> None
        """
            将该章节解锁
        """
        pass
