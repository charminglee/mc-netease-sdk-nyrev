# -*- coding: utf-8 -*-


from typing import Any, Callable, Union


class BaseSystem(object):
    def __init__(self, namespace, systemName):
        # type: (str, str) -> None
        self.namespace = namespace
        self.systemName = systemName
        self.registerEvents = []
        self.notifyEvents = {}
        self.nameToListenEvents = {}

    def Update(self):
        pass

    def Destroy(self):
        pass

    def CreateEventData(self):
        # type: () -> dict
        """
        创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple
        """
        pass

    def ListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        # type: (str, str, str, Any, Union[Callable[[dict], Any], Callable[[], Any]], int) -> None
        """
        注册监听某个系统抛出的事件。若监听引擎事件时，namespace和systemName分别为GetEngineNamespace()和GetEngineSystemName()。具体每个事件的详细事件data可以参考"事件"分类下的内容
        """
        pass

    def UnListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        # type: (str, str, str, Any, Union[Callable[[dict], Any], Callable[[], Any]], int) -> None
        """
        反注册监听某个系统抛出的事件，即不再监听。若是引擎事件，则namespace和systemName分别为GetEngineNamespace和GetEngineSystemName。与ListenForEvent对应。
        """
        pass

    def UnListenAllEvents(self):
        # type: () -> None
        """
        反注册监听某个系统抛出的所有事件，即不再监听。
        """
        pass

    def BroadcastEvent(self, eventName, eventData):
        # type: (str, dict) -> None
        """
        本地广播事件，客户端system广播的事件仅客户端system能监听，服务器system广播的事件仅服务端system能监听。
        """
        pass

