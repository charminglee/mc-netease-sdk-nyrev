# -*- coding: utf-8 -*-


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
        pass

    def OnDestroy(self):
        pass

    def OnTick(self):
        pass

    def GetCustomUIControl(self):
        # type: () -> BaseUIControl
        pass

    def GetCustomData(self):
        # type: () -> NativeScreenRegisterData
        pass
