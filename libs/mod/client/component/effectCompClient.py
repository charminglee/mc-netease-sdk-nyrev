# -*- coding: utf-8 -*-


from typing import List, Dict
from mod.common.component.baseComponent import BaseComponent


class EffectComponentClient(BaseComponent):
    def GetAllEffects(self):
        # type: () -> List[Dict[str, str | int | float]]
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

