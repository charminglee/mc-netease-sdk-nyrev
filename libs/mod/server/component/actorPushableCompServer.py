# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Literal


class ActorPushableCompServer(BaseComponent):
    def SetActorPushable(self, isPushable):
        # type: (Literal[0, 1] | int) -> bool
        """
        设置实体是否可推动
        """
        pass

