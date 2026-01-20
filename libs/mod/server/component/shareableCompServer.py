# -*- coding: utf-8 -*-


from typing import List, Dict
from mod.common.component.baseComponent import BaseComponent


class ShareableComponentServer(BaseComponent):
    def SetEntityShareablesItems(self, items):
        # type: (List[Dict[str, str | int | bool | list | dict | None]]) -> bool
        """
        设置生物可分享/可拾取的物品列表
        """
        pass

