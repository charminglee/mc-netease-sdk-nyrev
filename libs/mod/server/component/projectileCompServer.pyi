# -*- coding: utf-8 -*-


from typing import Dict
from mod.common.component.baseComponent import BaseComponent


class ProjectileComponentServer(BaseComponent):
    def CreateProjectileEntity(self, spawnerId, entityIdentifier, param=None):
        # type: (str, str, Dict[str, tuple | float | str | bool | int]) -> str
        """
        创建抛射物（直接发射）
        """
        pass

