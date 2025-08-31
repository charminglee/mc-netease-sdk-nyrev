# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ParticleSkeletonBindComp(BaseComponent):
    def Bind(self, modelId, boneName, offset, rot):
        # type: (int, str, Tuple[float,float,float], Tuple[float,float,float]) -> 'bool'
        """
        绑定骨骼模型
        """
        pass

