# -*- coding: utf-8 -*-

"""下面是异步任务池的接口
"""


def ForkNewPool(orderSize):
	# type: (int) -> MainPool
	"""
	创建线程池，设置线程池大小

	Args:
		orderSize      int            线程池的大小

	Returns:
		MainPool       线程池实例
	"""
	pass


class MainPool(object):


	def EmitOrder(self, key, func, callback, *args):
		# type: (string/int, function, function, *args) -> None
		"""
		添加一个异步任务

		Args:
			key            string/int     相同key的任务，线程池顺序执行；不同key的任务，线程池会并行执行。可以确认某些任务按照顺序执行。
			func           function       任务对应的函数，该函数会在线程池中运行。该任务和主线程会并行执行，需要确认任务是线程安全的。函数必须返回一个元组，若返回为空则要求返回空元组("()")。函数输入参数是*args
			callback       function       回调函数，它在主线程执行。func的返回值会是callback的实参。若没有回调，则传入None。
			*args          *args          func函数的非关键字参数

		"""
		pass


	def Finish(self, timeout):
		# type: (int) -> None
		"""
		等待线程池退出，线程池会执行完所有异步任务后退出，会阻塞主线程。建议Mod退出时执行

		Args:
			timeout        int            等待线程池退出时间，单位秒。若为None，则会一直等待。建议用None。

		"""
		pass

