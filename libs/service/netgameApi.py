# -*- coding: utf-8 -*-

"""这里是Service的一些接口
"""


def GetCommonConfig():
	"""
	获取服务器公共配置，包括所有服务器和db的配置，具体参见备注

	Returns:
		dict           配置内容
	"""
	pass


def GetServerId():
	"""
	获取服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注

	Returns:
		int            服务器id
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


def GetServiceConfig():
	"""
	获取service配置，该配置对应公共配置中servicelist下对应service的配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注

	Returns:
		dict           配置内容
	"""
	pass


def RegisterOpCommand(url, callback):
	# type: (str, function) -> None
	"""
	注册一个新的HTTP接口

	Args:
		url            str            接口url
		callback       function       响应HTTP请求的实例函数，参数有两个，第一个参数clientId，类型为int，是请求方的唯一标识，用于返回请求处理结果；第二个参数requestData，类型为dict，包含HTTP请求的参数（requestBody）

	"""
	pass


def ResponseOpCommandFail(clientId, code, message):
	# type: (int, int, str) -> None
	"""
	发送HTTP的失败Response，支持异步返回，返回时候指定请求传入的clientId

	Args:
		clientId       int            请求唯一id，识别HTTP请求。
		code           int            请求的失败原因code
		message        str            请求的失败原因的文本

	"""
	pass


def ResponseOpCommandSuccess(clientId, entity):
	# type: (int, dict) -> None
	"""
	发送HTTP的成功Response，支持异步返回，返回时候指定请求传入的clientId

	Args:
		clientId       int            请求唯一id，识别HTTP请求。
		entity         dict           请求中需要返回的内容，可自定义key/value的含义

	"""
	pass


def StartRecordEvent():
	"""
	开始启动大厅服/游戏服与功能服之间的脚本事件收发包统计，启动后调用[StopRecordEvent()](#StopRecordEvent)即可获取两个函数调用之间引擎收发包的统计信息

	Returns:
		bool           执行结果
	"""
	pass


def StopRecordEvent():
	"""
	停止大厅服/游戏服与功能服之间的脚本事件收发包统计并输出结果，与[StartRecordEvent()](#StartRecordEvent)配合使用，输出结果为字典，具体见示例

	Returns:
		dict           收发包信息，具体见示例，假如没有调用过StartRecordEvent，则返回为None
	"""
	pass


def UnRegisterOpCommand(url):
	# type: (str) -> None
	"""
	注销一个已注册的HTTP接口

	Args:
		url            str            接口url

	"""
	pass

