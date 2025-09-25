# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.blockPaletteComp import BlockPaletteComponent
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Optional

class BlockCompServer(BaseComponent):
    def RegisterBlockPatterns(self, pattern, defines, result_actor_name):
        # type: (List[str], dict, str) -> bool
        """
        注册特殊方块组合
        """
        pass

    def CreateMicroBlockResStr(self, identifier, start, end, colorMap=None, isMerge=False, icon=''):
        # type: (str, Tuple[int, int, int], Tuple[int, int, int], Optional[dict], bool, str) -> str
        """
        生成微缩方块资源Json字符串
        """
        pass

    def GetBlankBlockPalette(self):
        # type: () -> BlockPaletteComponent
        """
        获取一个空白的方块调色板。
        """
        pass

    def GetBlockPaletteFromPosList(self, dimensionId, posList):
        # type: (int, List[Tuple[int, int, int]]) -> BlockPaletteComponent
        """
        根据输入的方块位置列表创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。创建的方块调色板包含了这个位置列表中的所有方块及其相对位置。
        """
        pass

    def GetBlockPaletteBetweenPos(self, dimensionId, startBlockPos, endBlockPos, eliminateAir=True):
        # type: (int, Tuple[int, int, int], Tuple[int, int, int], bool) -> BlockPaletteComponent
        """
        根据输入的两个方块位置创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。这个方块调色板包含了这两个位置之间的所有方块及其相对位置。
        """
        pass

    def SetBlockByBlockPalette(self, blockPalette, dimensionId, pos, rotation, conflictMode=0):
        # type: (BlockPaletteComponent, int, Tuple[int, int, int], int, int) -> bool
        """
        根据输入的方块调色板内容，将调色板内记录的所有方块设置为实际的方块。
        """
        pass

