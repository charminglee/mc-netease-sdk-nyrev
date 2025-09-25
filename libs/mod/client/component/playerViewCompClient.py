# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class PlayerViewCompClient(BaseComponent):
    def GetPerspective(self):
        # type: () -> int
        """
        获取当前的视角模式
        """
        pass

    def SetPerspective(self, persp):
        # type: (int) -> bool
        """
        设置视角模式
        """
        pass

    def LockPerspective(self, lock):
        # type: (int) -> bool
        """
        锁定玩家的视角模式
        """
        pass

    def GetUIProfile(self):
        # type: () -> int
        """
        获取"UI 档案"模式
        """
        pass

    def SetUIProfile(self, profileType):
        # type: (int) -> bool
        """
        设置"UI 档案"模式
        """
        pass

    def SetToggleOption(self, optionId, isOn):
        # type: (str, bool) -> bool
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
        # type: (str) -> int
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
        # type: (int) -> dict
        """
        获取玩家控制器绑定映射
        """
        pass

    def GetSliderOption(self, optionId):
        # type: (str) -> float
        """
        获得某个滑动条设置选项的值
        """
        pass

    def SetSliderOption(self, optionId, value):
        # type: (str, float) -> bool
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

