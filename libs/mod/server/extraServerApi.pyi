# -*- coding: utf-8 -*-


from typing import Generator
from typing import Tuple
from typing import List
from typing import Any
from typing import Type
from typing import Callable, Dict, TypedDict, Literal
from mod.server.component.engineCompFactoryServer import EngineCompFactoryServer
from mod.server.gamePlay.AI.customGoal import CustomGoal
from mod.server.system.serverSystem import ServerSystem
from mod.common.component.baseComponent import BaseComponent
from mod.common import minecraftEnum


class __EntityDict(TypedDict):
    dimensionId: int
    identifier: str
class __RayResultDict(TypedDict):
    type: Literal["Entity", "Block"]
    entityId: str
    pos: Tuple[int, int, int]
    identifier: str
    hitPos: Tuple[float, float, float]


def RegisterComponent(nameSpace, name, clsPath):
    # type: (str, str, str) -> bool
    """
    用于将组件注册到引擎中
    """
    pass

def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> ServerSystem | None
    """
    用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与客户端进行通讯等。
    """
    pass

def GetSystem(nameSpace, systemName):
    # type: (str, str) -> ServerSystem | None
    """
    获取已注册的系统
    """
    pass

def CreateComponent(entityId, nameSpace, name):
    # type: (str | int, str, str) -> BaseComponent | None
    """
    给实体创建服务端组件
    """
    pass

def GetComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> BaseComponent | None
    """
    获取实体的服务端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent
    """
    pass

def DestroyComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> None
    """
    删除实体的服务端组件
    """
    pass

def GetEngineCompFactory():
    # type: () -> EngineCompFactoryServer
    """
    获取引擎组件的工厂，通过工厂可以创建服务端的引擎组件
    """
    pass

class __MinecraftEnumModule:
    ActorDamageCause = minecraftEnum.ActorDamageCause
    AniCheatBlockBreak = minecraftEnum.AniCheatBlockBreak
    AniCheatConsts = minecraftEnum.AniCheatConsts
    AniCheatMove = minecraftEnum.AniCheatMove
    AniCheatMoveRewind = minecraftEnum.AniCheatMoveRewind
    AnimationModeType = minecraftEnum.AnimationModeType
    ArmorSlotType = minecraftEnum.ArmorSlotType
    AttrType = minecraftEnum.AttrType
    AttributeBuffType = minecraftEnum.AttributeBuffType
    BiomeType = minecraftEnum.BiomeType
    BlockBreathability = minecraftEnum.BlockBreathability
    BrewingStandSlotType = minecraftEnum.BrewingStandSlotType
    ButtonEventType = minecraftEnum.ButtonEventType
    ButtonState = minecraftEnum.ButtonState
    CatVariantType = minecraftEnum.CatVariantType
    Change = minecraftEnum.Change
    ColorCode = minecraftEnum.ColorCode
    CommandBlockType = minecraftEnum.CommandBlockType
    ConditionType = minecraftEnum.ConditionType
    ContainerType = minecraftEnum.ContainerType
    EffectType = minecraftEnum.EffectType
    EnchantSlotType = minecraftEnum.EnchantSlotType
    EnchantType = minecraftEnum.EnchantType
    EntityColorType = minecraftEnum.EntityColorType
    EntityComponentType = minecraftEnum.EntityComponentType
    EntityTeleportCause = minecraftEnum.EntityTeleportCause
    EntityType = minecraftEnum.EntityType
    Facing = minecraftEnum.Facing
    FoxType = minecraftEnum.FoxType
    GameDiffculty = minecraftEnum.GameDiffculty
    GameType = minecraftEnum.GameType
    GamepadKeyType = minecraftEnum.GamepadKeyType
    HorseSpotType = minecraftEnum.HorseSpotType
    HorseType = minecraftEnum.HorseType
    InputMode = minecraftEnum.InputMode
    InventoryType = minecraftEnum.InventoryType
    ItemAcquisitionMethod = minecraftEnum.ItemAcquisitionMethod
    ItemCategory = minecraftEnum.ItemCategory
    ItemColor = minecraftEnum.ItemColor
    ItemPosType = minecraftEnum.ItemPosType
    ItemType = minecraftEnum.ItemType
    ItemUseMethodEnum = minecraftEnum.ItemUseMethodEnum
    KeyBoardType = minecraftEnum.KeyBoardType
    MirrorModeType = minecraftEnum.MirrorModeType
    OpenContainerId = minecraftEnum.OpenContainerId
    OptionId = minecraftEnum.OptionId
    OriginGUIName = minecraftEnum.OriginGUIName
    PermissionChangeCause = minecraftEnum.PermissionChangeCause
    PistonFacing = minecraftEnum.PistonFacing
    PlayerActionType = minecraftEnum.PlayerActionType
    PlayerExhauseRatioType = minecraftEnum.PlayerExhauseRatioType
    PlayerUISlot = minecraftEnum.PlayerUISlot
    RayFilterType = minecraftEnum.RayFilterType
    RedstoneModeType = minecraftEnum.RedstoneModeType
    RenderControllerArrayType = minecraftEnum.RenderControllerArrayType
    RenderLayer = minecraftEnum.RenderLayer
    SetBlockType = minecraftEnum.SetBlockType
    ShapeType = minecraftEnum.ShapeType
    SliderOptionId = minecraftEnum.SliderOptionId
    StructureFeatureType = minecraftEnum.StructureFeatureType
    TimeEaseType = minecraftEnum.TimeEaseType
    TouchEvent = minecraftEnum.TouchEvent
    TradeLevelType = minecraftEnum.TradeLevelType
    TransferServerFailReason = minecraftEnum.TransferServerFailReason
    UICategory = minecraftEnum.UICategory
    UiBaseLayer = minecraftEnum.UiBaseLayer
    UseAnimation = minecraftEnum.UseAnimation
    VillagerClothingType = minecraftEnum.VillagerClothingType
    VirtualWorldObjectType = minecraftEnum.VirtualWorldObjectType
    WalkState = minecraftEnum.WalkState

def GetMinecraftEnum():
    # type: () -> __MinecraftEnumModule
    """
    用于获取枚举值文档中的枚举值
    """
    pass

def GetServerSystemCls():
    # type: () -> Type[ServerSystem]
    """
    用于获取服务器system基类。实现新的system时，需要继承该接口返回的类
    """
    pass

def GetComponentCls():
    # type: () -> Type[BaseComponent]
    """
    用于获取服务器component基类。实现新的component时，需要继承该接口返回的类
    """
    pass

def GetEngineNamespace():
    # type: () -> Literal["Minecraft"] | str
    """
    获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace
    """
    return "Minecraft"

def GetEngineSystemName():
    # type: () -> Literal["Engine"] | str
    """
    获取引擎系统名。监听引擎事件时，systemName传该接口返回的systemName
    """
    return "Engine"

def GetLevelId():
    # type: () -> str
    """
    获取levelId。某些组件需要levelId创建，可以用此接口获取levelId。其中level即为当前地图的游戏。
    """
    pass

def GetEngineActor():
    # type: () -> Dict[str, __EntityDict]
    """
    获取所有维度中已加载的所有实体（不包含玩家）。
    """
    pass

def getEntitiesOrBlockFromRay(dimensionId, pos, rot, distance=16, isThrough=False, filterType=1):
    # type: (int, Tuple[float, float, float], Tuple[float, float, float], int, bool, int) -> List[__RayResultDict]
    """
    从指定位置发射一条射线，获取与射线相交的实体和方块
    """
    pass

def GetPlayerList():
    # type: () -> List[str]
    """
    获取所有维度中的全部玩家的id列表
    """
    pass

def SetEntityLimit(num):
    # type: (int) -> bool
    """
    设置世界最大可生成实体数量上限。可生成实体指具有spawnrule的实体。当前世界上被加载的可生成实体数量超过这个上限时，生物就不会再通过spawnrule刷出。
    """
    pass

def GetEntityLimit():
    # type: () -> int
    """
    获取世界最大可生成实体数量上限。可生成实体的含义见SetEntityLimit
    """
    pass

def GetLocalPosFromWorld(pos, entityId):
    # type: (Tuple[float, float, float], str) -> Tuple[float, float, float]
    """
    获取基于实体的世界坐标对应的局部坐标
    """
    pass

def GetWorldPosFromLocal(pos, entityId):
    # type: (Tuple[float, float, float], str) -> Tuple[float, float, float]
    """
    获取基于实体的局部坐标对应的世界坐标
    """
    pass

def GetDirFromRot(rot):
    # type: (Tuple[float, float]) -> Tuple[float, float, float]
    """
    通过旋转角度获取朝向
    """
    pass

def GetRotFromDir(dir):
    # type: (Tuple[float, float, float]) -> Tuple[float, float]
    """
    通过朝向获取旋转角度
    """
    pass

def StartProfile():
    # type: () -> bool
    """
    开始启动服务端脚本性能分析，启动后调用StopProfile即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。
    """
    pass

def StopProfile(fileName=None):
    # type: (str | None) -> bool
    """
    停止服务端脚本性能分析并生成火焰图，与StartProfile配合使用，此接口只支持PC端
    """
    pass

def StartMemProfile():
    # type: () -> bool
    """
    开始启动服务端脚本内存分析，启动后调用StopMemProfile即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。
    """
    pass

def StopMemProfile(fileName=None):
    # type: (str | None) -> bool
    """
    停止服务端脚本内存分析并生成火焰图，与StartMemProfile配合使用，此接口只支持PC端
    """
    pass

def StartMultiProfile():
    # type: () -> bool
    """
    开始启动服务端与客户端双端脚本性能分析，启动后调用StopMultiProfile即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用StartProfile单端版本，此接口只支持PC端
    """
    pass

def StopMultiProfile(fileName=None):
    # type: (str | None) -> bool
    """
    停止双端脚本性能分析并生成火焰图，与StartMultiProfile配合使用，此接口只支持PC端
    """
    pass

def StartRecordPacket():
    # type: () -> bool
    """
    开始启动服务端与客户端之间的引擎收发包统计，启动后调用StopRecordPacket即可获取两个函数调用之间引擎收发包的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def StopRecordPacket():
    # type: () -> dict
    """
    停止服务端与客户端之间的引擎收发包统计并输出结果，与StartRecordPacket配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def StartRecordEvent():
    # type: () -> bool
    """
    开始启动服务端与客户端之间的脚本事件收发统计，启动后调用StopRecordEvent即可获取两个函数调用之间脚本事件收发的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def StopRecordEvent():
    # type: () -> dict
    """
    停止服务端与客户端之间的脚本事件收发统计并输出结果，与StartRecordEvent配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def IsInServer():
    # type: () -> bool
    """
    获取当前游戏是否跑在服务器环境下
    """
    pass

def IsInApollo():
    # type: () -> bool
    """
    返回当前游戏Mod是否运行在Apollo网络服
    """
    pass

def AddEntityTickEventWhiteList(identifier):
    # type: (str) -> bool
    """
    添加实体类型到EntityTickServerEvent事件的触发白名单。
    """
    pass

def GetPlatform():
    # type: () -> int
    """
    获取脚本运行的平台
    """
    pass

def GetCustomGoalCls():
    # type: () -> Type[CustomGoal]
    """
    用于获取服务器自定义行为节点的基类。实现新的行为节点时，需要继承该接口返回的类
    """
    pass

def StartCoroutine(iterOrFunc, callback=None):
    # type: (Generator | Callable[[], Generator], Callable[[], Any] | None) -> Generator
    """
    开启服务端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题
    """
    pass

def StopCoroutine(iter):
    # type: (Generator) -> bool
    """
    停止协程
    """
    pass

def GetServerTickTime():
    # type: () -> float
    """
    获取服务端引擎上一帧的帧消耗时间
    """
    pass

def SetMcpModLogCanPostDump(canPost):
    # type: (bool) -> None
    """
    设置是否可以打印错误信息到McpModLog日志。
    """
    pass

def GetMcpModLogCanPostDump():
    # type: () -> bool
    """
    获取是否可以打印错误信息到McpModLog日志。
    """
    pass

def PostMcpModDump(msg, *args, **kwargs):
    # type: (str, Any, Any) -> None
    """
    主动打印信息到McpModLog日志，需要先调用 SetMcpModLogCanPostDump 接口进行设置，才能生效。
    """
    pass

def ImportModule(path):
    # type: (str) -> Any
    """
    使用字符串路径导入模块，作用与importlib.import_module类似，但只能导入当前加载的mod中的模块
    """
    pass

def GetMinecraftVersion():
    # type: () -> str
    """
    获取Minecraft版本-服务端。
    """
    pass

def GetIntPos(pos):
    # type: (Tuple[float, float, float]) -> Tuple[int, int, int]
    """
    获取坐标所在方块的位置，即浮点数坐标向下取整后的整数坐标。
    """
    pass

def GetHostPlayerId():
    # type: () -> str
    """
    获取房主的entityId
    """
    pass

