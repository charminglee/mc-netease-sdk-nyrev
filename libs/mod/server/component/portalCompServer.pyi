# -*- coding: utf-8 -*-


from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Dict


class PortalComponentServer(BaseComponent):
    def DetectStructure(self, playerId, pattern, defines, touchPos, pos, dimensionId=-1):
        # type: (None, List[str], Dict[str, str], List[Tuple[int, int]], Tuple[int, int, int], int) -> Tuple[bool, Tuple[int, int, int], Tuple[int, int, int]]
        """
        检测自定义门的结构
        """
        pass

