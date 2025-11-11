# -*- coding: utf-8 -*-


from typing import Union
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class ChunkSourceCompClient(BaseComponent):
    def GetChunkPosFromBlockPos(self, blockPos):
        # type: (Tuple[int, int, int]) -> Union[Tuple[int, int], None]
        """
        通过方块坐标获得该方块所在区块坐标
        """
        pass

