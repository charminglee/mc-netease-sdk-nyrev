# -*- coding: utf-8 -*-


from typing import Callable, List, Any


class SettingInst(object):
    def Clear(self):
        # type: () -> None
        """清除所有控件"""
        pass

    def AddText(self, key, name, priority=None):
        # type: (str, str, int | None) -> 'SettingInst'
        """
        添加文本控件

        :param str key: 控件id
        :param str name: 控件的文字描述
        :param int|None priority: 显示顺序优先级，默认根据添加顺序排列
        """
        pass

    def AddToggle(self, key, name, callback, priority=None, default=False):
        # type: (str, str, Callable, int | None, bool) -> 'SettingInst'
        """
        添加开关控件

        :param str key: 控件id
        :param str name: 控件的文字描述
        :param function callback: 控件的回调函数，定义：def callback(*args)
        :param int|None priority: 显示顺序优先级，默认根据添加顺序排列
        :param bool default: 默认值
        """
        pass

    def AddSlider(self, key, name, step, callback, priority=None, default=0):
        # type: (str, str, int, Callable, int | None, int) -> 'SettingInst'
        """
        添加滑动条控件

        :param str key: 控件id
        :param str name: 控件的文字描述
        :param int step: 滑动条的最大值，范围：0~step
        :param function callback: 控件的回调函数，定义：def callback(*args)
        :param int|None priority: 显示顺序优先级，默认根据添加顺序排列
        :param int default: 默认值
        """
        pass

    def AddDropDown(self, key, name, options, callback, priority=None, default=None):
        # type: (str, str, List[str], Callable, int | None, str | None) -> 'SettingInst'
        """
        添加下拉选项控件

        :param str key: 控件id
        :param str name: 控件的文字描述
        :param list[str] options: 下拉选项列表
        :param function callback: 控件的回调函数，定义：def callback(*args)
        :param int|None priority: 显示顺序优先级，默认根据添加顺序排列
        :param str|None default: 默认选项，该值需在options中
        """
        pass

    def AddInput(self, key, name, callback, priority=None, default=""):
        # type: (str, str, Callable, int | None, str) -> 'SettingInst'
        """
        添加输入框控件

        :param str key: 控件id
        :param str name: 控件的文字描述
        :param function callback: 控件的回调函数，定义：def callback(*args)
        :param int|None priority: 显示顺序优先级，默认根据添加顺序排列
        :param str default: 默认显示的文本
        """
        pass

    def GetToggleDefault(self, key):
        # type: (str) -> bool
        """
        获取开关控件的默认值

        :param str key: 控件id
        :return bool: 开关状态
        """
        pass

    def GetInputDefault(self, key):
        # type: (str) -> str
        """
        获输入框的默认输入文本

        :param str key: 控件id
        :return str: 输入框的文本
        """
        pass

    def GetDropDownDefault(self, key):
        # type: (str) -> str
        """
        获取下拉选项控件的默认值

        :param str key: 控件id
        :return str: 默认选项在列表中的索引
        """
        pass

    def GetSliderDefault(self, key):
        # type: (str) -> int
        """
        获取滑动条控件的默认值

        :param str key: 控件id
        :return int: 滑块的值
        """
        pass

    def GetText(self, key):
        # type: (str) -> str
        """
        获取文字控件的文本

        :param str key: 控件id
        :return str: 显示的文本
        """
        pass

    def SetToggleDefault(self, key, value):
        # type: (str, bool) -> 'SettingInst'
        """
        设置开关控件的默认值

        :param str key: 控件id
        :param bool value: 开关的值
        """
        pass

    def SetInputDefault(self, key, value):
        # type: (str, str) -> 'SettingInst'
        """
        设置输入框控件的默认文本

        :param str key: 控件id
        :param str value: 显示的文本
        """
        pass

    def SetDropDownDefault(self, key, option):
        # type: (str, str) -> 'SettingInst'
        """
        设置下拉选项控件的默认选项

        :param str key: 控件id
        :param str option: 选项文字，如文字不在选项列表里，会自动添加到列表
        """
        pass

    def SetSliderDefault(self, key, value):
        # type: (str, int) -> 'SettingInst'
        """
        设置滑动条控件的默认值

        :param str key: 控件id
        :param int value: 滑块的值
        """
        pass

    def SetText(self, key, value):
        # type: (str, str) -> 'SettingInst'
        """
        设置文本控件的值

        :param str key: 控件id
        :param str value: 显示的文本
        """
        pass

    def SetLockSettingComp(self, key, is_locked):
        # type: (str, bool) -> 'SettingInst'
        """
        设置锁定控件，锁定后无法点击

        :param str key: 控件id
        :param bool is_locked: 是否锁定
        """
        pass

    def GetFormatData(self):
        # type: () -> dict[str, str | list]
        """
        获取当前实例的结构化数据，控件数据根据priority的值升序排序

        返回格式:
        ```
        {
            "modId": str,      # 模组ID
            "name": str,        # 名称
            "icon": str,        # 图标路径
            "settings": list    # 设置项列表，按priority升序排序
        }
        ```
        """
        pass

    def GetSettingsControl(self, key):
        # type: (str) -> dict[str, Any]
        """获取控件的结构化数据"""
        pass

    def GetModId(self):
        # type: () -> str
        """获取实例的modId"""
        pass

    def GetAutoPriority(self):
        # type: () -> int
        """
        获取自动设置的优先级的值

        当添加控件时，如果不设置优先级，则会自动从0开始设置。

        优先级会影响控件排列顺序，升序排列。
        """
        pass
