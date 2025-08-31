# -*- coding: utf-8 -*-

"""
事件的定义。
"""

class ServerEvent:
		"""
		服务器配置发生变化时触发，具体包括：新增或删服服务器；服务器相关配置变化；日志等级发生变化

		"""
		NetGameCommonConfChangeEvent = "NetGameCommonConfChangeEvent"

		"""
		lobby/game/proxy成功建立连接时触发

		Event Function Args:
			serverId       int            服务器id
			protocolVersionint            协议版本号

		"""
		ServerConnectedEvent = "ServerConnectedEvent"

		"""
		lobby/game/proxy断开连接时触发

		Event Function Args:
			serverId       int            服务器id

		"""
		ServerDisconnectEvent = "ServerDisconnectEvent"

		"""
		lobby/game/proxy状态发生变化时触发

		Event Function Args:
			dict类型，key：str，服务器id的字符串，value：str，服务器状态字符串。服务器状态如下：‘1’就绪状态，‘2’停止状态，‘3’ 准备状态。服务器状态为'1'时，服务器才可用，其他状态下，服务器不可用。

		"""
		UpdateServerStatusEvent = "UpdateServerStatusEvent"

