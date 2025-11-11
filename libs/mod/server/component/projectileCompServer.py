# -*- coding: utf-8 -*-


from typing import TypedDict, Tuple
from mod.common.component.baseComponent import BaseComponent


class __ProjectileParamDict(TypedDict, total=False):
    position: Tuple[float, float, float]
    direction: Tuple[float, float, float]
    power: float
    gravity: float
    damage: float
    targetId: str
    isDamageOwner: bool
    auxValue: int


class ProjectileComponentServer(BaseComponent):
    def CreateProjectileEntity(self, spawnerId, entityIdentifier, param=None):
        # type: (str, str, __ProjectileParamDict) -> str
        """
        创建抛射物（直接发射）
        """
        pass

