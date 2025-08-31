# -*- coding: utf-8 -*-

from typing import Any

class ServiceSystem():
    def CreateEventData(self):
        # type: () -> 'dict'
        """
        创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple
        """
        pass

    def DefineEvent(self, eventName):
        # type: (str) -> 'None'
        """
        定义自定义事件
        """
        pass

    def ListenForEvent(self, namespace, systemName, eventName, instance, func):
        # type: (str, str, str, Any, function) -> 'None'
        """
        注册监听某个系统抛出的事件。若监听引擎事件时，namespace和systemName分别为GetEngineNamespace（）和GetEngineSystemName（）
        """
        pass

    def NotifyToServerNode(self, targetId, eventName, eventData):
        # type: (int, str, dict) -> 'None'
        """
        service给某个lobby/game发消息。
        """
        pass

    def RegisterRpcMethod(self, module, func, event):
        # type: (str, function, str) -> 'None'
        """
        用于注册一个监听函数，用于监听lobby/game发过来请求。
        """
        pass

    def RegisterRpcMethodForMod(self, method, func):
        # type: (str, function) -> 'None'
        """
        用于注册一个监听函数，用于监听lobby/game发过来请求。直接使用service进程的type作为默认模块名
        """
        pass

    def RequestToService(self, module, event, eventData, callback=None, timeout=2.0):
        # type: (str, str, dict, function, int) -> 'None'
        """
        给service发请求。两个service间可以通过这个接口通信。
        """
        pass

    def RequestToServiceMod(self, modname, method, args, callback=None, timeout=2.0):
        # type: (str, str, dict, function, int) -> 'None'
        """
        给service发请求。两个service间可以通过这个接口通信。
        """
        pass

    def ResponseToServer(self, serverId, callbackId, eventData):
        # type: (int, int, dict) -> 'None'
        """
        给lobby/game返回一个消息。若函数RequestToService的callback参数为空，则不能调用该接口。
        """
        pass

    def UnDefineEvent(self, eventName):
        # type: (str) -> 'None'
        """
        取消自定义事件
        """
        pass

    def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
        # type: (str, str, str, Any, function) -> 'None'
        """
        反注册监听某个系统抛出的事件，即不再监听。若是引擎事件，则namespace和systemName分别为GetEngineNamespace（）和GetEngineSystemName（）。与ListenForEvent对应。
        """
        pass

