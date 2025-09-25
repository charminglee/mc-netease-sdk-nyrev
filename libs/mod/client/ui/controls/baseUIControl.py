# -*- coding: utf-8 -*-


if 0:
    from typing import Tuple, Any, Callable, Dict, Optional
    from mod.client.ui.controls.minimapUIControl import MiniMapUIControl
    from mod.client.ui.controls.inputPanelUIControl import InputPanelUIControl
    from mod.client.ui.controls.itemRendererUIControl import ItemRendererUIControl
    from mod.client.ui.controls.neteaseComboBoxUIControl import NeteaseComboBoxUIControl
    from mod.client.ui.controls.progressBarUIControl import ProgressBarUIControl
    from mod.client.ui.controls.buttonUIControl import ButtonUIControl
    from mod.client.ui.controls.switchToggleUIControl import SwitchToggleUIControl
    from mod.client.ui.controls.imageUIControl import ImageUIControl
    from mod.client.ui.controls.stackPanelUIControl import StackPanelUIControl
    from mod.client.ui.controls.selectionWheelUIControl import SelectionWheelUIControl
    from mod.client.ui.controls.textEditBoxUIControl import TextEditBoxUIControl
    from mod.client.ui.controls.gridUIControl import GridUIControl
    from mod.client.ui.controls.labelUIControl import LabelUIControl
    from mod.client.ui.controls.neteasePaperDollUIControl import NeteasePaperDollUIControl
    from mod.client.ui.controls.scrollViewUIControl import ScrollViewUIControl
    from mod.client.ui.controls.sliderUIControl import SliderUIControl


class BaseUIControl(object):
    def __init__(self, screenNode, path):
        self.__path = path
        self.__sn = screenNode

    def FullPath(self):
        return self.__module__ + self.__path

    def SetPosition(self, pos):
        # type: (Tuple[float, float]) -> None
        """
        设置控件相对父节点的坐标
        """
        pass

    def SetFullSize(self, axis, paramDict):
        # type: (str, dict) -> bool
        """
        设置控件的大小，支持比例形式以及绝对值
        """
        pass

    def GetFullSize(self, axis):
        # type: (str) -> dict
        """
        获取控件的大小，支持百分比以及绝对值
        """
        pass

    def SetFullPosition(self, axis, paramDict):
        # type: (str, dict) -> bool
        """
        设置控件的锚点坐标（全局坐标），支持比例值以及绝对值
        """
        pass

    def GetFullPosition(self, axis):
        # type: (str) -> dict
        """
        获取控件的锚点坐标，支持比例值以及绝对值
        """
        pass

    def SetAnchorFrom(self, anchorFrom):
        # type: (str) -> bool
        """
        设置控件相对于父节点的锚点
        """
        pass

    def GetAnchorFrom(self):
        # type: () -> str
        """
        判断控件相对于父节点的哪个锚点来计算位置与大小
        """
        pass

    def SetAnchorTo(self, anchorTo):
        # type: (str) -> bool
        """
        设置控件自身锚点位置
        """
        pass

    def GetAnchorTo(self):
        # type: () -> str
        """
        获取控件自身锚点位置信息
        """
        pass

    def SetClipOffset(self, clipOffset):
        # type: (Tuple[float, float]) -> bool
        """
        设置控件的裁剪偏移信息
        """
        pass

    def GetClipOffset(self):
        # type: () -> Tuple[float, float]
        """
        获取控件的裁剪偏移信息
        """
        return (1, 1)

    def SetClipsChildren(self, clipsChildren):
        # type: (bool) -> bool
        """
        设置控件是否开启裁剪内容
        """
        pass

    def GetClipsChildren(self):
        # type: () -> bool
        """
        根据控件路径返回某控件是否开启裁剪内容
        """
        return False

    def SetMaxSize(self, maxSize):
        # type: (Tuple[float, float]) -> bool
        """
        设置控件所允许的最大的大小值
        """
        pass

    def GetMaxSize(self):
        # type: () -> Tuple[float, float]
        """
        获取控件所允许的最大的大小值
        """
        return (1, 1)

    def SetMinSize(self, minSize):
        # type: (Tuple[float, float]) -> bool
        """
        设置控件所允许的最小的大小值
        """
        pass

    def GetMinSize(self):
        # type: () -> Tuple[float, float]
        """
        获取控件所允许的最小的大小值
        """
        return (1, 1)

    def GetPosition(self):
        # type: () -> Tuple[float, float]
        """
        获取控件相对父节点的坐标
        """
        return (1, 1)

    def GetGlobalPosition(self):
        # type: () -> Tuple[float, float]
        """
        获取控件全局坐标
        """
        return (1, 1)

    def SetSize(self, size, resizeChildren=False):
        # type: (Tuple[float, float], bool) -> None
        """
        设置控件的大小
        """
        pass

    def GetSize(self):
        # type: () -> Tuple[float, float]
        """
        获取控件的大小
        """
        return (1, 1)

    def SetVisible(self, visible, forceUpdate=True):
        # type: (bool, bool) -> None
        """
        根据控件路径选择是否显示某控件，可以通过传入空字符串（""）的方式来调整整个JSON的显示/隐藏
        """
        pass

    def GetVisible(self):
        # type: () -> bool
        """
        根据控件路径返回某控件是否已显示
        """
        return True

    def SetTouchEnable(self, enable):
        # type: (bool) -> None
        """
        设置控件是否可点击交互
        """
        pass

    def SetAlpha(self, alpha):
        # type: (float) -> None
        """
        设置节点的透明度，仅对image和label控件生效
        """
        pass

    def SetLayer(self, layer, syncRefresh=True, forceUpdate=True):
        # type: (int, bool, bool) -> None
        """
        设置控件节点的层级，可以通过传入空字符串（""）的方式来调整整个JSON的基础层级
        """
        pass

    def GetPath(self):
        # type: () -> str
        """
        返回当前控件的相对路径，路径从画布节点开始算起
        """
        return self.__path

    def GetChildByName(self, childName):
        # type: (str) -> 'BaseUIControl'
        """
        根据子控件的名称获取BaseUIControl实例
        """
        return BaseUIControl(self.__sn, self.__path + "/" + childName)

    def GetChildByPath(self, childPath):
        # type: (str) -> 'BaseUIControl'
        """
        根据相对路径获取BaseUIControl实例
        """
        return BaseUIControl(self.__sn, self.__path + childPath)

    def resetAnimation(self):
        # type: () -> None
        """
        重置该控件的动画
        """
        pass

    def PauseAnimation(self, propertyName='all'):
        # type: (str) -> bool
        """
        暂停动画，暂停后的动画会停在当前的状态
        """
        pass

    def PlayAnimation(self, propertyName='all'):
        # type: (str) -> bool
        """
        继续播放动画，从动画当前状态开始播放
        """
        pass

    def StopAnimation(self, propertyName='all'):
        # type: (str) -> bool
        """
        停止动画，动画将恢复到第一段动画片段的from状态
        """
        pass

    def SetAnimation(self, propertyName, namespace, animName, autoPlay=False):
        # type: (str, str, str, bool) -> bool
        """
        给单一属性设置动画，已有重复的会设置失败，需要先remove
        """
        pass

    def RemoveAnimation(self, propertyName):
        # type: (str) -> bool
        """
        删除单一属性的动画，删除后的值与当前状态有关，建议删除后重新设置该属性值
        """
        pass

    def SetAnimEndCallback(self, animName, func):
        # type: (str, Callable[[], Any]) -> bool
        """
        设置动画播放结束后的回调，每次设置都会覆盖上一次的设置
        """
        pass

    def RemoveAnimEndCallback(self, animName):
        # type: (str) -> bool
        """
        移除动画播放结束后的回调
        """
        pass

    def IsAnimEndCallbackRegistered(self, animName):
        # type: (str) -> bool
        """
        控件是否对名称为animName的动画进行了注册回调
        """
        return False

    def asLabel(self):
        # type: () -> Optional[LabelUIControl]
        """
        将当前BaseUIControl转换为LabelUIControl实例，如当前控件非Label类型则返回None
        """
        from mod.client.ui.controls.labelUIControl import LabelUIControl
        LabelUIControl(self.__sn, self.__path)

    def asButton(self):
        # type: () -> Optional[ButtonUIControl]
        """
        将当前BaseUIControl转换为ButtonUIControl实例，如当前控件非button类型则返回None
        """
        from mod.client.ui.controls.buttonUIControl import ButtonUIControl
        ButtonUIControl(self.__sn, self.__path)

    def asImage(self):
        # type: () -> Optional[ImageUIControl]
        """
        将当前BaseUIControl转换为ImageUIControl实例，如当前控件非image类型则返回None
        """
        from mod.client.ui.controls.imageUIControl import ImageUIControl
        ImageUIControl(self.__sn, self.__path)

    def asGrid(self):
        # type: () -> Optional[GridUIControl]
        """
        将当前BaseUIControl转换为GridUIControl实例，如当前控件非grid类型则返回None
        """
        from mod.client.ui.controls.gridUIControl import GridUIControl
        GridUIControl(self.__sn, self.__path)

    def asScrollView(self):
        # type: () -> Optional[ScrollViewUIControl]
        """
        将当前BaseUIControl转换为ScrollViewUIControl实例，如当前控件非scrollview类型则返回None
        """
        from mod.client.ui.controls.scrollViewUIControl import ScrollViewUIControl
        ScrollViewUIControl(self.__sn, self.__path)

    def asSwitchToggle(self):
        # type: () -> Optional[SwitchToggleUIControl]
        """
        将当前BaseUIControl转换为SwitchToggleUIControl实例，如当前控件非panel类型或非toggle则返回None
        """
        from mod.client.ui.controls.switchToggleUIControl import SwitchToggleUIControl
        SwitchToggleUIControl(self.__sn, self.__path)

    def asTextEditBox(self):
        # type: () -> Optional[TextEditBoxUIControl]
        """
        将当前BaseUIControl转换为TextEditBoxUIControl实例，如当前控件非editbox类型则返回None
        """
        from mod.client.ui.controls.textEditBoxUIControl import TextEditBoxUIControl
        TextEditBoxUIControl(self.__sn, self.__path)

    def asProgressBar(self, fillImagePath='/filled_progress_bar'):
        # type: (str) -> Optional[ProgressBarUIControl]
        """
        将当前BaseUIControl转换为ProgressBarUIControl实例，如当前控件非panel类型则返回None
        """
        from mod.client.ui.controls.progressBarUIControl import ProgressBarUIControl
        ProgressBarUIControl(self.__sn, self.__path)

    def asNeteasePaperDoll(self):
        # type: () -> Optional[NeteasePaperDollUIControl]
        """
        将当前BaseUIControl转换为NeteasePaperDollUIControl实例，如当前控件非custom类型则返回None
        """
        from mod.client.ui.controls.neteasePaperDollUIControl import NeteasePaperDollUIControl
        NeteasePaperDollUIControl(self.__sn, self.__path)

    def asMiniMap(self):
        # type: () -> Optional[MiniMapUIControl]
        """
        将当前BaseUIControl转换为MiniMapUIControl实例，如当前控件非小地图类型则返回None
        """
        from mod.client.ui.controls.minimapUIControl import MiniMapUIControl
        MiniMapUIControl(self.__sn, self.__path)

    def asSlider(self):
        # type: () -> Optional[SliderUIControl]
        """
        将当前BaseUIControl转换为SliderUIControl实例，如当前控件非滑动条类型则返回None
        """
        from mod.client.ui.controls.sliderUIControl import SliderUIControl
        SliderUIControl(self.__sn, self.__path)

    def asItemRenderer(self):
        # type: () -> Optional[ItemRendererUIControl]
        """
        将当前BaseUIControl转换为ItemRenderer实例，如当前控件非custom类型则返回None
        """
        from mod.client.ui.controls.itemRendererUIControl import ItemRendererUIControl
        ItemRendererUIControl(self.__sn, self.__path)

    def asNeteaseComboBox(self):
        # type: () -> Optional[NeteaseComboBoxUIControl]
        """
        将当前BaseUIControl转换为NeteaseComboBoxUIControl实例，如当前控件非panel类型则返回None
        """
        from mod.client.ui.controls.neteaseComboBoxUIControl import NeteaseComboBoxUIControl
        NeteaseComboBoxUIControl(self.__sn, self.__path)

    def asStackPanel(self):
        # type: () -> Optional[StackPanelUIControl]
        """
        将当前BaseUIControl转换为StackPanelUIControl实例，如当前控件非stackPanel类型则返回None
        """
        from mod.client.ui.controls.stackPanelUIControl import StackPanelUIControl
        StackPanelUIControl(self.__sn, self.__path)

    def asInputPanel(self):
        # type: () -> Optional[InputPanelUIControl]
        """
        将当前BaseUIControl转换为InputPanelUIControl实例，如当前控件非inputPanel类型则返回None
        """
        from mod.client.ui.controls.inputPanelUIControl import InputPanelUIControl
        InputPanelUIControl(self.__sn, self.__path)

    def asSelectionWheel(self):
        # type: () -> Optional[SelectionWheelUIControl]
        """
        将当前BaseUIControl转换为SelectionWheelUIControl实例，如当前控件非selectionWheel类型则返回None
        """
        from mod.client.ui.controls.selectionWheelUIControl import SelectionWheelUIControl
        SelectionWheelUIControl(self.__sn, self.__path)

    def GetPropertyBag(self):
        # type: () -> Dict[str, Any]
        """
        获取PropertyBag
        """
        return {}

    def SetPropertyBag(self, params):
        # type: (Dict[str, Any]) -> bool
        """
        设置PropertyBag,将使用字典中的每个值来覆盖原本PropertyBag中的值
        """
        pass

