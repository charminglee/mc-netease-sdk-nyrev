# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
if 0:
    from typing import Optional


class ItemRendererUIControl(BaseUIControl):
    def SetUiItem(self, itemName, auxValue, isEnchanted=False, userData=None):
        # type: (str, int, bool, Optional[dict]) -> bool
        """
        设置ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见控件介绍ItemRenderer
        """
        pass

    def GetUiItem(self):
        # type: () -> dict
        """
        获取ItemRenderer控件显示的物品，ItemRenderer控件的配置方式详见控件介绍ItemRenderer
        """
        pass

