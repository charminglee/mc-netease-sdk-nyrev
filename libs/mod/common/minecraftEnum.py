# -*- coding: utf-8 -*-


class ActorDamageCause(object):
    NONE = "none"  							# 其他
    Override = "override"  					# 非正常方式（如脚本直接设置血量为0），这种方式的伤害不会被盔甲与buff吸收
    Contact = "contact"  					# 接触伤害（如仙人掌）
    EntityAttack = "entity_attack" 			# 生物攻击
    Projectile = "projectile"  				# 抛射物攻击
    Suffocation = "suffocation" 		 	# 窒息（密封空间）
    Fall = "fall"  							# 掉落
    Fire = "fire"  							# 着火
    FireTick = "fire_tick"  				# 连续着火（生物着火、在火中）
    Lava = "lava"  							# 熔岩
    Drowning = "drowning"  					# 溺水
    BlockExplosion = "block_explosion"  	# 方块爆炸
    EntityExplosion = "entity_explosion"  	# 生物爆炸
    Void = "void"  							# 虚空
    Suicide = "self_destruct"  				# 自杀（kill命令）兼容旧版
    SelfDestruct = "self_destruct"          # 自杀（kill命令）
    Magic = "magic"  						# 尖牙对生物造成的伤害、守卫者对生物造成的魔法伤害和药水伤害等
    Wither = "wither"  						# 凋零效果
    Starve = "starve"  						# 饥饿
    Anvil = "anvil"  						# 下落的铁砧
    Thorns = "thorns"  						# 荆棘反弹伤害
    FallingBlock = "falling_block"  		# 下落的方块（除了铁砧）
    Piston = "piston"  						# 活塞
    FlyIntoWall = "fly_into_wall"  			# 滑翔（撞墙）
    Magma = "magma"  						# 岩浆（如站在岩浆方块上）
    Fireworks = "fireworks"  				# 烟花
    Lightning = "lightning"  				# 闪电
    Freezing = "freezing"					# 冰冻
    Stalactite = "stalactite"				# 被钟乳石砸到
    Stalagmite = "stalagmite"				# 掉落到石笋上
    RamAttack = "ram_attack"				# 山羊冲撞
    Custom = "custom"						# 自定义
    SonicBoom = "sonic_boom"				# 音波尖啸(监守者的远程攻击)
    Campfire = "camp_fire"					# 营火
    SoulCampfire = "soul_camp_fire"			# 灵魂营火(营火的灵魂火变种)

class AniCheatBlockBreak(object):
	OpenSwitch = "server-authoritative-block-breaking"		# 是否开启破坏方块反作弊检查
	PickRangeScalar = "server-authoritative-block-breaking-pick-range-scalar"	# 破坏方块距离检查参数，最小值为1.0，设置小于1.0无效

class AniCheatConsts(object):
	Open = "on"		# 反作弊开关：开
	Close = "off"	# 反作弊开关：关闭
	MoveOff = "client-auth"					# 没有位移检查，完全信任客户端
	MoveOn = "server-auth"					# 服务端有位移检查，没有倒带模拟
	MoveRewind = "server-auth-with-rewind"	# 服务端有位移检查，有倒带模拟

class AniCheatMove(object):
	CheckStyle = "server-authoritative-movement"	# 位移检查的模式
	MinCorrectDelayTick = "player-rewind-min-correction-delay-ticks"	# 服务端从发现作弊到发送纠正指令的最小tick数，0表示发现作弊时每帧发送纠正指令(int)
	TickHistorySize = "player-rewind-history-size-ticks"		# 客户端保存历史帧数，用于倒带模拟。每秒20帧(int)

class AniCheatMoveRewind(object):
	PositionThreshold = "player-rewind-position-threshold"		# 某一帧中，客户端位置与服务端位置的距离平方阈值，超过阈值会触发反作弊纠正(float)
	PositionAcceptance = "player-rewind-position-acceptance"	# 某一帧中，如果客户端位置和服务端位置的距离平方小于这个值，服务端会采用客户端的值(float)
	PositionPersuasion = "player-rewind-position-persuasion"	# 如果客户端和服务端位置不一致，服务端会每帧在客户端的计算方向上加上这个值(float)

class AnimationModeType:
	NONE = 0  		# 无动画模式
	LAYERS = 1  	# 按照层数放置
	BLOCKS = 2  	# 按照方块放置

class ArmorSlotType(object):
	DEFAULT = -1
	HEAD = 0    # 头盔
	BODY = 1    # 胸甲
	LEG = 2     # 护腿
	FOOT = 3    # 鞋子

class AttrType(object):
	HEALTH = 0              # 生命值, 原版的值范围为[0,20]
	SPEED = 1               # 移速, 原版的值范围为[0,+∞]
	DAMAGE = 2              # 攻击力, 原版的值范围为[1,+∞], 默认最大值为1
	UNDERWATER_SPEED = 3    # 水里的移速, 原版的值范围为[0,+∞]
	HUNGER = 4              # 饥饿值, 原版的值范围为[0,20]
	SATURATION = 5          # 饱和值, 原版的值范围为[0,20]
	ABSORPTION = 6          # 伤害吸收生命值，详见备注, 原版的值范围为[0,16]
	LAVA_SPEED = 7          # 岩浆里的移速, 原版的值范围为[0,+∞]
	LUCK = 8                # 幸运值，原版的值范围为[-1024,1024]
	FOLLOW_RANGE = 9		# 跟随方块数(一般指怪的仇恨范围), 原版值范围为[1,2024]，默认值为16
	KNOCKBACK_RESISTANCE = 10	# 击退抵抗，原版值范围为[1,+∞]，默认最大值为1
	JUMP_STRENGTH = 11		# 跳跃力(指骑乘后跳跃可跳跃的高度)，原版值范围为[0,+∞]
	ARMOR = 12				# 护甲值，取决于身上穿戴的护甲总防御量和接口增加的额外护甲值。客户端无法获取接口增加的护甲值，建议开发者自行同步

class AttributeBuffType(object):
	Hunger = 0                    # 饥饿
	Saturation = 1                # 饱食
	Regeneration = 2              # 恢复
	Heal = 3                      # 治疗
	Harm = 4                      # 伤害
	Magic = 5                     # 魔法伤害
	Wither = 6                    # 凋零
	Poison = 7                    # 中毒
	FatalPoison = 8               # 致命中毒
	SelfHeal = 9                  # 自愈
	SelfDestruct = 10             # 自毁

class BiomeType(object):
	ocean = 0								# 海洋
	plains = 1								# 平原
	desert = 2								# 沙漠
	extreme_hills = 3						# 山地
	forest = 4								# 森林
	taiga = 5								# 针叶林
	swampland = 6							# 沼泽
	river = 7								# 河流
	hell = 8								# 下界荒地
	the_end = 9								# 末地
	legacy_frozen_ocean = 10				# 冻洋
	frozen_river = 11						# 冻河
	ice_plains = 12							# 积雪的冻原
	ice_mountains = 13						# 雪山
	mushroom_island = 14					# 蘑菇岛
	mushroom_island_shore = 15				# 蘑菇岛岸
	beach = 16								# 沙滩
	desert_hills = 17						# 沙漠丘陵
	forest_hills = 18						# 繁茂的丘陵
	taiga_hills = 19						# 针叶林丘陵
	extreme_hills_edge = 20					# 山地边缘
	jungle = 21								# 丛林
	jungle_hills = 22						# 丛林丘陵
	jungle_edge = 23						# 丛林边缘
	deep_ocean = 24							# 深海
	stone_beach = 25						# 石岸
	cold_beach = 26							# 积雪的沙滩
	birch_forest = 27						# 桦木森林
	birch_forest_hills = 28					# 桦木森林丘陵
	roofed_forest = 29						# 黑森林
	cold_taiga = 30							# 积雪的针叶林
	cold_taiga_hills = 31					# 积雪的针叶林丘陵
	mega_taiga = 32							# 巨型针叶林
	mega_taiga_hills = 33					# 巨型针叶林丘陵
	extreme_hills_plus_trees = 34			# 繁茂的山地
	savanna = 35							# 热带草原
	savanna_plateau = 36					# 热带高原
	mesa = 37								# 恶地
	mesa_plateau_stone = 38					# 繁茂的恶地高原
	mesa_plateau = 39						# 恶地高原
	warm_ocean = 40							# 暖水海洋
	deep_warm_ocean = 41					# 暖水深海
	lukewarm_ocean = 42						# 温水海洋
	deep_lukewarm_ocean = 43				# 温水深海
	cold_ocean = 44							# 冷水海洋
	deep_cold_ocean = 45					# 冷水深海
	frozen_ocean = 46						# 冻洋
	deep_frozen_ocean = 47					# 封冻深海
	bamboo_jungle = 48						# 竹林
	bamboo_jungle_hills = 49				# 竹林丘陵
	sunflower_plains = 129					# 向日葵平原
	desert_mutated = 130					# 沙漠湖泊
	extreme_hills_mutated = 131				# 沙砾山地
	flower_forest = 132						# 繁花森林
	taiga_mutated = 133						# 针叶林山地
	swampland_mutated = 134					# 沼泽山丘
	ice_plains_spikes = 140					# 冰刺平原
	jungle_mutated = 149					# 丛林变种
	jungle_edge_mutated = 151				# 丛林边缘变种
	birch_forest_mutated = 155				# 高大桦木森林
	birch_forest_hills_mutated = 156		# 高大桦木丘陵
	roofed_forest_mutated = 157				# 黑森林丘陵
	cold_taiga_mutated = 158				# 积雪的针叶林山地
	redwood_taiga_mutated = 160				# 巨型云杉针叶林
	redwood_taiga_hills_mutated = 161		# 巨型云杉针叶林丘陵
	extreme_hills_plus_trees_mutated = 162	# 沙砾山地+
	savanna_mutated = 163					# 破碎的热带草原
	savanna_plateau_mutated = 164			# 破碎的热带高原
	mesa_bryce = 165						# 被风蚀的恶地
	mesa_plateau_stone_mutated = 166		# 繁茂的恶地高原变种
	mesa_plateau_mutated = 167				# 恶地高原变种
	soulsand_valley = 178					# 灵魂沙峡谷
	crimson_forest = 179					# 绯红森林
	warped_forest = 180						# 诡异森林
	basalt_deltas = 181						# 玄武岩三角洲
	jagged_peaks = 182						# 尖峭山峰
	frozen_peaks = 183						# 冰封山峰
	snowy_slopes = 184						# 积雪的山坡
	grove = 185								# 雪林
	meadow = 186							# 草甸
	lush_caves = 187						# 繁茂洞穴
	dripstone_caves = 188					# 溶洞
	stony_peaks = 189						# 裸岩山峰
	deep_dark = 190						    # 深暗之域
	mangrove_swamp = 191					# 红树林沼泽
	cherry_grove = 192						# 樱花树林

class BlockBreathability(object):
	Solid = 0	# 固体
	Air = 1		# 空气

class BrewingStandSlotType:
	SLOT_INGREDIENT = 0  	# 提取槽位
	SLOT_POTION1 = 1  		# 药水槽位1
	SLOT_POTION2 = 2  		# 药水槽位2
	SLOT_POTION3 = 3  		# 药水槽位3
	SLOT_FUEL = 4 			# 燃料槽位

class ButtonEventType(object):
	Clicked = 0 	# 按钮点击
	Pressed = 1  	# 按钮按下
	Released = 2  	# 按钮抬起

class ButtonState(object):
	Up = 0		 # 按钮抬起
	Down = 1	 # 按钮按下

class CatVariantType:
	White = 0  		# 白猫
	Tuxedo = 1  	# 奶牛猫
	Red = 2  		# 红虎斑猫
	Siamese = 3  	# 暹罗猫
	British = 4 	# 英国短毛猫
	Calico = 5  	# 三花猫
	Persian = 6  	# 波斯猫
	Ragdoll = 7 	# 布偶猫
	Tabby = 8  		# 虎斑猫
	Black = 9  		# 黑猫
	Jellie = 10  	# 金吉拉猫

class Change:
	Add = 0     # 新增自定义刷怪区域
	Remove = 1  # 移除自定义刷怪区域

class ColorCode(object):
	BLACK = "\xc2\xa7" "0"          # 黑色
	DARK_BLUE = "\xc2\xa7" "1"      # 深蓝色
	DARK_GREEN = "\xc2\xa7" "2"     # 深绿色
	DARK_AQUA = "\xc2\xa7" "3"      # 湖蓝色
	DARK_RED = "\xc2\xa7" "4"       # 深红色
	DARK_PURPLE = "\xc2\xa7" "5"    # 紫色
	GOLD = "\xc2\xa7" "6"           # 金色
	GRAY = "\xc2\xa7" "7"           # 灰色
	DARK_GRAY = "\xc2\xa7" "8"      # 深灰色
	BLUE = "\xc2\xa7" "9"           # 蓝色
	GREEN = "\xc2\xa7" "a"          # 绿色
	AQUA = "\xc2\xa7" "b"           # 天蓝色
	RED = "\xc2\xa7" "c"            # 红色
	LIGHT_PURPLE = "\xc2\xa7" "d"   # 粉红色
	YELLOW = "\xc2\xa7" "e"         # 黄色
	WHITE = "\xc2\xa7" "f"          # 白色
	MINECOIN_GOLD = "\xc2\xa7" "g"  # 硬币金

	RAND = "\xc2\xa7" "k"           # 随机字符
	BOLD = "\xc2\xa7" "l"           # 粗体
	ITALIC = "\xc2\xa7" "o"         # 斜体
	RESET = "\xc2\xa7" "r"          # 重置文字样式

class CommandBlockType:
	PULSE = 0  		# 脉冲
	CYCLE = 1  		# 循环
	CHAIN = 2  		# 连锁

class ConditionType:
	UNCONDITIONAL = 0  		# 无条件
	CONDITIONAL = 1  		# 有条件

class ContainerType(object):
	NONE = -9 # 未定义类型
	INVENTORY = -1 # 物品栏
	CONTAINER = 0 # 储物容器
	WORKBENCH = 1 # 工作台
	FURNACE = 2 # 熔炉
	ENCHANTMENT = 3 # 附魔台
	BREWING_STAND = 4 # 酿造台
	ANVIL = 5 # 铁砧
	DISPENSER = 6 # 发射器
	DROPPER = 7 # 投掷器
	HOPPER = 8 # 漏斗
	CAULDRON = 9 # 炼药锅
	TRADE = 15 # 交易界面
	JUKEBOX = 17 # 唱片机
	ARMOR = 18 # 盔甲
	HAND = 19 # 副手
	LOOM = 24 # 织布机
	GRINDSTONE = 26 # 砂轮
	BLAST_FURNACE = 27 # 高炉
	SMOKER = 28 # 烟熏炉
	STONECUTTER = 29 # 切石机
	CARTOGRAPHY = 30 # 制图台
	SMITHING_TABLE= 33 # 锻造台
	CHEST_BOAT = 34 # 运输船
	DECORATED_POT = 35 # 饰纹陶罐
	CRAFTER = 36 # 合成器

class EffectType(object):
	EMPTY_EFFECT = "empty"                   # 无状态效果
	MOVEMENT_SPEED = "speed"                 # 速度，提升行走速度
	MOVEMENT_SLOWDOWN = "slowness"           # 缓慢，降低行走速度
	DIG_SPEED = "haste"                      # 急迫，加快挖掘速度及攻击速度
	DIG_SLOWDOWN = "mining_fatigue"          # 疲劳，减缓挖掘速度及攻击速度
	DAMAGE_BOOST = "strength"                # 力量，提升近战攻击伤害
	HEAL = "instant_health"                  # 瞬间治疗，瞬间回复实体生命值，伤害亡灵生物
	HARM = "instant_damage"                  # 瞬间伤害，瞬间伤害实体，治疗亡灵生物
	JUMP = "jump_boost"                      # 跳跃提升，提升跳跃高度，降低坠落伤害
	CONFUSION = "nausea"                     # 反胃，造成视野扭曲
	REGENERATION = "regeneration"            # 恢复，随时间持续恢复生命
	DAMAGE_RESISTANCE = "resistance"         # 伤害抗性提升，减少大部分的伤害
	FIRE_RESISTANCE = "fire_resistance"      # 防火，免疫火伤害
	WATER_BREATHING = "water_breathing"      # 水下呼吸，在水下时不消耗氧气
	INVISIBILITY = "invisibility"            # 隐身，获得隐形效果
	BLINDNESS = "blindness"                  # 失明，削弱视野，无法疾跑和产生暴击
	NIGHT_VISION = "night_vision"            # 夜视，增加视野亮度
	HUNGER = "hunger"                        # 饥饿，增加饥饿等级，加快饥饿值降低
	WEAKNESS = "weakness"                    # 虚弱，降低近战攻击伤害
	POISON = "poison"                        # 中毒，随时间给予伤害，不会致死
	WITHER = "wither"                        # 凋零，随时间给予伤害，会致死
	HEALTH_BOOST = "health_boost"            # 生命提升，提升生命值上限
	ABSORPTION = "absorption"                # 伤害吸收，增加用于吸收伤害的生命值
	SATURATION = "saturation"                # 饱食，恢复饥饿值和饱和度
	LEVITATION = "levitation"                # 漂浮，使实体不断提升高度
	FATAL_POISON = "fatal_poison"            # 致命中毒，随时间给予伤害，会致死
	CONDUIT_POWER = "conduit_power"          # 潮涌能量，在水下时拥有视野亮度增加、挖掘和攻击速度增加、可水下呼吸三种效果
	SLOW_FALLING = "slow_falling"            # 缓慢降落，降低掉落速度，减少掉落伤害
	BAD_OMEN = "bad_omen"                    # 不祥之兆， 进入村庄时触发袭击
	HERO_OF_THE_VILLAGE = "village_hero"     # 村庄英雄，与村民交易价格降低
	DARKNESS = "darkness"                    # 黑暗,是一种会将玩家的视野限制在15格内，且导致屏幕不时变暗的状态效果。
	WIND_CHARGED = "wind_charged"			 # 蓄风，是一种让生物死亡时产生风爆的状态效果
	INFESTED = "infested"					 # 寄生，是一个可以让生物生成蠹虫的状态效果
	OOZING = "oozing"						 # 渗浆，是一种让生物死亡时产生史莱姆的状态效果
	TRIAL_OMEN = "trial_omen"				 # 试炼之兆，是不祥之兆的变种，有此效果的玩家会被不祥的trial_omen粒子包围并播放event.mob_effect.trial_omen音效
	WEAVING = "weaving"						 # 盘丝，是一个可以让生物死亡时传播蜘蛛网以及让生物以较快速度穿过蜘蛛网的状态效果
	RAID_OMEN = "raid_omen"					 # 袭击之兆，是带有不祥之兆的玩家进入村庄时获得的状态效果，可触发袭击。

class EnchantSlotType(object):
	NONE = 0					# 非法
	ALL = 4294967295			# 全部
	G_ARMOR = 15				# 全部盔甲
	ARMOR_HEAD = 1				# 头盔
	ARMOR_TORSO = 2				# 胸甲
	ARMOR_FEET = 4				# 靴子
	ARMOR_LEGS = 8				# 护腿

	# ungrouped weapons
	SWORD = 16					# 剑
	BOW = 32					# 弓
	SPEAR = 32768				# 三叉戟
	CROSSBOW = 65536			# 弩
	HEAVY_WEAPON = 4194304		# 重锤

	# tool group
	G_TOOL = 131520				# 剪刀、打火石、盾
	SHEARS = 128				# 剪刀
	FLINTSTEEL = 256			# 打火石
	SHIELD = 131072				# 盾

	# digging tool group
	G_DIGGING = 3648			# 锄、斧、镐、锹
	HOE = 64					# 锄
	AXE = 512					# 斧
	PICKAXE = 1024				# 镐
	SHOVEL = 2048				# 锹

	# ungrouped tools
	FISHING_ROD = 4096			# 钓竿
	CARROT_STICK = 8192			# 胡萝卜钓竿
	ELYTRA = 16384				# 鞘翅
	COSMETIC_HEAD = 262144		# 骷髅模型/凋零骷髅模型/模型/僵尸模型/龙的模型/爬行者的模型/雕刻南瓜
	COMPASS = 524288			# 指南针
	MUSHROOM_STICK = 1048576	# 诡异菌钓竿
	BRUSH = 2097152				# 刷子

class EnchantType(object):
	ArmorAll = 0				# 保护
	ArmorFire = 1				# 火焰保护
	ArmorFall = 2				# 摔落保护
	ArmorExplosive = 3			# 爆炸保护
	ArmorProjectile = 4			# 弹射物保护
	ArmorThorns = 5				# 荆棘
	WaterBreath = 6				# 水下呼吸
	WaterSpeed = 7				# 深海探索者
	WaterAffinity = 8			# 水下速掘
	WeaponDamage = 9			# 锋利
	WeaponUndead = 10			# 亡灵杀手
	WeaponArthropod = 11		# 节肢杀手
	WeaponKnockback = 12		# 击退
	WeaponFire = 13				# 火焰附加
	WeaponLoot = 14				# 抢夺
	MiningEfficiency = 15		# 效率
	MiningSilkTouch = 16		# 精准采集
	MiningDurability = 17		# 耐久
	MiningLoot = 18				# 时运
	BowDamage = 19				# 力量
	BowKnockback = 20			# 冲击
	BowFire = 21				# 火矢
	BowInfinity = 22			# 无限
	FishingLoot = 23			# 海之眷顾
	FishingLure = 24			# 饵钓
	FrostWalker = 25			# 冰霜行者
	Mending = 26				# 经验修补
	CurseBinding = 27			# 绑定诅咒
	CurseVanishing = 28			# 消失诅咒
	TridentImpaling = 29		# 穿刺
	TridentRiptide = 30			# 激流
	TridentLoyalty = 31			# 忠诚
	TridentChanneling = 32		# 引雷
	CrossbowMultishot = 33		# 多重射击
	CrossbowPiercing = 34		# 穿透
	CrossbowQuickCharge = 35	# 快速装填
	SoulSpeed = 36				# 灵魂疾行
	SwiftSneak = 37             # 迅捷潜行
	WindBurst = 38				# 风爆
	Density = 39				# 致密
	Breach = 40					# 破甲
	NumEnchantments = 41		# 附魔种数
	InvalidEnchantment = 42		# 无效附魔

	ModEnchant = 255			# 自定义附魔

class EntityColorType:
	White = 0  		# 白色
	Orange = 1  	# 橘色
	Magenta = 2  	# 品红
	LightBlue = 3  	# 浅蓝
	Yellow = 4 		# 黄色
	LightGreen = 5  # 浅绿
	Pink = 6  		# 粉色
	Gray = 7 		# 灰色
	Silver = 8  	# 银色
	Cyan = 9  		# 青色
	Purple = 10  	# 紫色
	Blue = 11  		# 蓝色
	Brown = 12 		# 棕色
	Green = 13  	# 绿色
	Red = 14  		# 红色
	Black = 15  	# 黑色

class EntityComponentType(object):
	addrider = 0
	admire_item = 1
	ageable = 2
	anger_level = 3
	angry = 4
	annotation_break_door = 5
	annotation_open_door = 6
	area_attack = 7
	attack = 8
	attack_cooldown = 9
	attack_damage = 10
	balloonable = 11
	barter = 12
	block_climber = 13
	block_sensor = 14
	boostable = 15
	boss = 16
	break_blocks = 17
	breathable = 18
	breedable = 19
	bribeable = 20
	buoyant = 21
	burns_in_daylight = 22
	celebrate_hunt = 23
	combat_regeneration = 24
	conditional_bandwidth_optimization = 25
	custom_hit_test = 26
	damage_over_time = 27
	damage_sensor = 28
	despawn = 29
	drying_out_timer = 30
	dweller = 31
	economy_trade_table = 32
	entity_sensor = 33
	environment_sensor = 34
	equip_item = 35
	equippable = 36
	exhaustion_values = 37
	experience_reward = 38
	explode = 39
	flocking = 40
	follow_range = 41
	genetics = 42
	giveable = 43
	group_size = 44
	grows_crop = 45
	healable = 46
	health = 47
	heartbeat = 48
	hide = 49
	home = 50
	horse_jump_strength = 51
	hurt_on_condition = 52
	inside_block_notifier = 53
	insomnia = 54
	instant_despawn = 55
	interact = 56
	inventory = 57
	item_hopper = 58
	jump_dynamic = 59
	jump_static = 60
	knockback_resistance = 61
	lava_movement = 62
	leashable = 63
	lookat = 64
	managed_wandering_trader = 65
	mob_effect = 66
	movement_amphibious = 67
	movement_basic = 68
	movement_dolphin = 69
	movement_fly = 70
	movement_generic = 71
	movement_glide = 72
	movement_hover = 73
	movement_jump = 74
	movement_skip = 75
	movement_sway = 76
	nameable = 77
	navigation_climb = 78
	navigation_float = 79
	navigation_fly = 80
	navigation_generic = 81
	navigation_hover = 82
	navigation_swim = 83
	navigation_walk = 84
	out_of_control = 85
	peek = 86
	persistent = 87
	physics = 88
	player_exhaustion = 89
	player_experience = 90
	player_level = 91
	player_saturation = 92
	preferred_path = 93
	projectile = 94
	pushable = 95
	raid_trigger = 96
	rail_movement = 97
	rail_sensor = 98
	ravager_blocked = 99
	rideable = 100
	scaffolding_climber = 101
	scale_by_age = 102
	scheduler = 103
	shareables = 104
	shooter = 105
	sittable = 106
	spawn_entity = 107
	strength = 108
	tameable = 109
	tamemount = 110
	target_nearby_sensor = 111
	teleport = 112
	tick_world = 113
	timer = 114
	trade_table = 115
	trail = 116
	transformation = 117
	trust = 118
	trusting = 119
	underwater_movement = 120
	water_movement = 121

class EntityTeleportCause(object):
	Unkown = "0"		# 尚未具体分类，末影人自体传送目前归为此类
	Projectile = "1"	# 弹射物，类似末影珍珠
	Command = "3"		# op指令，类似tp指令，changedimension指令
	ChorusFruit = "2"	# 吃紫颂果传送
	Behavior = "4"		# 微软原生脚本组件
	Agent = "agent"		# 教育版指导传送
	Client = "client"	# 客户端发送的传送移动包
	GateWay = "gateway"	# 传送门
	Script = "script"	# python接口，类似SetPos，SetFootPos，ChangePlayerDimension，ChangeEntityDimension

class EntityType(object):
	Undefined = 1									# 未定义类型
	TypeMask = 0x000000ff							# 类型过滤
	Mob = 0x00000100								# 生物
	PathfinderMob = 0x00000200 | Mob				# 可寻路生物
	Monster = 0x00000800 | PathfinderMob			# 敌对怪物
	Animal = 0x00001000 | PathfinderMob				# 动物
	TamableAnimal = 0x00004000 | Animal				# 可驯服动物
	Ambient = 0x00008000 | Mob						# 环境
	UndeadMob = 0x00010000 | Monster				# 亡灵生物
	ZombieMonster = 0x00020000 | UndeadMob			# 僵尸生物
	Arthropod = 0x00040000 | Monster				# 节肢生物
	Minecart = 0x00080000							# 矿车
	SkeletonMonster = 0x00100000 | UndeadMob		# 骷髅生物
	EquineAnimal = 0x00200000 | TamableAnimal		# 马类生物
	Projectile = 0x00400000							# 抛射物
	AbstractArrow = 0x00800000						# 抽象箭矢
	WaterAnimal = 0x00002000 | PathfinderMob		# 水生生物
	VillagerBase = 0x01000000 | PathfinderMob		# 村民生物
	Chicken = 10 | Animal							# 鸡
	Cow = 11 | Animal								# 牛
	Pig = 12 | Animal								# 猪
	Sheep = 13 | Animal								# 羊
	Wolf = 14 | TamableAnimal						# 狼
	Villager = 15 | VillagerBase					# 村民
	MushroomCow = 16 | Animal						# 哞菇
	Squid = 17 | WaterAnimal						# 鱿鱼
	Rabbit = 18 | Animal							# 兔子
	Bat = 19 | Ambient								# 蝙蝠
	IronGolem = 20 | PathfinderMob					# 铁傀儡
	SnowGolem = 21 | PathfinderMob					# 雪傀儡
	Ocelot = 22 | TamableAnimal						# 豹猫
	Horse = 23 | EquineAnimal						# 马
	PolarBear = 28 | Animal							# 北极熊
	Llama = 29 | Animal								# 羊驼
	Parrot = 30 | TamableAnimal						# 鹦鹉
	Dolphin = 31 | WaterAnimal						# 海豚
	Donkey = 24 | EquineAnimal						# 驴
	Mule = 25 | EquineAnimal						# 骡
	SkeletonHorse = 26 | EquineAnimal | UndeadMob	# 骷髅马
	ZombieHorse = 27 | EquineAnimal | UndeadMob		# 僵尸马
	Zombie = 32 | ZombieMonster						# 僵尸
	Creeper = 33 | Monster							# 苦力怕
	Skeleton = 34 | SkeletonMonster					# 骷髅
	Spider = 35 | Arthropod							# 蜘蛛
	PigZombie = 36 | UndeadMob						# 僵尸猪灵
	Slime = 37 | Monster							# 史莱姆
	EnderMan = 38 | Monster							# 末影人
	Silverfish = 39 | Arthropod						# 蠹虫
	CaveSpider = 40 | Arthropod						# 洞穴蜘蛛
	Ghast = 41 | Monster							# 恶魂
	LavaSlime = 42 | Monster						# 岩浆怪
	Blaze = 43 | Monster							# 烈焰人
	ZombieVillager = 44 | ZombieMonster				# 僵尸村民
	Witch = 45 | Monster							# 女巫
	Stray = 46 | SkeletonMonster					# 流浪者
	Husk = 47 | ZombieMonster						# 尸壳
	WitherSkeleton = 48 | SkeletonMonster			# 凋灵骷髅
	Guardian = 49 | Monster							# 守卫者
	ElderGuardian = 50 | Monster					# 远古守卫者
	Npc = 51 | Mob									# NPC
	WitherBoss = 52 | UndeadMob						# 凋灵
	Dragon = 53 | Monster							# 末影龙
	Shulker = 54 | Monster							# 潜影贝
	Endermite = 55 | Arthropod						# 末影螨
	Agent = 56 | Mob								# 吉祥物
	Vindicator = 57 | Monster						# 卫道士
	Phantom = 58 | UndeadMob						# 幻翼
	IllagerBeast = 59 | Monster						# 劫掠兽
	ArmorStand = 61 | Mob							# 盔甲架
	TripodCamera = 62 | Mob							# 三脚架摄像机
	Player = 63 | Mob								# 玩家
	ItemEntity = 64									# 物品
	PrimedTnt = 65									# TNT
	FallingBlock = 66								# 下落的方块
	MovingBlock = 67								# 移动的方块
	ExperiencePotion = 68 | Projectile				# 附魔之瓶
	Experience = 69									# 经验球
	EyeOfEnder = 70									# 末影之眼
	EnderCrystal = 71								# 末影水晶
	FireworksRocket = 72							# 烟花火箭
	Trident = 73 | Projectile | AbstractArrow		# 三叉戟
	Turtle = 74 | Animal							# 海龟
	Cat = 75 | TamableAnimal						# 猫
	ShulkerBullet = 76 | Projectile					# 潜影贝导弹
	FishingHook = 77								# 浮漂
	Chalkboard = 78									# 黑板
	DragonFireball = 79 | Projectile				# 末影龙火球
	Arrow = 80 | Projectile | AbstractArrow			# 箭
	Snowball = 81 | Projectile						# 雪球
	ThrownEgg = 82 | Projectile						# 鸡蛋
	Painting = 83									# 画
	LargeFireball = 85 | Projectile					# 火球
	ThrownPotion = 86 | Projectile					# 喷溅药水
	Enderpearl = 87 | Projectile					# 末影珍珠
	LeashKnot = 88									# 栓绳结
	WitherSkull = 89 | Projectile					# 黑色凋灵骷髅头
	BoatRideable = 90								# 可乘骑船
	WitherSkullDangerous = 91 | Projectile			# 蓝色凋灵骷髅头
	LightningBolt = 93								# 闪电
	SmallFireball = 94 | Projectile					# 小火球
	AreaEffectCloud = 95							# 区域效果云
	LingeringPotion = 101 | Projectile				# 滞留药水
	LlamaSpit = 102 | Projectile					# 羊驼唾沫
	EvocationFang = 103 | Projectile				# 唤魔者尖牙
	EvocationIllager = 104 | Monster				# 唤魔者
	Vex = 105 | Monster								# 恼鬼
	MinecartRideable = 84 | Minecart				# 可乘骑矿车
	MinecartHopper = 96 | Minecart					# 漏斗矿车
	MinecartTNT = 97 | Minecart						# TNT矿车
	MinecartChest = 98 | Minecart					# 运输矿车
	MinecartFurnace = 99 | Minecart					# 动力矿车
	MinecartCommandBlock = 100 | Minecart			# 命令方块矿车
	IceBomb = 106 | Projectile						# 冰弹
	Balloon = 107									# 气球
	Pufferfish = 108 | WaterAnimal					# 河豚
	Salmon = 109 | WaterAnimal						# 鲑鱼
	Drowned = 110 | ZombieMonster					# 溺尸
	Tropicalfish = 111 | WaterAnimal				# 热带鱼
	Fish = 112 | WaterAnimal						# 鱼
	Panda = 113 | Animal							# 熊猫
	Pillager = 114 | Monster						# 掠夺者
	VillagerV2 = 115 | VillagerBase					# 村民
	ZombieVillagerV2 = 116 | ZombieMonster			# 僵尸村民
	Shield = 117									# 盾牌
	WanderingTrader = 118 | PathfinderMob			# 流浪商人
	Lectern = 119									# 讲台
	ElderGuardianGhost = 120 | Monster				# 远古守卫者恶魂
	Fox = 121 | Animal								# 狐狸
	Bee = 122 | Mob									# 蜜蜂
	Piglin = 123 | Mob								# 猪灵
	Hoglin = 124 | Animal							# 疣猪兽
	Strider = 125 | Animal							# 炽足兽
	Zoglin = 126 | UndeadMob						# 僵尸疣猪兽
	PiglinBrute = 127 | Mob							# 猪灵蛮兵
	Goat = 128 | Animal								# 山羊
	GlowSquid = 129 | WaterAnimal					# 发光鱿鱼
	Axolotl = 130 | Animal							# 美西螈
	Warden = 131 | Monster							# 监守者
	Frog = 132 | Animal								# 青蛙
	Tadpole = 133 | WaterAnimal						# 蝌蚪
	Allay = 134 | Mob								# 悦灵
	ChestBoatRideable = 136 | BoatRideable			# 可乘骑运输船
	TraderLlama = 137 | Llama						# 行商羊驼
	Camel = 138 | Animal							# 骆驼
	Sniffer = 139 | Animal							# 嗅探兽
	Breeze = 140 | Monster							# 旋风人
	BreezeWindChargeProjectile = 141 | Projectile	# 旋风人风弹
	Armadillo = 142 | Animal						# 犰狳
	WindChargeProjectile = 143 | Projectile			# 风弹
	Bogged = 144 | SkeletonMonster					# 沼骸
	OminousItemSpawner = 145						# 不祥之物生成器
	CustomProjectile = 254 | Projectile				# 自定义抛射物
	EntityExtension = 255							# 实体扩展
	MAX_ENTITY_ID = 256								# 最大实体ID

class Facing(object):
	Down = 0
	Up = 1
	North = 2
	South = 3
	West = 4
	East = 5

class FoxType:
	Red = 0  		# 红狐狸
	Arctic = 1  	# 北极狐

class GameDiffculty(object):
	Peaceful = 0	# 和平
	Easy = 1		# 简单
	Normal = 2		# 普通
	Hard = 3		# 困难
	Count = 4		# 游戏难度种数
	Unknown = 5		# 未知

class GameType(object):
	Undefined = -1            # 未定义类型
	Survival = 0              # 生存模式
	Creative = 1              # 创造模式
	Adventure = 2             # 冒险模式
	Spectator = 6             # 旁观模式
	Default = Survival        # 默认类型，默认为生存模式

class GamepadKeyType:
	UNDEFINED = 0					# 未定义按键
	TRIGGER = 0x00000100			# 扳机
	STICK = 0x00001000				# 摇杆
	KEY_A = 1			    		# A键
	KEY_B = 2			    		# B键
	KEY_X = 3			    		# X键
	KEY_Y = 4			    		# Y键
	KEY_DPAD_UP = 5					# 向上方向键
	KEY_DPAD_DOWN = 6				# 向下方向键
	KEY_DPAD_LEFT = 7				# 向左方向键
	KEY_DPAD_RIGHT = 8				# 向右方向键
	KEY_LS = 9			    		# LS键
	KEY_RS = 10			    		# RS键
	KEY_LB = 11			    		# LB键
	KEY_RB = 12			    		# RB键
	KEY_VIEW = 13					# VIEW键
	KEY_MENU = 14					# MENU键

	STICK_LEFT = 0 | STICK  		# 左摇杆
	STICK_RIGHT = 1 | STICK 		# 右摇杆

	TRIGGER_LEFT = 0 | TRIGGER  	# 左扳机
	TRIGGER_RIGHT = 1 | TRIGGER 	# 右扳机

class HorseSpotType:
	NoneSpot = 0  		# 无斑点
	WhiteStockings = 1  # 白袜
	WhiteField = 2  	# 雪片白斑
	WhiteDots = 3  		# 白色斑点
	BlackDots = 4 	 	# 黑色斑点

class HorseType:
	White = 0  		# 白色
	Creamy = 1  	# 淡栗色
	Chestnut = 2  	# 深枣红色
	Brown = 3  		# 褐色
	Black = 4 		# 黑色
	Gray = 5  		# 灰色
	Darkbrown = 6  	# 深褐色

class InputMode(object):
	Undefined = -1		# 未识别类型
	Mouse = 0			# 键鼠
	Touch = 1			# 触摸屏
	GamePad = 2 		# 游戏手柄

class InventoryType(object):
    CONSTRUCTION = "construction" #建筑
    EQUIPMENT = "equipment"       #装备
    ITEMS = "items"               #物品
    NATURE = "nature"             #自然
    SEARCH = "search"             #搜索

class ItemAcquisitionMethod(object):
    Unknown = -1                # 获得方法未知。
    MethodNone = 0              # 无获得方法。
    PickedUp = 1                # 通过捡起道具的方式获得。服务端和客户端均触发。
    Crafted = 2                 # 通过工具合成的方式获得，工具包括工作台、制图台、砂轮、织布机和切石机。从客户端触发。
    TakenFromChest = 3          # 通过从箱子中拿取的方式获得。从客户端触发。
    TakenFromEnderchest = 4     # 通过从末影箱中拿取的方式获得。目前从末影箱子拿取物品时只返回TakenFromChest的值。
    Bought = 5                  # 通过与村民交易的方式获得。目前与村民交易只返回Trading的值。
    Anvil = 6                   # 通过铁砧的方式获得。从客户端触发。
    Smelted = 7                 # 通过烧炼的方式获得，包括熔炉、烟熏炉及高炉。从客户端触发。
    Brewed = 8                  # 通过酿造的方式获得。只要从酿造台取下道具都会触发。从客户端触发。
    Filled = 9                  # 通过装满空瓶、空桶或炼药锅，又或是从其中倒出内容物的方式获得，服务端和客户端均触发。
                                # 注意，对象为炼药锅时仅从服务端触发事件。
    Trading = 10                # 通过交易的方式获得。从客户端触发。
    Fishing = 11                # 通过钓鱼的方式获得。服务端和客户端均触发。
    Container = 13              # 通过容器的方式获得，目前只支持锻造台。从客户端触发。
    Feeding = 14                # 被喂食。从服务端触发。

class ItemCategory(object):
	Construction = 1		# 建造栏
	Nature = 2				# 自然栏
	Equipment = 3			# 装备栏
	Items = 4				# 物品栏
	Custom = 7				# 自定义

class ItemColor(object):
	Black = 0			# 黑色
	Red = 1				# 红色
	Green = 2			# 绿色
	Brown = 3			# 棕色
	Blue = 4			# 蓝色
	Purple = 5			# 紫色
	Cyan = 6			# 蓝绿色
	Silver = 7			# 银色
	Gray = 8			# 灰色
	Pink = 9			# 粉红色
	Lime = 10			# 石灰色
	Yellow = 11			# 黄色
	LightBlue = 12		# 浅蓝色
	Magenta = 13		# 紫红色
	Orange = 14			# 橙色
	White = 15			# 白色

class ItemPosType(object):
	INVENTORY = 0   # 背包物品栏
	OFFHAND = 1     # 副手
	CARRIED = 2     # 主手
	ARMOR = 3       # 盔甲栏

class ItemType:
	apple = 260
	golden_apple = 322
	appleEnchanted = 466
	mushroom_stew = 282
	bread = 297
	porkchop = 319
	cooked_porkchop = 320
	fish = 349
	salmon = 460
	clownfish = 461
	pufferfish = 462
	cooked_fish = 350
	cooked_salmon = 463
	dried_kelp = 464
	cookie = 357
	melon = 360
	beef = 363
	cooked_beef = 364
	chicken = 365
	cooked_chicken = 366
	rotten_flesh = 367
	spider_eye = 375
	carrot = 391
	potato = 392
	baked_potato = 393
	poisonous_potato = 394
	golden_carrot = 396
	pumpkin_pie = 400
	beetroot = 457
	beetroot_soup = 459
	sweet_berries = 477
	rabbit = 411
	cooked_rabbit = 412
	rabbit_stew = 413
	wheat_seeds = 295
	pumpkin_seeds = 361
	melon_seeds = 362
	nether_wart = 372
	beetroot_seeds = 458
	iron_shovel = 256
	iron_pickaxe = 257
	iron_axe = 258
	flint_and_steel = 259
	bow = 261
	arrow = 262
	coal = 263
	diamond = 264
	iron_ingot = 265
	gold_ingot = 266
	iron_sword = 267
	wooden_sword = 268
	wooden_shovel = 269
	wooden_pickaxe = 270
	wooden_axe = 271
	stone_sword = 272
	stone_shovel = 273
	stone_pickaxe = 274
	stone_axe = 275
	diamond_sword = 276
	diamond_shovel = 277
	diamond_pickaxe = 278
	diamond_axe = 279
	stick = 280
	bowl = 281
	golden_sword = 283
	golden_shovel = 284
	golden_pickaxe = 285
	golden_axe = 286
	string = 287
	feather = 288
	gunpowder = 289
	wooden_hoe = 290
	stone_hoe = 291
	iron_hoe = 292
	diamond_hoe = 293
	golden_hoe = 294
	wheat = 296
	leather_helmet = 298
	leather_chestplate = 299
	leather_leggings = 300
	leather_boots = 301
	chainmail_helmet = 302
	chainmail_chestplate = 303
	chainmail_leggings = 304
	chainmail_boots = 305
	iron_helmet = 306
	iron_chestplate = 307
	iron_leggings = 308
	iron_boots = 309
	diamond_helmet = 310
	diamond_chestplate = 311
	diamond_leggings = 312
	diamond_boots = 313
	mod_armor = 454
	golden_helmet = 314
	golden_chestplate = 315
	golden_leggings = 316
	golden_boots = 317
	shield = 513
	flint = 318
	painting = 321
	sign = 323
	wooden_door = 324
	bucket = 325
	minecart = 328
	saddle = 329
	iron_door = 330
	redstone = 331
	snowball = 332
	boat = 333
	leather = 334
	kelp = 335
	brick = 336
	clay_ball = 337
	reeds = 338
	paper = 339
	book = 340
	slime_ball = 341
	chest_minecart = 342
	egg = 344
	compass = 345
	fishing_rod = 346
	clock = 347
	glowstone_dust = 348
	dye = 351
	bone = 352
	sugar = 353
	cake = 354
	bed = 355
	repeater = 356
	map = 358
	shears = 359
	ender_pearl = 368
	blaze_rod = 369
	ghast_tear = 370
	gold_nugget = 371
	potion = 373
	glass_bottle = 374
	fermented_spider_eye = 376
	blaze_powder = 377
	magma_cream = 378
	brewing_stand = 379
	cauldron = 380
	ender_eye = 381
	speckled_melon = 382
	spawn_egg = 383
	experience_bottle = 384
	fireball = 385
	writable_book = 386
	written_book = 387
	emerald = 388
	frame = 389
	flower_pot = 390
	emptyMap = 395
	skull = 397
	carrotOnAStick = 398
	netherStar = 399
	fireworks = 401
	fireworksCharge = 402
	enchanted_book = 403
	comparator = 404
	netherbrick = 405
	quartz = 406
	tnt_minecart = 407
	hopper_minecart = 408
	hopper = 410
	rabbit_foot = 414
	rabbit_hide = 415
	horsearmorleather = 416
	horsearmoriron = 417
	horsearmorgold = 418
	horsearmordiamond = 419
	record_13 = 500
	record_cat = 501
	record_blocks = 502
	record_chirp = 503
	record_far = 504
	record_mall = 505
	record_mellohi = 506
	record_stal = 507
	record_strad = 508
	record_ward = 509
	record_11 = 510
	record_wait = 511
	trident = 455
	lead = 420
	name_tag = 421
	prismarine_crystals = 422
	muttonRaw = 423
	muttonCooked = 424
	armor_stand = 425
	end_crystal = 426
	spruce_door = 427
	birch_door = 428
	jungle_door = 429
	acacia_door = 430
	dark_oak_door = 431
	chorus_fruit = 432
	chorus_fruit_popped = 433
	dragon_breath = 437
	splash_potion = 438
	lingering_potion = 441
	command_block_minecart = 443
	elytra = 444
	prismarine_shard = 409
	shulker_shell = 445
	banner = 446
	totem = 450
	iron_nugget = 452
	nautilus_shell = 465
	heart_of_the_sea = 467
	turtle_shell_piece = 468
	turtle_helmet = 469
	phantom_membrane = 470
	crossbow = 471
	spruce_sign = 472
	birch_sign = 473
	jungle_sign = 474
	acacia_sign = 475
	darkoak_sign = 476
	banner_pattern = 434
	campfire = 720
	suspicious_stew = 734
	debug_stick = 735
	honeycomb = 736
	honey_bottle = 737
	camera = 698
	compound = 499
	mod = 456
	ice_bomb = 453
	bleach = 451
	rapid_fertilizer = 449
	balloon = 448
	medicine = 447
	sparkler = 442
	glow_stick = 422
	lodestonecompass = 741
	netherite_ingot = 742
	netherite_sword = 743
	netherite_shovel = 744
	netherite_pickaxe = 745
	netherite_axe = 746
	netherite_hoe = 747
	netherite_helmet = 748
	netherite_chestplate = 749
	netherite_leggings = 750
	netherite_boots = 751
	netherite_scrap = 752
	crimson_sign = 753
	warped_sign = 754
	crimson_door = 755
	warped_door = 756
	warped_fungus_on_a_stick = 757
	chain = 758
	record_pigstep = 759
	nether_sprouts = 760
	soul_campfire = 801

class ItemUseMethodEnum(object):
    Unknown = -1  	        # 未知
    EquipArmor = 0          # 穿戴装备
    Eat = 1  		        # 吃食物
    Attack = 2  	        # 攻击
    Consume = 3  	        # 消耗药水
    Throw = 4  		        # 投掷物品（雪球，药水）
    Shoot = 5  		        # 射击（拉弓射箭）
    Place = 6  		        # 放置物品（例如告示牌）
    FillBottle = 7          # 装满一个空瓶子
    FillBucket = 8          # 装满一个空桶
    PourBucket = 9          # 倒出已装满的桶里的东西
    UseTool = 10  	        # 使用工具（打火石，锄，锹等）的右键单击功能
    Interact = 11  	        # 交互
    Retrieved = 12          # 收竿，目前仅用于钓鱼竿
    Dyed = 13		        # 使用炼药锅对物品染色
    Traded = 14		        # 交易
    BrushingCompleted = 15	# 刷子清刷完毕
    OpenedVault = 16        # 打开宝库

class KeyBoardType:
	KEY_GOBACK = 4			# 旧版本遗留，已弃用
	KEY_MOUSE_LEFT = -99 	# 鼠标左键
	KEY_MOUSE_RIGHT = -98 	# 鼠标右键
	KEY_MOUSE_Middle = -97 	# 鼠标中键

	KEY_BACKSPACE = 8		# Backspace键	
	KEY_TAB = 9				# Tab键
	KEY_RETURN = 13			# 回车键
	KEY_PAUSE = 19			# PAUSE键

	KEY_LSHIFT = 16			# SHIFT键		
	KEY_CONTROL = 17		# CONTROL键
	KEY_MENU = 18			# ALT键
	KEY_CAPS_LOCK = 20		# CAPS LOCK键(大小写键)
	KEY_ESCAPE = 27			# Esc键
	KEY_SPACE = 32			# 空格键
	KEY_PG_UP = 33			# Page Up键
	KEY_PG_DOWN = 34		# Page Down键
	KEY_END = 35			# End键
	KEY_HOME = 36			# Home键

	KEY_LEFT = 37			# 方向左键(←)
	KEY_UP = 38				# 方向上键(↑)
	KEY_RIGHT = 39			# 方向右键(→)
	KEY_DOWN = 40			# 方向下键(↓)
	KEY_INSERT = 45			# Insert键
	KEY_DELETE = 46			# Delete键

	KEY_0 = 48				# 数字0(大键盘不是小键盘，48~57同)
	KEY_1 = 49				# 数字1
	KEY_2 = 50				# 数字2
	KEY_3 = 51				# 数字3
	KEY_4 = 52				# 数字4
	KEY_5 = 53				# 数字5
	KEY_6 = 54				# 数字6
	KEY_7 = 55				# 数字7
	KEY_8 = 56				# 数字8
	KEY_9 = 57				# 数字9

	KEY_A = 65				# A键
	KEY_B = 66				# B键
	KEY_C = 67				# C键
	KEY_D = 68				# D键
	KEY_E = 69				# E键				
	KEY_F = 70				# F键
	KEY_G = 71				# G键
	KEY_H = 72				# H键
	KEY_I = 73				# I键
	KEY_J = 74				# J键
	KEY_K = 75				# K键
	KEY_L = 76				# L键
	KEY_M = 77				# M键
	KEY_N = 78				# N键
	KEY_O = 79				# O键
	KEY_P = 80				# P键
	KEY_Q = 81				# Q键
	KEY_R = 82				# R键
	KEY_S = 83				# S键
	KEY_T = 84				# T键
	KEY_U = 85				# U键
	KEY_V = 86				# V键
	KEY_W = 87				# W键
	KEY_X = 88				# X键
	KEY_Y = 89				# Y键
	KEY_Z = 90				# Z键

	KEY_NUMPAD0 = 96		# 数字0(小键盘，96~111同)
	KEY_NUMPAD1 = 97		# 数字1
	KEY_NUMPAD2 = 98		# 数字2
	KEY_NUMPAD3 = 99		# 数字3
	KEY_NUMPAD4 = 100		# 数字4
	KEY_NUMPAD5 = 101		# 数字5
	KEY_NUMPAD6 = 102		# 数字6
	KEY_NUMPAD7 = 103		# 数字7
	KEY_NUMPAD8 = 104		# 数字8
	KEY_NUMPAD9 = 105		# 数字9
	KEY_MULTIPLY = 106		# 乘号键(×)
	KEY_ADD = 107			# 加号键(+)

	KEY_SUBTRACT = 109		# 减号键(-)
	KEY_DECIMAL = 110		# 小数点(.)
	KEY_DIVIDE = 111		# 除法键(/)
	KEY_F1 = 112			# 功能键F1
	KEY_F2 = 113			# 功能键F2
	KEY_F3 = 114			# 功能键F3
	KEY_F4 = 115			# 功能键F4
	KEY_F5 = 116			# 功能键F5
	KEY_F6 = 117			# 功能键F6
	KEY_F7 = 118			# 功能键F7
	KEY_F8 = 119			# 功能键F8
	KEY_F9 = 120			# 功能键F9
	KEY_F10 = 121			# 功能键F10
	KEY_F11 = 122			# 功能键F11
	KEY_F12 = 123			# 功能键F12
	KEY_F13 = 124			# 功能键F13

	KEY_NUM_LOCK = 144		# Num Lock键
	KEY_SCROLL = 145		# Scroll Lock键

	KEY_SEMICOLON = 186		# : ; 键
	KEY_EQUALS = 187		# = + 键
	KEY_COMMA = 188			# , < 键
	KEY_MINUS = 189			# - _ 键
	KEY_PERIOD = 190		# . > 键
	KEY_SLASH = 191			# / ? 键
	KEY_GRAVE = 192			# ` ~ 键

	KEY_LBRACKET = 219		# [ { 键
	KEY_BACKSLASH = 220		# \ | 键
	KEY_RBRACKET = 221		# ] } 键
	KEY_APOSTRAPHE = 222	# ' " 键

class MirrorModeType:
	NONE = 0  		# 不使用镜像
	X = 1  			# 沿X轴进行镜像放置
	Y = 2  			# 沿Y轴进行镜像放置
	XY = 3  		# 沿XY轴进行镜像放置

class OpenContainerId(object):
	AnvilInputContainer = 0 # 铁砧输入位
	AnvilMaterialContainer = 1 # 铁砧材料位
	SmithingTableInputContainer = 3 # 锻造台输入位
	SmithingTableMaterialContainer = 4 # 锻造台材料位
	RecipeBookContainer = 22 # 配方位
	EnchantingInputContainer = 23 # 附魔台输入位
	EnchantingMaterialContainer = 24 # 附魔台材料位
	LoomInputContainer = 42 # 织布机输入位
	LoomDyeContainer = 43 # 织布机染料位
	LoomMaterialContainer = 44 # 织布图案位
	GrindstoneInputContainer = 51 # 砂轮输入位
	GrindstoneAdditionalContainer = 52 # 砂轮附加位
	StonecutterInputContainer = 54 # 切石机输入位
	CartographyInputContainer = 56 # 制图台输入位
	CartographyAdditionalContainer = 57 # 制图台附加位
	CursorContainer = 60 # 指针位置(目前无用)
	CreatedOutputContainer  = 61 # 创造输出位(目前无用)
	SmithingTableTemplateContainer = 62 # 锻造台模板位
	CrafterLevelEntityContainer = 63 # 合成器输入位
	NeteaseContainer = 64  # 自定义方块容器槽位 (关闭后放入物品数据存于方块实体中)
	NeteaseUIContainer = 65 # 网易UI槽位 (数据存于玩家中，关闭ui后放入物品返回背包)

class OptionId(object):
	Undefined = ""
	AUTO_JUMP = "AUTO_JUMP" 						#自动跳跃
	HIDE_PAPERDOLL = "HIDE_PAPERDOLL"				#隐藏纸娃娃
	HIDE_HAND = "HIDE_HAND" 						#隐藏手
	SPLIT_CONTROLS = "SPLIT_CONTROLS" 				#准心瞄准
	VIEW_BOBBING = "VIEW_BOBBING"  					#视角摇晃
	INPUT_MODE = "INPUT_MODE"						#操作模式
	TRADITION_CONTROLS = "TRADITION_CONTROLS"		#十字键操作
	HIDE_HUD = "HIDE_HUD"							#隐藏HUD
	CAMERA_SHAKE = "CAMERA_SHAKE"					#摄像机摇晃
	TRANSPARENTLEAVES = "TRANSPARENTLEAVES"			#花俏的树叶
	FANCY_SKIES = "FANCY_SKIES"						#美丽的天空
	SMOOTH_LIGHTING = "SMOOTH_LIGHTING"				#平滑光照
	GRAPHICS = "GRAPHICS"							#精美图像
	RENDER_CLOUDS = "RENDER_CLOUDS"					#渲染云
	FORCE_SPRINT = "FORCE_SPRINT"					#强制疾跑

class OriginGUIName(object):
	MoveUpBtn = "binding.area.move_up" 		# 上移键
	MoveDownBtn = "binding.area.move_down"  # 下移键
	MoveLeftBtn = "binding.area.move_left"  # 左移键
	MoveRightBtn = "binding.area.move_right" # 右移键
	SneakBtn = "binding.area.sneak"	# 潜行键
	NewSneakBtn = "binding.area.sneak_new_controls" # 新触控（摇杆模式）潜行键/空中&水底下潜键
	JumpBtn = "binding.area.jump"	# 跳跃键
	NewJumpBtn = "binding.area.jump_new_controls" # 新触控（摇杆模式）跳跃键/空中&水底上浮键
	SprintBtn = "binding.area.sprint" # 冲刺按钮（切换跑/走）
	AscendBtn = "binding.area.ascend" # 右侧双击跳跃键飞行后操作按键： 上移
	DescendBtn = "binding.area.descend" # 右侧双击跳跃键飞行后操作按键： 下移
	PauseBtn = "binding.area.pause" # 暂停键
	ChatBtn = "binding.area.chat"	# 聊天按钮
	MenuBtn = "binding.area.fold_menu"	# 菜单按钮(截图分享)
	ReportBtn = "binding.area.report_cheat" # 举报按钮（已废弃）
	CameraViewBtn = "binding.area.camera_view" # 摄像机视角按钮
	DestroyOrAttackBtn = "binding.area.destroy_or_attack" # 破坏/攻击按钮
	BuildOrInteractBtn = "binding.area.build_or_interact" # 建造/交互按钮
	MoveStickBtn = "binding.area.default_move_stick_area" # 新触控摇杆按钮

class PermissionChangeCause(object):
	ProgrammingInterfaceCaused = 1 #  API变更
	CommandCaused = 2 #  指令变更（包含玩家输入/命令方块）
	UserInterfaceCaused = 3#  房主变更（也即房主在设置给他人变更）

class PistonFacing(object):
	Down = 0
	Up = 1
	North = 2
	South = 3
	West = 4
	East = 5

class PlayerActionType(object):
	StartSleeping = 5 # 开始睡觉
	StopSleeping = 6 # 停止睡觉
	StartSprinting = 9 # 开始冲刺
	StopSprinting = 10 # 停止冲刺
	StartSneaking = 11 # 开始潜行
	StopSneaking = 12 # 停止潜行
	StartGliding = 15 # 开始滑翔（鞘翅）
	StopGliding = 16 # 停止滑翔（鞘翅）
	StartSwimming = 21 # 开始游泳
	StopSwimming = 22 # 停止游泳
	StartSpinAttack = 23 # 开始旋转攻击（三叉戟）
	StopSpinAttack = 24 # 停止旋转攻击（三叉戟）
	StartCrawling = 32 # 开始爬行
	StopCrawling = 33 # 停止爬行
	StartFlying = 34 # 开始飞行
	StopFlying = 35 # 停止飞行

class PlayerExhauseRatioType(object):
	HEAL = 0         #通过饥饿值恢复生命
	JUMP = 1         #跳跃
	SPRINT_JUMP = 2  #疾跑跳跃
	MINE = 3         #破坏方块
	ATTACK = 4       #攻击
	GLOBAL = 9       #全局

class PlayerUISlot(object):
	CursorSelected = 0 # 指针位置
	AnvilInput = 1	# 铁砧输入位
	AnvilMaterial = 2 # 铁砧材料位
	StoneCutterInput = 3 # 切石机输入位
	Trade2Ingredient1 = 4 # 交易输入位1
	Trade2Ingredient2 = 5 # 交易输入位2
	LoomInput = 9 # 织布机输入旗帜位
	LoomDye = 10 # 织布机输入染料位
	LoomMaterial = 11 # 织布机输入图案位
	CartographyInput = 12 # 制图台输入位
	CartographyAdditional = 13 # 制图台附加位
	EnchantingInput = 14 # 附魔台输入位
	EnchantingMaterial = 15 # 附魔台材料位
	GrindstoneInput = 16 # 砂轮输入位
	GrindstoneAdditional = 17 # 砂轮附加位
	BeaconPayment = 27 # 信标输入位
	Crafting2x2Input1 = 28 # 2X2工作台输入位1
	Crafting2x2Input2 = 29 # 2X2工作台输入位2
	Crafting2x2Input3 = 30 # 2X2工作台输入位3
	Crafting2x2Input4 = 31 # 2X2工作台输入位4
	Crafting3x3Input1 = 32 # 3X3工作台输入位1
	Crafting3x3Input2 = 33 # 3X3工作台输入位2
	Crafting3x3Input3 = 34 # 3X3工作台输入位3
	Crafting3x3Input4 = 35 # 3X3工作台输入位4
	Crafting3x3Input5 = 36 # 3X3工作台输入位5
	Crafting3x3Input6 = 37 # 3X3工作台输入位6
	Crafting3x3Input7 = 38 # 3X3工作台输入位7
	Crafting3x3Input8 = 39 # 3X3工作台输入位8
	Crafting3x3Input9 = 40 # 3X3工作台输入位9
	CreatedItemOutput = 50 # 创造输出物品生成位
	SmithingTableInput = 51 # 锻造台输入位
	SmithingTableMaterial = 52 # 锻造台材料位
	SmithingTableTemplate = 53 # 锻造台模板位

class RayFilterType(object):
	OnlyEntities = 1 << 0 #仅检测实体
	OnlyBlocks = 1 << 1 #仅检测方块
	BothEntitiesAndBlock = OnlyEntities | OnlyBlocks #检测方块和实体

class RedstoneModeType:
	KEEP_ON = 0  			# 保持开启
	REDSTONE_CONTROL = 1 	# 红石控制

class RenderControllerArrayType(object):
	Geometry = 0 #模型
	Material = 1 #材质
	Texture = 2 #贴图

class RenderLayer(object):
	DOUBLE_SIDED = 0 # 双面
	BLEND_WATER = 1 # 半透明水面
	ALPHATEST_MICRO_BLOCK = 2 # 全透明微缩方块
	RAY_TRACED_WATER = 3 # 原版光线追踪水面
	DEFERRED_WATER = 4 # 原版延迟渲染水面
	BLEND = 5 # 半透明
	OPAQUE = 6 # 不透明
	OPTIONAL_ALPHATEST = 7 # 局部全透明
	ALPHATEST = 8 # 全透明
	SEASONS_OPAQUE = 9 # 原版用于渲染不透明树叶
	SEASONS_OPTIONAL_ALPHATEST = 10 # 原版用于渲染局部全透明方块
	ALPHATEST_SINGLE_SIDE = 11 # 单面全透明
	ENDPORTAL = 12 # 原版末地传送门
	BARRIER = 13 # 原版屏障
	LIGHT = 14 # 原版光源
	STRUCTURE_VOID = 15

class SetBlockType(object):
	MAN_MADE = 0       #人为
	NATURE = 1         #自然生成
	API = 2            #api生成

class ShapeType(object):
	BOX = 1 # 盒子
	LINE = 2 # 线条
	CIRCLE = 3 # 圆
	ARROW = 4 # 箭头
	TEXT = 5 # 文本
	SPHERE = 6 # 球
	COUNT = 7 # 图形数量

class SliderOptionId(object):
	Undefined = ""
	MOUSE_SENSITIVITY = "MOUSE_SENSITIVITY"						#键盘和鼠标->鼠标灵敏度 范围:0-1
	MOUSE_SPYGLASS_DAMPING = "MOUSE_SPYGLASS_DAMPING"			#键盘和鼠标->望远镜移动速度 范围:0-1
	GAMEPAD_SENSITIVITY = "GAMEPAD_SENSITIVITY"					#控制器->鼠标灵敏度 范围:0-1
	GAMEPAD_SPYGLASS_DAMPING = "GAMEPAD_SPYGLASS_DAMPING"		#控制器->望远镜移动速度 范围:0-1
	GAMEPAD_CURSOR_SENSITIVITY = "GAMEPAD_CURSOR_SENSITIVITY"	#控制器->控制器光标灵敏度 范围:0-2
	TOUCH_SENSITIVITY = "TOUCH_SENSITIVITY"						#触摸屏->鼠标灵敏度 范围:0-1
	TOUCH_SPYGLASS_DAMPING = "TOUCH_SPYGLASS_DAMPING"			#触摸屏->望远镜移动速度 范围:0-1
	DPAD_SCALE = "DPAD_SCALE"									#触摸屏->按钮尺寸 范围:0-1
	GAMMA = "GAMMA"												#视频->亮度 范围:0-1
	INTERFACE_OPACITY = "INTERFACE_OPACITY"						#视频->HUD 不透明度 范围:0-1
	FIELD_OF_VIEW = "FIELD_OF_VIEW"								#视频->视野 范围:30-110

class StructureFeatureType(object):
	Unknown = 0				 # 未知结构
	EndCity = 1				 # 末地城
	Fortress = 2			 # 下界要塞
	Mineshaft = 3			 # 废弃矿井
	Monument = 4			 # 海底神殿
	Stronghold = 5			 # 要塞
	Temple = 6				 # 沙漠神殿/雪屋/丛林神庙/女巫小屋
	Village = 7				 # 村庄
	WoodlandMansion = 8		 # 林地府邸
	Shipwreck = 9			 # 沉船
	BuriedTreasure = 10		 # 埋藏的宝藏
	Ruins = 11				 # 水下遗迹
	PillagerOutpost = 12	 # 掠夺者前哨站
	RuinedPortal = 13		 # 废弃传送门
	Bastion = 14			 # 堡垒遗迹
	AncientCity = 15         # 远古城市
	TrailRuins = 16          # 古迹废墟
	TrialChambers = 17		 # 试炼密室
	NeteaseLargeFeature = 18 # 网易版大型结构特征

class TimeEaseType(object):
	linear = "linear"
	spring = "spring"
	in_quad = "in_quad"
	out_quad = "out_quad"
	in_out_quad = "in_out_quad"
	in_cubic = "in_cubic"
	out_cubic = "out_cubic"
	in_out_cubic = "in_out_cubic"
	in_quart = "in_quart"
	out_quart = "out_quart"
	in_out_quart = "in_out_quart"
	in_quint = "in_quint"
	out_quint = "out_quint"
	in_out_quint = "in_out_quint"
	in_sine = "in_sine"
	out_sine = "out_sine"
	in_out_sine = "in_out_sine"
	in_expo = "in_expo"
	out_expo = "out_expo"
	in_out_expo = "in_out_expo"
	in_circ = "in_circ"
	out_circ = "out_circ"
	in_out_circ = "in_out_circ"
	in_bounce = "in_bounce"
	out_bounce = "out_bounce"
	in_out_bounce = "in_out_bounce"
	in_back = "in_back"
	out_back = "out_back"
	in_out_back = "in_out_back"
	in_elastic = "in_elastic"
	out_elastic = "out_elastic"
	in_out_elastic = "in_out_elastic"

class TouchEvent:
	TouchUp = 0  		# 按钮抬起时触发回调
	TouchDown = 1  		# 按钮按下时触发回调
	TouchCancel = 3  	# 按钮按下后移出按钮范围抬起鼠标时触发回调
	TouchMove = 4  		# 按钮按下后移动鼠标触发回调
	TouchMoveIn = 5  	# 鼠标按下后移入按钮触发回调
	TouchMoveOut = 6  	# 鼠标按下后移出按钮触发回调
	TouchScreenExit = 7 # 按钮所在画布退出时若鼠标仍未抬起时触发

class TradeLevelType:
	Newbie = 0  		# 新手
	Apprentice = 1  	# 学徒
	Veteran = 2  		# 老手
	Expert = 3  		# 专家
	Master = 4 			# 大师

class TransferServerFailReason(object):
	TypeNotExist = 10		# 目标类型的服务器不存在
	VersionNotExist = 11	# 目标类型的服务器的版本与玩家客户端的版本不符
	ServerIsFull = 12		# 目标类型的服务器均已经满员了
	VersionNotFix = 13		# 目标ID的服务器的版本与玩家客户端版本不符
	TargetIsFull = 14		# 目标ID的服务器已经满员了
	TargetNotVaild = 15		# 目标ID的服务器不存在或者已经与控制服断开连接
	ApiInputFail = 16		# 目标玩家不在线

class UICategory(object):
	netease_chat_screen = "netease_chat_screen"	 		# 聊天框
	inventory_screen = "inventory_screen" 				# 物品栏
	anvil_screen = "anvil_screen"						# 铁毡
	crafting_screen = "crafting_screen"					# 工作台
	trade_screen = "trade_screen"						# 交易界面
	enchanting_screen = "enchanting_screen"				# 附魔台
	pause_screen = "pause_screen"						# 暂停界面
	cartography_screen = "cartography_screen"			# 制图台
	smithing_table_screen = "smithing_table_screen"		# 锻造台
	brewing_stand_screen = "brewing_stand_screen"		# 酿造台
	furnace_screen = "furnace_screen"					# 熔炉
	blast_furnace_screen = "blast_furnace_screen"		# 高炉
	smoker_screen = "smoker_screen"						# 烟熏炉
	grindstone_screen = "grindstone_screen"				# 砂轮
	small_chest_screen = "small_chest_screen"			# 小箱子
	large_chest_screen = "large_chest_screen"			# 大箱子
	barrel_screen = "barrel_screen"						# 木桶
	sign_screen = "sign_screen"							# 告示牌
	dropper_screen = "dropper_screen"					# 投掷器
	hopper_screen = "hopper_screen"						# 漏斗
	dispenser_screen = "dispenser_screen"				# 发射器
	stonecutter_screen = "stonecutter_screen"			# 切石机

class UiBaseLayer(object):
	Desk = 0				# 主界面常驻
	DeskFloat = 15000		# 主界面浮动提示（浮动提示信息）
	PopUpLv1 = 25000		# 一级弹出界面
	PopUpLv2 = 45000		# 二级弹出界面
	PopUpModal = 60000		# 模态弹出界面（弹出提示）
	PopUpFloat = 75000		# 模态弹出之上的浮动提示（大喇叭）

class UseAnimation(object):
	Undefined = 0  		# 未定义
	Eat = 1				# 吃食物
	Drink = 2			# 喝药水
	Block = 3			# 放置方块
	Bow = 4				# 拉弓
	Camera = 5			# 照相
	Spear = 6			# 三叉戟
	Crossbow = 9		# 拉弩
	Spyglass = 10		# 望远镜
	GoatHorn = 11		# 山羊号角
	Brush = 12			# 刷

class VillagerClothingType:
	Normal = 0  		# 正常服装
	Desert = 1  		# 沙漠服装
	Jungle = 2  		# 森林服装
	Savanna = 3  		# 草原服装
	Snow = 4 			# 雪地服装
	Swamp = 5  			# 沼泽服装
	Taiga = 6  			# 江河服装

class VirtualWorldObjectType(object):
	Model = 1
	Sfx = 2
	Textboard = 3
	Particle = 4

class WalkState(object):
	Walk = 1   # 移动
	Sneak = 2  # 潜行
	Sprint = 3    # 跑步


class _MinecraftEnum:
	ActorDamageCause = ActorDamageCause
	AniCheatBlockBreak = AniCheatBlockBreak
	AniCheatConsts = AniCheatConsts
	AniCheatMove = AniCheatMove
	AniCheatMoveRewind = AniCheatMoveRewind
	AnimationModeType = AnimationModeType
	ArmorSlotType = ArmorSlotType
	AttrType = AttrType
	AttributeBuffType = AttributeBuffType
	BiomeType = BiomeType
	BlockBreathability = BlockBreathability
	BrewingStandSlotType = BrewingStandSlotType
	ButtonEventType = ButtonEventType
	ButtonState = ButtonState
	CatVariantType = CatVariantType
	Change = Change
	ColorCode = ColorCode
	CommandBlockType = CommandBlockType
	ConditionType = ConditionType
	ContainerType = ContainerType
	EffectType = EffectType
	EnchantSlotType = EnchantSlotType
	EnchantType = EnchantType
	EntityColorType = EntityColorType
	EntityComponentType = EntityComponentType
	EntityTeleportCause = EntityTeleportCause
	EntityType = EntityType
	Facing = Facing
	FoxType = FoxType
	GameDiffculty = GameDiffculty
	GameType = GameType
	GamepadKeyType = GamepadKeyType
	HorseSpotType = HorseSpotType
	HorseType = HorseType
	InputMode = InputMode
	InventoryType = InventoryType
	ItemAcquisitionMethod = ItemAcquisitionMethod
	ItemCategory = ItemCategory
	ItemColor = ItemColor
	ItemPosType = ItemPosType
	ItemType = ItemType
	ItemUseMethodEnum = ItemUseMethodEnum
	KeyBoardType = KeyBoardType
	MirrorModeType = MirrorModeType
	OpenContainerId = OpenContainerId
	OptionId = OptionId
	OriginGUIName = OriginGUIName
	PermissionChangeCause = PermissionChangeCause
	PistonFacing = PistonFacing
	PlayerActionType = PlayerActionType
	PlayerExhauseRatioType = PlayerExhauseRatioType
	PlayerUISlot = PlayerUISlot
	RayFilterType = RayFilterType
	RedstoneModeType = RedstoneModeType
	RenderControllerArrayType = RenderControllerArrayType
	RenderLayer = RenderLayer
	SetBlockType = SetBlockType
	ShapeType = ShapeType
	SliderOptionId = SliderOptionId
	StructureFeatureType = StructureFeatureType
	TimeEaseType = TimeEaseType
	TouchEvent = TouchEvent
	TradeLevelType = TradeLevelType
	TransferServerFailReason = TransferServerFailReason
	UICategory = UICategory
	UiBaseLayer = UiBaseLayer
	UseAnimation = UseAnimation
	VillagerClothingType = VillagerClothingType
	VirtualWorldObjectType = VirtualWorldObjectType
	WalkState = WalkState