# -*- coding: utf-8 -*-


from typing import Union
from typing import Tuple
from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Any, Optional, TypedDict, Literal


class __BlockDict(TypedDict, total=False):
    name: str
    aux: int
class __JigsawBlockDict(TypedDict, total=False):
    name: str
    aux: int
    jigsaw_name: str
    jigsaw_target_name: str
    jigsaw_target_pool: str
    jigsaw_final_block: str
    jigsaw_join_type: Literal[0, 1]
__ItemPosType = Literal[0, 1, 2, 3]
__Facing = Literal[0, 1, 2, 3, 4, 5]
class _Tier(TypedDict, total=False):
    digger: Literal["shovel", "pickaxe", "hatchet", "hoe"]
    destroy_special: bool
    level: Literal[0, 1, 2, 3]
class __BlockInfoDict(TypedDict, total=False):
    blockLightAbsorption: int
    blockLightEmission: int
    breathability: Literal[0, 1]
    explosionResistance: float
    loot: str
    mapColor: str
    unwalkable: bool
    tier: _Tier
    renderLayer: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    solid: bool
    pathable: bool
    fireResistant: bool
    creativeCategory: Literal[1, 2, 3, 4, 7]
    destroyTime: float
__Side = Literal[0, 1]
class __MiningArgs(TypedDict, total=False):
    haste: int
    conduit_power: int
    mining_fatigue: int
    mining_efficiency: int


class BlockInfoComponentServer(BaseComponent):
    def GetBlockLightLevel(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> int
        """
        获取方块位置的光照等级
        """
        pass

    def SetBlockNew(self, pos, blockDict, oldBlockHandling=0, dimensionId=-1, isLegacy=False, updateNeighbors=True):
        # type: (Tuple[int, int, int], __BlockDict, Literal[0, 1, 2], int, bool, bool) -> bool
        """
        设置某一位置的方块
        """
        pass

    def SetJigsawBlock(self, pos, blockDict, dimensionId=-1):
        # type: (Tuple[int, int, int], __JigsawBlockDict, int) -> bool
        """
        在某一位置放置拼图方块
        """
        pass

    def SetLiquidBlock(self, pos, blockDict, dimensionId=-1):
        # type: (Tuple[int, int, int], __BlockDict, int) -> bool
        """
        设置某一位置的方块的extraBlock，可在此设置方块含水等
        """
        pass

    def SetSnowBlock(self, pos, dimensionId=-1, height=1):
        # type: (Tuple[int, int, int], int, int) -> bool
        """
        设置某一位置的方块含雪
        """
        pass

    def PlayerDestoryBlock(self, pos, particle=1, sendInv=False):
        # type: (Tuple[int, int, int], Literal[0, 1], bool) -> bool
        """
        使用手上工具破坏方块
        """
        pass

    def OpenWorkBench(self):
        # type: () -> bool
        """
        在玩家当前位置打开工作台UI，不依赖于工作台方块
        """
        pass

    def PlayerUseItemToPos(self, pos, posType, slotPos=0, facing=1):
        # type: (Tuple[int, int, int], __ItemPosType, int, __Facing) -> bool
        """
        模拟玩家对某个坐标使用物品
        """
        pass

    def PlayerUseItemToEntity(self, entityId):
        # type: (str) -> bool
        """
        玩家使用手上物品对某个生物使用
        """
        pass

    def GetBlockNew(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> dict
        """
        获取某一位置的block
        """
        pass

    def GetBlockTags(self, blockName):
        # type: (str) -> List[str]
        """
        获取方块在tags:*中定义的tags列表
        """
        pass

    def GetBlockBasicInfo(self, blockName):
        # type: (str) -> __BlockInfoDict
        """
        获取方块基本信息
        """
        pass

    def SetBlockBasicInfo(self, blockName, infoDict, auxValue=0):
        # type: (str, __BlockInfoDict, int) -> bool
        """
        设置方块基本信息
        """
        pass

    def GetBlockCollision(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> dict
        """
        获取某一位置方块当前collision的aabb
        """
        pass

    def GetBlockClip(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> dict
        """
        获取某一位置方块当前clip的aabb
        """
        pass

    def GetLiquidBlock(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> __BlockDict
        """
        获取某个位置的方块所含流体的信息
        """
        pass

    def GetTopBlockHeight(self, pos, dimension=0):
        # type: (Tuple[int, int], int) -> Union[int, None]
        """
        获取某一位置最高的非空气方块的高度
        """
        pass

    def CheckBlockToPos(self, fromPos, toPos, dimensionId=-1):
        # type: (Tuple[float, float, float], Tuple[float, float, float], int) -> int
        """
        判断位置之间是否有方块
        """
        pass

    def SetBlockTileEntityCustomData(self, pos, key, value, dimensionId=-1):
        # type: (Tuple[int, int, int], str, Any, int) -> bool
        """
        设置指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。
        """
        pass

    def GetBlockTileEntityCustomData(self, pos, key, dimensionId=-1):
        # type: (Tuple[int, int, int], str, int) -> Any
        """
        读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据
        """
        pass

    def GetBlockTileEntityWholeCustomData(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> Union[dict, None]
        """
        读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据字典。
        """
        pass

    def CleanBlockTileEntityCustomData(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> bool
        """
        清空指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。
        """
        pass

    def GetBlockEntityData(self, dimension, pos):
        # type: (int, Tuple[int, int, int]) -> Union[dict, None]
        """
        用于获取方块（包括自定义方块）的数据，如需修改，请使用setblockentitydata接口
        """
        pass

    def SetBlockEntityData(self, dimension, pos, nbtData):
        # type: (int, Tuple[int, int, int], dict) -> bool
        """
        用于设置方块（包括自定义方块）的数据
        """
        pass

    def SpawnResourcesSilkTouched(self, identifier, pos, aux, dimensionId=-1):
        # type: (str, Tuple[int, int, int], int, int) -> bool
        """
        模拟方块精准采集掉落
        """
        pass

    def SpawnResources(self, identifier, pos, aux, probability=1.0, bonusLootLevel=0, dimensionId=-1, allowRandomness=True, spawnOrb=False):
        # type: (str, Tuple[int, int, int], int, float, int, int, bool, bool) -> bool
        """
        产生方块随机掉落（该方法不适用于实体方块）
        """
        pass

    def GetChestPairedPosition(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> Union[Tuple[int, int, int], None]
        """
        获取与箱子A合并成一个大箱子的箱子B的坐标
        """
        pass

    def GetBedColor(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> int
        """
        获取床（方块）的颜色
        """
        pass

    def SetBedColor(self, pos, color, dimensionId=-1):
        # type: (Tuple[int, int, int], int, int) -> bool
        """
        设置床（方块）的颜色
        """
        pass

    def GetSignBlockText(self, pos, dimensionId=-1, side=0):
        # type: (Tuple[int, int, int], int, __Side) -> str
        """
        获取告示牌（方块）的文本内容
        """
        pass

    def SetSignBlockText(self, pos, text, dimensionId=-1, side=0):
        # type: (Tuple[int, int, int], str, int, __Side) -> bool
        """
        设置告示牌（方块）的文本内容
        """
        pass

    def MayPlace(self, identifier, blockPos, facing, dimensionId=0):
        # type: (str, Tuple[int, int, int], __Facing, int) -> bool
        """
        判断方块是否可以放置
        """
        pass

    def ListenOnBlockRemoveEvent(self, identifier, listen):
        # type: (str, bool) -> bool
        """
        是否监听方块BlockRemoveServerEvent事件，可以动态修改json组件netease:listen_block_remove的值
        """
        pass

    def GetDestroyTotalTime(self, blockName, itemName=None, miningArgs=None):
        # type: (str, Optional[str], __MiningArgs) -> float
        """
        获取使用物品破坏方块需要的时间
        """
        pass

    def RegisterOnStandOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_stand_on组件
        """
        pass

    def UnRegisterOnStandOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_stand_on组件
        """
        pass

    def RegisterOnStepOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_step_on组件
        """
        pass

    def UnRegisterOnStepOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_step_on组件
        """
        pass

    def RegisterOnStepOff(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_step_off组件
        """
        pass

    def UnRegisterOnStepOff(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_step_off组件
        """
        pass

    def RegisterOnEntityInside(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_entity_inside组件
        """
        pass

    def UnRegisterOnEntityInside(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_entity_inside组件
        """
        pass

    def GetLoadBlocks(self):
        # type: () -> List[str]
        """
        获取已经加载的方块id
        """
        pass

    def SetChestLootTable(self, blockPos, dimensionId, lootTable, isIgnoreSpilt=False):
        # type: (Tuple[int, int, int], int, str, bool) -> bool
        """
        设置箱子战利品表
        """
        pass

