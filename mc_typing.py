# -*- coding: utf-8 -*-
"""
| ==============================================
|
|   Copyright (c) 2025 Nuoyan
|
|   Author: Nuoyan
|   Email : 1279735247@qq.com
|   Gitee : https://gitee.com/charming-lee
|   Date  : 2025-11-12
|
| ==============================================
"""


from typing import Tuple, Optional, TypedDict, Literal, List, Dict, Any, Callable


__ItemPosType = Literal[0, 1, 2, 3]
__Facing = Literal[0, 1, 2, 3, 4, 5]
__GameType = Literal[0, 1, 2]
__GameDifficulty = Literal[0, 1, 2, 3]
__AttrType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
__Operation = Literal[0, 1, 2, 3]
__PlayerExhauseRatioType = Literal[0, 1, 2, 3, 4, 9]
__RenderControllerArrayType = Literal[0, 1, 2]
__UniformIndex = Literal[1, 2, 3, 4]
__ShapeType = Literal[1, 2, 3, 4, 5, 6]
__Persp = Literal[0, 1, 2]


__ActorDamageCause = Literal[
    "none",
    "override",
    "contact",
    "entity_attack",
    "projectile",
    "suffocation",
    "fall",
    "fire",
    "fire_tick",
    "lava",
    "drowning",
    "block_explosion",
    "entity_explosion",
    "void",
    "self_destruct",
    "self_destruct",
    "magic",
    "wither",
    "starve",
    "anvil",
    "thorns",
    "falling_block",
    "piston",
    "fly_into_wall",
    "magma",
    "fireworks",
    "lightning",
    "freezing",
    "stalactite",
    "stalagmite",
    "ram_attack",
    "custom",
    "sonic_boom",
    "camp_fire",
    "soul_camp_fire",
]
__RcpTypeStr = Literal[
    "recipe_shaped",
    "recipe_shapeless",
    "recipe_furnace",
    "recipe_brewing_mix",
    "recipe_brewing_container",
    "recipe_smithing_transform",
    "recipe_smithing_trim",
    "recipe_smithing_trim",
    "recipe_smithing_trim",
    "recipe_smithing_trim",
]
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
__Axis = Literal[
    "x",
    "y",
]
__Anchor = Literal[
    "top_left",
    "top_middle",
    "top_right",
    "left_middle",
    "center",
    "right_middle",
    "bottom_left",
    "bottom_middle",
    "bottom_right",
]
__PropertyName = Literal[
    "all",
    "size",
    "offset",
    "alpha",
    "clip",
    "color",
    "flip_book",
    "aseprite_flip_book",
    "uv",
    "wait",
]
__ClipDirection = Literal[
    "fromLeftToRight",
    "fromRightToLeft",
    "fromOutsideToInside",
    "fromTopToBottom",
    "fromBottomToTop",
]
__ImageAdaptionType = Literal[
    "normal",
    "filled",
    "oldNineSlice",
    "originNineSlice",
]
__TextAlignment = Literal[
    "left",
    "center",
    "right",
]
__Orientation = Literal[
    "horizontal",
    "vertical",
]
__ParamTypeStr = Literal[
    "textures",
    "geometry",
    "materials",
    "animations",
    "render_controllers",
    "particle_effects",
    "sound_effects",
]
__OptionId = Literal[
    "AUTO_JUMP",
    "HIDE_PAPERDOLL",
    "HIDE_HAND",
    "SPLIT_CONTROLS",
    "VIEW_BOBBING",
    "INPUT_MODE",
    "TRADITION_CONTROLS",
    "HIDE_HUD",
    "CAMERA_SHAKE",
    "TRANSPARENTLEAVES",
    "FANCY_SKIES",
    "SMOOTH_LIGHTING",
    "GRAPHICS",
    "RENDER_CLOUDS",
    "FORCE_SPRINT",
]
__SliderOptionId = Literal[
    "MOUSE_SENSITIVITY",
    "MOUSE_SPYGLASS_DAMPING",
    "GAMEPAD_SENSITIVITY",
    "GAMEPAD_SPYGLASS_DAMPING",
    "GAMEPAD_CURSOR_SENSITIVITY",
    "TOUCH_SENSITIVITY",
    "TOUCH_SPYGLASS_DAMPING",
    "DPAD_SCALE",
    "GAMMA",
    "INTERFACE_OPACITY",
    "FIELD_OF_VIEW",
]


class __ItemDict(TypedDict, total=False):
    newItemName: str
    newAuxValue: int
    itemName: str
    auxValue: int
    count: int
    showInHand: bool
    enchantData: List[Tuple[int, int]]
    modEnchantData: List[Tuple[str, int]]
    customTips: str
    extraId: str
    userData: Optional[dict]
    durability: int


class __ItemBasicInfo(TypedDict, total=False):
    itemName: str
    maxStackSize: int
    maxDurability: int
    id_aux: int
    tierDict: Optional[dict]
    itemCategory: Literal[
        "construction",
        "nature",
        "equipment",
        "items",
        "custom",
        "",
    ]
    itemType: Literal[
        "book",
        "sword",
        "shears",
        "axe",
        "clock",
        "bucket",
        "fishing_rod",
        "hoe",
        "shovel",
        "pickaxe",
        "dye",
        "food",
        "block",
        "armor",
        "custom_ranged_weapon",
        "compass",
        "trident",
        "potion",
        "crossbow",
    ]
    customItemType: str
    tags: List[str]
    customTips: str
    itemTierLevel: Literal[-1, 0, 1, 2, 3, 4]
    fuelDuration: float
    foodNutrition: int
    foodSaturation: float
    weaponDamage: int
    armorDefense: int
    armorSlot: int
    armorToughness: int
    armorKnockbackResistance: float
    enchant_slot_type: int


class __BlockDict(TypedDict, total=False):
    name: str
    aux: int


class __EffectDict(TypedDict):
    effectName: str
    duration: int
    duration_f: float
    amplifier: int


class __EnchantDict(TypedDict, total=False):
    identifier: str
    description: str
    primary_slots: Literal[
        "all",
        "g_armor",
        "armor_head",
        "armor_torso",
        "armor_legs",
        "armor_feet",
        "sword",
        "bow",
        "spear",
        "crossbow",
        "g_tool",
        "hoe",
        "shears",
        "flintsteel",
        "shield",
        "g_digging",
        "axe",
        "pickaxe",
        "shovel",
        "fishing_rod",
        "carrot_stick",
        "elytra",
        "cosmetic_head",
        "compass",
        "mushroom_stick",
        "brush",
    ]
    cost: List[int]
    frequency: Literal[
        "common",
        "uncommon",
        "rare",
        "very_rare",
    ]
    is_treasure_only: bool
    is_discoverable: bool
    is_lootable: bool
    is_curse: bool
    max_level: int
    incompatible: List[str]


class __AbilitiesDict(TypedDict):
    build: bool
    mine: bool
    doorsandswitches: bool
    opencontainers: bool
    attackplayers: bool
    attackmobs: bool
    op: bool
    teleport: bool


class __RespawnPosDict(TypedDict):
    dimensionId: int
    pos: Tuple[int, int, int]


class __ProjectileParamDict(TypedDict, total=False):
    position: Tuple[float, float, float]
    direction: Tuple[float, float, float]
    power: float
    gravity: float
    damage: float
    targetId: str
    isDamageOwner: bool
    auxValue: int


class __MolangReturnDict(TypedDict):
    value: Any
    error: str


class __RecipeResultDict(TypedDict):
    fullItemName: str
    auxValue: int
    num: int


class __CommandBlockDict(TypedDict):
    cmd: str
    name: str
    mode: Literal[0, 1, 2]
    isConditional: Literal[0, 1]
    redstoneMode: Literal[0, 1]


class __SignTextStyleDict(TypedDict):
    color: Tuple[float, float, float, float]
    lighting: bool


class __JigsawBlockDict(TypedDict, total=False):
    name: str
    aux: int
    jigsaw_name: str
    jigsaw_target_name: str
    jigsaw_target_pool: str
    jigsaw_final_block: str
    jigsaw_join_type: Literal[0, 1]


class _OptionInfoDict(TypedDict, total=False):
    pvp: bool
    show_coordinates: bool
    fire_spreads: bool
    tnt_explodes: bool
    mob_loot: bool
    natural_regeneration: bool
    respawn_block_explosion: bool
    respawn_radius: bool
    tile_drops: bool
    immediate_respawn: bool


class _CheatInfoDict(TypedDict, total=False):
    enable: bool
    always_day: bool
    mob_griefing: bool
    keep_inventory: bool
    weather_cycle: bool
    mob_spawn: bool
    entities_drop_loot: bool
    daylight_cycle: bool
    command_blocks_enabled: bool
    random_tick_speed: int


class __GameRuleDict(TypedDict, total=False):
    option_info: _OptionInfoDict
    cheat_info: _CheatInfoDict


class __ScoreDict(TypedDict, total=False):
    displayName: str
    name: str
    criteriaName: Literal["dummy"]
    value: int


class __RayResultDict(TypedDict):
    type: Literal["Entity", "Block"]
    entityId: str
    pos: Tuple[int, int, int]
    identifier: str
    hitPos: Tuple[float, float, float]


class __EntityDict(TypedDict):
    dimensionId: int
    identifier: str


class __BlockPaletteSerializedDict(TypedDict):
    extra: Dict[Tuple[str, int], List[int]]
    void: bool
    actor: Dict[str, Dict[int, dict]]
    volume: Tuple[int, int, int]
    common: Dict[Tuple[str, int], List[int]]
    eliminateAir: bool


class __CreateParamsDict(TypedDict, total=False):
    isHud: Literal[0, 1]
    inputMode: Literal[0, 1]
    bindEntityId: str
    bindWorldPosition: Tuple[int, Tuple[float, float, float]]
    bindOffset: Tuple[float, float, float]
    autoScale: Literal[0, 1]
    mini_map_root_path: str


class __FullPositionDict(TypedDict, total=False):
    followType: Literal["none", "parent", "maxChildren", "maxSibling", "children", "x", "y"]
    relativeValue: float
    absoluteValue: float


class __FullSizeDict(TypedDict, total=False):
    fit: bool
    followType: Literal["none", "parent", "maxChildren", "maxSibling", "children", "x", "y"]
    relativeValue: float
    absoluteValue: float


class __UiItemDict(TypedDict):
    itemName: str
    auxValue: int
    isEnchanted: bool


class __EntityParamDict(TypedDict, total=False):
    entity_id: str
    entity_identifier: str
    scale: float
    render_depth: int
    init_rot_x: float
    init_rot_y: float
    init_rot_z: float
    molang_dict: Dict[str, float]
    rotation_axis: Tuple[int, int, int]


class __SkeletonModelParamDict(TypedDict, total=False):
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


class __BlockGeometryModelParamDict(TypedDict, total=False):
    block_geometry_model_name: str
    scale: float
    init_rot_x: float
    init_rot_y: float
    init_rot_z: float
    molang_dict: Dict[str, float]
    rotation_axis: Tuple[int, int, int]


class __MiningArgs(TypedDict, total=False):
    haste: int
    conduit_power: int
    mining_fatigue: int
    mining_efficiency: int


class _TextureDict(TypedDict):
    paths: List[str]
    name: str


class __TextureInfoDict(TypedDict):
    North: _TextureDict
    West: _TextureDict
    Up: _TextureDict
    Down: _TextureDict
    East: _TextureDict
    South: _TextureDict


class __TargetInfoDict(TypedDict):
    type: Literal["Entity", "Block", "None"]
    entityId: str
    hitPosX: float
    hitPosY: float
    hitPosZ: float
    x: int
    y: int
    z: int
    face: Literal[0, 1, 2, 3, 4, 5]


class _RenderTargetDict(TypedDict):
    width: float
    height: float


class __PassDict(TypedDict, total=False):
    render_target: _RenderTargetDict
    material: str
    depth_enable: bool


class _ParasDict(TypedDict):
    name: str
    value: float
    range: List[float, float]


class _PassArrayDict(TypedDict):
    render_target: _RenderTargetDict
    material: str


class __ProcessDict(TypedDict, total=False):
    name: str
    enable: bool
    paras: List[_ParasDict]
    pass_array: List[_PassArrayDict]
