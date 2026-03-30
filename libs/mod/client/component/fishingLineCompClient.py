# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class FishingLineCompClient(BaseComponent):
    def GetFishingLineMax(self, itemName):
        # type: (str) -> float
        """
        获取钓鱼线的最大长度
        """
        pass

    def GetFishingLineColor(self, itemName):
        # type: (str) -> Tuple[float, float, float]
        """
        获取钓鱼线的颜色
        """
        pass

