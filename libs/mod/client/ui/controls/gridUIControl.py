# -*- coding: utf-8 -*-

from mod.client.ui.controls.baseUIControl import BaseUIControl
from typing import Tuple

class GridUIControl(BaseUIControl):
    def SetGridDimension(self, dimension):
        # type: (Tuple[int,int]) -> None
        """
        设置Grid控件的大小
        """
        pass

    def GetGridItem(self, x, y):
        # type: (int, int) -> BaseUIControl
        """
        根据网格位置获取元素控件
        """
        pass

