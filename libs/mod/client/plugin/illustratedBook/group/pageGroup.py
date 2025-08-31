
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.page.basePage import BasePage
from typing import List
from typing import Dict
from typing import Tuple


class PageGroup(object):

    def GetAddr(self):
        # type: () -> str
        """
            获取该页组的绝对路径
        """
        pass

    def GetPages(self):
        # type: () -> List[BasePage]
        """
            获取该页组的页面数量
        """ 
        pass

    def GetPagesCount(self):
        # type: () -> int
        """
            获取该页组的页面数量
        """  
        pass     

