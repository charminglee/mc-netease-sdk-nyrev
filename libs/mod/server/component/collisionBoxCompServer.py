# -*- coding: utf-8 -*-

from typing import Tuple

class CollisionBoxComponentServer(object):
    def SetSize(self, size):
        # type: (Tuple[float,float]) -> 'bool'
        """
        设置实体的包围盒。设置过大会导致游戏卡顿。实体的scale的立方乘以包围盒的体积不可超过32768
        """
        pass

    def GetSize(self):
        # type: () -> 'Tuple[float,float]'
        """
        获取实体的包围盒
        """
        pass

