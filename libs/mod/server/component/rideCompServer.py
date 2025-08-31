# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class RideCompServer(BaseComponent):
    def SetEntityRide(self, playerId, tamedEntityId):
        # type: (str, str) -> 'bool'
        """
        驯服可骑乘生物
        """
        pass

    def SetRidePos(self, tamedEntityId, pos):
        # type: (str, Tuple[float,float,float]) -> 'bool'
        """
        设置生物骑乘位置
        """
        pass

    def SetControl(self, tamedEntityId, isControl):
        # type: (str, bool) -> 'bool'
        """
        设置该生物无需装备鞍就可以控制行走跳跃
        """
        pass

    def SetCanOtherPlayerRide(self, tamedEntityId, canRide):
        # type: (str, bool) -> 'bool'
        """
        设置其他玩家是否有权限骑乘，True表示每个玩家都能骑乘，False只有驯服者才能骑乘
        """
        pass

    def SetShowRideUI(self, tamedEntityId, isShowUI):
        # type: (str, bool) -> 'bool'
        """
        设置是否显示马匹的UI界面
        """
        pass

    def IsEntityRiding(self):
        # type: () -> 'bool'
        """
        检查玩家是否骑乘。
        """
        pass

    def GetEntityRider(self):
        # type: () -> 'str'
        """
        获取骑乘者正在骑乘的实体的id。
        """
        pass

    def StopEntityRiding(self):
        # type: () -> 'bool'
        """
        强制骑乘者下坐骑。
        """
        pass

    def SetRiderRideEntity(self, riderId, riddenEntityId, riderIndex=-1):
        # type: (str, str, int) -> 'bool'
        """
        设置实体骑乘生物（或者船与矿车）
        """
        pass

    def SetEntityLockRider(self, isLock):
        # type: (bool) -> 'bool'
        """
        设置坐骑上的实体是否锁定序号
        """
        pass

    def ChangeRiderSeat(self, riderIndex):
        # type: (int) -> 'bool'
        """
        设置骑乘者在当前坐骑上的序号
        """
        pass

    def GetRiders(self):
        # type: () -> 'List[dict]'
        """
        获取坐骑上的骑乘者信息
        """
        pass

    def AddEntitySeat(self, pos, rot=0, lock_rot=181):
        # type: (Tuple[float,float,float], float, float) -> 'int'
        """
        增加坐骑座位
        """
        pass

    def SetEntitySeat(self, seatIndex, pos, rot=0, lock_rot=181):
        # type: (int, Tuple[float,float,float], float, float) -> 'bool'
        """
        设置坐骑座位的位置、旋转以及允许实体旋转范围
        """
        pass

    def DeleteEntitySeat(self, seatIndex):
        # type: (int) -> 'bool'
        """
        删除坐骑座位
        """
        pass

