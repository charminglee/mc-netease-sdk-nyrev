# -*- coding: utf-8 -*-

"""下面是mysql扩展线程池的一些接口
"""


def AsyncExecuteWithOrderKey(dbName, orderKey, sql, params, callback):
	# type: (string, string/int, string, tuple, function) -> None
	"""
	添加一个异步mysql任务，执行所有mysql操作。同AsyncExecute的区别是可以显示指定orderKey

	Args:
		dbName         string         mysql db名字，名字在deploy.json中extra_mysql下配置，具体参见[InitDB](#InitDB)备注说明
		orderKey       string/int     相同的orderKey会顺序执行，不同的orderKey会并行执行
		sql            string         mysql查询语句，格式化字符串
		params         tuple          填充sql
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def AsyncQueryWithOrderKey(dbName, orderKey, sql, params, callback):
	# type: (string, string/int, string, tuple, function) -> None
	"""
	添加一个异步mysql任务，执行mysql查询。同AsyncQuery区别是可以显示指定orderKey

	Args:
		dbName         string         mysql db名字，名字在deploy.json中extra_mysql下配置，具体参见[InitDB](#InitDB)备注说明
		orderKey       string/int     相同的orderKey会顺序执行，不同的orderKey会并行执行
		sql            string         mysql查询语句，格式化字符串
		params         tuple          填充sql
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None

	"""
	pass


def Finish():
	"""
	等待mysql线程池退出，会等待线程池中所有异步任务执行完毕后退出

	"""
	pass


def InitDB(dbName, poolSize):
	# type: (string, int) -> None
	"""
	初始化mysql连接池。可以支持多个mysql实例，它可以同“mysql连接池”一起使用。MCStudio打开配置文件目录，在deploy.json文件中配置extra_mysql，配置方法参见备注

	Args:
		dbName         string         mysql db名字，名字在deploy.json中extra_mysql下配置，比如示例配置中 “mysql_test1”
		poolSize       int            连接池大小

	"""
	pass

