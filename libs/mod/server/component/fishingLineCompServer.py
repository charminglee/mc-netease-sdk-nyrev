# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class FishingLineCompServer(BaseComponent):
    def SetFishingLineMax(self, itemName, maxLength):
        # type: (str, float) -> bool
        """
        设置钓鱼线的最大长度（超过此长度会断线），设置后会自动同步到所有客户端。
        """
        pass

    def GetFishingLineMax(self, itemName):
        # type: (str) -> float
        """
        获取服务端当前设置的钓鱼线最大长度
        """
        pass

    def SetFishingLineColor(self, itemName, color):
        # type: (str, Tuple[float, float, float]) -> bool
        """
        设置钓鱼线的颜色，设置后会自动同步到所有客户端。
        """
        pass

    def GetFishingLineColor(self, itemName):
        # type: (str) -> Tuple[float, float, float]
        """
        获取服务端当前设置的钓鱼线颜色
        """
        pass

