# -*- coding: utf-8 -*-


class BaseComponent(object):
    def __init__(self, entityId):
        # type: (str | int) -> None
        self.mEntityId = entityId # type: str | int

    def GetEntityId(self):
        # type: () -> str | int
        return self.mEntityId

    def Destroy(self):
        # type: () -> None
        pass
