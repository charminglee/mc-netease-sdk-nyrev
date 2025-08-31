# -*- coding: utf-8 -*-

from mod.common.utils.timer import CallLater
from typing import Any
from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class GameComponentClient(BaseComponent):
    def ShowHealthBar(self, show):
        # type: (bool) -> 'bool'
        """
        设置是否显示血条
        """
        pass

    def SetNameDeeptest(self, deeptest):
        # type: (bool) -> 'bool'
        """
        设置名字是否透视
        """
        pass

    def GetScreenSize(self):
        # type: () -> 'Tuple[float,float]'
        """
        获取游戏分辨率
        """
        pass

    def SetRenderLocalPlayer(self, render):
        # type: (bool) -> 'bool'
        """
        设置本地玩家是否渲染
        """
        pass

    def AddPickBlacklist(self, entityId):
        # type: (str) -> 'bool'
        """
        添加使用camera组件（例如GetChosen接口、PickFacing接口）选取实体时的黑名单，即该实体不会被选取到
        """
        pass

    def ClearPickBlacklist(self):
        # type: () -> 'bool'
        """
        清除使用camera组件（例如GetChosen接口、PickFacing接口）选取实体的黑名单
        """
        pass

    def HasEntity(self, entityId):
        # type: (str) -> 'int'
        """
        判断 entity 是否存在
        """
        pass

    def IsEntityAlive(self, entityId):
        # type: (str) -> 'bool'
        """
        判断生物实体是否存活或非生物实体是否存在
        """
        pass

    def CheckWordsValid(self, words):
        # type: (str) -> 'bool'
        """
        检查语句是否合法，即不包含敏感词
        """
        pass

    def GetFps(self):
        # type: () -> 'float'
        """
        获取fps
        """
        pass

    def CheckNameValid(self, name):
        # type: (str) -> 'bool'
        """
        检查昵称是否合法，即不包含敏感词
        """
        pass

    def GetScreenViewInfo(self):
        # type: () -> 'Tuple[float,float,float,float]'
        """
        获取游戏视角信息。首先获得当前分辨率下UI放大倍数，计算方式可参考<a href="../../../mcguide/18-界面与交互/1-界面编辑器使用说明.html#《我的世界》界面适配方法">《我的世界》界面适配方法</a>。则当前游戏视角的宽度的计算方式为：若当前分辨率的宽度能被该放大倍数整除，则等于当前分辨率，若不能，则等于当前分辨率加放大倍数再减去当前分辨率对放大倍数求余的结果，当前游戏视角的高度计算方法类似。例：以分辨率为1792，828的手机计算，画布是分辨率的3倍，所以x = 1792 + 3 - 1 = 1794；y = 828，该接口返回的结果为(1794.0, 828.0, 0.0, 0.0)
        """
        pass

    def SetPopupNotice(self, message, subtitle):
        # type: (str, str) -> 'bool'
        """
        在本地玩家的物品栏上方弹出popup类型通知，位置位于tip类型消息下方
        """
        pass

    def SetPopupState(self, state):
        # type: (int) -> 'bool'
        """
        设置Popup消息栏状态
        """
        pass

    def SetTipMessage(self, message):
        # type: (str) -> 'bool'
        """
        在本地玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方
        """
        pass

    def AddTimer(self, delay, func, *args, **kwargs):
        # type: (float, function, Any, Any) -> 'CallLater'
        """
        添加客户端触发的定时器，非重复
        """
        pass

    def AddRepeatedTimer(self, delay, func, *args, **kwargs):
        # type: (float, function, Any, Any) -> 'CallLater'
        """
        添加客户端触发的定时器，重复执行
        """
        pass

    def CancelTimer(self, timer):
        # type: (CallLater) -> 'None'
        """
        取消定时器
        """
        pass

    def SimulateTouchWithMouse(self, touch):
        # type: (bool) -> 'bool'
        """
        模拟使用鼠标控制UI（PC F11快捷键）
        """
        pass

    def GetCurrentDimension(self):
        # type: () -> 'int'
        """
        获取客户端当前维度
        """
        pass

    def GetChinese(self, langStr):
        # type: (str) -> 'str'
        """
        获取langStr对应的中文，可参考PC开发包中\handheld\localization\handheld\data\resource_packs\vanilla\texts\zh_CN.lang
        """
        pass

    def SetEmoteSwitch(self, flag):
        # type: (bool) -> 'bool'
        """
        设置是否开启表情功能，默认PC端关闭，手机端开启，且该接口只能在手机端使用，在原生UI初始化前调用设置
        """
        pass

    def GetPlayerGameType(self, playerId):
        # type: (str) -> 'int'
        """
        获取指定玩家的游戏模式
        """
        pass

    def GetPlayerExp(self, playerId, isPercent=True):
        # type: (str, bool) -> 'float'
        """
        获取玩家当前等级下的经验值
        """
        pass

    def GetPlayerCurLevelExp(self, playerId):
        # type: (str) -> 'int'
        """
        获取玩家当前等级需要的经验值
        """
        pass

    def GetPlayerTotalExp(self, playerId):
        # type: (str) -> 'int'
        """
        获取玩家的总经验值
        """
        pass

    def GetCurrentAirSupply(self, entityId):
        # type: (str) -> 'int'
        """
        玩家当前氧气储备值
        """
        pass

    def GetMaxAirSupply(self, entityId):
        # type: (str) -> 'int'
        """
        玩家最大氧气储备值
        """
        pass

    def GetRiderId(self, playerId):
        # type: (str) -> 'str'
        """
        获取玩家坐骑entityid
        """
        pass

    def GetArmorValue(self, playerId):
        # type: (str) -> 'int'
        """
        获取玩家护甲值
        """
        pass

    def GetEntitiesAround(self, entityId, radius, filters):
        # type: (str, int, dict) -> 'List[str]'
        """
        获取区域内的entity列表
        """
        pass

    def GetEntitiesInSquareArea(self, entityId, startPos, endPos):
        # type: (None, Tuple[int,int,int], Tuple[int,int,int]) -> 'List[str]'
        """
        获取区域内的entity列表
        """
        pass

    def GetEntitiesAroundByType(self, entityId, radius, entityType):
        # type: (str, int, int) -> 'List[str]'
        """
        获取区域内的某类型的entity列表
        """
        pass

    def GetAllScoreboardObjects(self):
        # type: () -> 'List[dict]'
        """
        获取所有记分板项
        """
        pass

    def GetAllPlayerScoreboardObjects(self):
        # type: () -> 'List[dict]'
        """
        获取玩家记分项
        """
        pass

    def EnableFontBatchRender(self, enable):
        # type: (bool) -> 'None'
        """
        是否开启字体合批
        """
        pass

    def CanSee(self, fromId, targetId, viewRange=8.0, onlySolid=True, angleX=180.0, angleY=180.0):
        # type: (str, str, float, bool, float, float) -> 'bool'
        """
        判断起始对象是否可看见目标对象,基于对象的Head位置判断
        """
        pass

    def GetPistonMaxInteractionCount(self):
        # type: () -> 'int'
        """
        获取活塞/粘性活塞最多推动的方块数量，默认为12个方块，可能被其他开发者修改。
        """
        pass

    def SetClipboardContent(self, content):
        # type: (str) -> 'bool'
        """
        设置系统剪贴板内容
        """
        pass

    def GetClipboardContent(self):
        # type: () -> 'str'
        """
        获取系统剪贴板内容
        """
        pass

    def IsOfficialSkin(self, playerId):
        # type: (str) -> 'bool'
        """
        获取玩家穿戴的皮肤是否为官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId
        """
        pass

    def IsHighLevelOfficialSkin(self, playerId):
        # type: (str) -> 'bool'
        """
        获取玩家穿戴的皮肤是否为史诗及以上的官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId
        """
        pass

    def IsHighLevelMultiJointOfficialSkin(self, playerId):
        # type: (str) -> 'bool'
        """
        获取玩家穿戴的皮肤是否为史诗及以上的多关节官方4d皮肤 在接收到 UpdatePlayerSkinClientEvent 事件后调用 此事件在客户端接收到玩家皮肤信息同步后触发 参数仅playerId
        """
        pass

