# -*- coding: utf-8 -*-


from typing import List, TypedDict, Tuple, Optional
from mod.common.component.baseComponent import BaseComponent


class __ItemDict(TypedDict, total=False):
    newItemName: str
    newAuxValue: int
    itemName: str
    auxValue: int
    count: int
    showInHand: bool
    enchantData: List[Tuple[int, int]]
    modEnchantData: List[Tuple[str, int]]
    customTips: str
    extraId: str
    userData: Optional[dict]
    durability: int


class ShareableComponentServer(BaseComponent):
    def SetEntityShareablesItems(self, items):
        # type: (List[__ItemDict]) -> bool
        """
        设置生物可分享/可拾取的物品列表
        """
        pass

