# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class BlockUseEventWhiteListComponentClient(BaseComponent):
    def AddBlockItemListenForUseEvent(self, blockName):
        # type: (str) -> bool
        """
        增加blockName方块对ClientBlockUseEvent事件的脚本层监听
        """
        pass

    def RemoveBlockItemListenForUseEvent(self, blockName):
        # type: (str) -> bool
        """
        移除blockName方块对ClientBlockUseEvent事件的脚本层监听
        """
        pass

    def ClearAllListenForBlockUseEventItems(self):
        # type: () -> bool
        """
        清空所有已添加方块对ClientBlockUseEvent事件的脚本层监听
        """
        pass

