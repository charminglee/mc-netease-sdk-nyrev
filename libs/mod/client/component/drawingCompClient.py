# -*- coding: utf-8 -*-

from typing import Tuple
from mod.common.component.baseComponent import BaseComponent
from mod.client.component.drawingShapeCompClient import DrawingShapeCompClient

class DrawingCompClient(BaseComponent):
    def AddBoxShape(self, pos, scale=(1, 1, 1), color=(1, 1, 1)):
        # type: (Tuple[float, float, float], Tuple[float, float, float], Tuple[float, float, float]) -> DrawingShapeCompClient
        """
        新建盒子形状
        """
        pass

    def AddLineShape(self, startPos, endPos, color=(1, 1, 1)):
        # type: (Tuple[float, float, float], Tuple[float, float, float], Tuple[float, float, float]) -> DrawingShapeCompClient
        """
        新建线条形状
        """
        pass

    def AddCircleShape(self, pos, radius, color=(1, 1, 1), plane=2, segmentsNum=20):
        # type: (Tuple[float, float, float], float, Tuple[float, float, float], int, int) -> DrawingShapeCompClient
        """
        新建圆形状
        """
        pass

    def AddArrowShape(self, startPos, endPos, color=(1, 1, 1), headSegmentsNum=20, arrowHeadLength=1, radius=0.5):
        # type: (Tuple[float, float, float], Tuple[float, float, float], Tuple[float, float, float], int, float, float) -> DrawingShapeCompClient
        """
        新建箭头形状
        """
        pass

    def AddTextShape(self, pos, text, color=(1, 1, 1)):
        # type: (Tuple[float, float, float], str, Tuple[float, float, float]) -> DrawingShapeCompClient
        """
        新建文本形状
        """
        pass

    def AddSphereShape(self, pos, radius, color=(1, 1, 1), segmentsNum=20):
        # type: (Tuple[float, float, float], float, Tuple[float, float, float], int) -> DrawingShapeCompClient
        """
        新建球形状
        """
        pass

    def RemoveAll(self):
        # type: () -> bool
        """
        删除当前所有Shape
        """
        pass

