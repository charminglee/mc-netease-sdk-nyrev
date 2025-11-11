# -*- coding: utf-8 -*-


from typing import List


class NativeScreenManager(object):
	def __init__(self):
		pass

	def RegisterCustomControl(self, nativeData, customControlName, proxyClassName):
		# type: (List[str, str], str, str) -> bool
		pass

	def UnRegisterCustomControl(self, nativeData, customControlName):
		# type: (List[str, str], str) -> None
		pass

	def RegisterScreenProxy(self, screenName, proxyClassName):
		# type: (str, str) -> bool
		pass

	def UnRegisterScreenProxy(self, screenName, proxyClassName):
		# type: (str, str) -> None
		pass


def instance():
	# type: () -> NativeScreenManager
	pass
