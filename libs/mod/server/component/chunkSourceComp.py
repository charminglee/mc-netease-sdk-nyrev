# -*- coding: utf-8 -*-

from typing import Union
from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ChunkSourceCompServer(BaseComponent):
    def SetAddArea(self, key, dimensionId, minPos, maxPos):
        # type: (str, int, Tuple[int,int,int], Tuple[int,int,int]) -> 'bool'
        """
        设置区块的常加载
        """
        pass

    def DeleteArea(self, key):
        # type: (str) -> 'bool'
        """
        删除一个常加载区域
        """
        pass

    def DeleteAllArea(self):
        # type: () -> 'int'
        """
        删除所有常加载区域
        """
        pass

    def GetAllAreaKeys(self):
        # type: () -> 'List[str]'
        """
        获取所有常加载区域名称列表
        """
        pass

    def CheckChunkState(self, dimension, pos):
        # type: (int, Tuple[int,int,int]) -> 'bool'
        """
        判断指定位置的chunk是否加载完成
        """
        pass

    def GetLoadedChunks(self, dimension):
        # type: (int) -> 'Union[None,List[Tuple[int,int]]]'
        """
        获取指定维度当前已经加载完毕的全部区块的坐标列表
        """
        pass

    def GetChunkEntites(self, dimension, pos):
        # type: (int, Tuple[int,int,int]) -> 'Union[None,List[str]]'
        """
        获取指定位置的区块中，全部的实体和玩家的ID列表
        """
        pass

    def GetChunkMinPos(self, chunkPos):
        # type: (Tuple[int,int]) -> 'Union[None,Tuple[int,int,int]]'
        """
        获取某区块最小点的坐标
        """
        pass

    def GetChunkMaxPos(self, chunkPos):
        # type: (Tuple[int,int]) -> 'Union[None,Tuple[int,int,int]]'
        """
        获取某区块最大点的坐标
        """
        pass

    def GetChunkMobNum(self, dimension, chunkPos):
        # type: (int, Tuple[int,int]) -> 'int'
        """
        获取某区块中的生物数量（不包括玩家，但包括盔甲架）
        """
        pass

    def GetChunkPosFromBlockPos(self, blockPos):
        # type: (Tuple[int,int,int]) -> 'Union[None,Tuple[int,int]]'
        """
        通过方块坐标获得该方块所在区块坐标
        """
        pass

    def IsChunkGenerated(self, dimensionId, chunkPos):
        # type: (int, Tuple[int,int]) -> 'bool'
        """
        获取某个区块是否生成过。
        """
        pass

    def IsSlimeChunk(self, dimensionId, chunkPos):
        # type: (int, Tuple[int,int]) -> 'bool'
        """
        获取某个区块是否是史莱姆区块。
        """
        pass

    def DoTaskOnChunkAsync(self, dimensionId, posMin, posMax, callback):
        # type: (int, Tuple[int,int,int], Tuple[int,int,int], function) -> 'bool'
        """
        异步加载指定范围区块，加载完成后调用输入的回调函数。
        """
        pass

    def OpenClientChunkGeneration(self, val):
        # type: (bool) -> 'bool'
        """
        开启/关闭客户端区块生成功能，需要在LoadServerAddonScriptsAfter事件触发时调用。开启客户端区块生成功能时，如果使用了netease:structure_feature或修改了大部分地图，会导致客户端和服务端地图不一致的问题。此时可以通过关闭客户端区块生成功能解决该问题。
        """
        pass

