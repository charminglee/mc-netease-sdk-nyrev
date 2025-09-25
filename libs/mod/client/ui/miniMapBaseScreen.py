# -*- coding: utf-8 -*-


from .screenNode import ScreenNode
if 0:
    from typing import Tuple


class MiniMapBaseScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        # type: (str, str, dict) -> None
        super(MiniMapBaseScreen, self).__init__(namespace, name, param)

    def AddEntityMarker(self, entityId, texturePath, size=(4, 4), enableRotation=False, isRevertZRot=False):
        # type: (str, str, Tuple[float, float], bool, bool) -> bool
        """
        增加实体位置标记
        """

    def RemoveEntityMarker(self, entityId):
        # type: (str) -> bool
        """
        删除实体位置标记
        """

    def AddStaticMarker(self, key, vec2, texturePath, size=(4, 4)):
        # type: (str, Tuple[float, float], str, Tuple[float, float]) -> bool
        """
        增加地图上静态位置的标记。如使用该接口请勿将地图缩小倍数设置过大（建议ZoomOut设置后的地图倍数不小于原地图大小的0.5倍），以免造成地图缩小后静态标记位置失效等问题。
        """

    def RemoveStaticMarker(self, key):
        # type: (str) -> bool
        """
        删除静态位置的标记
        """

    def ZoomIn(self, value=0.05):
        # type: (float) -> bool
        """
        放大地图
        """

    def ZoomOut(self, value=0.05):
        # type: (float) -> bool
        """
        缩小地图
        客户端地图区块加载有限，如果地图UI界面太大或者缩小地图倍数太大，会导致小地图无法显示未加载的区块。
        """

    def ZoomReset(self):
        # type: () -> bool
        """
        恢复地图放缩大小为默认值
        """

    def SetHighestY(self, highestY):
        # type: (int) -> bool
        """
        设置绘制地图的最大高度
        动态调整高度值后，已经绘制过的区块不会刷新为新的高度值，只有没有绘制过的区块会以新的高度值来绘制。
        """

    def AddEntityTextMarker(self, entityId, text, scale):
        # type: (str, str, float) -> bool
        """
        在小地图上增加实体文本标记
        """

    def RemoveEntityTextMarker(self, entityId):
        # type: (str) -> bool
        """
        删除实体文本标记
        """

    def AddStaticTextMarker(self, key, vec2, text, scale):
        # type: (str, Tuple[float, float], str, float) -> bool
        """
        在小地图上增加静态文本的标记
        """

    def RemoveStaticTextMarker(self, key):
        # type: (str) -> bool
        """
        删除静态文本标记
        """
