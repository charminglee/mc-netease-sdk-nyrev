# -*- coding: utf-8 -*-


from typing import List, Any
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Optional, Callable, Literal, TypedDict


__GameType = Literal[0, 1, 2]
class __AbilitiesDict(TypedDict):
    build: bool
    mine: bool
    doorsandswitches: bool
    opencontainers: bool
    attackplayers: bool
    attackmobs: bool
    op: bool
    teleport: bool
class __RespawnPosDict(TypedDict):
    dimensionId: int
    pos: Tuple[int, int, int]
__Operation = Literal[0, 1, 2, 3]


class PlayerCompServer(BaseComponent):
    def GetPlayerHunger(self):
        # type: () -> float
        """
        获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。
        """
        pass

    def SetPlayerHunger(self, value):
        # type: (float) -> bool
        """
        设置玩家饥饿度。
        """
        pass

    def GetPlayerCurrentExhaustionValue(self):
        # type: () -> float
        """
        获取玩家foodExhaustionLevel的当前消耗度。详见消耗度介绍
        """
        pass

    def SetPlayerCurrentExhaustionValue(self, value):
        # type: (float) -> bool
        """
        设置玩家foodExhaustionLevel的当前消耗度。详见消耗度介绍
        """
        pass

    def GetPlayerMaxExhaustionValue(self):
        # type: () -> float
        """
        获取玩家foodExhaustionLevel的归零值，常量值，默认为4。**消耗度（exhaustion）**是指玩家当前消耗度水平，初始值为0，该值会随着玩家一系列动作（如跳跃）的影响而增加，当该值大于最大消耗度（maxExhaustion）后归零，并且把饱和度（saturation）减少1（为了说明饥饿度机制，我们将此定义为**消耗事件**）
        """
        pass

    def SetPlayerMaxExhaustionValue(self, value):
        # type: (float) -> bool
        """
        设置玩家**最大消耗度(maxExhaustion)**，通过调整 **最大消耗度(maxExhaustion)** 的大小，就可以调整 **饥饿度(hunger)** 的消耗速度，当 **最大消耗度(maxExhaustion)** 很大时，饥饿度可以看似一直不下降
        """
        pass

    def GetPlayerHealthLevel(self):
        # type: () -> int
        """
        获取玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认值为18
        """
        pass

    def SetPlayerHealthLevel(self, healthLevel):
        # type: (int) -> bool
        """
        设置玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为18
        """
        pass

    def GetPlayerHealthTick(self):
        # type: () -> int
        """
        获取玩家自然恢复速度，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认值为80刻（即每4秒）恢复1点血量
        """
        pass

    def SetPlayerHealthTick(self, healthTick):
        # type: (int) -> bool
        """
        设置玩家自然恢复速度，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为80刻（即每4秒）恢复1点血量
        """
        pass

    def IsPlayerNaturalRegen(self):
        # type: () -> bool
        """
        是否开启玩家自然恢复，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认开启
        """
        pass

    def SetPlayerNaturalRegen(self, value):
        # type: (bool) -> bool
        """
        设置是否开启玩家自然恢复，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认开启
        """
        pass

    def GetPlayerStarveLevel(self):
        # type: () -> int
        """
        获取玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1
        """
        pass

    def SetPlayerStarveLevel(self, starveLevel):
        # type: (int) -> bool
        """
        设置玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1
        """
        pass

    def GetPlayerStarveTick(self):
        # type: () -> int
        """
        获取玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为80刻（即每4秒）扣除1点血量
        """
        pass

    def SetPlayerStarveTick(self, starveTick):
        # type: (int) -> bool
        """
        设置玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认值为80刻（即每4秒）扣除1点血量
        """
        pass

    def IsPlayerNaturalStarve(self):
        # type: () -> bool
        """
        是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动恢复血量，开启饥饿值且开启饥饿掉血时有效。原版默认开启
        """
        pass

    def SetPlayerNaturalStarve(self, value):
        # type: (bool) -> bool
        """
        设置是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认开启
        """
        pass

    def OpenPlayerCritBox(self):
        # type: () -> None
        """
        开启玩家爆头，开启后该玩家头部被击中后会触发ProjectileCritHitEvent事件。
        """
        pass

    def ClosePlayerCritBox(self):
        # type: () -> None
        """
        关闭玩家爆头，关闭后将无法触发ProjectileCritHitEvent事件。
        """
        pass

    def SetPlayerMovable(self, isMovable):
        # type: (bool) -> bool
        """
        设置玩家是否可移动
        """
        pass

    def SetPlayerJumpable(self, isJumpable):
        # type: (bool) -> bool
        """
        设置玩家是否可跳跃
        """
        pass

    def SetPlayerGameType(self, gameType):
        # type: (__GameType) -> bool
        """
        设置玩家个人游戏模式
        """
        pass

    def OpenPlayerHitBlockDetection(self, precision):
        # type: (float) -> bool
        """
        开启碰撞方块的检测，开启后碰撞时会触发OnPlayerHitBlockServerEvent事件
        """
        pass

    def ClosePlayerHitBlockDetection(self):
        # type: () -> bool
        """
        关闭碰撞方块的检测，关闭后将不会触发OnPlayerHitBlockServerEvent事件
        """
        pass

    def OpenPlayerHitMobDetection(self):
        # type: () -> bool
        """
        开启对其他生物的碰撞检测，开启后和生物间发生碰撞时会触发OnMobHitMobServerEvent事件。（该接口对生物同样有效）
        """
        pass

    def ClosePlayerHitMobDetection(self):
        # type: () -> bool
        """
        关闭碰撞生物的检测，关闭后将不会触发OnMobHitMobServerEvent事件。
        """
        pass

    def SetPickUpArea(self, area):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置玩家的拾取物品范围，设置后该玩家的拾取物品范围会在原版拾取范围的基础上进行改变。
        """
        pass

    def EnableKeepInventory(self, enable):
        # type: (bool) -> bool
        """
        设置玩家死亡不掉落物品
        """
        pass

    def isSneaking(self):
        # type: () -> bool
        """
        获取玩家是否处于潜行状态
        """
        pass

    def isSwimming(self):
        # type: () -> bool
        """
        获取玩家是否处于游泳状态。
        """
        pass

    def ClearDefinedLevelUpCost(self, level):
        # type: (int) -> bool
        """
        接口用于重置升级经验。使用ChangeLevelUpCostServerEvent事件设置升级经验后，升级经验无法调整。需要调整升级经验时，可使用该接口。使用步骤如下：1、使用ClearDefineLevelUpconst，2、在升级抛出ChangeLevelUpCostServerEvent事件后重新设置经验。
        """
        pass

    def ChangeSelectSlot(self, slot):
        # type: (int) -> bool
        """
        设置玩家当前选中快捷栏物品的index
        """
        pass

    def GetPlayerOperation(self):
        # type: () -> __Operation
        """
        获取玩家权限类型信息
        """
        pass

    def GetPlayerAbilities(self):
        # type: () -> __AbilitiesDict
        """
        获取玩家具体权限
        """
        pass

    def GetPlayerExhaustionRatioByType(self, type):
        # type: (Literal[0, 1, 2, 3, 4, 9]) -> float
        """
        获取玩家某行为饥饿度消耗倍率
        """
        pass

    def SetPlayerExhaustionRatioByType(self, type, ratio):
        # type: (Literal[0, 1, 2, 3, 4, 9], float) -> bool
        """
        设置玩家某行为饥饿度消耗倍率
        """
        pass

    def SetInteracteCenterOffset(self, offset):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置玩家服务端交互中心的偏移
        """
        pass

    def GetInteracteCenterOffset(self):
        # type: () -> Tuple[float, float, float]
        """
        获取玩家服务端交互中心的偏移
        """
        pass

    def GetPlayerInteracteRange(self):
        # type: () -> float
        """
        获取玩家服务端的交互距离
        """
        pass

    def SetPlayerInteracteRange(self, interacteRange):
        # type: (float) -> bool
        """
        设置玩家服务端的交互距离
        """
        pass

    def SetPlayerRespawnPos(self, pos, dimensionId=0):
        # type: (Tuple[int, int, int], int) -> bool
        """
        设置玩家复活的位置与维度
        """
        pass

    def GetPlayerRespawnPos(self):
        # type: () -> __RespawnPosDict
        """
        获取玩家复活点
        """
        pass

    def CollectOnlineClientData(self, collectTypes, callback, extraArgs=None):
        # type: (List[Literal["game", "player", "world", "entity"]], Callable[[str, Optional[dict]], Any], Optional[dict]) -> None
        """
        收集在线玩家客户端数据，用于判断玩家是否作弊
        """
        pass

    def SetPlayerAttackSpeedAmplifier(self, amplifier):
        # type: (float) -> bool
        """
        设置玩家攻击速度倍数，1.0表示正常水平，1.2表示速度减益20%，0.8表示速度增益20%
        """
        pass

    def GetIsBlocking(self):
        # type: () -> bool
        """
        获取玩家激活盾牌状态
        """
        pass

    def GetRelevantPlayer(self, exceptList=None):
        # type: (Optional[List[str]]) -> List[str]
        """
        获取附近玩家id列表
        """
        pass

    def SetBanPlayerFishing(self, isBan):
        # type: (bool) -> bool
        """
        设置是否屏蔽玩家钓鱼功能，屏蔽后玩家可以正常抛甩鱼竿，但无法钓起任何物品
        """
        pass

    def GetEnchantmentSeed(self):
        # type: () -> int
        """
        获取玩家的附魔种子，该种子会决定附魔台上准备附魔的装备的附魔项
        """
        pass

    def SetEnchantmentSeed(self, enchantmentSeed):
        # type: (int) -> bool
        """
        设置玩家的附魔种子，该种子会决定附魔台上准备附魔的装备的附魔项
        """
        pass

    def SetBuildAbility(self, canBuild):
        # type: (bool) -> bool
        """
        设置玩家能否放置方块，该接口的设置会存档，且只影响生存模式
        """
        pass

    def SetMineAbility(self, canMine):
        # type: (bool) -> bool
        """
        设置玩家能否摧毁方块，该接口的设置会存档，且只影响生存模式
        """
        pass

    def SetOperateDoorsAndSwitchesAbility(self, canOperate):
        # type: (bool) -> bool
        """
        设置玩家能否与门和开关交互
        """
        pass

    def SetOpenContainersAbility(self, canOpen):
        # type: (bool) -> bool
        """
        设置玩家能否打开容器
        """
        pass

    def SetAttackPlayersAbility(self, canAttack):
        # type: (bool) -> bool
        """
        设置玩家能否攻击其他玩家
        """
        pass

    def SetAttackMobsAbility(self, canAttack):
        # type: (bool) -> bool
        """
        设置玩家能否攻击生物
        """
        pass

    def SetOperatorCommandAbility(self, canOperate):
        # type: (bool) -> bool
        """
        设置玩家是否具有操作员命令权限
        """
        pass

    def SetTeleportAbility(self, canTeleport):
        # type: (bool) -> bool
        """
        设置玩家能否使用TP指令
        """
        pass

    def SetPlayerMute(self, isMute):
        # type: (bool) -> bool
        """
        设置玩家是否禁言，该接口的设置不存档
        """
        pass

    def SetPermissionLevel(self, level):
        # type: (__Operation) -> bool
        """
        设置玩家权限等级
        """
        pass

    def PlayerAttackEntity(self, entityId):
        # type: (str) -> bool
        """
        玩家使用手持武器攻击某个生物
        """
        pass

    def GetPlayerDestroyTotalTime(self, blockName):
        # type: (str) -> float
        """
        获取玩家破坏方块需要的时间，受玩家状态（急迫、潮涌、挖掘疲劳）和手持物及手持物附魔（效率）影响
        """
        pass

    def OpenNeteaseContainer(self, screenName, customDescription, isCloseReturnItem=False):
        # type: (str, str, bool) -> bool
        """
        打开自定义容器界面，不依赖于方块。该界面的物品数据需由开发者自行维护。
        """
        pass

