# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class AchievementCompClient(BaseComponent):
    def SetAchievementGatePosition(self, x, y):
        # type: (float, float) -> bool
        """
        设置自定义成就系统的入口按钮位置
        """
        pass

    def GetAchievementGatePosition(self):
        # type: () -> Tuple[float, float]
        """
        获取自定义成就系统的入口按钮位置
        """
        pass

