# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class BlockStateComponentServer(BaseComponent):
    def GetBlockStates(self, pos, dimensionId=-1):
        # type: (Tuple[float,float,float], int) -> 'dict'
        """
        获取<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>
        """
        pass

    def SetBlockStates(self, pos, data, dimensionId=-1):
        # type: (Tuple[float,float,float], dict, int) -> 'bool'
        """
        设置<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>
        """
        pass

    def GetBlockAuxValueFromStates(self, blockName, states):
        # type: (str, dict) -> 'int'
        """
        根据方块名称和<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>获取方块附加值AuxValue
        """
        pass

    def GetBlockStatesFromAuxValue(self, blockName, auxValue):
        # type: (str, int) -> 'dict'
        """
        根据方块名称和方块附加值AuxValue获取<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>
        """
        pass

