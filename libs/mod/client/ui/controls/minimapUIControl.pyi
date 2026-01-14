# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
from typing import Tuple


class MiniMapUIControl(BaseUIControl):
    def ZoomIn(self, value=0.05):
        # type: (float) -> bool
        """
        放大地图
        """
        pass

    def ZoomOut(self, value=0.05):
        # type: (float) -> bool
        """
        缩小地图
        """
        pass

    def ZoomReset(self):
        # type: () -> bool
        """
        恢复地图放缩大小为默认值
        """
        pass

    def SetHighestY(self, highestY):
        # type: (int) -> bool
        """
        设置绘制地图的最大高度
        """
        pass

    def AddEntityMarker(self, entityId, texturePath, size=(4, 4), enableRotation=False, isRevertZRot=False):
        # type: (str, str, Tuple[float, float], bool, bool) -> bool
        """
        增加实体位置标记
        """
        pass

    def AddEntityTextMarker(self, entityId, text, scale):
        # type: (str, str, float) -> bool
        """
        在小地图上增加实体文本标记
        """
        pass

    def AddStaticMarker(self, key, vec2, texturePath, size=(4, 4)):
        # type: (str, Tuple[float, float], str, Tuple[float, float]) -> bool
        """
        增加地图上静态位置的标记
        """
        pass

    def AddStaticTextMarker(self, key, vec2, text, scale):
        # type: (str, Tuple[float, float], str, float) -> bool
        """
        在小地图上增加静态文本的标记
        """
        pass

    def RemoveEntityMarker(self, entityId):
        # type: (str) -> bool
        """
        删除实体位置标记
        """
        pass

    def RemoveEntityTextMarker(self, entityId):
        # type: (str) -> bool
        """
        在小地图上删除实体文本标记
        """
        pass

    def RemoveStaticMarker(self, key):
        # type: (str) -> bool
        """
        删除静态位置标记
        """
        pass

    def RemoveStaticTextMarker(self, key):
        # type: (str) -> bool
        """
        在小地图上删除静态文本标记
        """
        pass

    def RepaintMiniMap(self):
        # type: () -> None
        """
        重新绘制小地图
        """
        pass

