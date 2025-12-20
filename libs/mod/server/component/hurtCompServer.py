# -*- coding: utf-8 -*-


from typing import Literal
from mod.common.component.baseComponent import BaseComponent


class HurtCompServer(BaseComponent):
    def ImmuneDamage(self, immune):
        # type: (bool) -> bool
        """
        设置实体是否免疫伤害（该属性存档）
        """
        pass

    def Hurt(self, damage, cause, attackerId=None, childAttackerId=None, knocked=True, customTag=None):
        # type: (float, Literal["none", "override", "contact", "entity_attack", "projectile", "suffocation", "fall", "fire", "fire_tick", "lava", "drowning", "block_explosion", "entity_explosion", "void", "self_destruct", "self_destruct", "magic", "wither", "starve", "anvil", "thorns", "falling_block", "piston", "fly_into_wall", "magma", "fireworks", "lightning", "freezing", "stalactite", "stalagmite", "ram_attack", "custom", "sonic_boom", "camp_fire", "soul_camp_fire"] | str, str | None, str | None, bool, str | None) -> bool
        """
        设置实体伤害
        """
        pass
