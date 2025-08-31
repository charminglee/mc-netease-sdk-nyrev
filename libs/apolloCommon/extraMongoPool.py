# -*- coding: utf-8 -*-

"""下面是mongo扩展线程池的一些接口
"""


def AsyncExecute(dbName, collection, func, callback, *args, **kwargs):
	# type: (str, str, function, function, *args, **kwargs) -> None
	"""
	添加一个异步mongo任务

	Args:
		dbName         str            mongo db名字，名字在deploy.json中extra_mongo下配置，具体参见[InitDB](#InitDB)备注说明
		collection     str            mongo中的一个集合，相同集合的所有操作串行执行，不同集合操作并行执行
		func           function       mongo异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mongo长连接，是pymongo.MongoClient连接池实例中的一个连接
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None
		*args          *args          func的非关键字参数
		**kwargs       **kwargs       暂无用，预留用

	"""
	pass


def AsyncExecuteWithOrderKey(dbName, collection, func, orderKey, callback, *args, **kwargs):
	# type: (str, str, function, str/int, function, *args, **kwargs) -> None
	"""
	添加一个异步mongo任务。同async_execute区别是，可以显示设置orderKey

	Args:
		dbName         str            mongo db名字，名字在deploy.json中extra_mongo下配置，具体参见[InitDB](#InitDB)备注说明
		collection     str            mongo中的一个集合
		func           function       mongo异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mongo长连接，是pymongo.MongoClient连接池实例中的一个连接，其他参数是*args
		orderKey       str/int        相同的orderKey会顺序执行，不同的orderKey会并行执行
		callback       function       回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None
		*args          *args          func的非关键字参数
		**kwargs       **kwargs       暂无用，预留

	"""
	pass


def Finish():
	"""
	等待mongo线程池退出，会等待线程池中所有异步任务执行完毕后退出

	"""
	pass


def InitDB(dbName, poolSize):
	# type: (str, int) -> None
	"""
	初始化mongo连接池。可以支持多个mongo实例，它可以同“mongo连接池”一起使用。MCStudio打开配置文件目录，在deploy.json文件中配置extra_mongo，配置方法参见备注

	Args:
		dbName         str            mongo db名字，名字在deploy.json中extra_mongo下配置，比如示例配置中 “mongo_test1”
		poolSize       int            连接池大小

	"""
	pass

