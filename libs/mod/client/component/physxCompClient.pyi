# -*- coding: utf-8 -*-


from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class PhysxComponentClient(BaseComponent):
    def GetQuaternion(self):
        # type: () -> Tuple[float, float, float, float]
        """
        获取自定义刚体的四元数旋转
        """
        pass

    def Raycast(self, origin, dir, maxDist, maxHits):
        # type: (Tuple[float, float, float], Tuple[float, float, float], float, int) -> List[dict]
        """
        射线检测，获取与射线相交的碰撞体。目前仅支持获取自定义刚体
        """
        pass

