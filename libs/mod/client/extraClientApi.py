# -*- coding: utf-8 -*-


from typing import Generator, Union, List, Type, Tuple, Any, Callable, Optional, TypedDict, Dict, Literal
from mod.client.ui import NativeScreenManager
from mod.client.ui.screenNode import ScreenNode
from mod.client.ui.miniMapBaseScreen import MiniMapBaseScreen
from mod.client.component.engineCompFactoryClient import EngineCompFactoryClient
from mod.client.ui.viewRequest import ViewRequest
from mod.common.component.baseComponent import BaseComponent
from mod.client.ui.CustomUIScreenProxy import CustomUIScreenProxy
from mod.client.ui.CustomUIControlProxy import CustomUIControlProxy
from mod.common import minecraftEnum
from mod.client.ui.viewBinder import ViewBinder
from mod.client.system.clientSystem import ClientSystem
from mod.client.plugin.illustratedBook.bookManager import BookManager


class __EntityDict(TypedDict):
    dimensionId: int
    identifier: str
class __RayResultDict(TypedDict):
    type: Literal["Entity", "Block"]
    entityId: str
    pos: Tuple[int, int, int]
    identifier: str
    hitPos: Tuple[float, float, float]
class __CreateParamsDict(TypedDict, total=False):
    isHud: Literal[0, 1]
    inputMode: Literal[0, 1]
    bindEntityId: str
    bindWorldPosition: Tuple[int, Tuple[float, float, float]]
    bindOffset: Tuple[float, float, float]
    autoScale: Literal[0, 1]
    mini_map_root_path: str


def RegisterComponent(nameSpace, name, clsPath):
    # type: (str, str, str) -> bool
    """
    用于将组件注册到引擎中
    """
    pass

def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> Optional[ClientSystem]
    """
    用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与服务端进行通讯等。
    """
    pass

def GetSystem(nameSpace, systemName):
    # type: (str, str) -> Optional[ClientSystem]
    """
    用于获取其他系统实例
    """
    pass

def CreateComponent(entityId, nameSpace, name):
    # type: (Union[str, int], str, str) -> Optional[BaseComponent]
    """
    给实体创建客户端组件
    """
    pass

def GetComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> Optional[BaseComponent]
    """
    获取实体的客户端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent
    """
    pass

def DestroyComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> None
    """
    删除实体的客户端组件
    """
    pass

def GetEngineCompFactory():
    # type: () -> EngineCompFactoryClient
    """
    获取引擎组件的工厂，通过工厂可以创建客户端的引擎组件
    """
    pass

def RegisterUI(nameSpace, uiKey, clsPath, uiScreenDef=None):
    # type: (str, str, str, Optional[str]) -> bool
    """
    注册UI，创建UI前，需要先注册UI。同一UI只需要注册一次即可。详见界面创建流程及生命周期
    """
    pass

def CreateUI(nameSpace, uiKey=None, createParams=None):
    # type: (str, Optional[str], __CreateParamsDict) -> Optional[ScreenNode]
    """
    创建UI，详见界面创建流程及生命周期
    """
    pass

def GetUI(nameSpace, uiKey=None):
    # type: (str, Optional[str]) -> Optional[ScreenNode]
    """
    获取UI节点，详见界面创建流程及生命周期
    """
    pass

def GetTopUINode():
    # type: () -> Optional[ScreenNode]
    """
    获取Push进来的最顶层界面，包括原生界面，详见 界面创建流程及生命周期 
    """
    pass

def CheckCanBindUI(entityId):
    # type: (str) -> bool
    """
    检查实体是否可以绑定头顶UI，如何将UI与实体绑定详见CreateUI接口
    """
    pass

def HideHudGUI(isHide):
    # type: (bool) -> None
    """
    隐藏HUD游戏界面的游戏原生UI。与原版F1按钮效果一致，只隐藏显示，但点击跳跃键等位置依然会响应
    """
    pass

def HidePauseGUI(isHide):
    # type: (bool) -> None
    """
    隐藏暂停按钮原生UI。
    """
    pass

def HideChatGUI(isHide):
    # type: (bool) -> None
    """
    隐藏聊天按钮原生UI。该接口在开启新版聊天时不生效
    """
    pass

def HideFoldGUI(isHide):
    # type: (bool) -> None
    """
    隐藏下拉按钮原生UI。
    """
    pass

def HideEmoteGUI(isHide):
    # type: (bool) -> None
    """
    设置是否开启表情功能，默认PC端关闭，手机端开启，且该接口只能在手机端使用。该接口在开启新版聊天时不生效
    """
    pass

def HideVoiceGUI(isHide):
    # type: (bool) -> None
    """
    隐藏语音按钮原生UI。该接口在开启新版聊天时不生效
    """
    pass

def HideWalkGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中跑/走按钮。隐藏后点击相应位置不会响应
    """
    pass

def HideJumpGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中右下角的跳跃按钮。隐藏后点击相应位置不会响应
    """
    pass

def HideSlotBarGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中底部中间的物品栏界面
    """
    pass

def HideSneakGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中左下角方向键的中心处潜行按钮。隐藏后点击相应位置不会响应
    """
    pass

def HideNeteaseStoreGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中的网易商店按钮。隐藏后点击相应位置不会响应
    """
    pass

def OpenNeteaseStoreGui(categoryName, itemName):
    # type: (str, str) -> None
    """
    打开游戏中的网易商店购买商品界面
    """
    pass

def HideSwimGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中的浮潜按钮。隐藏后点击相应位置不会响应。
    """
    pass

def HideChangePersonGui(isHide):
    # type: (bool) -> None
    """
    隐藏切换人称的按钮。隐藏后点击相应位置不会响应
    """
    pass

def HideNameTag(isHide):
    # type: (bool) -> None
    """
    隐藏场景内所有名字，包括玩家名字，生物的自定义名称，物品展示框与命令方块的悬浮文本等
    """
    pass

def IsHideNameTag():
    # type: () -> bool
    """
    获取是否隐藏场景内所有名字
    """
    pass

def HideInteractGui(isHide):
    # type: (bool) -> None
    """
    隐藏交互按钮。隐藏后点击相应位置不会响应
    """
    pass

def HideHealthGui(isHide):
    # type: (bool) -> bool
    """
    隐藏hud界面的血量显示
    """
    pass

def HideHorseHealthGui(isHide):
    # type: (bool) -> bool
    """
    隐藏hud界面的坐骑的血量显示
    """
    pass

def HideHungerGui(isHide):
    # type: (bool) -> bool
    """
    隐藏hud界面的饥饿值显示
    """
    pass

def HideArmorGui(isHide):
    # type: (bool) -> bool
    """
    隐藏hud界面的护甲值显示
    """
    pass

def SetResponse(response):
    # type: (bool) -> None
    """
    设置原生UI是否响应
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

def GetClientSystemCls():
    # type: () -> Type[ClientSystem]
    """
    用于获取客户端system基类。实现新的system时，需要继承该接口返回的类
    """
    pass

def GetComponentCls():
    # type: () -> Type[BaseComponent]
    """
    用于获取客户端component基类。实现新的component时，需要继承该接口返回的类
    """
    pass

def GetEngineNamespace():
    # type: () -> Literal["Minecraft"]
    """
    获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace
    """
    return "Minecraft"

def GetEngineSystemName():
    # type: () -> Literal["Engine"]
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

def GetLocalPlayerId():
    # type: () -> str
    """
    获取本地玩家的id
    """
    pass

def GetScreenNodeCls():
    # type: () -> Type[ScreenNode]
    """
    获得ScreenNode类
    """
    pass

def GetViewBinderCls():
    # type: () -> Type[ViewBinder]
    """
    获得ViewBinder类
    """
    pass

def GetViewViewRequestCls():
    # type: () -> Type[ViewRequest]
    """
    获得ViewRequest类
    """
    pass

class __NativeScreenManagerModule:
    instance = NativeScreenManager.instance

def GetNativeScreenManagerCls():
    # type: () -> __NativeScreenManagerModule
    """
    获得NativeScreenManager类
    """
    pass

def GetCustomUIControlProxyCls():
    # type: () -> Type[CustomUIControlProxy]
    """
    获得原生界面自定义UI代理基类
    """
    pass

def GetUIScreenProxyCls():
    # type: () -> Type[CustomUIScreenProxy]
    """
    获得原生界面Screen代理基类
    """
    pass

def GetMiniMapScreenNodeCls():
    # type: () -> Type[MiniMapBaseScreen]
    """
    获取小地图ScreenNode基类
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

def GetEngineVersion():
    # type: () -> str
    """
    获取游戏版本-客户端。
    """
    pass

def GetMinecraftVersion():
    # type: () -> str
    """
    获取Minecraft版本-客户端。
    """
    pass

def GetTouchPos():
    # type: () -> Tuple[float, float]
    """
    获取点击的屏幕坐标。可以监听TapBeforeClientEvent或TapOrHoldReleaseClientEvent事件，调用本API获取点击坐标。
    """
    pass

def GetNavPath(pos, maxTrimNode=16, maxIteration=800, isSwimmer=False):
    # type: (Tuple[float, float, float], int, int, bool) -> Union[int, List[Tuple[float, float, float]]]
    """
    获取本地玩家到目标点的寻路路径，开发者可以通过该接口定制自定义的导航系统。
    """
    pass

def StartNavTo(pos, sfxPath, callback=None, sfxIntl=2, sfxMaxNum=16, sfxScale=(0.5, 0.5), maxIteration=800, isSwimmer=False, fps=20, playIntl=8, duration=60, oneTurnDuration=90, sfxDepthTest=False):
    # type: (Tuple[float, float, float], str, Optional[Callable[[bool], Any]], float, int, Tuple[float, float], int, bool, int, int, int, int, bool) -> int
    """
    我们提供了一个基于GetNavPath的导航系统实现，做法是在路径上生成序列帧以引导玩家通向目标点，并且当玩家偏离路径会重新进行导航。
    """
    pass

def StopNav():
    # type: () -> None
    """
    终止当前的导航
    """
    pass

def GetIP():
    # type: () -> str
    """
    获取本地玩家的ip地址
    """
    pass

def StartProfile():
    # type: () -> bool
    """
    开始启动客户端脚本性能分析，启动后调用StopProfile即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。
    """
    pass

def StopProfile(fileName=None):
    # type: (Optional[str]) -> bool
    """
    停止客户端脚本性能分析并生成火焰图，与StartProfile配合使用，此接口只支持PC端
    """
    pass

def StartMemProfile():
    # type: () -> bool
    """
    开始启动客户端脚本内存分析，启动后调用StopMemProfile即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。
    """
    pass

def StopMemProfile(fileName=None):
    # type: (Optional[str]) -> bool
    """
    停止客户端脚本内存分析并生成火焰图，与StartMemProfile配合使用，此接口只支持PC端
    """
    pass

def StartMultiProfile():
    # type: () -> bool
    """
    开始启动服务端与客户端双端脚本性能分析，启动后调用StopMultiProfile即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用StartProfile单端版本，此接口只支持PC端
    """
    pass

def StopMultiProfile(fileName=None):
    # type: (Optional[str]) -> bool
    """
    停止双端脚本性能分析并生成火焰图，与StartMultiProfile配合使用，此接口只支持PC端
    """
    pass

def HideAirSupplyGUI(isHide):
    # type: (bool) -> bool
    """
    隐藏玩家氧气值界面
    """
    pass

def HideExpGui(isHide):
    # type: (bool) -> None
    """
    非创造者模式下隐藏经验条显示
    """
    pass

def HideMoveGui(isHide):
    # type: (bool) -> None
    """
    隐藏游戏中左下角的移动按钮。隐藏后点击相应位置不会响应
    """
    pass

def SetCrossHair(visible):
    # type: (bool) -> None
    """
    设置是否使用“准星瞄准”
    """
    pass

def SetHudChatStackVisible(visible):
    # type: (bool) -> None
    """
    设置HUD界面左上小聊天窗口可见性
    """
    pass

def SetHudChatStackPosition(pos):
    # type: (Tuple[float, float]) -> None
    """
    设置HUD界面左上小聊天窗口位置
    """
    pass

def ReloadAllMaterials():
    # type: () -> bool
    """
    重新加载所有材质文件
    """
    pass

def ReloadAllShaders():
    # type: () -> bool
    """
    重新加载所有Shader文件
    """
    pass

def ReloadOneShader(shaderName):
    # type: (str) -> bool
    """
    重新加载某个Shader文件
    """
    pass

def SetKeepResourceWhenTransfer(keep=True):
    # type: (bool) -> bool
    """
    设置快速切服
    """
    pass

def SetEnableReconnectNetgame(keep=True):
    # type: (bool) -> bool
    """
    设置是否允许断线重连
    """
    pass

def GetKeepResourceWhenTransfer():
    # type: () -> bool
    """
    获取快速切服设置
    """
    pass

def SetResourceFastload(fastload=True):
    # type: (bool) -> bool
    """
    设置资源快速加载
    """
    pass

def GetResourceFastload():
    # type: () -> bool
    """
    获取资源快速加载设置
    """
    pass

def GetEnableReconnectNetgame():
    # type: () -> bool
    """
    获取是否允许断线重连
    """
    pass

def GetModConfigJson(path):
    # type: (str) -> dict
    """
    以字典形式返回指定路径的json格式配置文件的内容，文件必须放置在资源包的/modconfigs目录下
    """
    pass

def PushScreen(namespace, uiname, createParams=None):
    # type: (str, str, Optional[dict]) -> Optional[ScreenNode]
    """
    使用堆栈管理的方式创建UI
    """
    pass

def PopScreen():
    # type: () -> bool
    """
    使用堆栈管理的方式关闭UI
    """
    pass

def GetTopScreen():
    # type: () -> Optional[ScreenNode]
    """
    获取UI堆栈栈顶的UI节点
    """
    pass

def GetTopUI():
    # type: () -> str
    """
    获取UI栈顶的UI名称
    """
    pass

def PopTopUI():
    # type: () -> bool
    """
    弹出UI栈顶的UI
    """
    pass

def GetPlatform():
    # type: () -> Literal[-1, 0, 1, 2]
    """
    获取脚本运行的平台
    """
    pass

def GetWalkState():
    # type: () -> Literal[1, 2, 3]
    """
    获取玩家行走/潜行/跑步状态
    """
    pass

def ChangeSneakState():
    # type: () -> None
    """
    切换潜行状态
    """
    pass

def SimulateJump():
    # type: () -> None
    """
    模拟跳跃
    """
    pass

def ClickInteractGUI():
    # type: () -> None
    """
    模拟点击交互按钮，交互按钮指的在喂食、钓鱼、交易等交互场景出现的按钮
    """
    pass

def OpenPauseGui(isForce=False):
    # type: (bool) -> None
    """
    打开原版暂停界面
    """
    pass

def OpenChatGui(isForce=False):
    # type: (bool) -> None
    """
    打开原版聊天栏
    """
    pass

def OpenFoldGui():
    # type: () -> None
    """
    打开原版下拉界面
    """
    pass

def OpenVoiceGui():
    # type: () -> None
    """
    打开原版语音界面
    """
    pass

def OpenReportGui():
    # type: () -> None
    """
    打开原版举报界面
    """
    pass

def OpenEmoteGui():
    # type: () -> None
    """
    打开表情界面
    """
    pass

def StartCoroutine(iterOrFunc, callback=None):
    # type: (Union[Generator, Callable[[], Generator]], Optional[Callable[[], Any]]) -> Generator
    """
    开启客户端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题
    """
    pass

def StopCoroutine(iter):
    # type: (Generator) -> bool
    """
    停止客户端协程
    """
    pass

def OpenInventoryGui(categoryName='', isForce=False):
    # type: (Literal["construction", "nature", "equipment", "items", "search", ""], bool) -> None
    """
    打开原版背包界面，并支持选中某个分页(支持自定义分页名称)
    """
    pass

def GetOriginAreaOffset(areaEnum):
    # type: (str) -> Tuple[float, float, float, float]
    """
    获取指定原生UI的offset,包括左上角和右下角
    """
    pass

def GetBookManager():
    # type: () -> BookManager
    """
    获取书本管理对象
    """
    pass

def PlayHudHeartBlinkAnim():
    # type: () -> None
    """
    播放原版受伤时血量变化的动效
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

def GetPlayerList():
    # type: () -> List[str]
    """
    获取所有维度中的全部玩家的id列表
    """
    pass

def GetEngineActor():
    # type: () -> Dict[str, __EntityDict]
    """
    获取客户端当前维度中已加载的所有实体（不包含玩家）。
    """
    pass

def RegisterUIAnimations(data, override=True):
    # type: (dict, bool) -> bool
    """
    注册UI动画
    """
    pass

def UnregisterUIAnimation(namespace, defName):
    # type: (str, str) -> bool
    """
    取消UI动画的注册
    """
    pass

def ImportModule(path):
    # type: (str) -> Any
    """
    使用字符串路径导入模块，作用与importlib.import_module类似，但只能导入当前加载的mod中的模块
    """

def ToggleGyroSensor(isOpen=False):
    # type: (bool) -> bool
    """
    开启或关闭陀螺仪传感器采集
    """
    pass

def SetGyroSensorReportRate(reportRate=1):
    # type: (int) -> bool
    """
    设置陀螺仪传感器(上报/触发)频率
    """
    pass

def IsTouchWithMouse():
    # type: () -> bool
    """
    获取是否正在使用鼠标点击模拟触屏
    """
    pass

def HideCrossHairGUI(isHide):
    # type: (bool) -> bool
    """
    隐藏hud界面的十字准心显示
    """
    pass

def getEntitiesOrBlockFromRay(pos, rot, distance=16, isThrough=False, filterType=1):
    # type: (Tuple[float, float, float], Tuple[float, float, float], int, bool, int) -> List[__RayResultDict]
    """
    从指定位置发射一条射线，获取与射线相交的实体和方块
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

