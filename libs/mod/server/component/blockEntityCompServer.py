# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class BlockEntityCompServer(BaseComponent):
    def SetCommandBlock(self, pos, dimensionId, cmd, name, mode, isConditional, redstoneMode):
        # type: (Tuple[int,int,int], int, str, str, int, int, int) -> 'bool'
        """
        对命令方块进行内容设置
        """
        pass

    def GetCommandBlock(self, pos, dimensionId):
        # type: (Tuple[int,int,int], int) -> 'dict'
        """
        获取命令方块的设置内容
        """
        pass

    def ExecuteCommandBlock(self, pos, dimensionId):
        # type: (Tuple[int,int,int], int) -> 'bool'
        """
        执行一次命令方块
        """
        pass

    def SetHopperSpeed(self, pos, dimensionId, moveTime):
        # type: (Tuple[int,int,int], int, int) -> 'bool'
        """
        设置漏斗运输一个物品所需的时间（单位：红石刻，1秒10刻），默认值为4刻，该设置存档
        """
        pass

    def GetHopperSpeed(self, pos, dimensionId):
        # type: (Tuple[int,int,int], int) -> 'int'
        """
        获取漏斗运输一个物品所需的时间（单位：刻）
        """
        pass

    def SetSignTextStyle(self, pos, dimensionId, color, lighting, side=0):
        # type: (Tuple[int,int,int], int, Tuple[float,float,float,float], bool, int) -> 'bool'
        """
        设置告示牌的文本样式
        """
        pass

    def GetSignTextStyle(self, pos, dimensionId, side=0):
        # type: (Tuple[int,int,int], int, int) -> 'dict'
        """
        获取告示牌的文本样式信息
        """
        pass

    def SetFrameRotation(self, pos, dimensionId, rot):
        # type: (Tuple[int,int,int], int, float) -> 'bool'
        """
        设置物品展示框里物品的顺时针旋转角度
        """
        pass

    def GetFrameRotation(self, pos, dimensionId):
        # type: (Tuple[int,int,int], int) -> 'float'
        """
        获取物品展示框里物品的顺时针旋转角度
        """
        pass

    def SetFrameItemDropChange(self, pos, dimensionId, change):
        # type: (Tuple[int,int,int], int, float) -> 'bool'
        """
        设置点击物品展示框时生成掉落的几率，默认为1
        """
        pass

    def GetFrameItemDropChange(self, pos, dimensionId):
        # type: (Tuple[int,int,int], int) -> 'float'
        """
        获取物品展示框里物品的掉落几率
        """
        pass

    def SetFrameItem(self, pos, dimensionId, itemDict):
        # type: (Tuple[int,int,int], int, dict) -> 'bool'
        """
        设置物品展示框的物品
        """
        pass

    def GetFrameItem(self, pos, dimensionId):
        # type: (Tuple[int,int,int], int) -> 'dict'
        """
        获取物品展示框的物品
        """
        pass

