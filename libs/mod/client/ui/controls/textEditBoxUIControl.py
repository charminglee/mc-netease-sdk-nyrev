# -*- coding: utf-8 -*-

from mod.client.ui.controls.baseUIControl import BaseUIControl

class TextEditBoxUIControl(BaseUIControl):
    def GetEditText(self):
        # type: () -> str
        """
        获取edit_box输入框的文本信息，获取失败会返回None
        """
        pass

    def SetEditText(self, text):
        # type: (str) -> None
        """
        设置edit_box输入框的文本信息
        """
        pass

    def SetEditTextMaxLength(self, maxLength):
        # type: (int) -> None
        """
        设置输入框的最大输入长度
        """
        pass

