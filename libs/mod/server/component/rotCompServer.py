# -*- coding: utf-8 -*-


from typing import Tuple


class RotComponentServer(object):
    def SetRot(self, rot):
        # type: (Tuple[float, float]) -> bool
        """
        设置实体头与水平方向的俯仰角度和竖直方向的旋转角度
        """
        pass

    def GetRot(self):
        # type: () -> Tuple[float, float]
        """
        获取实体头与水平方向的俯仰角度和竖直方向的旋转角度，获得角度后可用GetDirFromRot接口转换为朝向的单位向量
        """
        pass

    def SetEntityLookAtPos(self, targetPos, minTime, maxTime, reject):
        # type: (Tuple[float, float, float], float, float, bool) -> bool
        """
        设置非玩家的实体看向某个位置
        """
        pass

