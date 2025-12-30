# -*- coding: utf-8 -*-


from typing import Tuple


class PosComponentClient(object):
    def GetPos(self):
        # type: () -> Tuple[float, float, float]
        """
        获取实体位置
        """
        pass

    def GetFootPos(self):
        # type: () -> Tuple[float, float, float]
        """
        获取实体脚所在的位置
        """
        pass

    def SetPosForClientEntity(self, pos):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置客户端实体位置。
        """
        pass

