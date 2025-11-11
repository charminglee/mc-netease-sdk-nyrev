# -*- coding: utf-8 -*-


from typing import Tuple, Optional


class TextBoardComponentClient(object):
    def SetText(self, boardId, text):
        # type: (int, str) -> bool
        """
        修改文字面板内容
        """
        pass

    def SetBoardDepthTest(self, boardId, depthTest):
        # type: (int, bool) -> bool
        """
        设置是否开启深度测试, 默认状态下是开启
        """
        pass

    def SetBoardScale(self, boardId, scale):
        # type: (int, Tuple[float, float]) -> bool
        """
        内容整体缩放
        """
        pass

    def SetBoardBackgroundColor(self, boardId, backgroundColor):
        # type: (int, Tuple[float, float, float, float]) -> bool
        """
        修改背景颜色
        """
        pass

    def SetBoardPos(self, boardId, pos):
        # type: (int, Tuple[float, float, float]) -> bool
        """
        修改位置
        """
        pass

    def SetBoardRot(self, boardId, rot):
        # type: (int, Tuple[float, float, float]) -> bool
        """
        修改旋转角度, 若设置了文本朝向相机，则旋转角度的修改不会生效
        """
        pass

    def SetBoardTextColor(self, boardId, textColor):
        # type: (int, Tuple[float, float, float, float]) -> bool
        """
        修改字体颜色
        """
        pass

    def SetBoardBindEntity(self, boardId, bindEntityId, offset, rot):
        # type: (int, str, Tuple[float, float, float], Tuple[float, float, float]) -> bool
        """
        文字面板绑定实体对象
        """
        pass

    def SetBoardFaceCamera(self, boardId, faceCamera):
        # type: (int, bool) -> bool
        """
        设置文字面板的朝向
        """
        pass

    def CreateTextBoardInWorld(self, text, textColor, boardColor=None, faceCamera=True):
        # type: (str, Tuple[float, float, float, float], Optional[Tuple[float, float, float, float]], bool) -> int
        """
        创建文字面板
        """
        pass

    def RemoveTextBoard(self, boardId):
        # type: (int) -> bool
        """
        删除文字面板
        """
        pass

