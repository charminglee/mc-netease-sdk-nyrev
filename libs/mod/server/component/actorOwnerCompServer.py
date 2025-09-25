# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class ActorOwnerComponentServer(BaseComponent):
    def SetEntityOwner(self, targetId):
        # type: (str) -> bool
        """
        设置实体的属主（包括可驯服生物的主人，或者掉落物的丢弃者，弹射物的发射者等）
        """
        pass

    def GetEntityOwner(self):
        # type: () -> str
        """
        获取实体的属主（包括可驯服生物的主人，或者掉落物的丢弃者，弹射物的发射者等）
        """
        pass

