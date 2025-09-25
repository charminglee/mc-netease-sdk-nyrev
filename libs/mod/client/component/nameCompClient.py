# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class NameComponentClient(BaseComponent):
    def SetShowName(self, show):
        # type: (bool) -> bool
        """
        设置生物名字是否按照默认游戏逻辑显示（包括玩家）
        """
        pass

    def IsShowName(self):
        # type: () -> bool
        """
        获取生物名字是否按照默认游戏逻辑显示（包括玩家）
        """
        pass

    def SetAlwaysShowName(self, show):
        # type: (bool) -> bool
        """
        设置生物名字是否一直显示，瞄准点不指向生物时也能显示
        """
        pass

    def GetName(self):
        # type: () -> str
        """
        获取生物的自定义名称（即使用命名牌或者SetName接口设置的名称），或者玩家的名字。
        """
        pass

