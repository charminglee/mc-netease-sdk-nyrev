# -*- coding: utf-8 -*-


if 0:
    from typing import Any
    from .controls.baseUIControl import BaseUIControl


class NativeScreenRegisterData:
    def __init__(self, targetScreenName, targetComponentPath, customControlName, proxyClassName):
        # type: (str, str, str, str) -> None
        self.targetScreenName = targetScreenName # type: str
        self.targetComponentPath = targetComponentPath # type: str
        self.customControlName = customControlName # type: str
        self.proxyClassName = proxyClassName # type: str


class CustomUIControlProxy(object):
    def __init__(self, customData, customUIControl):
        # type: (NativeScreenRegisterData, BaseUIControl) -> None
        pass

    def OnCreate(self):
        # type: () -> None
        pass

    def OnDestroy(self):
        # type: () -> None
        pass

    def OnTick(self):
        # type: () -> None
        pass

    def GetCustomUIControl(self):
        # type: () -> BaseUIControl
        pass

    def GetCustomData(self):
        # type: () -> NativeScreenRegisterData
        pass
