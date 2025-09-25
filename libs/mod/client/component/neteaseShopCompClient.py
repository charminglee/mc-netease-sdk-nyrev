# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class NeteaseShopCompClient(BaseComponent):
    def HideShopGate(self):
        # type: () -> None
        """
        隐藏网易商城入口
        """
        pass

    def ShowShopGate(self):
        # type: () -> None
        """
        显示网易商城入口
        """
        pass

    def OpenShopWindow(self):
        # type: () -> None
        """
        打开网易商城窗口。PC端无效（Apollo的PC端请使用商城插件）
        """
        pass

    def OpenItemDetailWindow(self, categoryName, itemName):
        # type: (str, str) -> None
        """
        打开特定商品的详情界面
        """
        pass

    def CloseShopWindow(self):
        # type: () -> None
        """
        关闭网易商城窗口
        """
        pass

