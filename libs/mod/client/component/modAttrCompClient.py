# -*- coding: utf-8 -*-

from typing import Any
from mod.common.component.baseComponent import BaseComponent

class ModAttrComponentClient(BaseComponent):
    def RegisterUpdateFunc(self, paramName, func):
        # type: (str, function) -> 'None'
        """
        注册属性值变换时的回调函数，当属性变化时会调用该函数
        """
        pass

    def UnRegisterUpdateFunc(self, paramName, func):
        # type: (str, function) -> 'None'
        """
        反注册属性值变换时的回调函数
        """
        pass

    def SetAttr(self, paramName, paramValue):
        # type: (str, Any) -> 'None'
        """
        设置客户端属性值
        """
        pass

    def GetAttr(self, paramName, defaultValue=None):
        # type: (str, Any) -> 'Any'
        """
        获取SetAttr设置的属性值
        """
        pass

