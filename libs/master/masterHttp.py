# -*- coding: utf-8 -*-

"""这里是Master的Http接口
"""


def RegisterMasterHttp(url, binder, func):
	# type: (str, instance, function) -> None
	"""
	注册一个新的HTTP接口

	Args:
		url            str            接口url
		binder         instance       响应HTTP请求的实例
		func           function       响应HTTP请求的实例函数

	"""
	pass


def SendHttpRequestToService(serverId, requestUrl, body):
	# type: (int, str, str) -> None
	"""
	给service发送http请求

	Args:
		serverId       int            service的服务器id
		requestUrl     str            请求url，例如“/test-reqeust”
		body           str            HTTP post body，是个json字符串

	"""
	pass


def SendHttpResponse(clientId, message):
	# type: (int, str) -> None
	"""
	发送HTTP的Response，支持异步返回，返回时候指定请求传入的clientId

	Args:
		clientId       int            请求唯一id，识别HTTP请求。
		message        str            HTTP Response的内容

	"""
	pass

