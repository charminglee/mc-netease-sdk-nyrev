# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ItemCompClient(BaseComponent):
    def GetOffhandItem(self, getUserData=False):
        # type: (bool) -> 'dict'
        """
        获取左手物品的信息
        """
        pass

    def GetCarriedItem(self, getUserData=False):
        # type: (bool) -> 'dict'
        """
        获取右手物品的信息
        """
        pass

    def GetSlotId(self):
        # type: () -> 'int'
        """
        获取当前手持的快捷栏的槽id
        """
        pass

    def AddDropItemToWorld(self, itemDict, dimension_id, position, bobSpeed=0, spinSpeed=0):
        # type: (dict, int, Tuple[float,float,float], float, float) -> 'str'
        """
        在客户端添加一个掉落物渲染
        """
        pass

    def SetDropItemTransform(self, entityId, position, rotation=None, scale=None):
        # type: (str, Tuple[float,float,float], Tuple[float,float,float], float) -> 'bool'
        """
        设置通过AddDropItemToWorld添加的掉落物的位置、角度和缩放
        """
        pass

    def GetClientDropItemEntityIdList(self):
        # type: () -> 'List[str]'
        """
        获得所有通过AddDropItemToWorld创建的entityId的list
        """
        pass

    def DeleteClientDropItemEntity(self, entityId):
        # type: (str) -> 'bool'
        """
        删除AddDropItemToWorld创建的客户端掉落物
        """
        pass

    def GetItemTags(self, itemName, auxValue=0):
        # type: (str, int) -> 'List[str]'
        """
        获取物品在minecraft:tags中定义的tags列表
        """
        pass

    def GetItemBasicInfo(self, itemName, auxValue=0, isEnchanted=False):
        # type: (str, int, bool) -> 'dict'
        """
        获取物品的基础信息
        """
        pass

    def GetItemFormattedHoverText(self, itemName, auxValue=0, showCategory=False, userData=None):
        # type: (str, int, bool, dict) -> 'str'
        """
        获取物品的格式化hover文本，如：§f灾厄旗帜§r
        """
        pass

    def GetItemHoverName(self, itemName, auxValue=0, userData=None):
        # type: (str, int, dict) -> 'str'
        """
        获取物品的hover名称，如：灾厄旗帜§r
        """
        pass

    def GetItemEffectName(self, itemName, auxValue=0, userData=None):
        # type: (str, int, dict) -> 'str'
        """
        获取物品的状态描述，如：§7保护 0§r
        """
        pass

    def GetUserDataInEvent(self, eventName):
        # type: (str) -> 'bool'
        """
        使物品相关客户端事件的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>参数带有userData。在mod初始化时调用即可
        """
        pass

    def ChangeItemTexture(self, identifier, texturePath):
        # type: (str, str) -> 'bool'
        """
        替换物品的贴图，修改后所有用到该贴图的物品都会被改变，后续创建的此类物品也会被改变。会同时修改物品在UI界面上的显示，手持时候的显示与场景掉落的显示。
        """
        pass

    def GetItemTexture(self, identifier):
        # type: (str) -> 'str'
        """
        获取item_texture.json中物品的贴图路径。
        """
        pass

    def GetPlayerItem(self, posType, slotPos=0, getUserData=False):
        # type: (int, int, bool) -> 'dict'
        """
        获取玩家物品，支持获取背包（本地玩家），盔甲栏，副手以及主手物品
        """
        pass

    def GetPlayerAllItems(self, posType, getUserData=False):
        # type: (int, bool) -> 'List[dict]'
        """
        获取玩家指定的槽位的批量物品信息，支持获取盔甲栏，副手以及主手物品，背包物品仅支持本地玩家
        """
        pass

    def GetAllEnchantsInfo(self):
        # type: () -> 'List[dict]'
        """
        获取目前已注册的所有附魔信息
        """
        pass

    def SetCompassTarget(self, x, y, z):
        # type: (int, int, int) -> 'bool'
        """
        设置指南针的朝向位置
        """
        pass

    def SetCompassEntity(self, entityId):
        # type: (str) -> 'bool'
        """
        设置指南针朝向的实体
        """
        pass

    def AddUseItemParticleEffect(self, name, aux, pos):
        # type: (str, int, Tuple[float,float,float]) -> 'bool'
        """
        在指定位置播放指定物品被开始使用时的粒子效果（如果有）。
        """
        pass

    def RemoveUseItemParticleEffect(self, name, aux, pos):
        # type: (str, int, Tuple[float,float,float]) -> 'bool'
        """
        停止指定位置播放的物品被开始使用时的粒子效果。
        """
        pass

