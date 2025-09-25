# -*- coding: utf-8 -*-

from typing import Any
from mod.common.component.baseComponent import BaseComponent

class ModAttrComponentServer(BaseComponent):
    def SetAttr(self, paramName, paramValue, needRestore=False, autoSave=True):
        # type: (str, Any, bool, bool) -> None
        """
        设置属性值。服务端设置后会自动同步到客户端，可以用客户端的GetAttr获取。默认不会存档，需要存档的话可以设置needRestore=True。
        """
        pass

    def SaveAttr(self):
        # type: () -> None
        """
        保存SetAttr设置的属性值
        """
        pass

    def GetAttr(self, paramName, defaultValue=None):
        # type: (str, Any) -> Any
        """
        获取SetAttr设置的属性值
        """
        pass

