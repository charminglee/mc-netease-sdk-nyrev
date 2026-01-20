# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
from mod.client.ui.screenNode import ScreenNode


class ProgressBarUIControl(BaseUIControl):
    def __init__(self, screenNode, path, valueImagePath="/filled_progress_bar"):
        # type: (ScreenNode, str, str) -> None
        super(ProgressBarUIControl, self).__init__(screenNode, path)
        self.valueImagePath = valueImagePath # type: str

    def SetValue(self, progress):
        # type: (float) -> None
        """
        设置进度条的进度
        """
        pass

