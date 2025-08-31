# -*- coding: utf-8 -*-
class CustomGoal(object):
    def __init__(self, entityId, argsJson):
        pass

    def CanUse(self):
        pass

    def CanContinueToUse(self):
        pass

    def CanBeInterrupted(self):
        pass

    def Start(self):
        pass

    def Tick(self):
        pass

    def Stop(self):
        pass

    def GetEntityId(self):
        # type: () -> str
        pass

    def GetArgs(self):
        # type: () -> dict
        pass
