# -*- coding: utf-8 -*-


from typing import List
from mod.common.component.baseComponent import BaseComponent


class EntityDefinitionsCompServer(BaseComponent):
    def GetEntityNBTTags(self):
        # type: () -> dict | None
        """
        获取实体的NBT标签
        """
        pass

    def GetEntityDefinitions(self):
        # type: () -> List[str]
        """
        获取实体的命名空间ID及其当前和之前的定义组件群
        """
        pass

    def GetEntityFallDistance(self):
        # type: () -> float
        """
        获取实体的坠落高度，越大的值会给予实体更大的坠落伤害，建议在OnGroundServerEvent事件中调用
        """
        pass

    def GetEntityLinksTag(self):
        # type: () -> dict
        """
        获取实体相连接的实体，如获取entityId为马，会返回骑乘者的信息
        """
        pass

    def IsLootDropped(self):
        # type: () -> bool
        """
        获取生物是否生成掉落物
        """
        pass

    def SetLootDropped(self, isLootDropped):
        # type: (bool) -> bool
        """
        设置生物是否生成掉落物
        """
        pass

    def GetMobColor(self):
        # type: () -> int
        """
        获取生物的颜色，截止至网易2.9版本，只对羊和热带鱼有效
        """
        pass

    def SetMobColor(self, colorType):
        # type: (int) -> bool
        """
        设置生物的颜色，截止至网易2.9版本，只对羊和热带鱼有效
        """
        pass

    def GetMobStrength(self):
        # type: () -> int
        """
        获取生物的强度，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多
        """
        pass

    def SetMobStrength(self, strength):
        # type: (int) -> bool
        """
        设置生物的强度，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多
        """
        pass

    def GetMobStrengthMax(self):
        # type: () -> int
        """
        获取生物强度的最大值，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多，SetMobStrength无法超过SetMobStrengthMax的值
        """
        pass

    def SetMobStrengthMax(self, strength):
        # type: (int) -> bool
        """
        设置生物强度的最大值，截止至网易2.9版本，只对羊驼有效，强度越大羊驼驮运的箱子时格子数量越多，SetMobStrength无法超过SetMobStrengthMax的值。由于引擎限制，在羊驼被打时候会reload组件，strengthMax会恢复成llama.json中的配置值(minecraft:strength)
        """
        pass

    def IsSheared(self):
        # type: () -> bool
        """
        判断实体是否被剃毛，截止至网易2.9版本，只对羊有效
        """
        pass

    def SetSheared(self, isSheared):
        # type: (bool) -> bool
        """
        设置实体是否被剃毛，截止至网易2.9版本，只对羊有效
        """
        pass

    def IsIllagerCaptain(self):
        # type: () -> bool
        """
        判断实体是否为袭击队长，截止至网易2.9版本，只对掠夺者和卫道士有效
        """
        pass

    def PromoteToIllagerCaptain(self):
        # type: () -> bool
        """
        晋升实体为袭击队长，截止至网易2.9版本，只对掠夺者和卫道士有效
        """
        pass

    def IsSitting(self):
        # type: () -> bool
        """
        判断实体是否处于坐下状态
        """
        pass

    def SetSitting(self, shouldSitDown):
        # type: (bool) -> bool
        """
        设置生物是否坐下
        """
        pass

    def IsBaby(self):
        # type: () -> bool
        """
        判断实体是否为幼年
        """
        pass

    def SetAsAdult(self):
        # type: () -> bool
        """
        设置实体为成年体
        """
        pass

    def IsTamed(self):
        # type: () -> bool
        """
        判断实体是否被驯服
        """
        pass

    def IsAngry(self):
        # type: () -> bool
        """
        判断实体是否处于激怒状态
        """
        pass

    def SetAngry(self, isAngry, targerId=''):
        # type: (bool, str) -> bool
        """
        设置实体是否处于激怒状态
        """
        pass

    def IsOutOfControl(self):
        # type: () -> bool
        """
        判断实体是否处于失控状态，截止至网易2.9版本，只对船有效
        """
        pass

    def SetOutOfControl(self, isOutOfControl):
        # type: (bool) -> bool
        """
        设置实体是否处于失控状态，截止至网易2.9版本，只对船有效
        """
        pass

    def GetVariant(self):
        # type: () -> int
        """
        获取实体的变种属性值
        """
        pass

    def SetVariant(self, variantType):
        # type: (int) -> bool
        """
        设置实体的变种属性值
        """
        pass

    def GetMarkVariant(self):
        # type: () -> int
        """
        获取实体的标记变种属性值
        """
        pass

    def SetMarkVariant(self, variantType):
        # type: (int) -> bool
        """
        设置实体的标记变种属性值
        """
        pass

    def HasSaddle(self):
        # type: () -> bool
        """
        判断实体是否装备了鞍
        """
        pass

    def HasChest(self):
        # type: () -> bool
        """
        判断生物是否背负了箱子，截止至网易2.9版本，只对羊驼、驴、骡生效
        """
        pass

    def SetChest(self, hasChest):
        # type: (bool) -> bool
        """
        设置生物是否背负了箱子，截止至网易2.9版本，只对羊驼、驴、骡生效
        """
        pass

    def IsEating(self):
        # type: () -> bool
        """
        判断非玩家实体是否在进食
        """
        pass

    def IsStunned(self):
        # type: () -> bool
        """
        判断是否处于眩晕状态，截止至网易2.9版本，仅对劫掠兽有效
        """
        pass

    def IsRoaring(self):
        # type: () -> bool
        """
        判断是否处于咆哮状态，截止至网易2.9版本，仅对劫掠兽有效
        """
        pass

    def IsPersistent(self):
        # type: () -> bool
        """
        判断是否为持久性生物
        """
        pass

    def GetLeashHolder(self):
        # type: () -> str
        """
        获取实体被使用拴绳牵引时牵引者的ID
        """
        pass

    def SetLeashHolder(self, holderId):
        # type: (str) -> bool
        """
        为实体添加牵引者，与原版拴绳的作用相同，详见基岩版栓绳介绍
        """
        pass

    def GetTradeLevel(self):
        # type: () -> int
        """
        获取村民的交易等级
        """
        pass

    def SetTradeLevel(self, holderId):
        # type: (int) -> bool
        """
        设置村民的交易等级
        """
        pass

    def GetDeathTime(self):
        # type: () -> int
        """
        获取生物死亡后持续的时间（刻，1秒20刻），用于控制死亡动画。0表示生物未死亡。
        """
        pass

    def IsNaturallySpawned(self):
        # type: () -> bool
        """
        获取生物是否为自然生成的
        """
        pass

    def IsPregnant(self):
        # type: () -> bool
        """
        获取生物是否怀孕，截止至网易2.9版本，只对海龟有效
        """
        pass

