# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class HealthComponentClient(BaseComponent):
    def SetColor(self, front, back):
        # type: (Tuple[float,float,float,float], Tuple[float,float,float,float]) -> 'None'
        """
        设置血条的颜色及背景色
        """
        pass

    def ShowHealth(self, show):
        # type: (bool) -> 'None'
        """
        设置某个entity是否显示血条，默认为显示
        """
        pass

    def SetHealthBarDeviation(self, health_bar_deviation):
        # type: (float) -> 'bool'
        """
        设置某个entity血条的相对高度
        """
        pass

