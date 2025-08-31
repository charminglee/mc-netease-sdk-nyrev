# -*- coding: utf-8 -*-

from typing import Union
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ParticleSystemCompClient(BaseComponent):
    def Create(self, effect_name, offset=None, rotation=None):
        # type: (str, Tuple[float,float,float], Tuple[float,float,float]) -> 'int'
        """
        创建粒子发射器, 创建后立即播放
        """
        pass

    def CreateBindEntityNew(self, effect_name, entity_id, bone_name='body', offset=None, rotation=None):
        # type: (str, Union[str,int], str, Tuple[float,float,float], Tuple[float,float,float]) -> 'int'
        """
        创建粒子发射器并绑定到指定实体的指定骨骼上, 创建后立即播放
        """
        pass

    def EmitManually(self, par_id):
        # type: (int) -> 'bool'
        """
        手动发射粒子一次
        """
        pass

    def BindEntity(self, par_id, entity_id, bone_name='body', offset=None, rotation=None):
        # type: (int, Union[str,int], str, Tuple[float,float,float], Tuple[float,float,float]) -> 'bool'
        """
        绑定粒子发射器到指定实体的指定骨骼上
        """
        pass

    def BindModel(self, par_id, model_id, bone_name='root', offset=None, rotation=None):
        # type: (int, int, str, Tuple[float,float,float], Tuple[float,float,float]) -> 'bool'
        """
        绑定粒子发射器到指定骨骼模型的指定骨骼上
        """
        pass

    def Unbind(self, par_id, keep_position=True, keep_rotation=True):
        # type: (int, bool, bool) -> 'bool'
        """
        解除指定粒子发射器的绑定状态
        """
        pass

    def SetRelative(self, par_id, is_relative=True):
        # type: (int, bool) -> 'bool'
        """
        设置粒子是否在局部空间进行计算
        """
        pass

    def GetBindingID(self, par_id):
        # type: (int) -> 'str'
        """
        返回粒子绑定的实体id，没有则返回"0"
        """
        pass

    def GetBindingModelID(self, par_id):
        # type: (int) -> 'int'
        """
        返回绑定的骨骼模型id 没有则返回-1
        """
        pass

    def Remove(self, par_id):
        # type: (int) -> 'bool'
        """
        销毁指定粒子发射器
        """
        pass

    def RemoveByName(self, effect_name):
        # type: (str) -> 'bool'
        """
        销毁场景中指定名称(粒子发射器json中的identifier)的所有粒子发射器
        """
        pass

    def Exist(self, par_id):
        # type: (int) -> 'bool'
        """
        判断指定粒子发射器是否存在
        """
        pass

    def Play(self, par_id):
        # type: (int) -> 'bool'
        """
        播放粒子发射器
        """
        pass

    def Stop(self, par_id):
        # type: (int) -> 'bool'
        """
        停止粒子发射器播放(不渲染且不更新逻辑)
        """
        pass

    def Hide(self, par_id):
        # type: (int) -> 'bool'
        """
        隐藏粒子发射器(不渲染)
        """
        pass

    def Show(self, par_id):
        # type: (int) -> 'bool'
        """
        显示粒子发射器(开启渲染)
        """
        pass

    def Pause(self, par_id):
        # type: (int) -> 'bool'
        """
        暂停粒子发射器的逻辑更新，但保持渲染状态
        """
        pass

    def Resume(self, par_id):
        # type: (int) -> 'bool'
        """
        恢复粒子发射器的逻辑更新，不影响渲染状态
        """
        pass

    def Replay(self, par_id):
        # type: (int) -> 'bool'
        """
        重播粒子发射器
        """
        pass

    def PlayAt(self, par_id, at_second):
        # type: (int, float) -> 'bool'
        """
        设置粒子发射器播放时间点
        """
        pass

    def IsPausing(self, par_id):
        # type: (int) -> 'bool'
        """
        返回粒子发射器的逻辑是否正在被暂停
        """
        pass

    def IsHiding(self, par_id):
        # type: (int) -> 'bool'
        """
        返回粒子发射器是否正在被隐藏(不渲染)
        """
        pass

    def SetPos(self, par_id, pos=None):
        # type: (int, Tuple) -> 'bool'
        """
        设置粒子发射器位置
        """
        pass

    def GetPos(self, par_id, is_local=True):
        # type: (int, bool) -> 'Tuple'
        """
        获取粒子发射器位置
        """
        pass

    def SetRot(self, par_id, rot=None):
        # type: (int, Tuple) -> 'bool'
        """
        设置粒子发射器局部旋转
        """
        pass

    def SetRotUseZXY(self, par_id, rot=None):
        # type: (int, Tuple) -> 'bool'
        """
        设置粒子发射器局部旋转，旋转顺序按照绕z,x,y轴旋转
        """
        pass

    def GetRot(self, par_id, is_local=True):
        # type: (int, bool) -> 'Tuple'
        """
        获取粒子发射器局部旋转
        """
        pass

    def SetTimeScale(self, par_id, scale):
        # type: (int, float) -> 'bool'
        """
        设置粒子发射器的播放速度
        """
        pass

    def GetTimeScale(self, par_id):
        # type: (int) -> 'float'
        """
        获取粒子发射器的播放速度
        """
        pass

    def GetDuration(self, par_id):
        # type: (int) -> 'float'
        """
        获取粒子发射器的播放周期(激活+休眠时间)
        """
        pass

    def GetActiveDuration(self, par_id):
        # type: (int) -> 'float'
        """
        获取粒子发射器的激活周期
        """
        pass

    def GetSleepDuration(self, par_id):
        # type: (int) -> 'float'
        """
        获取粒子发射器的休眠周期
        """
        pass

    def GetLoopAge(self, par_id):
        # type: (int) -> 'float'
        """
        获取粒子发射器当前播放周期内已播放的时间
        """
        pass

    def GetVariable(self, par_id, variable_name):
        # type: (int, str) -> 'float'
        """
        获取粒子发射器的Molang变量值
        """
        pass

    def SetVariable(self, par_id, variable_name, value):
        # type: (int, str, float) -> 'bool'
        """
        设置粒子发射器的Molang变量值
        """
        pass

    def GetFacingMode(self, par_id):
        # type: (int) -> 'str'
        """
        返回粒子发射器的粒子朝向模式
        """
        pass

