# -*- coding: utf-8 -*-


from typing import List, Literal
from mod.common.component.baseComponent import BaseComponent


__AttrType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


class AttrCompServer(BaseComponent):
    def SetAttrValue(self, attrType, value, setDefault=1):
        # type: (__AttrType, float, Literal[0, 1]) -> bool
        """
        设置实体的引擎属性
        """
        pass

    def GetAttrValue(self, attrType):
        # type: (__AttrType) -> float
        """
        获取实体的引擎属性
        """
        pass

    def SetAttrMaxValue(self, type, value):
        # type: (__AttrType, float) -> bool
        """
        设置实体的引擎属性的最大值
        """
        pass

    def GetAttrMaxValue(self, type):
        # type: (__AttrType) -> float
        """
        获取实体的引擎属性的最大值
        """
        pass

    def IsEntityOnFire(self):
        # type: () -> bool
        """
        获取实体是否着火
        """
        pass

    def SetEntityOnFire(self, seconds, burn_damage=1):
        # type: (int, int) -> bool
        """
        设置实体着火
        """
        pass

    def SetStepHeight(self, stepHeight):
        # type: (float) -> bool
        """
        设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶
        """
        pass

    def GetStepHeight(self):
        # type: () -> float
        """
        返回玩家前进非跳跃状态下能上的最大台阶高度
        """
        pass

    def ResetStepHeight(self):
        # type: () -> bool
        """
        恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度
        """
        pass

    def GetTypeFamily(self):
        # type: () -> List[str]
        """
        获取生物行为包字段 type_family
        """
        pass

    def SetPersistent(self, persistent):
        # type: (bool) -> bool
        """
        设置实体不会因为离玩家太远而被清除
        """
        pass

    def ResetToDefaultValue(self, type):
        # type: (__AttrType) -> bool
        """
        重置实体引擎属性到默认值
        """
        pass

    def ResetToMaxValue(self, type):
        # type: (__AttrType) -> bool
        """
        重置实体引擎属性到最大值
        """
        pass

