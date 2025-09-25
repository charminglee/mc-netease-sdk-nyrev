# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.blockPaletteComp import BlockPaletteComponent
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class BlockCompClient(BaseComponent):
    def GetBlankBlockPalette(self):
        # type: () -> BlockPaletteComponent
        """
        获取一个空白的方块调色板。
        """
        pass

    def GetBlockPaletteFromPosList(self, posList):
        # type: (List[Tuple[int, int, int]]) -> BlockPaletteComponent
        """
        根据输入的方块位置列表创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。创建的方块调色板包含了这个位置列表中的所有方块及其相对位置。
        """
        pass

    def GetBlockPaletteBetweenPos(self, startPos, endPos, eliminateAir=True):
        # type: (Tuple[int, int, int], Tuple[int, int, int], bool) -> BlockPaletteComponent
        """
        根据输入的两个位置创建并获取一个方块调色板，该接口会搜索这两个位置之间的所有方块创建方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。这个方块调色板包含了这两个位置之间的所有方块及其相对位置。
        """
        pass

