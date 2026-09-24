# -*- coding: utf-8 -*-


from typing import Any, Callable, Dict
from mod.common.component.baseComponent import BaseComponent


class LobbyGameCompServer(BaseComponent):
    def GetRoomInfo(self):
        # type: () -> Dict[str, str | int] | None
        """
        获取当前所在联机大厅的房间信息，非联机大厅时返回None
        """
        pass

    def KickPlayer(self, playerId, message=None):
        # type: (str, str | None) -> bool
        """
        踢出玩家，可传入自定义提示信息在客户端断线提示中展示，非联机大厅时返回False
        """
        pass

    def KickPlayerByUid(self, uid, message=None):
        # type: (int, str | None) -> bool
        """
        通过uid踢出玩家，可传入自定义提示信息。
        """
        pass

    def GetHostPlayerUid(self):
        # type: () -> int
        """
        获取当前联机大厅房主的uid，非联机大厅时返回空字符串
        """
        pass

    def TransferRoomHost(self, playerId):
        # type: (str) -> bool
        """
        将联机大厅房主转移给指定在线玩家。仅联机大厅可用，且目标玩家必须在线。
        """
        pass

    def TransferRoomHostByUid(self, playerUid):
        # type: (str) -> bool
        """
        通过uid将联机大厅房主转移给指定在线玩家。仅联机大厅可用，且目标玩家必须在线。
        """
        pass

    def SetRoomMeta(self, key, value):
        # type: (str, Any) -> bool
        """
        设置当前联机大厅房间的元数据，房间关闭时清除数据。非联机大厅返回False
        """
        pass

    def GetRoomMeta(self, callback, roomId):
        # type: (Callable[[dict | None], Any], int) -> bool
        """
        异步获取指定房间的所有元数据。非联机大厅时返回False
        """
        pass

    def GetPlayerRoomId(self, callback, uid):
        # type: (Callable[[int | None], Any], int) -> bool
        """
        异步获取uid对应的玩家所在的房间id，非联机大厅时回调返回None
        """
        pass

