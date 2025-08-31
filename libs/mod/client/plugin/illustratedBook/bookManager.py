
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.bookConfig import BookConfig
from mod.client.plugin.illustratedBook.bookInstance.preset.normalBook import NormalBook

from mod.client.plugin.illustratedBook.comp.baseComp import BaseComp
from mod.client.plugin.illustratedBook.comp.preset.buttonComp import ButtonComp
from mod.client.plugin.illustratedBook.comp.preset.entityComp import EntityComp
from mod.client.plugin.illustratedBook.comp.preset.highlightComp import HighlightComp
from mod.client.plugin.illustratedBook.comp.preset.imageComp import ImageComp
from mod.client.plugin.illustratedBook.comp.preset.textComp import TextComp
from mod.client.plugin.illustratedBook.comp.preset.progressBarComp import ProgressBarComp

from mod.client.plugin.illustratedBook.page.basePage import BasePage
from mod.client.plugin.illustratedBook.page.preset.titlePage import TitlePage

from mod.client.plugin.illustratedBook.group.pageGroup import PageGroup
from mod.client.plugin.illustratedBook.group.preset.book import Book
from mod.client.plugin.illustratedBook.group.preset.category import Category
from mod.client.plugin.illustratedBook.group.preset.entry import Entry


from typing import List
from typing import Dict
from typing import Tuple
from typing import TypeVar
from typing import Type

class BookManager(object):

    def GetBookInstance(self, bookName):
        # type: (str) -> NormalBook
        """
            根据书本名称获取管理该书本的对象
        """
        pass

    def GetOpeningBookInstance(self):
        # type: () -> NormalBook
        """
            获取当前处于打开状态的书本的管理对象
        """
        pass

    def ShowMsg(self, position, msg):
        # type: (Tuple[int, int], str) -> None
        """
            全局显示消息文本
        """   
        pass    

    def HideMsg(self):
        # type: () -> None
        """
            隐藏全局消息文本
        """ 
        pass

    def AddPageType(self, pageName, pageCls):
        # type: (str, Type) -> None
        """
            注册自定义页面
        """ 
        pass

    def UpdateScreen(self):
        # type: () -> None
        """
            刷新书本界面
        """
        pass

    def To(self, addr):
        # type: (str) -> None
        """
            注册自定义页面
        """ 
        pass

    def GetBookConfig(self):
        # type: () -> BookConfig
        """
            获取书本配置常量
        """   
        pass      

    def GetBasePageCls(self):
        # type: () -> Type[BasePage]
        """
            获取页面类的基类
        """
        pass

    def GetTitlePageCls(self):
        # type: () -> Type[TitlePage]
        """
            获取 预设页面 TitlePage 类
        """
        pass

    def GetBaseCompCls(self):
        # type: () -> Type[BaseComp]
        """
            获取组件类的基类
        """
        pass

    def GetButtonCompCls(self):
        # type: () -> Type[ButtonComp]
        """
            获取 预设组件 ButtonComp 类
        """
        pass

    def GetEntityCompCls(self):
        # type: () -> Type[EntityComp]
        """
            获取 预设组件 EntityComp 类
        """
        pass

    def GetHighlightCompCls(self):
        # type: () -> Type[HighlightComp]
        """
            获取 预设组件 HighlightComp 类
        """
        pass
        
    def GetTableRecipeCompCls(self):
        # type: () -> Type[TableRecipeComp]
        """
            获取 预设组件 TableRecipeComp 类
        """
        pass

    def GetImageCompCls(self):
        # type: () -> Type[ImageComp]
        """
            获取 预设组件 ImageComp 类
        """
        pass

    def GetTextCompCls(self):
        # type: () -> Type[TextComp]
        """
            获取 预设组件 TextComp 类
        """
        pass

    def GetProgressBarCompCls(self):
        # type: () -> Type[ProgressBarComp]
        """
            获取 预设组件 ProgressBarComp 类
        """
        pass

    def GetPageGroupCls(self):
        # type: () -> Type[PageGroup]
        """
            获取页组类的基类
        """
        pass

    def GetBookCls(self):
        # type: () -> Type[Book]
        """
            获取包含书本首页的页组类 
        """
        pass

    def GetCategoryCls(self):
        # type: () -> Type[Category]
        """
            获取包含目录首页的页组类 
        """
        pass

    def GetEntryCls(self):
        # type: () -> Type[Entry]
        """
            获取包含章节首页的页组类 
        """
        pass
