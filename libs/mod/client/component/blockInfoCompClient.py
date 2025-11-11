# -*- coding: utf-8 -*-


from typing import TypedDict, Union, Optional
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple, Literal


class __MiningArgs(TypedDict, total=False):
    haste: int
    conduit_power: int
    mining_fatigue: int
    mining_efficiency: int
__UniformIndex = Literal[1, 2, 3, 4]


class BlockInfoComponentClient(BaseComponent):
    def GetBlockClip(self, pos):
        # type: (Tuple[int, int, int]) -> dict
        """
        获取指定位置方块当前clip的aabb
        """
        pass

    def GetBlockCollision(self, pos):
        # type: (Tuple[int, int, int]) -> dict
        """
        获取指定位置方块当前collision的aabb
        """
        pass

    def GetBlock(self, pos):
        # type: (Tuple[float, float, float]) -> Tuple[str, int]
        """
        获取某一位置的block
        """
        pass

    def GetTopBlockHeight(self, pos):
        # type: (Tuple[int, int]) -> Union[int, None]
        """
        获取当前维度某一位置最高的非空气方块的高度
        """
        pass

    def ChangeBlockTextures(self, blockName, tileName, texturePath):
        # type: (str, str, str) -> bool
        """
        替换方块贴图
        """
        pass

    def GetBlockTextures(self, blockName, face=6):
        # type: (str, int) -> dict
        """
        获取方块的初始贴图信息
        """
        pass

    def GetDestroyTotalTime(self, blockName, itemName=None, miningArgs=None):
        # type: (str, Optional[str], __MiningArgs) -> float
        """
        获取使用物品破坏方块需要的时间
        """
        pass

    def SetBlockEntityMolangValue(self, pos, variableName, value):
        # type: (Tuple[int, int, int], str, float) -> bool
        """
        设置自定义方块实体的Molang变量，与实体的molang变量作用相同。目前主要用于控制自定义实体的动画状态转变。Molang变量的定义方式与原版实体的Molang变量定义方法相同。详细可参考自定义方块实体动画的教学文档。
        """
        pass

    def GetBlockEntityMolangValue(self, pos, variableName):
        # type: (Tuple[int, int, int], str) -> float
        """
        获取自定义方块实体的Molang变量的值。
        """
        pass

    def SetEnableBlockEntityAnimations(self, pos, enable):
        # type: (Tuple[int, int, int], bool) -> bool
        """
        设置是否开启自定义方块实体的动画效果，开启之后，自定义实体方块会按照实体文件中animation_controller所定义的动画状态机进行动画播放。关闭之后，则会停止所有动画播放。
        """
        pass

    def CreateParticleEffectForBlockEntity(self, pos, path, particleKeyName, effectPos):
        # type: (Tuple[int, int, int], str, str, Tuple[float, float, float]) -> Union[int, None]
        """
        在自定义方块实体上创建粒子特效，创建后该接口返回粒子特效的Id，利用该Id可以使用特效/粒子中的接口对该粒子特效进行播放、设置位置、大小等操作。与实体的粒子特效创建方式类似。若自定义方块实体已存在键值名称相同的特效，则不会创建新的特效，接口返回已有的特效Id。
        """
        pass

    def GetParticleEffectIdInBlockEntity(self, pos, particleKeyName):
        # type: (Tuple[int, int, int], str) -> Union[int, None]
        """
        获取在自定义方块实体中已创建的指定粒子特效的Id，已创建的特效分为两种：一是通过resource_pack/entity/下的实体json文件中使用“netease_particle_effects”所定义的特效；二是使用接口CreateParticleEffectForBlockEntity创建的特效。 返回的特效Id可以使用特效/粒子中的接口对该粒子特效进行播放、设置位置、大小等操作。与实体的粒子特效创建方式类似。
        """
        pass

    def RemoveParticleEffectInBlockEntity(self, pos, particleKeyName):
        # type: (Tuple[int, int, int], str) -> bool
        """
        移除在自定义方块实体上创建的粒子特效。移除后的特效Id将会失效。
        """
        pass

    def CreateFrameEffectForBlockEntity(self, pos, path, frameKeyName, effectPos):
        # type: (Tuple[int, int, int], str, str, Tuple[float, float, float]) -> Union[int, None]
        """
        在自定义方块实体上创建序列帧特效，创建后该接口返回序列帧特效的Id，利用该Id可以使用特效/序列帧中的接口对该序列帧特效进行播放、设置位置、大小等操作。与实体的序列帧特效创建方式类似。
        """
        pass

    def GetFrameEffectIdInBlockEntity(self, pos, frameKeyName):
        # type: (Tuple[int, int, int], str) -> Union[int, None]
        """
        获取在自定义方块实体中已创建的指定序列帧特效的Id，已创建的特效分为两种：一是通过resource_pack/entity/下的实体json文件中使用“netease_frame_effects”所定义的特效；二是使用接口CreateFrameEffectForBlockEntity创建的特效。 返回的特效Id可以使用特效/序列帧中的接口对该序列帧特效进行播放、设置位置、大小等操作。与实体的序列帧特效创建方式类似。
        """
        pass

    def RemoveFrameEffectInBlockEntity(self, pos, frameKeyName):
        # type: (Tuple[int, int, int], str) -> bool
        """
        移除在自定义方块实体上创建的序列帧特效。移除后的特效Id将会失效。
        """
        pass

    def SetBlockEntityParticlePosOffset(self, pos, particleKeyName, effectPosOffset):
        # type: (Tuple[int, int, int], str, Tuple[int, int, int]) -> bool
        """
        设置自定义方块实体中粒子特效位置偏移值，用于调整粒子特效相对于方块位置的偏移。与特效/粒子/SetPos接口不同，该接口调整的是相对于方块位置的位置偏移值，而不是世界坐标。
        """
        pass

    def SetBlockEntityFramePosOffset(self, pos, frameKeyName, effectPosOffset):
        # type: (Tuple[int, int, int], str, Tuple[int, int, int]) -> bool
        """
        设置自定义方块实体中序列帧特效位置偏移值，用于调整序列帧特效相对于方块位置的偏移。与特效/序列帧/SetPos接口不同，该接口调整的是相对于方块位置的位置偏移值，而不是世界坐标。
        """
        pass

    def SetBlockEntityModelPosOffset(self, pos, modelPosOffset):
        # type: (Tuple[int, int, int], Tuple[int, int, int]) -> bool
        """
        设置自定义方块实体的实体模型位置偏移值，用于调整实体模型相对于方块位置的偏移。可通过该接口来调整自定义方块实体的实体模型的位置。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。
        """
        pass

    def SetBlockEntityModelScale(self, pos, scale):
        # type: (Tuple[int, int, int], Tuple[float, float, float]) -> bool
        """
        设置自定义方块实体的实体模型大小的缩放值，可通过该接口来调整自定义方块实体的实体模型的大小。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。
        """
        pass

    def SetBlockEntityModelRotation(self, pos, angles, rotateAxis):
        # type: (Tuple[int, int, int], float, str) -> bool
        """
        设置自定义方块实体的实体模型在各个轴上的旋转值，可通过该接口来调整自定义方块实体的实体模型的旋转。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。
        """
        pass

    def RegisterOnStandOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_stand_on组件
        """
        pass

    def UnRegisterOnStandOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_stand_on组件
        """
        pass

    def RegisterOnStepOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_step_on组件
        """
        pass

    def UnRegisterOnStepOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_step_on组件
        """
        pass

    def RegisterOnStepOff(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_step_off组件
        """
        pass

    def UnRegisterOnStepOff(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_step_off组件
        """
        pass

    def RegisterOnEntityInside(self, blockName):
        # type: (str) -> bool
        """
        可以动态注册与修改netease:on_entity_inside组件
        """
        pass

    def UnRegisterOnEntityInside(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_entity_inside组件
        """
        pass

    def GetBlockEntityData(self, pos):
        # type: (Tuple[int, int, int]) -> Union[dict, None]
        """
        用于获取客户端当前维度中方块（包括自定义方块）的数据，数据只读不可写，无法获取箱子内的物品信息。
        """
        pass

    def SetBlockEntityExtraUniforms(self, pos, uniformIndex, data):
        # type: (Tuple[int, int, int], __UniformIndex, Tuple[float, float, float, float]) -> bool
        """
        设置可在自定义方块实体的shader当中使用的自定义变量的值，该自定义变量总共可设置EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量，向量的默认值为(1.0,1.0,1.0,1.0)。
        """
        pass

    def GetBlockEntityExtraUniforms(self, pos, uniformIndex):
        # type: (Tuple[int, int, int], __UniformIndex) -> Tuple[float, float, float, float]
        """
        获取在自定义方块实体的shader当中使用的自定义变量的值，该自定义变量总共可设置EXTRA_ACTOR_UNIFORM1,EXTRA_ACTOR_UNIFORM2,EXTRA_ACTOR_UNIFORM3,EXTRA_ACTOR_UNIFORM4，总共4组，每组为一个vec4(float, float, float ,float)类型的向量。
        """
        pass

    def SetBlockRenderDistance(self, distance):
        # type: (float) -> bool
        """
        设置玩家周围方块的可渲染距离
        """
        pass

    def GetBlockRenderDistance(self):
        # type: () -> float
        """
        获取玩家周围的可渲染距离
        """
        pass

    def AddTerrainDestroyParticleEffect(self, name, aux, pos):
        # type: (str, int, Tuple[float, float, float]) -> bool
        """
        在指定位置播放指定方块被开始破坏时的粒子效果（如果有）。
        """
        pass

    def RemoveTerrainDestroyParticleEffect(self, name, aux, pos):
        # type: (str, int, Tuple[float, float, float]) -> bool
        """
        停止指定位置播放的方块被开始破坏时的粒子效果。
        """
        pass

    def SetCrackFrame(self, dimensionId, blockPos, frame):
        # type: (int, Tuple[int, int, int], int) -> bool
        """
        仅客户端的破坏纹理的渲染，可自定义破坏阶段在第几帧。
        """
        pass

    def DestroyCrackFrame(self, dimensionId, blockPos):
        # type: (int, Tuple[int, int, int]) -> bool
        """
        销毁特定方块位置上的破坏纹理（仅能销毁SetCrackFrame接口创建的破坏纹理）。
        """
        pass

