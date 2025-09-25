# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
if 0:
    from typing import Callable, Any


class SelectionWheelUIControl(BaseUIControl):
    def GetSliceCount(self):
        # type: () -> int
        """
        获取轮盘可以选择的总切片数量
        """
        pass

    def GetCurrentSliceIndex(self):
        # type: () -> int
        """
        获取轮盘当前选择的切片的index，一般是在SetHoverCallback和SetTouchUpCallback中使用，表示当前鼠标悬浮或者点击的轮盘切片index
        """
        pass

    def SetCurrentSliceIndex(self, index):
        # type: (int) -> None
        """
        设置轮盘选择的切片
        """
        pass

    def SetTouchUpCallback(self, callbackFunc):
        # type: (Callable[[], Any]) -> None
        """
        设置轮盘选择切片并且鼠标按下抬起后触发回调函数
        """
        pass

    def SetHoverCallback(self, callbackFunc):
        # type: (Callable[[], Any]) -> None
        """
        设置轮盘选择切片触发回调函数
        """
        pass

