# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class FrameAniTransComp(BaseComponent):
    def GetPos(self):
        # type: () -> Tuple[float, float, float]
        """
        获取序列帧特效的位置
        """
        pass

    def SetPos(self, pos):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置序列帧的位置
        """
        pass

    def GetRot(self):
        # type: () -> Tuple[float, float, float]
        """
        获取序列帧特效的旋转角度
        """
        pass

    def SetRot(self, rot):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置序列帧的旋转
        """
        pass

    def SetRotUseZXY(self, rot):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置序列帧的旋转，旋转顺序按照绕z,x,y轴旋转
        """
        pass

    def GetScale(self):
        # type: () -> Tuple[float, float, float]
        """
        获取序列帧特效的缩放值
        """
        pass

    def SetScale(self, scale):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置序列帧的缩放
        """
        pass

