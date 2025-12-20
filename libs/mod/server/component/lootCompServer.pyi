# -*- coding: utf-8 -*-


from typing import List, TypedDict, Tuple
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
    userData: dict | None
    durability: int


class LootComponentServer(BaseComponent):
    def GetLootItems(self, lootPath, entityId='-1', killerId='-1', luck=0.0, getUserData=False):
        # type: (str, str, str, float, bool) -> List[__ItemDict]
        """
        指定战利品表获取一次战利品，返回的物品与json定义的概率有关
        """
        pass

