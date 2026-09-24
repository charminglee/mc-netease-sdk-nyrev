# -*- coding: utf-8 -*-


from typing import Any
from typing import Dict
from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class PhysxComponentClient(BaseComponent):
    def GetLinearVelocity(self):
        # type: () -> Tuple[float, float, float]
        """
        获取自定义刚体在世界坐标系下的线速度
        """
        pass

    def GetAngularVelocity(self):
        # type: () -> Tuple[float, float, float]
        """
        获取自定义刚体在世界坐标系下的角速度
        """
        pass

    def GetQuaternion(self):
        # type: () -> Tuple[float, float, float, float]
        """
        获取自定义刚体的四元数旋转
        """
        pass

    def Raycast(self, origin, dir, maxDist, maxHits):
        # type: (Tuple[float, float, float], Tuple[float, float, float], float, int) -> List[dict]
        """
        射线检测，获取与射线相交的碰撞体。目前仅支持获取自定义刚体
        """
        pass

    def RemoveShape(self, shapeIndex):
        # type: (int) -> bool
        """
        删除客户端本地自定义刚体上指定索引的碰撞 shape
        """
        pass

    def AddBoxGeometry(self, localTransform, halfX, halfY, halfZ, staticFriction, dynamicFriction, restitution, eventMask=0, userData=None, density=10.0):
        # type: (Tuple[float, float, float], float, float, float, float, float, float, int, str | None, float) -> bool
        """
        给客户端本地自定义刚体创建盒形碰撞体
        """
        pass

    def GetShapeCount(self):
        # type: () -> int
        """
        获取客户端本地自定义刚体当前的碰撞 shape 数量
        """
        pass

    def GetShapeInfo(self, shapeIndex):
        # type: (int) -> Dict[str, Any] | None
        """
        获取客户端本地指定碰撞 shape 的信息
        """
        pass

    def RemoveShapeByUserData(self, userData):
        # type: (str) -> int
        """
        删除客户端本地所有 userData 与指定值相同的碰撞 shape
        """
        pass

    def SetGlobalPose(self, pos, rot):
        # type: (Tuple[float, float, float] | None, Tuple[float, float, float, float] | None) -> bool
        """
        设置客户端本地自定义刚体的变换（直接瞬移）
        """
        pass

