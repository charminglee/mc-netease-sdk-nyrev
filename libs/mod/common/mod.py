# -*- coding: utf-8 -*-


from typing import Callable, TypeVar, Optional


_T = TypeVar("_T")


class Mod(object):
    @staticmethod
    def Binding(name, version=None):
        # type: (str, Optional[str]) -> Callable[[_T], _T]
        pass

    @staticmethod
    def InitClient():
        # type: () -> Callable[[_T], _T]
        pass

    @staticmethod
    def DestroyClient():
        # type: () -> Callable[[_T], _T]
        pass

    @staticmethod
    def InitServer():
        # type: () -> Callable[[_T], _T]
        pass

    @staticmethod
    def DestroyServer():
        # type: () -> Callable[[_T], _T]
        pass
