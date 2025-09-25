# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class EntityEventComponentServer(BaseComponent):
    def AddActorComponentGroup(self, groupName):
        # type: (str) -> bool
        """
        给指定实体添加实体json中配置的ComponentGroup
        """
        pass

    def RemoveActorComponentGroup(self, groupName):
        # type: (str) -> bool
        """
        移除指定实体在实体json中配置的ComponentGroup
        """
        pass

    def AddActorComponent(self, componentName, componentValue):
        # type: (str, str) -> bool
        """
        给指定实体自定义添加实体Component
        """
        pass

    def RemoveActorComponent(self, componentName):
        # type: (str) -> bool
        """
        删除指定实体的指定Component
        """
        pass

    def GetComponents(self):
        # type: () -> dict
        """
        获取指定实体的生效Components
        """
        pass

    def TriggerCustomEvent(self, entityId, eventName):
        # type: (str, str) -> bool
        """
        触发生物自定义事件
        """
        pass

