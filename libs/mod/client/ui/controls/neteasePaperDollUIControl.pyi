# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
from typing import Dict


class NeteasePaperDollUIControl(BaseUIControl):
    def GetModelId(self):
        # type: () -> int
        """
        获取渲染的骨骼模型Id
        """
        pass

    def RenderEntity(self, params):
        # type: (Dict[str, str | float | int | dict | tuple]) -> bool
        """
        渲染实体
        """
        pass

    def RenderSkeletonModel(self, params):
        # type: (Dict[str, str | bool | float | int | dict | tuple]) -> bool
        """
        渲染骨骼模型（不依赖实体）
        """
        pass

    def RenderBlockGeometryModel(self, params):
        # type: (Dict[str, str | float | dict | tuple]) -> bool
        """
        渲染网格体模型
        """
        pass
