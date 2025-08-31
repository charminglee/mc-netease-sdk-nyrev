# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ModelComponentClient(BaseComponent):
    def SetModel(self, modelName):
        # type: (str) -> 'int'
        """
        替换实体的骨骼模型
        """
        pass

    def GetModelId(self):
        # type: () -> 'int'
        """
        获取骨骼模型的Id，主要用于特效绑定骨骼模型
        """
        pass

    def ResetModel(self):
        # type: () -> 'bool'
        """
        恢复实体为原版模型
        """
        pass

    def GetBonePositionFromMinecraftObject(self, boneName):
        # type: (str) -> 'Tuple[float,float,float]'
        """
        获取原版模型的骨骼世界坐标
        """
        pass

    def PlayAnim(self, aniName, isLoop, modelId=None):
        # type: (str, bool, int) -> 'bool'
        """
        播放骨骼动画
        """
        pass

    def GetPlayingAnimList(self, modelId):
        # type: (int) -> 'List[str]'
        """
        获取指定的骨骼模型中正处于播放状态的骨骼动画名称列表
        """
        pass

    def GetAnimLength(self, aniName, modelId=None):
        # type: (str, int) -> 'float'
        """
        获取某个骨骼动画的长度，单位为秒
        """
        pass

    def SetAnimSpeed(self, aniName, speed, modelId=None):
        # type: (str, float, int) -> 'bool'
        """
        设置某个骨骼动画的播放速度
        """
        pass

    def BindModelToModel(self, boneName, modelName):
        # type: (str, str) -> 'int'
        """
        在骨骼模型上挂接其他骨骼模型
        """
        pass

    def UnBindModelToModel(self, modelId):
        # type: (int) -> 'bool'
        """
        取消骨骼模型上挂接的某个骨骼模型。取消挂接后，这个modelId的模型便会销毁，无法再使用，如果是临时隐藏可以使用HideModel
        """
        pass

    def BindModelToEntity(self, boneName, modelName, offset=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # type: (str, str, Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]) -> 'int'
        """
        实体替换骨骼模型后，再往上挂接其他骨骼模型。
        """
        pass

    def UnBindModelToEntity(self, modelId):
        # type: (int) -> 'bool'
        """
        取消实体上挂接的某个骨骼模型。取消挂接后，这个modelId的模型便会销毁，无法再使用，如果是临时隐藏可以使用HideModel
        """
        pass

    def GetAllBindModelToEntity(self, boneName):
        # type: (str) -> 'List[int]'
        """
        获取实体上某个骨骼上挂接的所有骨骼模型的id
        """
        pass

    def SetTexture(self, texture, modelId=None):
        # type: (str, int) -> 'bool'
        """
        设置骨骼模型的贴图，该接口与SetModelTexture功能相同，但属于客户端接口。
        """
        pass

    def GetTexture(self, modelId=None):
        # type: (int) -> 'str'
        """
        获取骨骼模型的贴图路径
        """
        pass

    def SetSkin(self, skin):
        # type: (str) -> 'bool'
        """
        更换原版自定义皮肤
        """
        pass

    def ResetSkin(self, isSteve=True):
        # type: (bool) -> 'bool'
        """
        还原默认皮肤
        """
        pass

    def SetLegacyBindRot(self, enable, modelId=None):
        # type: (bool, int) -> 'bool'
        """
        用于修复特效挂接到骨骼时的方向
        """
        pass

    def GetBoneWorldPos(self, boneName, modelId=None):
        # type: (str, int) -> 'Tuple[float,float,float]'
        """
        获取骨骼的坐标
        """
        pass

    def GetEntityBoneWorldPos(self, entityId, boneName):
        # type: (str, str) -> 'Tuple[float,float,float]'
        """
        获取换了骨骼模型的实体的骨骼坐标
        """
        pass

    def CreateFreeModel(self, modelName):
        # type: (str) -> 'int'
        """
        创建自由的模型（无需绑定Entity）
        """
        pass

    def RemoveFreeModel(self, modelId):
        # type: (int) -> 'bool'
        """
        移除自由模型
        """
        pass

    def SetFreeModelPos(self, modelId, x, y, z):
        # type: (int, float, float, float) -> 'bool'
        """
        设置自由模型的位置
        """
        pass

    def SetFreeModelRot(self, modelId, x, y, z):
        # type: (int, float, float, float) -> 'bool'
        """
        设置自由模型的方向
        """
        pass

    def SetFreeModelAniSpeed(self, modelId, aniName, speed):
        # type: (int, str, float) -> 'bool'
        """
        设置自由模型动画的播放速度
        """
        pass

    def SetFreeModelScale(self, modelId, x, y, z):
        # type: (int, float, float, float) -> 'bool'
        """
        设置自由模型的大小
        """
        pass

    def ModelPlayAni(self, modelId, aniName, isLoop=False, isBlended=False, layer=0):
        # type: (int, str, bool, bool, int) -> 'bool'
        """
        纯骨骼播放动作。 支持骨骼动画混合，可参考SetAnimationBoneMask接口以及RegisterAnim1DControlParam接口说明。
        """
        pass

    def HideModel(self, modelId):
        # type: (int) -> 'None'
        """
        隐藏纯模型
        """
        pass

    def ShowModel(self, modelId):
        # type: (int) -> 'None'
        """
        显示纯模型
        """
        pass

    def SetFreeModelBoundingBox(self, modelId, min, max):
        # type: (int, Tuple[float,float,float], Tuple[float,float,float]) -> 'bool'
        """
        设置自由模型的包围盒
        """
        pass

    def BindEntityToEntity(self, bindEntityId):
        # type: (str) -> 'bool'
        """
        绑定骨骼模型跟随其他entity,如果当前entity是本地玩家，摄像机也跟随其他entity
        """
        pass

    def ResetBindEntity(self):
        # type: () -> 'bool'
        """
        取消目标entity的绑定实体，取消后不再跟随任何其他entity
        """
        pass

    def SetModelOffset(self, offset):
        # type: (Tuple[float,float,float]) -> 'None'
        """
        模型增加偏移量
        """
        pass

    def BindItemToBone(self, modelId, boneName, bindSlot=0, offset=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
        # type: (int, str, int, Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]) -> 'bool'
        """
        将使用了骨骼模型的玩家的手持物绑定到指定的骨骼上
        """
        pass

    def SetModelPerspectiveEffect(self, isPerspective, color):
        # type: (bool, Tuple[float,float,float,float]) -> 'None'
        """
        设置模型透视效果。注：只对自定义骨骼模型生效
        """
        pass

    def SetEntityOpacity(self, opacity):
        # type: (float) -> 'None'
        """
        设置骨骼模型的透明度，只能对骨骼模型生效，如果设置的是原版模型，则模型的影子会被隐藏。
        """
        pass

    def ShowCommonHurtColor(self, show):
        # type: (bool) -> 'bool'
        """
        设置挂接骨骼模型的实体是否显示通用的受伤变红效果
        """
        pass

    def SetShowArmModel(self, modelId, show):
        # type: (int, bool) -> 'bool'
        """
        设置使用骨骼模型后切换至第一人称时是否显示手部模型。需要先为骨骼模型定义arm_model，arm_model的定义可参考demo示例-AwesomeMod中的resourcePack/models/netease_models.json中的大天狗模型定义
        """
        pass

    def SetExtraUniformValue(self, modelId, uniformIndex, vec4data):
        # type: (int, int, Tuple[float,float,float,float]) -> 'bool'
        """
        设置shader中特定Uniform的值
        """
        pass

    def GetExtraUniformValue(self, modelId, uniformIndex):
        # type: (int, int) -> 'Tuple[float,float,float,float]'
        """
        获取在骨骼模型shader中使用的自定义变量Uniform的值
        """
        pass

    def ModelStopAni(self, modelId, aniName):
        # type: (int, str) -> 'bool'
        """
        暂停指定的骨骼动画
        """
        pass

    def SetAnimationBoneMask(self, modelId, aniName, boneNamesList, enable, applyToChild=True):
        # type: (int, str, List[str], bool, bool) -> 'bool'
        """
        设置是否屏蔽动画中指定的骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。
        """
        pass

    def SetAnimationAllBoneMask(self, modelId, aniName, ignoreBonesList, enable, applyToChild=True):
        # type: (int, str, List[str], bool, bool) -> 'bool'
        """
        设置是否屏蔽动画中所有骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。该接口会对该动画中所有骨骼生效，可通过参数ignoreBoneList来指定不受影响的骨骼名称。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。
        """
        pass

    def CancelAllBoneMask(self, modelId, aniName):
        # type: (int, str) -> 'bool'
        """
        取消动画中的所有骨骼屏蔽。
        """
        pass

    def SetAnimLayer(self, modelId, aniName, layer):
        # type: (int, str, int) -> 'bool'
        """
        设置骨骼动画的层级，动画层级越大，则优先度越高，骨骼模型的骨骼优先播放优先度最高的动画，相同层级的动画则优先播放率先播放的动画。
        """
        pass

    def RegisterAnim1DControlParam(self, modelId, leftAniName, rightAniName, paramName):
        # type: (int, str, str, str) -> 'bool'
        """
        当同时播放多个骨骼动画时，新建用于控制动画进行1D线性混合的参数。目前线性混合仅支持对两个动画进行混合。新建的参数值范围为[0,1]。指定的骨骼将会按照这个参数的值对两个动画进行线性混合。
        """
        pass

    def SetAnim1DControlParam(self, modelId, paramName, value):
        # type: (int, str, float) -> 'bool'
        """
        新建动画的1D控制参数后，使用该接口对相应的参数进行控制。
        """
        pass

    def RegisterAnim1DMultiControlParam(self, modelId, paramName, animList):
        # type: (int, str, List[str]) -> 'bool'
        """
        当同时播放多个骨骼动画时，注册用于根据权重控制多动画进行混合的参数
        """
        pass

    def SetAnim1DMultiControlParam(self, modelId, paramName, animWeightDict):
        # type: (int, str, dict) -> 'bool'
        """
        新建动画的1D控制参数后，设置用于根据权重控制多动画进行混合的参数
        """
        pass

    def RemoveAnim1DMultiControlParam(self, modelId, paramName):
        # type: (int, str) -> 'bool'
        """
        删除用于根据权重控制多动画进行混合的参数
        """
        pass

    def SetEntityShadowShow(self, flag):
        # type: (bool) -> 'None'
        """
        设置实体打开/关闭影子渲染
        """
        pass

    def SetModelPartVisible(self, modelId, boneName, visible):
        # type: (int, str, bool) -> 'bool'
        """
        对骨骼模型中指定的骨骼进行渲染屏蔽，屏蔽后该骨骼不会被渲染出来。
        """
        pass

    def SetModelMaterial(self, modelId, material, materialcpu='', boneName=''):
        # type: (int, str, str, str) -> 'bool'
        """
        设置骨骼模型所使用的的材质，除了可以设置骨骼模型所使用的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#7.模型使用自定义材质及更多贴图">自定义材质</a>以外，也可对单个骨骼设置所使用的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#7.模型使用自定义材质及更多贴图">自定义材质</a>。如果需要设置单个骨骼所使用的材质，需要先在netease_model.json下设置"useSplitMeshes"字段为true。
        """
        pass

    def SetModelMultiPassMaterial(self, modelId, materialList, materialCpuList=None, boneName=''):
        # type: (int, List[str], List[str], str) -> 'bool'
        """
        设置骨骼模型多pass中使用到的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#9.骨骼模型自定义多pass">材质列表</a>，也可对单个骨骼设置所使用的自定义多Pass材质。如果需要设置单个骨骼所使用的多Pass材质，需要先在netease_model.json下设置"useSplitMeshes"字段为true。
        """
        pass

    def GetModelMaterial(self, modelId, boneName=''):
        # type: (int, str) -> 'List[str]'
        """
        获取骨骼模型的正在使用的材质名称，也可获取骨骼模型中指定骨骼所使用的<a href="../../../mcguide/16-美术/6-模型和动作/04-骨骼模型的使用.html#7.模型使用自定义材质及更多贴图">材质名称</a>。如果获取指定骨骼所使用的材质，需要先在netease_model.json下设置"useSplitMeshes"字段为true。
        """
        pass

