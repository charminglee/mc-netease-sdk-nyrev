# -*- coding: utf-8 -*-


from typing import Dict, Any
from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple


class PhysxComponentServer(BaseComponent):
    def ConnectPvd(self):
        # type: () -> bool
        """
        连接本机 PhysX Visual Debugger（PVD）以调试当前 PhysX 场景
        """
        pass

    def DisconnectPvd(self):
        # type: () -> None
        """
        断开当前 PhysX 场景与本机 PhysX Visual Debugger（PVD）的连接
        """
        pass

    def CreatePxActor(self):
        # type: () -> bool
        """
        给实体创建自定义刚体
        """
        pass

    def AddBoxGeometry(self, localTransform, halfX, halfY, halfZ, staticFriction, dynamicFriction, restitution, eventMask=0, userData=None, density=10.0):
        # type: (Tuple[float, float, float], float, float, float, float, float, float, int, str | None, float) -> bool
        """
        给自定义刚体创建盒形碰撞体
        """
        pass

    def AddCapsuleGeometry(self, localTransform, radius, halfHeight, staticFriction, dynamicFriction, restitution, eventMask=0, userData=None, density=10.0):
        # type: (Tuple[float, float, float], float, float, float, float, float, int, str | None, float) -> bool
        """
        给自定义刚体创建胶囊形碰撞体
        """
        pass

    def AddSphereGeometry(self, localTransform, radius, staticFriction, dynamicFriction, restitution, eventMask=0, userData=None, density=10.0):
        # type: (Tuple[float, float, float], float, float, float, float, int, str | None, float) -> bool
        """
        给自定义刚体创建球形碰撞体
        """
        pass

    def AddBoxTrigger(self, localTransform, halfX, halfY, halfZ, eventMask=0, userData=None, density=10.0):
        # type: (Tuple[float, float, float], float, float, float, int, str | None, float) -> bool
        """
        给自定义刚体创建盒子形触发器
        """
        pass

    def RemoveShape(self, shapeIndex):
        # type: (int) -> bool
        """
        删除自定义刚体上指定索引的碰撞 shape，适用于盒形、胶囊形、球形碰撞体和触发器
        """
        pass

    def GetShapeCount(self):
        # type: () -> int
        """
        获取自定义刚体当前的碰撞 shape 数量
        """
        pass

    def GetShapeInfo(self, shapeIndex):
        # type: (int) -> Dict[str, Any] | None
        """
        获取指定碰撞 shape 的信息
        """
        pass

    def RemoveShapeByUserData(self, userData):
        # type: (str) -> int
        """
        删除所有 userData 与指定值相同的碰撞 shape
        """
        pass

    def SetRigidBodyFlag(self, flag, val):
        # type: (int, bool) -> bool
        """
        设置自定义刚体的行为开关
        """
        pass

    def SetLinearDamping(self, damping):
        # type: (float) -> bool
        """
        设置动态刚体的线性阻尼，值越大线速度衰减越快
        """
        pass

    def SetAngularDamping(self, damping):
        # type: (float) -> bool
        """
        设置动态刚体的角阻尼，值越大角速度衰减越快
        """
        pass

    def SetMass(self, mass):
        # type: (float) -> bool
        """
        设置动态刚体质量
        """
        pass

    def SetRigidDynamicLockFlags(self, flag):
        # type: (int) -> bool
        """
        设置自定义刚体的约束
        """
        pass

    def SetActorFlag(self, flag, val):
        # type: (int, bool) -> bool
        """
        设置物理实体的行为开关
        """
        pass

    def GetRigidBodyFlags(self):
        # type: () -> 'int'
        """
        获取刚体当前 RigidBodyFlags(诊断接口,bit0=eKINEMATIC)
        """
        pass

    def GetRigidDynamicLockFlags(self):
        # type: () -> int
        """
        获取动态刚体当前 RigidDynamicLockFlags(诊断接口,bit0-2=Linear XYZ lock,bit3-5=Angular XYZ lock)
        """
        pass

    def GetActorFlags(self):
        # type: () -> int
        """
        获取 actor 当前 ActorFlags(诊断接口,bit1=eDISABLE_SIMULATION,bit3=eDISABLE_GRAVITY)
        """
        pass

    def IsDefaultPxActor(self):
        # type: () -> bool
        """
        是否为引擎默认创建的 PxActor(诊断接口,True 表示 mod CreatePxActor 实际是 no-op)
        """
        pass

    def GetMass(self):
        # type: () -> float
        """
        获取自定义刚体的质量(PhysX 内部 mass,由 density+体积合成)
        """
        pass

    def GetLinearVelocity(self):
        # type: () -> Tuple[float, float, float]
        """
        获取自定义刚体的线速度(world space)
        """
        pass

    def SetLinearVelocity(self, velocity):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置自定义刚体的线速度(world space),仅对PxRigidDynamic生效
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
        对自定义刚体的质心施加全局坐标力；数值单位由mode决定，对运动学刚体无效
        """
        pass

    def AddTorque(self, torque, mode):
        # type: (Tuple[float, float, float], int) -> bool
        """
        对自定义刚体添加扭矩，对运动学刚体无效
        """
        pass

    def AddTorqueLocal(self, torque, mode):
        # type: (Tuple[float, float, float], int) -> bool
        """
        在自定义刚体本地坐标系中添加扭矩，对运动学刚体无效。X轴为Roll（滚转），Y轴为Yaw（偏航），Z轴为Pitch（俯仰）
        """
        pass

    def AddForceAtPosLocal(self, force, mode, pos):
        # type: (Tuple[float, float, float], int, Tuple[float, float, float]) -> bool
        """
        对自定义刚体的指定位置添加力，对运动学刚体无效
        """
        pass

    def AddForceAtPos(self, force, mode, pos):
        # type: (Tuple[float, float, float], int, Tuple[float, float, float]) -> bool
        """
        对自定义刚体的指定位置添加力，对运动学刚体无效
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

    def GetAngularVelocity(self):
        # type: () -> Tuple[float, float, float]
        """
        获取自定义刚体的角速度
        """
        pass

    def SetAngularVelocity(self, velocity):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置自定义刚体的角速度，对运动学刚体无效
        """
        pass

    def SetMaxAngularVelocity(self, maxVel):
        # type: (float) -> bool
        """
        设置自定义刚体的最大角速度，防止碰撞后疯转
        """
        pass

    def SetMaxLinearVelocity(self, maxVel):
        # type: (float) -> bool
        """
        设置自定义刚体的最大线速度，防止物体飞出天际
        """
        pass

    def SetSceneGravity(self, dimensionId, gravity):
        # type: (int, Tuple[float, float, float]) -> bool
        """
        设置指定维度 PhysX 场景的全局重力，仅服务端可调用；立即影响该维度内全部受重力的动态 PhysX 刚体。
        """
        pass

    def SampleBuoyancy(self, samples, yOffset, fluidDensities, gravityMagnitude=9.81, forceScale=2.0):
        # type: (List[Tuple[float, float, float, float]], float, Dict[str, float], float, float) -> Dict[str, Any] | None
        """
        使用C++批量采样自定义刚体的浸没体积、浮力合力和浮心；本接口只计算，不施力，仅服务端可调用。
        """
        pass

    def SetRemoteVisualSync(self, maxOptimizedDistance, maxDroppedTicks):
        # type: (float, int) -> bool
        """
        设置该自定义 PhysX 刚体的远端位置与四元数同步降频参数，整个刚体的所有 shape/mesh 一并生效，仅服务端可调用。
        """
        pass

    def ClearRemoteVisualSync(self):
        # type: () -> bool
        """
        清除该自定义 PhysX 刚体的运行时远端同步配置，恢复实体定义的默认带宽优化行为，仅服务端可调用。
        """
        pass

    def IsSleeping(self):
        # type: () -> bool
        """
        查询自定义刚体是否处于休眠状态
        """
        pass

    def WakeUp(self):
        # type: () -> bool
        """
        唤醒休眠中的刚体
        """
        pass

    def PutToSleep(self):
        # type: () -> bool
        """
        强制刚体进入休眠
        """
        pass

    def SetCMassLocalPose(self, pos):
        # type: (Tuple[float,float,float]) -> bool
        """
        设置质心相对于actor原点的偏移，用于手动调整重心
        """
        pass

    def GetMassSpaceInertiaTensor(self):
        # type: () -> Tuple[float, float, float]
        """
        获取刚体的惯性张量对角线分量
        """
        pass

    def CreateFixedJoint(self, entityId0, entityId1, anchor0, anchor1):
        # type: (str, str, Tuple[float, float, float], Tuple[float, float, float]) -> int
        """
        创建固定关节，两个刚体刚性连接，无自由度
        """
        pass

    def CreateDistanceJoint(self, entityId0, entityId1, anchor0, anchor1):
        # type: (str, str, Tuple[float, float, float], Tuple[float, float, float]) -> int
        """
        创建距离关节，限制两个锚点之间的距离范围，可配弹簧
        """
        pass

    def CreateSphericalJoint(self, entityId0, entityId1, anchor0, anchor1):
        # type: (str, str, Tuple[float, float, float], Tuple[float, float, float]) -> int
        """
        创建球窝关节，允许三轴旋转，可加锥形角度限制
        """
        pass

    def CreateRevoluteJoint(self, entityId0, entityId1, anchor0, anchor1, axis):
        # type: (str, str, Tuple[float, float, float], Tuple[float, float, float], Tuple[float, float, float]) -> int
        """
        创建铰链关节，绕指定轴单轴旋转，可加角度限制和电机
        """
        pass

    def CreatePrismaticJoint(self, entityId0, entityId1, anchor0, anchor1, axis):
        # type: (str, str, Tuple[float, float, float], Tuple[float, float, float], Tuple[float, float, float]) -> int
        """
        创建滑动关节；两个刚体仅能沿指定轴相对平移，旋转被锁定，可加行程限制
        """
        pass

    def DestroyJoint(self, jointId):
        # type: (int) -> bool
        """
        销毁关节
        """
        pass

    def DestroyJointsForEntity(self, entityId):
        # type: (str) -> int
        """
        销毁指定实体上所有关联的关节，应在实体销毁前调用
        """
        pass

    def DestroyAllJoints(self):
        # type: () -> None
        """
        销毁所有关节
        """
        pass

    def SetJointBreakForce(self, jointId, force, torque):
        # type: (int, float, float) -> bool
        """
        设置关节可承受的约束力/约束扭矩阈值；PhysX求解出的实际约束载荷超过任一阈值时自动断裂。冲量(eIMPULSE，单位N·s)不能直接与力阈值(N)比较
        """
        pass

    def SetJointCollisionEnabled(self, jointId, enabled):
        # type: (int, bool) -> bool
        """
        设置关节关联的两个刚体之间是否发生碰撞，适用于所有关节类型
        """
        pass

    def GetJointBreakForce(self, jointId):
        # type: (int) -> Tuple[float, float]
        """
        获取关节的断裂力和断裂扭矩
        """
        pass

    def IsJointBroken(self, jointId):
        # type: (int) -> bool
        """
        查询关节是否已断裂
        """
        pass

    def GetJointType(self, jointId):
        # type: (int) -> int
        """
        查询关节类型
        """
        pass

    def GetRevoluteJointAngle(self, jointId):
        # type: (int) -> float
        """
        获取铰链关节当前相对于创建零位的旋转角度。仅对RevoluteJoint有效
        """
        pass

    def GetRevoluteJointVelocity(self, jointId):
        # type: (int) -> float
        """
        获取铰链关节当前角速度。仅对RevoluteJoint有效
        """
        pass

    def GetJointFrames(self, jointId):
        # type: (int) -> Dict[str, Any] | None
        """
        获取关节两端当前的本地frame和世界frame
        """
        pass

    def SetDistanceJointParams(self, jointId, minDist, maxDist, stiffness, damping, flags):
        # type: (int, float, float, float, float, int) -> bool
        """
        设置距离关节参数
        """
        pass

    def SetSphericalJointLimitCone(self, jointId, yAngle, zAngle):
        # type: (int, float, float) -> bool
        """
        设置球窝关节的锥形角度限制并启用
        """
        pass

    def SetRevoluteJointLimit(self, jointId, lower, upper):
        # type: (int, float, float) -> bool
        """
        设置铰链关节的角度限制并启用
        """
        pass

    def SetPrismaticJointLimit(self, jointId, lower, upper):
        # type: (int, float, float) -> bool
        """
        设置滑动关节的行程限制并启用
        """
        pass

    def SetRevoluteJointDrive(self, jointId, velocity, forceLimit):
        # type: (int, float, float) -> bool
        """
        设置铰链关节的电机并启用
        """
        pass

