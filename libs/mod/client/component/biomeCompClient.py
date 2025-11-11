# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class BiomeCompClient(BaseComponent):
    def GetBiomeName(self, pos):
        # type: (Tuple[int, int, int]) -> str
        """
        获取客户端当前维度已加载区域某一位置所属的生物群系信息
        """
        pass

