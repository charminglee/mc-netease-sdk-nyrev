# -*- coding: utf-8 -*-


from typing import List, Dict
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class BiomeCompServer(BaseComponent):
    def SetBiomeInfo(self, biomeName, snowAccumulation, temperature, downfall, isRain):
        # type: (str, Tuple[float, float], float, float, bool) -> bool
        """
        设置群系天气相关参数
        """
        pass

    def GetBiomeInfo(self, biomeName):
        # type: (str) -> dict
        """
        获取群系天气相关参数
        """
        pass

    def GetBiomeName(self, pos, dimId=-1):
        # type: (Tuple[int, int, int], int) -> str
        """
        获取某一位置所属的生物群系信息
        """
        pass

    def SetBiomeByPos(self, pos, biomeName, dimId):
        # type: (Tuple[int, int, int], str, int) -> bool
        """
        设置某一位置所属的生物群系信息
        """
        pass

    def SetBiomeByPosList(self, posList, biomeName, dimId):
        # type: (List[Tuple[int, int, int]], str, int) -> Dict[str, bool | list]
        """
        设置所有列表中位置所属的生物群系信息
        """
        pass

    def SetBiomeByVolume(self, minPos, maxPos, biomeName, dimId):
        # type: (Tuple[int, int, int], Tuple[int, int, int], str, int) -> bool
        """
        设置长方体空间中所属的生物群系信息
        """
        pass

