# -*- coding: utf-8 -*-


from typing import Tuple, Optional, Literal
from mod.common.component.baseComponent import BaseComponent


__TimeEaseType = Literal[
    "linear",
    "spring",
    "in_quad",
    "out_quad",
    "in_out_quad",
    "in_cubic",
    "out_cubic",
    "in_out_cubic",
    "in_quart",
    "out_quart",
    "in_out_quart",
    "in_quint",
    "out_quint",
    "in_out_quint",
    "in_sine",
    "out_sine",
    "in_out_sine",
    "in_expo",
    "out_expo",
    "in_out_expo",
    "in_circ",
    "out_circ",
    "in_out_circ",
    "in_bounce",
    "out_bounce",
    "in_out_bounce",
    "in_back",
    "out_back",
    "in_out_back",
    "in_elastic",
    "out_elastic",
    "in_out_elastic",
]


class CameraComponentClient(BaseComponent):
    def GetFov(self):
        # type: () -> float
        """
        获取视野大小
        """
        pass

    def SetFov(self, fov):
        # type: (float) -> bool
        """
        设置视野大小
        """
        pass

    def LockCamera(self, lockPos, lockRot):
        # type: (Tuple[float, float, float], Tuple[float, float, float]) -> bool
        """
        锁定摄像机
        """
        pass

    def UnLockCamera(self):
        # type: () -> bool
        """
        解除摄像机锁定
        """
        pass

    def PickFacing(self):
        # type: () -> dict
        """
        获取准星选中的实体或者方块
        """
        pass

    def GetFpHeight(self):
        # type: () -> float
        """
        获取本地玩家当前状态下，第一人称视角时的摄像机高度偏移量。游泳时，滑翔时以及普通状态下会有所不同
        """
        pass

    def GetChosenEntity(self):
        # type: () -> str
        """
        获取屏幕点击位置的实体id，通常与GetEntityByCoordEvent配合使用
        """
        pass

    def GetChosen(self):
        # type: () -> dict
        """
        获取屏幕点击位置的实体或方块信息，通常与GetEntityByCoordEvent配合使用
        """
        pass

    def DepartCamera(self):
        # type: () -> None
        """
        分离玩家与摄像机
        """
        pass

    def UnDepartCamera(self):
        # type: () -> None
        """
        绑定玩家与摄像机
        """
        pass

    def SetCameraBindActorId(self, targetId):
        # type: (str) -> bool
        """
        将摄像机绑定到目标实体身上（调用者与目标必须在同一个dimension，同时需要在加载范围之内，若绑定后目标离开了范围或者死亡，则会自动解除绑定）
        """
        pass

    def ResetCameraBindActorId(self):
        # type: () -> bool
        """
        将摄像机重新绑定回主角身上
        """
        pass

    def SetCameraDistanceFixed(self, isFixed):
        # type: (bool) -> bool
        """
        设置相机弹簧臂固定，即设置当相机遇到阻挡时是否压缩与人物之间的距离
        """
        pass

    def GetForward(self):
        # type: () -> Tuple[float, float, float]
        """
        返回相机向前的方向
        """
        pass

    def GetPosition(self):
        # type: () -> Tuple[float, float, float]
        """
        返回相机中心
        """
        pass

    def SetCameraPos(self, pos):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置相机中心的位置
        """
        pass

    def SetCameraRotation(self, rot):
        # type: (Tuple[float, float, float]) -> bool
        """
        设定摄像机的朝向
        """
        pass

    def GetCameraRotation(self):
        # type: () -> Tuple[float, float, float]
        """
        获取摄像机的朝向
        """
        pass

    def SetCameraOffset(self, offset):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置摄像机偏移量
        """
        pass

    def GetCameraOffset(self):
        # type: () -> Tuple[float, float, float]
        """
        获取摄像机偏移量
        """
        pass

    def SetCameraAnchor(self, offset):
        # type: (Tuple[float, float, float]) -> bool
        """
        设置相机锚点
        """
        pass

    def GetCameraAnchor(self):
        # type: () -> Tuple[float, float, float]
        """
        获取相机锚点
        """
        pass

    def LockModCameraPitch(self, enable):
        # type: (int) -> bool
        """
        锁定摄像机上下角度（第三人称下生效，锁定后不能上下调整视角）
        """
        pass

    def IsModCameraLockPitch(self):
        # type: () -> bool
        """
        是否锁定摄像机上下角度
        """
        pass

    def GetCameraPitchLimit(self):
        # type: () -> Tuple[float, float]
        """
        获取摄像机上下角度限制值
        """
        pass

    def SetCameraPitchLimit(self, limit):
        # type: (Tuple[float, float]) -> bool
        """
        设置摄像机上下角度限制值，默认是（-90，90）
        """
        pass

    def LockModCameraYaw(self, enable):
        # type: (int) -> bool
        """
        锁定摄像机左右角度（第三人称下生效，锁定后不能通过鼠标左右调整视角）
        """
        pass

    def IsModCameraLockYaw(self):
        # type: () -> bool
        """
        是否锁定摄像机左右角度
        """
        pass

    def SetSpeedFovLock(self, isLocked):
        # type: (bool) -> None
        """
        是否锁定相机视野fov，锁定后不随速度变化而变化
        """
        pass

    def AddCameraTrackMotion(self, targetPos, duraTime, startPos=None, relativeCoord=False, isLoop=False, targetRot=None, startRot=None, useVelocityDir=False, ease='linear'):
        # type: (Tuple[float, float, float], float, Optional[Tuple[float, float, float]], bool, bool, Optional[Tuple[float, float, float]], Optional[Tuple[float, float, float]], bool, __TimeEaseType) -> int
        """
        给相机添加轨迹运动器
        """
        pass

    def AddCameraVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        # type: (Tuple[float, float, float], Optional[Tuple[float, float, float]], bool) -> int
        """
        给相机添加速度运动器
        """
        pass

    def AddCameraAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        # type: (Tuple[float, float, float], float, Tuple[float, float, float], bool, float) -> int
        """
        给相机添加对点环绕运动器
        """
        pass

    def AddCameraAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        # type: (str, float, Tuple[float, float, float], bool, float, float) -> int
        """
        给相机添加对实体环绕运动器
        """
        pass

    def GetCameraMotions(self):
        # type: () -> dict
        """
        获取相机上的所有运动器
        """
        pass

    def RemoveCameraMotion(self, motionId):
        # type: (int) -> bool
        """
        移除相机上的某个运动器
        """
        pass

    def StartCameraMotion(self, motionId):
        # type: (int) -> bool
        """
        启动相机上的某个运动器
        """
        pass

    def StopCameraMotion(self, motionId):
        # type: (int) -> bool
        """
        停止相机上的某个运动器
        """
        pass

