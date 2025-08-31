
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.comp.baseComp import BaseComp
from mod.client.plugin.illustratedBook.bookConfig import BookConfig
from typing import List
from typing import Dict
from typing import Tuple

class EntityComp(BaseComp):

    def __init__(self):
        # type: () -> EntityComp
        """
            工作台合成表组件初始化
        """
        pass

    def SetDataBeforeShow(self, entityName, molang_dict = {}, entityOffset = (0, 0), backgroundImage = BookConfig.Images.sqrtPanel_light):
        # type: (str, Dict, Tuple[int, int], str) -> EntityComp
        """
            在显示组件之前，设置组件的数据
        """       
        pass
    


