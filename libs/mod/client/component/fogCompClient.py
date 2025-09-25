# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class FogCompClient(BaseComponent):
    def SetFogColor(self, color):
        # type: (Tuple[float, float, float, float]) -> bool
        """
        设置雾效颜色
        """
        pass

    def ResetFogColor(self):
        # type: () -> bool
        """
        重置雾效颜色
        """
        pass

    def GetUseFogColor(self):
        # type: () -> bool
        """
        判断当前是否开启设置雾效颜色，该值默认为False，使用mod传入的颜色值后为True
        """
        pass

    def GetFogColor(self):
        # type: () -> Tuple[float, float, float, float]
        """
        获取当前雾效颜色
        """
        pass

    def SetFogLength(self, start=None, end=None):
        # type: (float, float) -> bool
        """
        设置雾效范围
        """
        pass

    def GetFogLength(self):
        # type: () -> Tuple[float, float]
        """
        获取雾效范围
        """
        pass

    def ResetFogLength(self):
        # type: () -> bool
        """
        重置雾效范围
        """
        pass

    def GetUseFogLength(self):
        # type: () -> bool
        """
        判断当前是否开启设置雾效范围,该值默认为False，使用mod传入的范围值后为True
        """
        pass

