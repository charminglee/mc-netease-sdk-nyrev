# -*- coding: utf-8 -*-

from typing import Union

class BlockEntityData(object):
    def __getitem__(self, key):
        # type: (str) -> Union[int, float, str, bool, dict, list]
        pass

    def __setitem__(self, key, value):
        # type: (str, Union[int, float, str, bool, dict, list]) -> None
        pass
