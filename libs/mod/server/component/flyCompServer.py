# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class FlyComponentServer(BaseComponent):
    def IsPlayerCanFly(self):
        # type: () -> bool
        """
        获取玩家能否飞行
        """
        pass

    def IsPlayerFlying(self):
        # type: () -> bool
        """
        获取玩家是否在飞行
        """
        pass

    def ChangePlayerFlyState(self, isFly, enterFly=True):
        # type: (bool, bool) -> bool
        """
        给予/取消飞行能力, 并根据enterFly参数确定是否进入飞行状态
        """
        pass

