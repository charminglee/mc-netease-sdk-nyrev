# -*- coding: utf-8 -*-


from typing import Optional
from typing import List, TypedDict
from mod.common.component.baseComponent import BaseComponent


class __EffectDict(TypedDict):
    effectName: str
    duration: int
    duration_f: float
    amplifier: int


class EffectComponentClient(BaseComponent):
    def GetAllEffects(self):
        # type: () -> Optional[List[__EffectDict]]
        """
        获取实体当前所有状态效果
        """
        pass

    def HasEffect(self, effectName):
        # type: (str) -> bool
        """
        获取实体是否存在当前状态效果
        """
        pass

