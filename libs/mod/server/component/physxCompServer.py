# -*- coding: utf-8 -*-


from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class PhysxComponentServer(BaseComponent):
    def CreatePxActor(self):
        # type: () -> bool
        """
        给实体创建自定义刚体
        """
        pass

    def AddBoxGeometry(self, localTransform, halfX, halfY, halfZ, staticFriction, dynamicFriction, restitution, eventMask=0, userData=None):
        # type: (Tuple[float, float, float], float, float, float, float, float, float, int, str | None) -> bool
        """
        给自定义刚体创建盒形碰撞体
        """
        pass

    def SetRigidBodyFlag(self, flag, val):
        # type: (int, bool) -> bool
        """
        设置自定义刚体的行为开关
        """
        pass

    def SetRigidDynamicLockFlags(self, flag):
        # type: (int) -> bool
        """
        设置自定义刚体的约束
        """
        pass

    def SetActorFlag(self, flag):
        # type: (int) -> bool
        """
        设置物理实体的行为开关
        """
        pass

    def SetKinematicTarget(self, pos=None, rot=None):
        # type: (Tuple[float, float, float] | None, Tuple[float, float, float, float] | None) -> bool
        """
        设置运动学刚体的目标变换，仅对开启了PxRigidBodyFlag.eKINEMATIC的自定义刚体生效
        """
        pass

    def SetGlobalPose(self, pos=None, rot=None):
        # type: (Tuple[float, float, float] | None, Tuple[float, float, float, float] | None) -> bool
        """
        设置自定义刚体的变换（直接瞬移）
        """
        pass

    def AddForce(self, dir, mode):
        # type: (Tuple[float, float, float], int) -> bool
        """
        对自定义刚体的质心添加力，对运动学刚体无效
        """
        pass

    def GetQuaternion(self):
        # type: () -> Tuple[float, float, float, float]
        """
        获取自定义刚体的四元数旋转
        """
        pass

    def Raycast(self, dimensionId, origin, dir, maxDist, maxHits=1):
        # type: (int, Tuple[float, float, float], Tuple[float, float, float], float, int) -> List[dict]
        """
        射线检测，获取与射线相交的碰撞体。目前仅支持获取自定义刚体
        """
        pass

