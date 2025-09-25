# -*- coding: utf-8 -*-

from mod.client.ui.controls.baseUIControl import BaseUIControl

class SliderUIControl(BaseUIControl):
    def GetSliderValue(self):
        # type: () -> float
        """
        获取滑动条的值，失败返回0
        """
        pass

    def SetSliderValue(self, value):
        # type: (float) -> None
        """
        设置滑动条的值
        """
        pass

