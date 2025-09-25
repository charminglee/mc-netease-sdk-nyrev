# -*- coding: utf-8 -*-

from typing import Union
from typing import List
from mod.common.component.baseComponent import BaseComponent

class HttpToWebServerCompServer(BaseComponent):
    def GetPlayerUid(self, playerId):
        # type: (str) -> int
        """
        获取玩家的uid。只有在线玩家才可获取
        """
        pass

    def QueryLobbyUserItem(self, callback, uid):
        # type: (Callable, int) -> None
        """
        查询还没发货的订单。仅联机大厅可用
        """
        pass

    def LobbyGetStorage(self, callback, uid, keys):
        # type: (Callable, int, List[str]) -> None
        """
        获取存储的数据。仅联机大厅可用
        """
        pass

    def LobbySetStorageAndUserItem(self, callback, uid, orderId=None, entitiesGetter=None):
        # type: (Callable, int, Union[int,None], Union[Callable,None]) -> None
        """
        设置订单已发货或者存数据。仅联机大厅可用
        """
        pass

    def LobbyGetStorageBySort(self, callback, key, ascend, offset, length):
        # type: (Callable, str, bool, int, int) -> None
        """
        排序获取存储的数据。仅联机大厅可用
        """
        pass

