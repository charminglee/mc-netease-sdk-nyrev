# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class ScaleComponentServer(BaseComponent):
    def SetEntityScale(self, entityId, scale):
        # type: (str, float) -> int
        """
        设置实体的放缩比例大小，设置比例过大会导致游戏卡顿，建议控制在20倍以内。实体的scale的立方乘以包围盒的体积不可超过32768
        """
        pass

    def GetEntityScale(self):
        # type: () -> float
        """
        获取实体的放缩比例大小
        """
        pass

