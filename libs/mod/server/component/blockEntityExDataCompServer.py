# -*- coding: utf-8 -*-


from typing import Union
from typing import Tuple
from mod.common.component.baseComponent import BaseComponent
from mod.server.blockEntityData import BlockEntityData


class BlockEntityExDataCompServer(BaseComponent):
    def GetBlockEntityData(self, dimension, pos):
        # type: (int, Tuple[int, int, int]) -> Union[BlockEntityData, None]
        """
        用于获取可操作某个自定义方块实体数据的对象，操作方式与dict类似
        """
        pass
