# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class FrameAniEntityBindComp(BaseComponent):
    def Bind(self, bindEntityId, offset, rot):
        # type: (str, Tuple[float, float, float], Tuple[float, float, float]) -> bool
        """
        绑定entity
        """
        pass

