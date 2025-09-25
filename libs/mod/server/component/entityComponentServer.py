# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent

class EntityComponentServer(BaseComponent):
    def HasComponent(self, attrType):
        # type: (int) -> bool
        """
        判断实体是否有原版组件
        """
        pass

    def GetAllComponentsName(self):
        # type: () -> List[str]
        """
        获取实体所拥有的原版组件list
        """
        pass

    def GetEntitiesBySelector(self, command):
        # type: (str) -> List[str]
        """
        传入目标选择器，获取对应实体id (最大范围是所有已加载的实体)
        """
        pass

