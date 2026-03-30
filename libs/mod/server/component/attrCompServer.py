# -*- coding: utf-8 -*-


from typing import List, Literal
from mod.common.component.baseComponent import BaseComponent


class AttrCompServer(BaseComponent):
    def SetAttrValue(self, attrType, value, setDefault=1):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int, float, Literal[0, 1] | int) -> bool
        """
        设置实体的引擎属性
        """
        pass

    def GetAttrValue(self, attrType):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int) -> float
        """
        获取实体的引擎属性
        """
        pass

    def SetAttrMaxValue(self, type, value):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int, float) -> bool
        """
        设置实体的引擎属性的最大值
        """
        pass

    def GetAttrMaxValue(self, type):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int) -> float
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
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int) -> bool
        """
        重置实体引擎属性到默认值
        """
        pass

    def ResetToMaxValue(self, type):
        # type: (Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | int) -> bool
        """
        重置实体引擎属性到最大值
        """
        pass

    def AddModifier(self, attrType, modifierId, amount, operation, operand):
        # type: (int, str, float, int, int) -> bool
        """
        为指定生物增加属性修饰符
        """
        pass

    def UpdateModifier(self, attrType, modifierId, amount, operation, operand):
        # type: (int, str, float, int, int) -> bool
        """
        为指定生物更新属性修饰符
        """
        pass

    def RemoveModifier(self, attrType, modifierId):
        # type: (int, str) -> bool
        """
        为指定生物移除属性修饰符
        """
        pass

    def HasModifier(self, attrType, modifierId):
        # type: (int, str) -> bool
        """
        获取指定生物是否含有属性修饰符
        """
        pass

    def GetAllModifiers(self, attrType):
        # type: (int) -> List[dict]
        """
        获取指定生物的某属性所有属性修饰符
        """
        pass

