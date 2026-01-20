# -*- coding: utf-8 -*-


from typing import List, Callable, Any
from collections import OrderedDict
from mod.client.ui.screenNode import ScreenNode


class RichTextItem(object):
    def __init__(self, screenNode, parentPath):
        # type: (ScreenNode, str) -> None
        self.screenNode = screenNode            # type: ScreenNode
        self.RichTextPanelPath = parentPath     # type: str
        self.RichTextItemPath = ""              # type: str
        self.CalculateText = ""                 # type: str
        self.CalculateLabel = ""                # type: str
        self.RichTextBGPath = ""                # type: str
        self.RichTextRowPrefab = ""             # type: str
        self.canHandleType = []                 # type: List[str]
        self.curRowPathToItem = OrderedDict()   # type: OrderedDict
        self.curRowItem = None
        self.pathToData = {}                    # type: dict
        self.OnButtonItemClickCallback = None   # type: Callable[[dict, float, float], Any] | None
        self.OnLinkItemClickCallback = None     # type: Callable[[dict, float, float], Any] | None
        self.OnRichTextCreateFinish = None      # type: Callable[[], Any] | None
        self.isCreateFinish = True              # type: bool
        self.curRichText = None
        self.curStartIndex = 0                  # type: int
        self.WideMark = ""                      # type: unicode

    def readRichText(self, richText):
        # type: (str) -> None
        """
        创建富文本入口，接受一个符合格式的字符串，将其转变为富文本显示出来。
        """
        pass

    def clearRichText(self):
        # type: () -> None
        pass

    def registerLinkItemClickCallback(self, callback):
        # type: (Callable[[dict, float, float], Any]) -> None
        """
        注册点击超链接回调函数，参数为一个函数引用。超链接点击触发时会返回开发者给超链接设置的数据，以及当前点击屏幕的坐标值touchX和touchY
        """
        pass

    def registerButtonItemClickCallback(self, callback):
        # type: (Callable[[dict, float, float], Any]) -> None
        """
        注册点击按钮回调函数，参数为一个函数引用。按钮点击触发时会返回开发者给按钮设置的数据，以及当前点击屏幕的坐标值touchX和touchY
        """
        pass

    def registerRichTextFinishCallback(self, callback):
        # type: (Callable[[], Any]) -> None
        """
        注册富文本创建完毕回调函数，由于富文本构成较为复杂，无法在一帧之内生成完毕，因此生成需要一点点时间，等富文本创建完毕后会调用该回调函数。
        """
        self.OnRichTextCreateFinish = callback
