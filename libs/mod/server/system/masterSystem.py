# -*- coding: utf-8 -*-

from typing import Any, Optional, Callable

class MasterSystem(object):
    def CreateEventData(self):
        # type: () -> dict
        """
        创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple
        """
        pass

    def DefineEvent(self, eventName):
        # type: (str) -> None
        """
        定义自定义事件
        """
        pass

    def ListenForEvent(self, namespace, systemName, eventName, instance, func):
        # type: (str, str, str, Any, Callable) -> None
        """
        注册监听某个系统抛出的事件。若监听引擎事件时，namespace和systemName分别为GetEngineNamespace（）和GetEngineSystemName（）
        """
        pass

    def NotifyToServerNode(self, targetId, eventName, eventData):
        # type: (int, str, dict) -> None
        """
        master给某个lobby/game发事件
        """
        pass

    def RegisterRpcMethod(self, module, func, event):
        # type: (str, Callable, str) -> None
        """
        用于注册一个监听函数。用于监听service/master发过来请求。要求公共配置netgame_common.json中配置service/master module_names信息。
        """
        pass

    def RequestToService(self, module, event, eventData, callback=None, timeout=2.0):
        # type: (str, str, dict, Optional[Callable], int) -> None
        """
        给service/master发请求。
        """
        pass

    def ResponseToServer(self, serverId, callbackId, eventData):
        # type: (int, int, dict) -> None
        """
        给service/master返回一个消息。若函数RequestToService的callback参数为空，则不能调用该接口。
        """
        pass

    def UnDefineEvent(self, eventName):
        # type: (str) -> None
        """
        取消自定义事件
        """
        pass

    def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
        # type: (str, str, str, Any, Callable) -> None
        """
        反注册监听某个系统抛出的事件，即不再监听。若是引擎事件，则namespace和systemName分别为GetEngineNamespace（）和GetEngineSystemName（）。与ListenForEvent对应。
        """
        pass

