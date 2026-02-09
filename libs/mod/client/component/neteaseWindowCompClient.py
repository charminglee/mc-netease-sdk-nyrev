# -*- coding: utf-8 -*-


from mod.common.component.baseComponent import BaseComponent
from mod.client.plugin.generalSetting.SettingInst import SettingInst


class NeteaseWindowCompClient(BaseComponent):
    def OpenResourceCenterDetailWindow(self, itemId):
        # type: (str) -> None
        """
        打开网易资源中心组件详情界面。该接口只能在横屏版本手机端使用
        """
        pass

    def OpenDeveloperHomeWindow(self, mailAddress):
        # type: (str) -> None
        """
        打开网易资源中心开发者主页。该接口只能在横屏版本手机端使用
        """
        pass

    def RegisterSettingInst(self, modNamespace, modName=None, iconPath=None):
        # type: (str, str | None, str | None) -> SettingInst
        """
        注册通用设置实例
        """
        pass

    def GetSettingInst(self, modNamespace):
        # type: (str) -> SettingInst
        """
        获取当前模组的通用设置实例
        """
        pass

