# -*- coding: utf-8 -*-

from mod.common.minecraftEnum import ShapeType
from typing import Tuple

class DrawingShapeCompClient():
    def GetPos(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取Shape的位置
        """
        pass

    def GetBoxScale(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取BoxShape的大小
        """
        pass

    def GetColor(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取Shape的颜色
        """
        pass

    def GetType(self):
        # type: () -> 'ShapeType'
        """
        获取Shape的类型
        """
        pass

    def GetPriority(self):
        # type: () -> 'int'
        """
        获取Shape的优先级
        """
        pass

    def GetVisible(self):
        # type: () -> 'bool'
        """
        获取Shape是否可见
        """
        pass

    def GetEndPos(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取LineShape或ArrowShape的结束位置
        """
        pass

    def GetRadius(self):
        # type: () -> 'float'
        """
        获取CircleShape或ArrowShape或SphereShape的半径
        """
        pass

    def GetSegments(self):
        # type: () -> 'int'
        """
        获取CircleShape或ArrowShape头部的分段数
        """
        pass

    def GetText(self):
        # type: () -> 'str'
        """
        获取TextShape的文本
        """
        pass

    def GetLength(self):
        # type: () -> 'float'
        """
        获取ArrowShape的头部长度
        """
        pass

    def SetPos(self, pos):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置Shape的位置
        """
        pass

    def SetBoxScale(self, scale):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置BoxShape的大小
        """
        pass

    def SetEndPos(self, endPos):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置LineShape或ArrowShape的结束位置
        """
        pass

    def SetRadius(self, radius):
        # type: (float) -> 'bool'
        """
        设置CircleShape或ArrowShape或SphereShape的半径
        """
        pass

    def SetSegments(self, segments):
        # type: (int) -> 'bool'
        """
        设置组成ArrowShape头部的网格数量, 最小为3
        """
        pass

    def SetLength(self, length):
        # type: (float) -> 'bool'
        """
        设置组成ArrowShape头部的长度
        """
        pass

    def SetText(self, text):
        # type: (str) -> 'bool'
        """
        设置TextShape的文本内容
        """
        pass

    def SetColor(self, color):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置Shape的颜色
        """
        pass

    def SetPriority(self, priority):
        # type: (int) -> 'bool'
        """
        设置Shape的渲染优先级, 同一像素点处优先渲染优先级高的Shape, 默认为0
        """
        pass

    def SetVisible(self, visible):
        # type: (bool) -> 'bool'
        """
        设置Shape是否可见
        """
        pass

    def Remove(self):
        # type: () -> 'bool'
        """
        删除Shape
        """
        pass

