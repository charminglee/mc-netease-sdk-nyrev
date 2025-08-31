
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.group.preset.book import Book
from mod.client.plugin.illustratedBook.group.preset.category import Category
from mod.client.plugin.illustratedBook.group.preset.entry import Entry
from typing import List
from typing import Dict
from typing import Tuple


class NormalBook(object):

    def GetOriginJsonData(self):
        # type: () -> Dict
        """
            获取从书本json文件传过来未经处理的数据，如果想获取当前被修改的数据则可以调用GetCurrentJsonData
        """
        pass

    def GetCurrentJsonData(self):
        # type: () -> Dict
        """
            获取从书本json文件传过来并经过修改的数据，如果想获取未被修改的数据则可以调用GetOriginJsonData
        """   
        pass    

    def GetBook(self):
        # type: () -> Book
        """
            获取书本首页所在的页组对象
        """   
        pass

    def GetCategory(self, identitfier):
        # type: (str) -> Category
        """
            根据目录的identitfier获取其对象
        """ 
        pass

    def GetEntry(self, identitfier):
        # type: (str) -> Entry
        """
            根据章节的identitfier获取其对象
        """ 
        pass

    def LockCategory(self, identitfier):
        # type: (str) -> None
        """
            根据目录的identitfier上锁s对应的目录
        """ 
        pass

    def UnlockCategory(self, identitfier):
        # type: (str) -> None
        """
            根据目录的identitfier解锁对应的目录
        """ 

    def LockEntry(self, identitfier):
        # type: (str) -> None
        """
            根据章节的identitfier锁住对应的章节
        """ 
        pass

    def UnlockEntry(self, identitfier):
        # type: (str) -> None
        """
            根据章节的identitfier解锁对应的章节
        """ 
        pass
       
