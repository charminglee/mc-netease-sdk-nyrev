# -*- coding: utf-8 -*-

from typing import Union
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class PlayerCompClient(BaseComponent):
    def OpenPlayerHitBlockDetection(self, precision):
        # type: (float) -> 'bool'
        """
        开启碰撞方块的检测，开启后碰撞时会触发OnPlayerHitBlockClientEvent事件
        """
        pass

    def ClosePlayerHitBlockDetection(self):
        # type: () -> 'bool'
        """
        关闭碰撞方块的检测，关闭后将不会触发OnPlayerHitBlockClientEvent事件
        """
        pass

    def OpenPlayerHitMobDetection(self):
        # type: () -> 'bool'
        """
        开启对其他生物的碰撞检测，开启后和生物间发生碰撞时会触发OnMobHitMobClientEvent事件。（该接口对生物同样有效）
        """
        pass

    def ClosePlayerHitMobDetection(self):
        # type: () -> 'bool'
        """
        关闭碰撞生物的检测，关闭后将不会触发OnMobHitMobClientEvent事件。（该接口对生物同样有效）
        """
        pass

    def isGliding(self):
        # type: () -> 'bool'
        """
        是否鞘翅飞行
        """
        pass

    def SetPickCenterOffset(self, offset):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置第三人称下，玩家客户端交互中心的偏移
        """
        pass

    def GetPickCenterOffset(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取玩家设置的第三人称下客户端交互中心的偏移
        """
        pass

    def SetPickRange(self, pickRange):
        # type: (float) -> 'bool'
        """
        设置玩家客户端的交互距离
        """
        pass

    def GetPickRange(self):
        # type: () -> 'float'
        """
        获取玩家客户端的交互距离
        """
        pass

    def isSwimming(self):
        # type: () -> 'bool'
        """
        是否游泳
        """
        pass

    def isRiding(self):
        # type: () -> 'bool'
        """
        是否骑乘
        """
        pass

    def isSneaking(self):
        # type: () -> 'bool'
        """
        是否潜行
        """
        pass

    def setSneaking(self):
        # type: () -> 'bool'
        """
        设置是否潜行，只能设置本地玩家（只适用于移动端）
        """
        pass

    def setUsingShield(self, flag=True):
        # type: (bool) -> 'int'
        """
        激活盾牌状态
        """
        pass

    def isSprinting(self):
        # type: () -> 'bool'
        """
        是否在疾跑
        """
        pass

    def setSprinting(self):
        # type: () -> 'bool'
        """
        设置行走模式为疾跑/冲刺，只能设置本地玩家（只适用于移动端）
        """
        pass

    def isInWater(self):
        # type: () -> 'bool'
        """
        是否在水中
        """
        pass

    def isMoving(self):
        # type: () -> 'bool'
        """
        是否在行走
        """
        pass

    def setMoving(self):
        # type: () -> 'bool'
        """
        设置是否行走，只能设置本地玩家（只适用于移动端）
        """
        pass

    def getUid(self):
        # type: () -> 'Union[long,None]'
        """
        获取本地玩家的uid
        """
        pass

    def Swing(self):
        # type: () -> 'bool'
        """
        本地玩家播放原版攻击动作
        """
        pass

    def GetPlayerHunger(self):
        # type: () -> 'float'
        """
        获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。
        """
        pass

    def GetPlayerDestroyTotalTime(self, blockName):
        # type: (str) -> 'float'
        """
        获取玩家破坏方块需要的时间，受玩家状态（急迫、潮涌、挖掘疲劳）和手持物及手持物附魔（效率）影响
        """
        pass

    def IsOnLadder(self):
        # type: () -> 'bool'
        """
        获取玩家是否在梯子/藤蔓上
        """
        pass

    def IsInScaffolding(self):
        # type: () -> 'bool'
        """
        获取玩家是否在脚手架中
        """
        pass

