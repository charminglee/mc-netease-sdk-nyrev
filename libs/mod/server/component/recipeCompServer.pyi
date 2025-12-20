# -*- coding: utf-8 -*-


from typing import Dict
from typing import List, Literal
from mod.common.component.baseComponent import BaseComponent


class RecipeCompServer(BaseComponent):
    def RemoveRecipe(self, rcpIdentifier, rcpTypeStr):
        # type: (str, Literal["recipe_shaped", "recipe_shapeless", "recipe_furnace", "recipe_brewing_mix", "recipe_brewing_container", "recipe_smithing_transform", "recipe_smithing_trim", "recipe_smithing_trim", "recipe_smithing_trim", "recipe_smithing_trim"] | str) -> bool
        """
        动态禁用配方
        """
        pass

    def AddRecipe(self, rcp):
        # type: (str | dict) -> bool
        """
        动态注册配方，支持配方类型详见[配方类型说明]
        """
        pass

    def GetRecipeResult(self, recipeId):
        # type: (str) -> List[Dict[str, str | int]]
        """
        根据配方id获取配方结果。仅支持合成配方
        """
        pass

    def GetRecipesByResult(self, resultIdentifier, tag, aux=0, maxResultNum=-1):
        # type: (str, str, int, int) -> List[dict]
        """
        通过输出物品查询配方所需要的输入材料
        """
        pass

    def AddBrewingRecipes(self, brewType, inputName, reagentName, outputName):
        # type: (Literal["recipe_brewing_mix", "recipe_brewing_container"] | str, str, str, str) -> bool
        """
        添加酿造台配方的接口
        """
        pass

    def GetRecipesByInput(self, inputIdentifier, tag, aux=0, maxResultNum=-1):
        # type: (str, str, int, int) -> List[dict]
        """
        通过输入物品查询配方
        """
        pass

