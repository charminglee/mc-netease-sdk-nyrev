# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Literal


class AttrCompClient(BaseComponent):
    def isEntityInLava(self):
        # type: () -> bool
        """
        实体是否在岩浆中
        """
        pass

    def isEntityOnGround(self):
        # type: () -> bool
        """
        实体是否触地
        """
        pass

    def GetAttrValue(self, attrType):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int) -> float
        """
        获取属性值，包括生命值，饥饿度，移速
        """
        pass

    def GetAttrMaxValue(self, type):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int) -> float
        """
        获取属性最大值，包括生命值，饥饿度，移速等
        """
        pass

