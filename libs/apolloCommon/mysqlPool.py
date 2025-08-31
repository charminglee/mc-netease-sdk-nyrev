# -*- coding: utf-8 -*-

"""下面是mysql线程池的接口
"""


def AsyncExecuteFunctionWithOrderKey(func, orderKey, callback, *args, **kwargs):
	# type: (function, str/int, function, *args, **kwargs) -> None
	"""
	添加一个异步mysql任务，func将在子线程中执行，注意func中不支持执行引擎提供的API

	Args:
		func           function       mysql异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mysql长连接，可以通过conn.cursor()获取cursor
		orderKey       str/int        相同的orderKey会顺序执行，不同的orderKey会并行执行
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None
		*args          *args          func的其它非关键字参数
		**kwargs       **kwargs       暂无用，预留用。

	"""
	pass


def AsyncExecuteWithOrderKey(orderKey, sql, params, callback):
	# type: (str/int, str, tuple, function) -> None
	"""
	添加一个异步mysql任务，执行所有mysql操作

	Args:
		orderKey       str/int        相同的orderKey会顺序执行，不同的orderKey会并行执行
		sql            str            mysql查询语句，格式化字符串
		params         tuple          填充sql
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def AsyncExecutemanyWithOrderKey(orderKey, sql, paramsList, callback):
	# type: (string/int, string, list, function) -> None
	"""
	添加一个异步mysql任务，针对同一条sql语句，使用paramsList中的每个参数各执行一次，并且返回成功修改/新建的记录数，其中任何一条语句执行失败，最终所有语句都会被执行失败，返回None

	Args:
		orderKey       string/int     相同的orderKey会顺序执行，不同的orderKey会并行执行
		sql            string         mysql插入语句，格式化字符串
		list           list           填充sql的参数列表，每个元素都会被执行一次
		callback       function       回调函数，在主线程执行，只有唯一一个参数，成功修改/新建的记录数，假如sql执行失败，返回参数将会是None。若没有回调，则传入None

	"""
	pass


def AsyncInsertOneWithOrderKey(orderKey, sql, params, callback):
	# type: (string/int, string, tuple, function) -> None
	"""
	添加一个异步mysql任务，向主键为AUTO INCREASEl类型的表格中插入一条记录，并且返回新建记录的主键

	Args:
		orderKey       string/int     相同的orderKey会顺序执行，不同的orderKey会并行执行
		sql            string         mysql插入语句，格式化字符串
		params         tuple          填充sql
		callback       function       回调函数，在主线程执行，只有唯一一个参数，是新建记录的主键，假如sql执行失败，返回参数将会是None。若没有回调，则传入None

	"""
	pass


def AsyncQueryWithOrderKey(orderKey, sql, params, callback):
	# type: (str/int, str, tuple, function) -> None
	"""
	添加一个异步mysql任务，执行mysql查询

	Args:
		orderKey       str/int        相同的orderKey会顺序执行，不同的orderKey会并行执行
		sql            str            mysql查询语句，格式化字符串
		params         tuple          填充sql
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def Finish():
	"""
	等待mysql线程池退出，会等待线程池中所有异步任务执行完毕后退出

	"""
	pass


def InitDB(poolSize):
	# type: (int) -> None
	"""
	初始化myqsl连接池，要求在MCStudio的“服务器配置”中配置mysql

	Args:
		poolSize       int            连接池大小

	"""
	pass


def SyncFetchAll(sql, params):
	# type: (string, tuple) -> None/list
	"""
	阻塞性执行sql语句，查询数据

	Args:
		sql            string         mysql查询语句，格式化字符串
		params         tuple          填充sql

	Returns:
		None/list      错误返回None，否则返回列表，列表中每个元素表示一条查询记录
	"""
	pass


def SyncInsert(sql, params):
	# type: (string, tuple) -> None/id
	"""
	阻塞性执行sql语句，插入数据

	Args:
		sql            string         mysql查询语句，格式化字符串
		params         tuple          填充sql

	Returns:
		None/id        错误返回None，否则返回成功插入的id
	"""
	pass

