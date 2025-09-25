# -*- coding: utf-8 -*-

from typing import Union
from typing import List
from mod.common.component.baseComponent import BaseComponent

class ItemBannedCompServer(BaseComponent):
    def AddBannedItem(self, itemName):
        # type: (str) -> bool
        """
        增加禁用物品
        """
        pass

    def GetBannedItemList(self):
        # type: () -> Union[List[str], None]
        """
        获取禁用物品列表
        """
        pass

    def RemoveBannedItem(self, itemName):
        # type: (str) -> bool
        """
        移除禁用物品
        """
        pass

    def ClearBannedItems(self):
        # type: () -> bool
        """
        清空禁用物品
        """
        pass

