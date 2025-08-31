# -*- coding: utf-8 -*-

"""这里是service的一些服务的管理接口
"""


def GetServerIdsByServerType(serverType):
	# type: (str) -> list(int)
	"""
	根据类型获取服务器id列表

	Args:
		serverType     str            服务器类型

	Returns:
		list(int)      服务器id列表，若服务器类型不存在，则返回空列表
	"""
	pass


def GetServerProtocolVersion(serverId):
	# type: (int) -> int
	"""
	获取服务器的协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中

	Args:
		serverId       int            lobby/game服务器id

	Returns:
		int            协议版本
	"""
	pass


def GetServerType(serverId):
	# type: (int) -> str
	"""
	获取服务器类型

	Args:
		serverId       int            master/service/lobby/game服务器id

	Returns:
		str            服务器类型字符串。若服务器不存在，则返回空字符串
	"""
	pass


def GetServersStatus():
	"""
	获取所有lobby/game服务器的状态。只有状态1表示服务器正常服务，其他状态表示服务器不能对外服务

	Returns:
		dict           key:int, 服务器id，value:int 服务器状态。服务器状态如下：<br/>1:正常状态<br/>2:正在滚动更新关闭状态，服务器马上会下架 <br/>3:滚动更新新增服务器状态，服务器就绪后会转化为状态1 <br/>4:服务器已上架，但是未同service建立连接状态（可能是服务器崩溃或被重置或关服等原因导致），建立连接后会转换为状态1
	"""
	pass


def IsConnectedServer(serverId):
	# type: (int) -> bool
	"""
	service是否与lobby/game/proxy建立连接

	Args:
		serverId       int            服务器id

	Returns:
		bool           True，已经建立连接;False未建立连接
	"""
	pass


def ResetServer(serverId):
	# type: (int) -> None
	"""
	重置服务器

	Args:
		serverId       int            lobby/game的服务器id

	"""
	pass

