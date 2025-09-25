# -*- coding: utf-8 -*-

from typing import List, Callable, Optional
from mod.common.component.baseComponent import BaseComponent

class AchievementCompServer(BaseComponent):
    def GetNodeDetailInfo(self, playerId, nodeId):
        # type: (str, str) -> dict
        """
        获取对应玩家的对应节点信息
        """
        pass

    def SetNodeFinish(self, playerId, nodeId, callback=None, getExtra=None):
        # type: (str, str, Optional[Callable], Optional[Callable]) -> bool
        """
        设置对应玩家的对应成就节点完成
        """
        pass

    def AddNodeProgress(self, playerId, nodeId, delta, callback=None, getExtra=None):
        # type: (str, str, int, Optional[Callable], Optional[Callable]) -> bool
        """
        增加对应玩家的对应成就节点的成就进度
        """
        pass

    def GetChildrenNode(self, nodeId):
        # type: (str) -> List[str]
        """
        获得该成就节点的下一级所有孩子节点的list
        """
        pass

    def LobbyGetAchievementStorage(self, callback, playerId):
        # type: (Callable, int) -> None
        """
        获取成就节点的存储的数据。
        """
        pass

    def LobbySetAchievementStorage(self, callback, playerId, nodeId, delta, getExtraData=None):
        # type: (Callable, int, str, int, Optional[Callable]) -> None
        """
        添加成就节点的进度。
        """
        pass

