# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Literal


__Persp = Literal[0, 1, 2]
__ProfileType = Literal[0, 1]
__OptionId = Literal[
    "AUTO_JUMP",
    "HIDE_PAPERDOLL",
    "HIDE_HAND",
    "SPLIT_CONTROLS",
    "VIEW_BOBBING",
    "INPUT_MODE",
    "TRADITION_CONTROLS",
    "HIDE_HUD",
    "CAMERA_SHAKE",
    "TRANSPARENTLEAVES",
    "FANCY_SKIES",
    "SMOOTH_LIGHTING",
    "GRAPHICS",
    "RENDER_CLOUDS",
    "FORCE_SPRINT",
]
__LayoutType = Literal[0, 1]
__SliderOptionId = Literal[
    "MOUSE_SENSITIVITY",
    "MOUSE_SPYGLASS_DAMPING",
    "GAMEPAD_SENSITIVITY",
    "GAMEPAD_SPYGLASS_DAMPING",
    "GAMEPAD_CURSOR_SENSITIVITY",
    "TOUCH_SENSITIVITY",
    "TOUCH_SPYGLASS_DAMPING",
    "DPAD_SCALE",
    "GAMMA",
    "INTERFACE_OPACITY",
    "FIELD_OF_VIEW",
]


class PlayerViewCompClient(BaseComponent):
    def GetPerspective(self):
        # type: () -> __Persp
        """
        获取当前的视角模式
        """
        pass

    def SetPerspective(self, persp):
        # type: (__Persp) -> bool
        """
        设置视角模式
        """
        pass

    def LockPerspective(self, lock):
        # type: (__Persp) -> bool
        """
        锁定玩家的视角模式
        """
        pass

    def GetUIProfile(self):
        # type: () -> __ProfileType
        """
        获取"UI 档案"模式
        """
        pass

    def SetUIProfile(self, profileType):
        # type: (__ProfileType) -> bool
        """
        设置"UI 档案"模式
        """
        pass

    def SetToggleOption(self, optionId, isOn):
        # type: (__OptionId, bool) -> bool
        """
        修改开关型设置的接口
        """
        pass

    def SetSplitControlCanChange(self, canChange):
        # type: (bool) -> bool
        """
        设置是否允许使用准星瞄准按钮
        """
        pass

    def GetToggleOption(self, optionId):
        # type: (__OptionId) -> int
        """
        获得某个开关设置值的接口
        """
        pass

    def HighlightBoxSelection(self, isHighlight):
        # type: (bool) -> None
        """
        镜头移动时高亮当前视角中心所指的方块
        """
        pass

    def GetControllerLayout(self, layoutType):
        # type: (__LayoutType) -> dict
        """
        获取玩家控制器绑定映射
        """
        pass

    def GetSliderOption(self, optionId):
        # type: (__SliderOptionId) -> float
        """
        获得某个滑动条设置选项的值
        """
        pass

    def SetSliderOption(self, optionId, value):
        # type: (__SliderOptionId, float) -> bool
        """
        设置某个滑动条设置选项的值
        """
        pass

    def SetPlayerFovScale(self, fovScale):
        # type: (float) -> bool
        """
        将渲染实际使用的fov变为设置中的fov乘以fovScale,fovScale越接近0，其效果越接近原版望远镜效果
        """
        pass
