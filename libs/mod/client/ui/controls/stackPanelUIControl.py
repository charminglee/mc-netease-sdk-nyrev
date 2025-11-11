# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
from typing import Literal


__Orientation = Literal["horizontal", "vertical"]


class StackPanelUIControl(BaseUIControl):
    def SetOrientation(self, orientation):
        # type: (__Orientation) -> bool
        """
        设置stackPanel的排列方向
        """
        pass

    def GetOrientation(self):
        # type: () -> __Orientation
        """
        获取stackPanel的排列方向
        """
        pass

