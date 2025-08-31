
# -*- coding: utf-8 -*-
from mod.client.ui.controls.baseUIControl import BaseUIControl
from mod.client.plugin.illustratedBook.page.basePage import BasePage
from typing import List
from typing import Dict
from typing import Tuple


class BaseComp(object):

    def __init__(self, compName, jsonFile, compNodeName, recycled = False):
        # type: (str, str, str, bool) -> BaseComp
        """
            初始化组件
        """
        self.compName = ''  # type: str
        self.jsonFile = ''  # type: str
        self.compNodeName = ''  # type: str
        self.recycled = ''  # type: bool

    def Show(self):
        # type: () -> BaseComp
        """
            显示组件
        """       
        return self

    def Hide(self):
        # type: () -> BaseComp
        """
            隐藏组件
        """       
        return self    

    def Reset(self):
        # type: () -> BaseComp
        """
            当组件回收的时候对UI控件节点进行属性重置
        """       
        return self        

    def GetPosition(self):
        # type: () -> Tuple[int, int]
        """
            当组件回收的时候对UI控件节点进行属性重置
        """       
        pass        

    def SetPosition(self, newPosition):
        # type: (Tuple[int,int]) -> BaseComp
        """
            当组件回收的时候对UI控件节点进行属性重置
        """       
        return self 

    def GetSize(self):
        # type: () -> Tuple[int, int]
        """
            获取组件的大小
        """       
        pass        

    def SetSize(self, newSize):
        # type: (Tuple[int,int]) -> BaseComp
        """
            设置组件大小
        """       
        return self 

    def Center(self):
        # type: () -> Tuple[int, int]
        """
            获取组件的中心坐标
        """       
        pass

    def Left(self):
        # type: () -> int
        """
            获取组件左边界的X值
        """       
        pass
    
    def Right(self):
        # type: () -> int
        """
            获取组件右边界的X值
        """       
        pass

    def Top(self):
        # type: () -> int
        """
            获取组件上边界的Y值
        """       
        pass

    def Bottom(self):
        # type: () -> int
        """
            获取组件下边界的Y值
        """       
        pass

    def MoveToX(self, x):
        # type: (int) -> BaseComp
        """
            不改变组件位置坐标的Y值，单独设置组件位置坐标的X值
        """       
        return self

    def MoveToY(self, y):
        # type: (int) -> BaseComp
        """
            不改变组件位置坐标的X值，单独设置组件位置坐标的Y值
        """       
        return self

    def MoveX(self, x):
        # type: (int) -> BaseComp
        """
            沿X轴正方向移动一段距离
        """       
        return self

    def MoveY(self, y):
        # type: (int) -> BaseComp
        """
            沿Y轴正方向移动一段距离
        """       
        return self

    def AlignCenterToX(self, x):
        # type: (int) -> BaseComp
        """
            水平移动组件使组件中心到指定的x值
        """       
        return self

    def AlignCenterToY(self, y):
        # type: (int) -> BaseComp
        """
            垂直移动组件使组件中心到指定的y值
        """       
        return self

    def AlignCenterToPosition(self, position):
        # type: (Tuple[int, int]) -> BaseComp
        """
            移动组件使组件中心到指定的坐标值
        """       
        return self

    def AlignLeftToX(self, x):
        # type: (int) -> BaseComp
        """
            水平移动组件使组件左边界到指定的x值
        """       
        return self

    def AlignRightToX(self, x):
        # type: (int) -> BaseComp
        """
            水平移动组件使组件右边界到指定的x值
        """       
        return self

    def AlignTopToY(self, y):
        # type: (int) -> BaseComp
        """
            垂直移动组件使组件上边界到指定的y值
        """       
        return self

    def AlignBottomToY(self, y):
        # type: (int) -> BaseComp
        """
            垂直移动组件使组件下边界到指定的y值
        """       
        return self

    def GetRootUINode(self):
        # type: () -> BaseUIControl
        """
            获取组件所封装的UI控件根节点
        """       
        pass

    def HasRootUINode(self):
        # type: () -> bool
        """
            判断组件是否拥有UI控件根节点
        """       
        pass

    def SetNodeOffset(self, node, offset):
        # type: (BaseUIControl, Tuple[int, int]) -> BaseComp
        """
            对组件所封装的UI控件节点（以及其子孙节点）进行位置偏移
        """       
        return self

    def SetNodeSize(self, node, newSize):
        # type: (BaseUIControl, Tuple[int, int]) -> BaseComp
        """
            对组件所封装的UI控件节点（以及其子孙节点）进行大小设置
        """      
        return self

    def SetNodeText(self, node, text):
        # type: (BaseUIControl, str) -> BaseComp
        """
            对组件中指定的文本控件（LabelUIControl）设置文本
        """      
        return self

    def SetNodeTextFontSize(self, node, originFontSize, newFontSize):
        # type: (BaseUIControl, int, int) -> BaseComp
        """
            对组件中指定的文本控件（LabelUIControl）设置其文字大小
        """      
        return self

    def GetNodeCenterGlobal(self, node):
        # type: (BaseUIControl) -> Tuple[int, int]
        """
            获取组件中的指定UI控件节点的中心全局坐标
        """      
        pass

    def SetLayer(self, layer):
        # type: (int) -> BaseComp
        """
            更改组件所封装UI控件根节点的UI层级
        """      
        return self        

    def Call(self, callbackDict):
        # type: (Dict) -> object
        """
            调用回调函数
        """      
        pass

    def GetPage(self):        
        # type: () -> BasePage
        """
            返回组件当前所在的页面
        """      
        pass               
