# -*- coding: utf-8 -*-


from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Optional, TypedDict, Literal, Dict


class __ItemDict(TypedDict, total=False):
    newItemName: str
    newAuxValue: int
    itemName: str
    auxValue: int
    count: int
    showInHand: bool
    enchantData: List[Tuple[int, int]]
    modEnchantData: List[Tuple[str, int]]
    customTips: str
    extraId: str
    userData: Optional[dict]
    durability: int
__ItemPosType = Literal[0, 1, 2, 3]
class __ItemBasicInfo(TypedDict, total=False):
    itemName: str
    maxStackSize: int
    maxDurability: int
    id_aux: int
    tierDict: Optional[dict]
    itemCategory: Literal[
        "construction",
        "nature",
        "equipment",
        "items",
        "custom",
        "",
    ]
    itemType: Literal[
        "book",
        "sword",
        "shears",
        "axe",
        "clock",
        "bucket",
        "fishing_rod",
        "hoe",
        "shovel",
        "pickaxe",
        "dye",
        "food",
        "block",
        "armor",
        "custom_ranged_weapon",
        "compass",
        "trident",
        "potion",
        "crossbow",
    ]
    customItemType: str
    tags: List[str]
    customTips: str
    itemTierLevel: Literal[-1, 0, 1, 2, 3, 4]
    fuelDuration: float
    foodNutrition: int
    foodSaturation: float
    weaponDamage: int
    armorDefense: int
    armorSlot: int
    armorToughness: int
    armorKnockbackResistance: float
    enchant_slot_type: int
__Facing = Literal[0, 1, 2, 3, 4, 5]
class __EnchantDict(TypedDict, total=False):
    identifier: str
    description: str
    primary_slots: Literal[
        "all",
        "g_armor",
        "armor_head",
        "armor_torso",
        "armor_legs",
        "armor_feet",
        "sword",
        "bow",
        "spear",
        "crossbow",
        "g_tool",
        "hoe",
        "shears",
        "flintsteel",
        "shield",
        "g_digging",
        "axe",
        "pickaxe",
        "shovel",
        "fishing_rod",
        "carrot_stick",
        "elytra",
        "cosmetic_head",
        "compass",
        "mushroom_stick",
        "brush",
    ]
    cost: List[int]
    frequency: Literal[
        "common",
        "uncommon",
        "rare",
        "very_rare",
    ]
    is_treasure_only: bool
    is_discoverable: bool
    is_lootable: bool
    is_curse: bool
    max_level: int
    incompatible: List[str]


class ItemCompServer(BaseComponent):
    def SpawnItemToPlayerCarried(self, itemDict, playerId):
        # type: (__ItemDict, str) -> bool
        """
        生成物品到玩家右手
        """
        pass

    def SpawnItemToPlayerInv(self, itemDict, playerId, slotPos=-1):
        # type: (__ItemDict, str, int) -> bool
        """
        生成物品到玩家背包
        """
        pass

    def GetPlayerItem(self, posType, slotPos=0, getUserData=False):
        # type: (__ItemPosType, int, bool) -> __ItemDict
        """
        获取玩家物品，支持获取背包，盔甲栏，副手以及主手物品
        """
        pass

    def ChangePlayerItemTipsAndExtraId(self, posType, slotPos=0, customTips='', extraId=''):
        # type: (__ItemPosType, int, str, str) -> bool
        """
        修改玩家物品的自定义tips和自定义标识符
        """
        pass

    def AddEnchantToInvItem(self, slotPos, enchantType, level):
        # type: (int, int, int) -> bool
        """
        给物品栏的物品添加附魔信息
        """
        pass

    def AddModEnchantToInvItem(self, slotPos, modEnchantId, level):
        # type: (int, str, int) -> bool
        """
        给物品栏中物品添加自定义附魔信息
        """
        pass

    def RemoveEnchantToInvItem(self, slotPos, enchantType):
        # type: (int, int) -> bool
        """
        给物品栏的物品移除附魔信息
        """
        pass

    def RemoveModEnchantToInvItem(self, slotPos, modEnchantId):
        # type: (int, str) -> bool
        """
        给物品栏中物品移除自定义附魔信息
        """
        pass

    def GetInvItemEnchantData(self, slotPos):
        # type: (int) -> List[Tuple[int, int]]
        """
        获取物品栏的物品附魔信息
        """
        pass

    def GetInvItemModEnchantData(self, slotPos):
        # type: (int) -> List[Tuple[str, int]]
        """
        获取物品栏的物品自定义附魔信息
        """
        pass

    def SetInvItemNum(self, slotPos, num):
        # type: (int, int) -> bool
        """
        设置玩家背包物品数目
        """
        pass

    def SetInvItemExchange(self, pos1, pos2):
        # type: (int, int) -> bool
        """
        交换玩家背包物品
        """
        pass

    def GetDroppedItem(self, itemEntityId, getUserData=False):
        # type: (str, bool) -> __ItemDict
        """
        获取掉落物的物品信息
        """
        pass

    def GetEquItemEnchant(self, slotPos):
        # type: (int) -> List[Tuple[int, int]]
        """
        获取装备槽位中盔甲的附魔
        """
        pass

    def GetEquItemModEnchant(self, slotPos):
        # type: (int) -> List[Tuple[str, int]]
        """
        获取装备槽位中盔甲的自定义附魔
        """
        pass

    def GetItemTags(self, itemName, auxValue=0):
        # type: (str, int) -> List[str]
        """
        获取物品在minecraft:tags中定义的tags列表
        """
        pass

    def GetItemBasicInfo(self, itemName, auxValue=0, isEnchanted=False):
        # type: (str, int, bool) -> __ItemBasicInfo
        """
        获取物品的基础信息
        """
        pass

    def GetPlayerAllItems(self, posType, getUserData=False):
        # type: (__ItemPosType, bool) -> List[__ItemDict]
        """
        获取玩家指定的槽位的批量物品信息
        """
        pass

    def SetPlayerAllItems(self, itemsDictMap):
        # type: (Dict[Tuple[__ItemPosType, int], __ItemDict]) -> Dict[Tuple[__ItemPosType, int], bool]
        """
        添加批量物品信息到指定槽位
        """
        pass

    def GetEntityItem(self, posType, slotPos=0, getUserData=False):
        # type: (__ItemPosType, int, bool) -> __ItemDict
        """
        获取生物物品，支持获取背包，盔甲栏，副手以及主手物品
        """
        pass

    def SetEntityItem(self, posType, itemDict, slotPos=0):
        # type: (__ItemPosType, __ItemDict, int) -> bool
        """
        设置生物物品，建议开发者根据生物特性来进行设置，部分生物设置装备后可能不显示但是死亡后仍然会掉落所设置的装备
        """
        pass

    def GetCustomName(self, itemDict):
        # type: (__ItemDict) -> str
        """
        获取物品的自定义名称，与铁砧修改的名称一致
        """
        pass

    def SetCustomName(self, itemDict, name):
        # type: (__ItemDict, str) -> bool
        """
        设置物品的自定义名称，与使用铁砧重命名一致
        """
        pass

    def GetUserDataInEvent(self, eventName):
        # type: (str) -> bool
        """
        使物品相关服务端事件的物品信息字典参数带有userData。在mod初始化时调用即可
        """
        pass

    def GetSelectSlotId(self):
        # type: () -> int
        """
        获取玩家当前选中槽位
        """
        pass

    def GetContainerItem(self, pos, slotPos, dimensionId=-1, getUserData=False):
        # type: (Tuple[int, int, int], int, int, bool) -> dict
        """
        获取容器内的物品
        """
        pass

    def GetEnderChestItem(self, playerId, slotPos, getUserData=False):
        # type: (str, int, bool) -> dict
        """
        获取末影箱内的物品
        """
        pass

    def GetOpenContainerItem(self, playerId, containerId, getUserData=False):
        # type: (str, int, bool) -> dict
        """
        获取开放容器的物品
        """
        pass

    def GetPlayerUIItem(self, playerId, slot, getUserData=False, isNeteaseUI=False):
        # type: (str, int, bool, bool) -> dict
        """
        获取合成容器的物品
        """
        pass

    def SetPlayerUIItem(self, playerId, slot, itemDict=None, needBack=True, isNeteaseUI=False):
        # type: (str, int, __ItemDict, bool, bool) -> bool
        """
        设置合成容器的物品
        """
        pass

    def SpawnItemToContainer(self, itemDict, slotPos, blockPos, dimensionId=-1):
        # type: (__ItemDict, int, Tuple[int, int, int], int) -> bool
        """
        生成物品到容器方块的物品栏
        """
        pass

    def SpawnItemToEnderChest(self, itemDict, slotPos):
        # type: (__ItemDict, int) -> bool
        """
        生成物品到末影箱
        """
        pass

    def GetContainerSize(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> int
        """
        获取容器容量大小
        """
        pass

    def MayPlaceOn(self, identifier, auxValue, blockPos, facing):
        # type: (str, int, Tuple[int, int, int], __Facing) -> bool
        """
        判断物品是否可以放到指定的位置上
        """
        pass

    def GetItemDurability(self, posType, slotPos):
        # type: (__ItemPosType, int) -> int
        """
        获取指定槽位的物品耐久
        """
        pass

    def SetItemDurability(self, posType, slotPos, durability):
        # type: (__ItemPosType, int, int) -> bool
        """
        设置物品的耐久值
        """
        pass

    def GetItemDefenceAngle(self, posType, slotPos):
        # type: (__ItemPosType, int) -> List[float]
        """
        获取盾牌物品的抵挡角度范围
        """
        pass

    def SetItemDefenceAngle(self, posType, slotPos, angleLeft, angleRight):
        # type: (__ItemPosType, int, float, float) -> bool
        """
        设置盾牌物品的抵挡角度范围
        """
        pass

    def SetItemMaxDurability(self, posType, slotPos, maxDurability, isUserData):
        # type: (__ItemPosType, int, int, bool) -> bool
        """
        设置物品的最大耐久值
        """
        pass

    def GetItemMaxDurability(self, posType, slotPos, isUserData):
        # type: (__ItemPosType, int, bool) -> int
        """
        获取指定槽位的物品耐最大耐久
        """
        pass

    def SetMaxStackSize(self, itemDict, maxStackSize):
        # type: (__ItemDict, int) -> bool
        """
         设置物品的最大堆叠数量（存档）
        """
        pass

    def SetAttackDamage(self, itemDict, attackDamage):
        # type: (__ItemDict, int) -> bool
        """
         设置物品的攻击伤害值
        """
        pass

    def SetItemTierLevel(self, itemDict, level):
        # type: (__ItemDict, int) -> bool
        """
         设置工具类物品的挖掘等级
        """
        pass

    def SetItemTierSpeed(self, itemDict, speed):
        # type: (__ItemDict, float) -> bool
        """
         设置工具类物品的挖掘速度(可通过userData中的ModTierSpeed获取挖掘速度)
        """
        pass

    def SetItemLayer(self, itemDict, layer, texture):
        # type: (__ItemDict, int, str) -> bool
        """
        设置物品的叠加贴图，可以在物品的上层与下层叠加自定义贴图。具体使用可参考CustomItemsMod示例。
        """
        pass

    def RemoveItemLayer(self, itemDict, layer):
        # type: (__ItemDict, int) -> bool
        """
        移除物品的叠加贴图。物品叠加贴图详见SetItemLayer
        """
        pass

    def GetItemLayer(self, itemDict, layer):
        # type: (__ItemDict, int) -> str
        """
        获取物品的叠加贴图。物品叠加贴图详见SetItemLayer
        """
        pass

    def SetShearsDestoryBlockSpeed(self, blockName, speed):
        # type: (str, float) -> bool
        """
         设置剪刀对某一方块的破坏速度
        """
        pass

    def CancelShearsDestoryBlockSpeed(self, blockName):
        # type: (str) -> bool
        """
         取消剪刀对某一方块的破坏速度设置
        """
        pass

    def CancelShearsDestoryBlockSpeedAll(self):
        # type: () -> bool
        """
         取消剪刀对全部方块的破坏速度设置
        """
        pass

    def SetBrewingStandSlotItem(self, itemDict, slot, pos, dimensionId):
        # type: (__ItemDict, int, Tuple[int, int, int], int) -> bool
        """
        设置酿造台指定槽位物品
        """
        pass

    def GetBrewingStandSlotItem(self, slot, pos, dimensionId):
        # type: (int, Tuple[int, int, int], int) -> __ItemDict
        """
        获取酿造台指定槽位物品
        """
        pass

    def SetInputSlotItem(self, itemDict, pos, dimensionId=-1):
        # type: (__ItemDict, Tuple[int, int, int], int) -> bool
        """
        设置熔炉输入栏物品
        """
        pass

    def GetInputSlotItem(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> __ItemDict
        """
        获取熔炉输入栏物品, 支持使用下面参数清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0
        """
        pass

    def GetOutputSlotItem(self, pos, dimensionId=-1):
        # type: (Tuple[int, int, int], int) -> __ItemDict
        """
        获取熔炉输出栏物品
        """
        pass

    def GetLoadItems(self, flag=True):
        # type: (bool) -> List[str]
        """
        获取已经加载的物品id
        """
        pass

    def GetAllEnchantsInfo(self):
        # type: () -> List[__EnchantDict]
        """
        获取目前已注册的所有附魔信息
        """
        pass

    def GetItemInfoByBlockName(self, blockName, auxValue=0, isLegacy=True):
        # type: (str, int, bool) -> __ItemDict
        """
        通过方块名称及aux值获取物品信息
        """
        pass

