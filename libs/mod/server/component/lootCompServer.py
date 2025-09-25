# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent

class LootComponentServer(BaseComponent):
    def GetLootItems(self, lootPath, entityId='-1', killerId='-1', luck=0.0, getUserData=False):
        # type: (str, str, str, float, bool) -> List[dict]
        """
        指定战利品表获取一次战利品，返回的物品与json定义的概率有关
        """
        pass

