# -*- coding: utf-8 -*-

"""
事件的定义。
"""

class ServerEvent:
		"""
		master成功连接到当前服务器事件

		Event Function Args:
			isConnect      int            1代表连接建立，0代表连接中断
			serverId       int            当前lobby/game服务器id

		"""
		MasterConnectStatusEvent = "MasterConnectStatusEvent"

		"""
		不建议开发者使用，强制关闭当前服务器时会触发本事件

		"""
		MasterForceShutDownEvent = "MasterForceShutDownEvent"

		"""
		不建议开发者使用，优雅关闭当前服务器时会触发本事件

		"""
		MasterGraceShutDownEvent = "MasterGraceShutDownEvent"

		"""
		转服失败事件，当玩家试图转服时，没有符合条件的目标服务器时抛出此事件

		Event Function Args:
			uid            int/long       玩家uid，玩家的唯一标识
			reason         int            失败的错误码，serverApi.GetMinecraftEnum().TransferServerFailReason

		"""
		MasterResponseTransferFailServerEvent = "MasterResponseTransferFailServerEvent"

		"""
		转服成功事件，当玩家试图转服时，成功定位到可转服的目标服务器时抛出此事件

		Event Function Args:
			uid            int/long       玩家uid，玩家的唯一标识

		"""
		MasterResponseTransferSucServerEvent = "MasterResponseTransferSucServerEvent"

		"""
		不建议开发者使用，公共配置发生变化时触发本事件，注意只有与本服相关配置发生变化时才会触发本事件，比如日志等级

		"""
		ReloadCommonConfigEvent = "ReloadCommonConfigEvent"

		"""
		玩家登录到lobby/game过程中，获取玩家在线锁事件。事件触发时，玩家还处于开始登录阶段，
	还没有下载行为包，且没有在地图中出生。在线锁实质是redis中记录的玩家在线信息，redis key格式
	是“user:online: + netease uid”，它是个hash表，包含两个hash key:serverid,proxyid

		Event Function Args:
			uid            int/long       玩家的netease uid，玩家的唯一标识
			serverId       int            当前服务器id
			proxyId        int            当前客户端连接的proxy服务器id

		"""
		ServerGetPlayerLockEvent = "ServerGetPlayerLockEvent"

		"""
		创建玩家对象过程中，设置玩家出生位置时触发本事件

		Event Function Args:
			userId         int            玩家的netease uid
			dimensionId    int            玩家出生dimension，支持修改
			posx           int            玩家出生位置，支持修改
			posy           int            玩家出生位置，支持修改
			posz           int            玩家出生位置，支持修改
			deltax         int            玩家motion位置，初始值为存档中的数据。若修改了posx/posy/posz，则建议设置为0。
			deltay         int            玩家motion位置，初始值为存档中的数据。若修改了posx/posy/posz，则建议设置为0。
			deltaz         int            玩家motion位置，初始值为存档中的数据。若修改了posx/posy/posz，则建议设置为0。
			rotx           int            玩家的rot，初始值为存档中的数据，支持修改
			roty           int            玩家的rot，初始值为存档中的数据，支持修改
			ret            bool           是否需要修改玩家初始位置，设置为True后其他数据的修改才会生效
			retRespawn     bool           是否需要设置玩家的重生位置，仅在ret设置True时生效。设置True时，会使用dimensionId，posx，posy，posz设置玩家的重生位置。如果修改了dimensionId，请务必将这个字段设为True，否则可能引起崩溃。

		"""
		ServerPlayerBornPosEvent = "ServerPlayerBornPosEvent"

		"""
		玩家下线过程中，释放在redis中的玩家在线锁事件。事件触发时，客户端同服务端断开了连接，玩
	家数据已经保存到地图，玩家已经不存在于mc的世界中。在线锁实质是redis中记录的玩家在线信息，
	redis key格式是“user:online: + netease uid”，它是个hash表，包含两个hash key:serverid,proxyid

		Event Function Args:
			uid            int/long       玩家的netease uid，玩家的唯一标识

		"""
		ServerReleasePlayerLockEvent = "ServerReleasePlayerLockEvent"

		"""
		不建议开发者使用，游戏强制关闭过程中，玩家强制下线时触发本事件。事件回调函数需要释放在redis中的
	玩家的在线锁

		Event Function Args:
			idx            int            事件唯一id，回调时返回
			uid            int/long       玩家的netease uid，玩家的唯一标识

		"""
		ServerReleasePlayerLockOnShutDownEvent = "ServerReleasePlayerLockOnShutDownEvent"

		"""
		不建议开发者使用，游戏即将强制关闭触发本事件。事件回调函数需要好清理和存档工作，同时终止或强制join所有异步线程

		"""
		ServerWillShutDownEvent = "ServerWillShutDownEvent"

		"""
		service与lobby/game的成功建立连接事件

		Event Function Args:
			serverId       int            service的服务器id
			serviceType    str            service的服务器类型

		"""
		ServiceConnectEvent = "ServiceConnectEvent"

		"""
		service与lobby/game断开连接事件

		Event Function Args:
			serverId       int            service的服务器id

		"""
		ServiceDisconnectEvent = "ServiceDisconnectEvent"

		"""
		不建议开发者使用，service向lobby/game注册module

		Event Function Args:
			serverId       int            service服务器id
			moduleName     str            模块名，是公共配置中module_names中某个module

		"""
		ServiceRegisterModuleEvent = "ServiceRegisterModuleEvent"

		"""
		玩家游戏内购买商品时服务端抛出的事件

		Event Function Args:
			playerId       str            玩家id

		"""
		StoreBuySuccServerEvent = "StoreBuySuccServerEvent"

