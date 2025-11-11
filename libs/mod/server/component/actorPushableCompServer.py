# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Literal


__IsPushable = Literal[0, 1]


class ActorPushableCompServer(BaseComponent):
    def SetActorPushable(self, isPushable):
        # type: (__IsPushable) -> bool
        """
        设置实体是否可推动
        """
        pass

