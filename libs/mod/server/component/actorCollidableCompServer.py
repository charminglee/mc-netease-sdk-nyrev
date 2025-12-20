# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Literal


class ActorCollidableCompServer(BaseComponent):
    def SetActorCollidable(self, isCollidable):
        # type: (Literal[0, 1] | int) -> bool
        """
        设置实体是否可碰撞
        """
        pass

