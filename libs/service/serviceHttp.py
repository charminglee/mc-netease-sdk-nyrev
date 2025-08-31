# -*- coding: utf-8 -*-

"""这里是service的一些HTTP接口
"""


def RegisterServiceHttp(url, binder, func):
	# type: (string, instance, function) -> None
	"""
	注册一个新的HTTP接口

	Args:
		url            string         接口url
		binder         instance       响应HTTP请求的实例
		func           function       响应HTTP请求的实例函数

	"""
	pass


def SendHttpRequestToMaster(requestUrl, body):
	# type: (string, string) -> None
	"""
	给master发送http请求

	Args:
		requestUrl     string         请求url，例如“/test-reqeust”
		message        string         HTTP post body，是个json字符串

	"""
	pass


def SendHttpResponse(clientId, message):
	# type: (int, string) -> None
	"""
	发送HTTP的Response。支持异步返回，返回时指定输入clientId

	Args:
		clientId       int            请求唯一id，识别HTTP请求
		message        string         HTTP Response的内容

	"""
	pass

