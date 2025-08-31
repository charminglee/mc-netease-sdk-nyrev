
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.comp.baseComp import BaseComp
from mod.client.plugin.illustratedBook.bookConfig import BookConfig
from typing import List
from typing import Dict
from typing import Tuple

class TextComp(BaseComp):

    def __init__(self, textAlign = BookConfig.TextAlign.Left):
        # type: (int) -> TextComp
        """
            文本组件初始化
        """
        pass

    def SetDataBeforeShow(self, text, textSize):
        # type: (str, int) -> TextComp
        """
            在显示组件之前，设置组件的数据
        """       
        pass 

    def SetAlpha(self, alpha):
        # type: (float) -> TextComp
        """
            设置文本字体透明度
        """       
        pass        

    def SetColor(self, color):
        # type: (Tuple[float, float, float, float]) -> TextComp
        """
            设置文本字体颜色
        """       
        pass        


