# -*- coding: utf-8 -*-

from typing import Union
from typing import List
from mod.common.component.baseComponent import BaseComponent

class RecipeCompServer(BaseComponent):
    def RemoveRecipe(self, rcpIdentifier, rcpTypeStr):
        # type: (str, str) -> 'bool'
        """
        动态禁用配方
        """
        pass

    def AddRecipe(self, rcp):
        # type: (Union[str,dict]) -> 'bool'
        """
        动态注册配方，支持配方类型详见<a href="../../../../mcguide/20-玩法开发/15-自定义游戏内容/5-自定义配方.html#配方类型说明">[配方类型说明]</a>
        """
        pass

    def GetRecipeResult(self, recipeId):
        # type: (str) -> 'List[dict]'
        """
        根据配方id获取配方结果。仅支持合成配方
        """
        pass

    def GetRecipesByResult(self, resultIdentifier, tag, aux=0, maxResultNum=-1):
        # type: (str, str, int, int) -> 'List[dict]'
        """
        通过输出物品查询配方所需要的输入材料
        """
        pass

    def AddBrewingRecipes(self, brewType, inputName, reagentName, outputName):
        # type: (str, str, str, str) -> 'bool'
        """
        添加酿造台配方的接口
        """
        pass

    def GetRecipesByInput(self, inputIdentifier, tag, aux=0, maxResultNum=-1):
        # type: (str, str, int, int) -> 'List[dict]'
        """
        通过输入物品查询配方
        """
        pass

