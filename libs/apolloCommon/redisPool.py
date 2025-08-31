# -*- coding: utf-8 -*-

"""下面是redis线程池的接口
"""


def AsyncDelete(key, callback):
	# type: (string, function) -> None
	"""
	执行redis操作，删除某个redis key,相当于redis中执行命令:del key

	Args:
		key            string         redis中的key
		callback       function       回调函数，输入参数是redis操作返回值,是个int，表示删除redis key的个数 ,它在主线程执行。可以不传入回调函数。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def AsyncFuncWithKey(func, orderKey, callback, *args, **kwargs):
	# type: (function, str/int, function, *args, **kwargs) -> None
	"""
	添加一个异步redis任务

	Args:
		func           function       redis异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个redis长连接，是一个redis.StrictRedis实例，其他参数是*args
		orderKey       str/int        相同的orderKey会顺序执行，不同的orderKey会并行执行
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值是callback的输入参数。若func抛出异常，则callback输入参数是None。若没有回调，则传入None
		*args          *args          func的其它非关键字参数
		**kwargs       **kwargs       暂无用，预留用。

	"""
	pass


def AsyncGet(key, callback):
	# type: (str, function) -> None
	"""
	执行redis操作，获取key的value,相当于redis中执行命令:get key

	Args:
		key            str            redis中的key
		callback       function       回调函数，默认为空。函数输入参数是redis key对应的value字符串，它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def AsyncHgetall(key, callback):
	# type: (string, function) -> None
	"""
	执行redis操作，获取key的value,相当于redis中执行命令:hgetall key

	Args:
		key            string         redis中的key
		callback       function       回调函数，输入参数是redis key对应的值，是个dict，它在主线程执行。可以不传入回调函数。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def AsyncMget(keys, callback):
	# type: (list/tuple, function) -> None
	"""
	执行redis操作，获取多个key的值,相当于redis中执行命令:mget key1 key2 ...

	Args:
		key            list/tuple     多个redis中的key
		callback       function       回调函数，默认为空。函数输入参数redis操作返回值, 是个列表，每个元素对应单个redis key的值，它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def AsyncSet(key, value, callback):
	# type: (string, string, function) -> None
	"""
	执行redis操作，设置key的值为value,相当于redis中执行命令:set key value

	Args:
		key            string         redis中的key
		value          string         redis中key的值
		callback       function       回调函数，默认为空。函数输入参数是redis操作返回值，True表示设置成功，False失败。 若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def Finish():
	"""
	等待redis线程池退出，会等待线程池中所有异步任务执行完毕后退出

	"""
	pass


def InitDB(poolSize):
	# type: (int) -> None
	"""
	初始化redis连接池，要求在MCStudio的“服务器配置”中配置redis

	Args:
		poolSize       int            连接池大小

	"""
	pass

