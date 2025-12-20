# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class ActorLootComponentServer(BaseComponent):
    def SpawnLootTable(self, pos, identifier, playerKillerId=None, damageCauseEntityId=None):
        # type: (Tuple[int, int, int], str, str | None, str | None) -> bool
        """
        使用生物类型模拟一次随机掉落，生成的物品与json定义的概率有关
        """
        pass

    def SpawnLootTableWithActor(self, pos, entityId, playerKillerId=None, damageCauseEntityId=None):
        # type: (Tuple[int, int, int], str, str | None, str | None) -> bool
        """
        使用生物实例模拟一次随机掉落，生成的物品与json定义的概率有关
        """
        pass

