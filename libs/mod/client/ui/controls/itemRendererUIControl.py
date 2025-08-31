# -*- coding: utf-8 -*-

from mod.client.ui.controls.baseUIControl import BaseUIControl

class ItemRendererUIControl(BaseUIControl):
    def SetUiItem(self, itemName, auxValue, isEnchanted=False, userData=None):
        # type: (str, int, bool, dict) -> 'bool'
        """
        设置ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见<a href="../../../../mcguide/18-界面与交互/30-UI说明文档.html#itemrenderer">控件介绍ItemRenderer</a>
        """
        pass

    def GetUiItem(self):
        # type: () -> 'dict'
        """
        获取ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见<a href="../../../../mcguide/18-界面与交互/30-UI说明文档.html#itemrenderer">控件介绍ItemRenderer</a>
        """
        pass

