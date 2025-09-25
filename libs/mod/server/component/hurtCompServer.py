# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class HurtCompServer(BaseComponent):
    def ImmuneDamage(self, immune):
        # type: (bool) -> bool
        """
        设置实体是否免疫伤害（该属性存档）
        """
        pass

    def Hurt(self, damage, cause, attackerId=None, childAttackerId=None, knocked=True, customTag=None):
        # type: (float, str, str, str, bool, str) -> bool
        """
        设置实体伤害
        """
        pass

