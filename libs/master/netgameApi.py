# -*- coding: utf-8 -*-

"""这里是一些Master的基础API接口。
"""


def BanUser(uid, banTime, reason, bCombineReason):
	# type: (int/long, int, str, bool) -> bool
	"""
	封禁某个玩家

	Args:
		uid            int/long       玩家uid
		banTime        int            封禁时间，单位为秒，-1表示永封
		reason         str            封禁原因，使用utf8编码
		bCombineReason bool           是否组合显示封禁原因。若为True，则按备注说明处理，否则被封禁玩家登陆会提示【reason】

	Returns:
		bool           True设置成功，False表示失败。失败后请延迟一帧后重试
	"""
	pass


def GetBanUserInfo(uid, callback):
	# type: (int/long, function) -> None
	"""
	获取玩家的封禁信息

	Args:
		uid            int/long       玩家uid
		callback       function       回调函数，包含两个参数：第一个参数是uid；第二个参数是封禁信息，若获取失败，则为None，若没有被封禁则为“{}”，若被封禁，则为dict，解释参见备注

	"""
	pass


def GetCommonConfig():
	"""
	获取服务器公共配置，包括所有服务器和db的配置，具体参见备注

	Returns:
		dict           配置内容
	"""
	pass


def GetGameTypeByServerId(serverId):
	# type: (int) -> None或str
	"""
	获取指定ID服务器的类型

	Args:
		serverId       int            服务器ID

	Returns:
		None或str     指定ID的服务器的类型，没有符合条件的服务器时返回None
	"""
	pass


def GetOnlineUidList():
	"""
	获取所有在线玩家的uid列表

	Returns:
		list(int)      在线玩家的uid列表，当没有玩家在线时返回空列表
	"""
	pass


def GetProtocolVersionByUID(uid):
	# type: (int/long) -> None或者int
	"""
	获取在线玩家客户端协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中

	Args:
		uid            int/long       玩家的UID

	Returns:
		None或者int  玩家在线时，返回此玩家客户端协议版本号，玩家不在线时返回None
	"""
	pass


def GetServerIdByUid(uid):
	# type: (int/long) -> None或者int
	"""
	获取在线玩家所在的服务器的ID，返回的信息为当前控制服内存缓存中的信息，玩家很可能很快就离线或者转服

	Args:
		uid            int/long       需要获取的玩家的UID

	Returns:
		None或者int  玩家在线时，返回此玩家当前所在的服务器ID，玩家不在线时返回None
	"""
	pass


def GetServerIdsByGameType(gameType):
	# type: (str) -> list(int)
	"""
	获取指定类型的服务器id列表

	Args:
		gameType       str            服务器类型名

	Returns:
		list(int)      指定类型的服务器ID的列表，没有符合条件的服务器时返回空列表
	"""
	pass


def GetServerLoadedModsById(serverId):
	# type: (int) -> list(str)
	"""
	根据服务器id获取服务器加载mod列表

	Args:
		serverId       int            服务器id，id为0表示master

	Returns:
		list(str)      服务器mod列表
	"""
	pass


def GetServerLoadedModsByType(serverType):
	# type: (str) -> list(str)
	"""
	根据服务器类型获取服务器加载mod列表。若同种类型服务器配置了不同的mod，则返回其中一个对应mod列表。

	Args:
		serverType     str            服务器类型

	Returns:
		list(str)      服务器mod列表
	"""
	pass


def GetUserSilentInfo(uid, callback):
	# type: (int/long, function) -> None
	"""
	获取玩家的禁言信息

	Args:
		uid            int/long       玩家uid
		callback       function       回调函数，包含两个参数：第一个参数是uid；第二个参数是禁言信息，若获取失败，则为None，若没有被禁言则为“{}”，若被禁言，则为dict，解释如下：

	"""
	pass


def IsService(serverId):
	# type: (int) -> bool
	"""
	服务器是否是service服

	Args:
		serverId       int            服务器id

	Returns:
		bool           True表示是service，False不是service
	"""
	pass


def SetLoginStratege(func):
	# type: (function) -> bool
	"""
	设置玩家登陆选服策略，要求服务器启动后加载mod时候设置

	Args:
		func           function       计算玩家登陆服务器，包含两个参数：第一个参数为玩家uid；第二个参数为回调函数，执行后续登陆逻辑，无论登陆是否成功，必须要执行，回调函数只有一个参数，也即目标服务器。

	Returns:
		bool           True设置成功，False表示失败。失败后请延迟一帧后重试
	"""
	pass


def SilentByUID(uid, banTime, reason):
	# type: (int/long, int, str) -> bool
	"""
	禁言某个玩家

	Args:
		uid            int/long       玩家uid
		banTime        int            禁言时间，单位为秒，-1表示永封
		reason         str            禁言原因，使用utf8编码

	Returns:
		bool           True设置成功，False表示失败。失败后请延迟一帧后重试
	"""
	pass


def UnBanUser(uid):
	# type: (int/long) -> bool
	"""
	解除某个玩家的封禁

	Args:
		uid            int/long       玩家uid

	Returns:
		bool           True设置成功，False表示失败。失败后请延迟一帧后重试
	"""
	pass


def UnSilentByUID(uid):
	# type: (int/long) -> bool
	"""
	解除某个玩家的禁言

	Args:
		uid            int/long       玩家uid

	Returns:
		bool           True设置成功，False表示失败。失败后请延迟一帧后重试
	"""
	pass

