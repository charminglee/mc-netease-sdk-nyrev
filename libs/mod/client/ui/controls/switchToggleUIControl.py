# -*- coding: utf-8 -*-

from mod.client.ui.controls.baseUIControl import BaseUIControl

class SwitchToggleUIControl(BaseUIControl):
    def SetToggleState(self, is_on, toggle_path='/this_toggle'):
        # type: (bool, str) -> None
        """
        设置Toggle开关控件的值
        """
        pass

    def GetToggleState(self, toggle_path='/this_toggle'):
        # type: (str) -> bool
        """
        获取Toggle开关控件的状态
        """
        pass

