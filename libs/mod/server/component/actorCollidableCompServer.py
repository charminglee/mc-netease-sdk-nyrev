# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Literal


__IsCollidable = Literal[0, 1]


class ActorCollidableCompServer(BaseComponent):
    def SetActorCollidable(self, isCollidable):
        # type: (__IsCollidable) -> bool
        """
        设置实体是否可碰撞
        """
        pass

