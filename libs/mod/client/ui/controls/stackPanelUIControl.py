# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
from typing import Literal


class StackPanelUIControl(BaseUIControl):
    def SetOrientation(self, orientation):
        # type: (Literal["horizontal", "vertical"] | str) -> bool
        """
        设置stackPanel的排列方向
        """
        pass

    def GetOrientation(self):
        # type: () -> Literal["horizontal", "vertical"] | str
        """
        获取stackPanel的排列方向
        """
        pass

