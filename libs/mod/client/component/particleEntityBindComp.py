# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ParticleEntityBindComp(BaseComponent):
    def Bind(self, bindEntityId, offset, rot, correction=False, isClientEntity=False):
        # type: (str, Tuple[float, float, float], Tuple[float, float, float], bool, bool) -> bool
        """
        绑定entity
        """
        pass

