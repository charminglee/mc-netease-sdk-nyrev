# -*- coding: utf-8 -*-


if 0:
	from .screenNode import ScreenNode


class CustomUIScreenProxy(object):
	def __init__(self, screenName, screenNode):
		# type: (str, ScreenNode) -> None
		pass

	def GetScreenNode(self):
		# type: () -> ScreenNode
		pass

	def GetScreenName(self):
		# type: () -> str
		pass

	def OnCreate(self):
		pass

	def OnDestroy(self):
		pass

	def OnTick(self):
		pass
