# -*- coding: utf-8 -*-


from mod.client.ui.controls.baseUIControl import BaseUIControl
if 0:
    from typing import TypedDict, Dict, Tuple

    class __RenderEntityParamDict(TypedDict, total=False):
        entity_id: str
        entity_identifier: str
        scale: float
        render_depth: int
        init_rot_x: float
        init_rot_y: float
        init_rot_z: float
        molang_dict: Dict[str, float]
        rotation_axis: Tuple[int, int, int]

    class __RenderSkeletonModelParamDict(TypedDict, total=False):
        skeleton_model_name: str
        animation: str
        animation_looped: bool
        scale: float
        render_depth: int
        init_rot_x: float
        init_rot_y: float
        init_rot_z: float
        molang_dict: Dict[str, float]
        rotation_axis: Tuple[int, int, int]
        light_direction: Tuple[float, float, float]

    class __RenderBlockGeometryModelParamDict(TypedDict, total=False):
        block_geometry_model_name: str
        scale: float
        init_rot_x: float
        init_rot_y: float
        init_rot_z: float
        molang_dict: Dict[str, float]
        rotation_axis: Tuple[int, int, int]


class NeteasePaperDollUIControl(BaseUIControl):
    def GetModelId(self):
        # type: () -> int
        """
        获取渲染的骨骼模型Id
        """
        pass

    def RenderEntity(self, params):
        # type: (__RenderEntityParamDict) -> bool
        """
        渲染实体
        """
        pass

    def RenderSkeletonModel(self, params):
        # type: (__RenderSkeletonModelParamDict) -> bool
        """
        渲染骨骼模型（不依赖实体）
        """
        pass

    def RenderBlockGeometryModel(self, params):
        # type: (__RenderBlockGeometryModelParamDict) -> bool
        """
        渲染网格体模型
        """
        pass

