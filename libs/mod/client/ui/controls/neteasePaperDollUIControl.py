# -*- coding: utf-8 -*-

from mod.client.ui.controls.baseUIControl import BaseUIControl

class NeteasePaperDollUIControl(BaseUIControl):
    def GetModelId(self):
        # type: () -> 'int'
        """
        获取渲染的骨骼模型Id
        """
        pass

    def RenderEntity(self, params):
        # type: (dict) -> 'bool'
        """
        渲染实体
        """
        pass

    def RenderSkeletonModel(self, params):
        # type: (dict) -> 'bool'
        """
        渲染骨骼模型（不依赖实体）
        """
        pass

    def RenderBlockGeometryModel(self, params):
        # type: (dict) -> 'bool'
        """
        渲染网格体模型
        """
        pass

