# -*- coding: utf-8 -*-


from typing import Union
from typing import List
from mod.common.system.baseSystem import BaseSystem
from typing import Tuple, Optional


class ServerSystem(BaseSystem):
    def BroadcastToAllClient(self, eventName, eventData):
        # type: (str, dict) -> None
        """
        服务器广播事件到所有客户端
        """
        pass

    def NotifyToMultiClients(self, targetIdList, eventName, eventData):
        # type: (List[str], str, dict) -> None
        """
        服务器发送事件到指定一批客户端，相比于在for循环内使用NotifyToClient性能更好
        """
        pass

    def NotifyToClient(self, targetId, eventName, eventData):
        # type: (str, str, dict) -> None
        """
        服务器发送事件到指定客户端
        """
        pass

    def CreateEngineEntityByNBT(self, nbtDict, pos=None, rot=None, dimensionId=0, isNpc=False, isGlobal=None):
        # type: (dict, Optional[Tuple[float, float, float]], Optional[Tuple[float, float]], int, bool, Optional[bool]) -> Union[str, None]
        """
        根据nbt数据创建实体
        """
        pass

    def CreateEngineEntityByTypeStr(self, engineTypeStr, pos, rot, dimensionId=0, isNpc=False, isGlobal=False):
        # type: (str, Tuple[float, float, float], Tuple[float, float], int, bool, bool) -> Union[str, None]
        """
        创建指定identifier的实体
        """
        pass

    def CreateEngineItemEntity(self, itemDict, dimensionId=0, pos=(0, 0, 0)):
        # type: (dict, int, Tuple[float, float, float]) -> Union[str, None]
        """
        用于创建物品实体（即掉落物），返回物品实体的entityId
        """
        pass

    def DestroyEntity(self, entityId):
        # type: (str) -> bool
        """
        销毁实体
        """
        pass

