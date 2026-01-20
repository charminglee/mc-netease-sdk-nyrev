# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Dict, Any


class QueryVariableComponentServer(BaseComponent):
    def EvalMolangExpression(self, expression):
        # type: (str) -> Dict[str, str | Any]
        """
        在实体上下文上执行molang表达式
        """
        pass

    def GetAllProperties(self):
        # type: () -> Tuple[str, ...]
        """
        获取实体属性列表
        """
        pass

    def SetPropertyValue(self, propertyName, value):
        # type: (str, str) -> bool
        """
        设置实体属性的值
        """
        pass

