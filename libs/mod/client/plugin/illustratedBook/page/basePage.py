
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.comp.baseComp import BaseComp
from typing import List
from typing import Dict
from typing import Tuple
from typing import Iterable

class BasePage(object):

    def __init__(self, size = None, position = None):
        # type: (Tuple[int, int], Tuple[int, int]) -> BasePage
        """
            初始化页面
        """
        pass

    def Show(self):
        # type: () -> BasePage
        """
            显示页面
        """       
        return self

    def Hide(self):
        # type: () -> BasePage
        """
            隐藏页面
        """       
        return self    

    def GetPosition(self):
        # type: () -> Tuple[int, int]
        """
            获取页面在书本坐标系中的位置
        """       
        pass        

    def GetSize(self):
        # type: () -> Tuple[int, int]
        """
            获取页面的大小
        """       
        pass        

    def Center(self):
        # type: () -> Tuple[int, int]
        """
            获取页面的中心坐标
        """       
        pass

    def Left(self):
        # type: () -> int
        """
            获取页面左边界的X值
        """       
        pass
    
    def Right(self):
        # type: () -> int
        """
            获取页面右边界的X值
        """       
        pass

    def Top(self):
        # type: () -> int
        """
            获取页面上边界的Y值
        """       
        pass

    def Bottom(self):
        # type: () -> int
        """
            获取页面下边界的Y值
        """       
        pass

    def Call(self, callbackDict):
        # type: (Dict) -> object
        """
            调用回调函数
        """      
        pass

    def ResetCompsPosition(self):
        # type: () -> BasePage
        """
            重置所有组件的位置为页面当前的位置
        """      
        return self        

    def GetPageGroup(self):
        # type: () -> BasePage
        """
            获取页面当前所在的页组对象
        """      
        pass

    def AddComps(self, *comps):
        # type: (*BaseComp) -> BasePage
        """
            向页面中添加组件
        """      
        return self    
