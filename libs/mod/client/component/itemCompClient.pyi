# -*- coding: utf-8 -*-


from typing import List, TypedDict
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Literal


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
    userData: dict | None
    durability: int
class __ItemBasicInfo(TypedDict, total=False):
    itemName: str
    maxStackSize: int
    maxDurability: int
    id_aux: int
    tierDict: dict | None
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
    itemTierLevel: int
    fuelDuration: float
    foodNutrition: int
    foodSaturation: float
    weaponDamage: int
    armorDefense: int
    armorSlot: int
    armorToughness: int
    armorKnockbackResistance: float
    enchant_slot_type: int
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


class ItemCompClient(BaseComponent):
    def GetOffhandItem(self, getUserData=False):
        # type: (bool) -> __ItemDict
        """
        获取左手物品的信息
        """
        pass

    def GetCarriedItem(self, getUserData=False):
        # type: (bool) -> __ItemDict
        """
        获取右手物品的信息
        """
        pass

    def GetSlotId(self):
        # type: () -> int
        """
        获取当前手持的快捷栏的槽id
        """
        pass

    def AddDropItemToWorld(self, itemDict, dimension_id, position, bobSpeed=0, spinSpeed=0):
        # type: (__ItemDict, int, Tuple[float, float, float], float, float) -> str
        """
        在客户端添加一个掉落物渲染
        """
        pass

    def SetDropItemTransform(self, entityId, position, rotation=None, scale=None):
        # type: (str, Tuple[float, float, float], Tuple[float, float, float] | None, float | None) -> bool
        """
        设置通过AddDropItemToWorld添加的掉落物的位置、角度和缩放
        """
        pass

    def GetClientDropItemEntityIdList(self):
        # type: () -> List[str]
        """
        获得所有通过AddDropItemToWorld创建的entityId的list
        """
        pass

    def DeleteClientDropItemEntity(self, entityId):
        # type: (str) -> bool
        """
        删除AddDropItemToWorld创建的客户端掉落物
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

    def GetItemFormattedHoverText(self, itemName, auxValue=0, showCategory=False, userData=None):
        # type: (str, int, bool, dict | None) -> str
        """
        获取物品的格式化hover文本，如：§f灾厄旗帜§r
        """
        pass

    def GetItemHoverName(self, itemName, auxValue=0, userData=None):
        # type: (str, int, dict | None) -> str
        """
        获取物品的hover名称，如：灾厄旗帜§r
        """
        pass

    def GetItemEffectName(self, itemName, auxValue=0, userData=None):
        # type: (str, int, dict | None) -> str
        """
        获取物品的状态描述，如：§7保护 0§r
        """
        pass

    def GetUserDataInEvent(self, eventName):
        # type: (str) -> bool
        """
        使物品相关客户端事件的物品信息字典参数带有userData。在mod初始化时调用即可
        """
        pass

    def ChangeItemTexture(self, identifier, texturePath):
        # type: (str, str) -> bool
        """
        替换物品的贴图，修改后所有用到该贴图的物品都会被改变，后续创建的此类物品也会被改变。会同时修改物品在UI界面上的显示，手持时候的显示与场景掉落的显示。
        """
        pass

    def GetItemTexture(self, identifier):
        # type: (str) -> str
        """
        获取item_texture.json中物品的贴图路径。
        """
        pass

    def GetPlayerItem(self, posType, slotPos=0, getUserData=False):
        # type: (Literal[0, 1, 2, 3] | int, int, bool) -> __ItemDict
        """
        获取玩家物品，支持获取背包（本地玩家），盔甲栏，副手以及主手物品
        """
        pass

    def GetPlayerAllItems(self, posType, getUserData=False):
        # type: (Literal[0, 1, 2, 3] | int, bool) -> List[__ItemDict]
        """
        获取玩家指定的槽位的批量物品信息，支持获取盔甲栏，副手以及主手物品，背包物品仅支持本地玩家
        """
        pass

    def GetAllEnchantsInfo(self):
        # type: () -> List[__EnchantDict]
        """
        获取目前已注册的所有附魔信息
        """
        pass

    def SetCompassTarget(self, x, y, z):
        # type: (int, int, int) -> bool
        """
        设置指南针的朝向位置
        """
        pass

    def SetCompassEntity(self, entityId):
        # type: (str) -> bool
        """
        设置指南针朝向的实体
        """
        pass

    def AddUseItemParticleEffect(self, name, aux, pos):
        # type: (str, int, Tuple[float, float, float]) -> bool
        """
        在指定位置播放指定物品被开始使用时的粒子效果（如果有）。
        """
        pass

    def RemoveUseItemParticleEffect(self, name, aux, pos):
        # type: (str, int, Tuple[float, float, float]) -> bool
        """
        停止指定位置播放的物品被开始使用时的粒子效果。
        """
        pass

