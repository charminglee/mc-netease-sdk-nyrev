# -*- coding: utf-8 -*-


from typing import Literal
from mod.common.component.baseComponent import BaseComponent


class MobSpawnComponentServer(BaseComponent):
    def SpawnCustomModule(self, biomeType, change, entityType, probability, minCount, maxCount, environment, minBrightness=-1, maxBrightness=-1, minHeight=-1, maxHeight=-1):
        # type: (int, Literal[0, 1] | int, int, int, int, Literal[1, 2] | int, int, int, int, int, int) -> bool
        """
        设置自定义刷怪
        """
        pass

