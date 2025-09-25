# -*- coding: utf-8 -*-

from mod.server.system.serviceSystem import ServiceSystem

def GetSystem(nameSpace, systemName):
    # type: (str, str) -> ServiceSystem
    """
    获取已注册的系统
    """
    pass

def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> ServiceSystem
    """
    系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与服务端进行通讯等。
    """
    pass

