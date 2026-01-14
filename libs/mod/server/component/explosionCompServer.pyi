# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class ExplosionComponentServer(BaseComponent):
    def CreateExplosion(self, pos, radius, fire, breaks, sourceId, playerId):
        # type: (Tuple[float, float, float], int, bool, bool, str, str) -> bool
        """
        用于生成爆炸
        """
        pass

