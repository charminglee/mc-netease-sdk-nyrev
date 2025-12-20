# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
from typing import Callable, Any
from mod.client.ui.screenNode import ScreenNode


class ButtonUIControl(BaseUIControl):
    def __init__(self, screenNode, path):
        # type: (ScreenNode, str) -> None
        super(ButtonUIControl, self).__init__(screenNode, path)
        self.buttonArgs = None                      # type: dict | None
        self.buttonHoverArgs = None                 # type: dict | None
        self.onButtonTouchUpCallback = None         # type: Callable[[dict], Any] | None
        self.onButtonTouchDownCallback = None       # type: Callable[[dict], Any] | None
        self.onButtonTouchCancelCallback = None     # type: Callable[[dict], Any] | None
        self.onButtonTouchMoveCallback = None       # type: Callable[[dict], Any] | None
        self.onButtonTouchMoveInCallback = None     # type: Callable[[dict], Any] | None
        self.onButtonTouchMoveOutCallback = None    # type: Callable[[dict], Any] | None
        self.onButtonScreenExitCallback = None      # type: Callable[[dict], Any] | None
        self.onButtonHoverMoveInCallback = None     # type: Callable[[dict], Any] | None
        self.onButtonHoverMoveOutCallback = None    # type: Callable[[dict], Any] | None

    def AddTouchEventParams(self, args=None):
        # type: (dict | None) -> None
        """
        开启按钮回调功能，不调用该函数则按钮无回调
        """
        pass

    def AddHoverEventParams(self):
        # type: () -> None
        """
        开启按钮的悬浮回调功能，不调用该函数则按钮无悬浮回调
        """
        pass

    def SetButtonTouchDownCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置按钮按下时触发的回调函数
        """
        pass

    def SetButtonHoverInCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置鼠标进入按钮时触发的悬浮回调函数
        """
        pass

    def SetButtonHoverOutCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置鼠标退出按钮时触发的悬浮回调函数
        """
        pass

    def SetButtonTouchUpCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置触控在按钮范围内弹起时的回调函数
        """
        pass

    def SetButtonTouchCancelCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置触控在按钮范围外弹起时触发的回调函数
        """
        pass

    def SetButtonTouchMoveCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置按下后触控移动时触发的回调函数
        """
        pass

    def SetButtonTouchMoveInCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置按下按钮后进入控件时触发的回调函数
        """
        pass

    def SetButtonTouchMoveOutCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置按下按钮后退出控件时触发的回调函数
        """
        pass

    def SetButtonScreenExitCallback(self, callbackFunc):
        # type: (Callable[[dict], Any]) -> None
        """
        设置按钮所在画布退出时若鼠标仍未抬起时触发回调函数
        """
        pass

