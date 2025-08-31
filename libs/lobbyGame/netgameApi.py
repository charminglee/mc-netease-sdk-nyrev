# -*- coding: utf-8 -*-

"""这里是lobbygame的一些通用的接口
"""


def AddGetPlayerLockTask(func):
	# type: (function) -> bool
	"""
	添加获取玩家在线锁时的处理任务，会在玩家刚连接到服务端时执行，在所有任务都完成后，才会继续玩家的登录流程

	Args:
		func           function       处理任务，需要接收两个参数：uid和callback，详见示例

	Returns:
		bool           True:添加成功<br>False:添加失败
	"""
	pass


def ChangeAllPerformanceSwitch(isDisable, extra):
	# type: (bool, list) -> None
	"""
	整体关闭/打开预定义的游戏原生逻辑，所有的逻辑默认状态均为【开】（也就是is_disable=False），
	只有当调用此接口关闭之后，才会进入到【关】的状态，关闭这类原生逻辑能够提
	高服务器的性能，承载更高的同时在线人数，同时也会使一些生存服的玩法失效。另外，强烈建议在服务
	器初始化时调用此接口，同时不要在服务器运行中途修改

	Args:
		is_disable     bool           True代表【关】，False代表【开】
		extra          list           剔除掉不需要改变开关状态的具体功能的枚举值列表。默认为空

	"""
	pass


def ChangePerformanceSwitch(key, isDisable):
	# type: (int, bool) -> None
	"""
	关闭/打开某个游戏原生逻辑，所有的逻辑默认状态均为【开】（也就是is_disable=False），
	只有当调用此接口关闭之后，才会进入到【关】的状态，关闭这类原生逻辑能够提高服务器的性能，
	承载更高的同时在线人数，同时也会使一些生存服的玩法失效。另外，强烈建议在服务器初始化时调用此接口，同时不要在服务器运行中途修改

	Args:
		key            int            具体功能的枚举值，详情见备注
		isDisable      bool           True代表【关】，False代表【开】

	"""
	pass


def CheckMasterExist():
	"""
	检查服务器是否与master建立连接

	Returns:
		bool           是否与master建立连接
	"""
	pass


def DelForbidDragonEggTeleportField(fid):
	# type: (int) -> bool
	"""
	删除禁止龙蛋传送的地图区域

	Args:
		fid            int            区域的唯一ID，必须大于等于0

	Returns:
		bool           是否成功删除（对应fid无法找到返回删除失败）
	"""
	pass


def DelForbidFlowField(fid):
	# type: (int) -> bool
	"""
	删除地图区域，不同的ID的区域边界会阻挡流体的流动

	Args:
		fid            int            区域的唯一ID，必须大于等于0

	Returns:
		bool           是否成功删除（对应fid无法找到返回删除失败）
	"""
	pass


def EnableNetgamePacketIdStatistics(enable):
	# type: (bool) -> None
	"""
	开启（或关闭）玩家向服务器发包的数量统计。长时间不使用数据时请关掉统计，避免内存泄露。

	Args:
		enable         bool           True开启/False关闭

	"""
	pass


def GetAndClearNetgamePacketIdStatistics():
	"""
	获取玩家向服务器发包的数量统计，然后重置统计数据。即每次返回从上一次获取到现在的数量。需要用EnableNetgamePacketIdStatistics开启后才有数据

	Returns:
		dict           key:playerId，value:一个dict表示packetId对应的数量
	"""
	pass


def GetCommonConfig():
	"""
	获取服务器公共配置，包括本服、所有db和所有功能服的配置，具体参见备注，注意可能不包含其他大厅服和游戏服配置，不能获取所有服的配置

	Returns:
		dict           配置内容
	"""
	pass


def GetConnectingProxyIdOfPlayer(playerId):
	# type: (str) -> int
	"""
	获取玩家客户端连接的proxy服务器id

	Args:
		playerId       str            玩家id

	Returns:
		int            proxy服务器id
	"""
	pass


def GetLastFrameTime():
	"""
	获取服务端脚本上一帧运行时间

	Returns:
		int            服务端脚本上一帧运行时间,单位纳秒
	"""
	pass


def GetMongoConfig():
	"""
	获取mongo数据库的连接参数，对应公共配置中mongo配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注

	Returns:
		tuple          (exist, host, user, password, database, port).exist：bool,是否存在mongo数据库配置; host：str, mongo数据库的地址;user：str,mongo数据库的访问用户; port：int, mongo数据库的端口; password：str,mongo数据库的访问密码;database：str,mongo数据库的数据库名
	"""
	pass


def GetMysqlConfig():
	"""
	获取mysql数据库的连接参数，对应公共配置中mysql配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注

	Returns:
		tuple          (exist, host, user, password, database, port).exist：bool,是否存在mysql数据库配置; host：string, mysql数据库的地址;user：string,mysql数据库的访问用户; port：int, mysql数据库的端口; password：string,mysql数据库的访问密码;database：string,mysql数据库的数据库名
	"""
	pass


def GetOnlinePlayerNum():
	"""
	获取当前服务器的在线人数

	Returns:
		int            当前服务器在线人数
	"""
	pass


def GetPlatformUid(playerId):
	# type: (str) -> int/long/None
	"""
	获取玩家登录端的uid，假如玩家从手机端登录，返回手机端的uid，否则返回PC端的uid

	Args:
		playerId       str            玩家id

	Returns:
		int/long/None  玩家不在线时返回None，在线时假如玩家从手机端登录，返回手机端的uid，否则返回PC端的uid
	"""
	pass


def GetPlayerIdByUid(uid):
	"""
	根据玩家uid获取玩家ID（也即playerId）。若玩家不在这个lobby/game，则返回为空字符

	Returns:
		str            玩家id，也即玩家的playerId
	"""
	pass


def GetPlayerIpHash(playerId):
	# type: (str) -> str
	"""
	获取玩家客户端ip的特征哈希值

	Args:
		playerId       str            玩家id

	Returns:
		str            一个32位哈希字符串
	"""
	pass


def GetPlayerLockResult(id, success):
	# type: (int, bool) -> None
	"""
	不建议开发者使用，把获取玩家在线锁结果告知给引擎层

	Args:
		id             int            对应【ServerGetPlayerLockEvent】事件的传入唯一ID
		success        bool           是否成功

	"""
	pass


def GetPlayerNickname(playerId):
	# type: (str) -> str
	"""
	获取玩家的昵称。

	Args:
		playerId       str            玩家id

	Returns:
		str            昵称
	"""
	pass


def GetPlayerUid(playerId):
	# type: (str) -> int/long
	"""
	获取玩家的uid

	Args:
		playerId       str            玩家id

	Returns:
		int/long       玩家的uid；玩家的唯一标识
	"""
	pass


def GetRedisConfig():
	"""
	获取redis数据库的连接参数，对应公共配置中redis配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注

	Returns:
		tuple          (exist, host, port, password).exist：bool,是否存在redis配置; host：str, redis数据库的地址;port：int, redis数据库的端口; password：str,redis数据库的访问密码
	"""
	pass


def GetServerId():
	"""
	获取本服的服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注

	Returns:
		int            服务器id
	"""
	pass


def GetServerProtocolVersion():
	"""
	获取服务器的协议版本号

	Returns:
		int            服务器的协议版本号
	"""
	pass


def GetUidIsSilent(uid):
	"""
	根据玩家uid获取是否被禁言

	Returns:
		int            0:全局禁言，1:普通禁言，2:没有被禁言
	"""
	pass


def HidePlayerFootprint(playerId, hide):
	# type: (playerId, bool) -> bool
	"""
	隐藏某个玩家的会员脚印外观

	Args:
		str            playerId       玩家id
		hide           bool           是否隐藏，True为隐藏脚印，False为恢复脚印显示

	Returns:
		bool           True:设置成功<br>False:设置失败
	"""
	pass


def HidePlayerMagicCircle(playerId, hide):
	# type: (playerId, bool) -> bool
	"""
	隐藏某个玩家的会员法阵外观

	Args:
		str            playerId       玩家id
		hide           bool           是否隐藏，True为隐藏法阵，False为恢复法阵显示

	Returns:
		bool           True:设置成功<br>False:设置失败
	"""
	pass


def IsPlayerPeUser(playerId):
	# type: (str) -> bool/None
	"""
	获取玩家是否从手机端登录

	Args:
		playerId       str            玩家id

	Returns:
		bool/None      玩家不在线时返回None，在线时返回True代表此玩家本次从手机端登录，返回False代表此玩家从PC端登录
	"""
	pass


def IsServiceConnected(serviceId):
	"""
	检查服务器是否与某个service建立连接

	Returns:
		bool           是否与service建立连接
	"""
	pass


def IsShowDebugLog():
	"""
	当前服务器是否打印debug等级的日志

	Returns:
		bool           True，打印debug log，否则不打印debug log
	"""
	pass


def NotifyClientToOpenShopUi(playerId):
	# type: (str) -> None
	"""
	通知客户端打开商城界面

	Args:
		playerId       str            玩家id

	"""
	pass


def RegisterOpCommand(url, callback):
	# type: (str, function) -> None
	"""
	注册一个新的HTTP接口

	Args:
		url            str            接口url
		callback       function       响应HTTP请求的实例函数，参数有两个，第一个参数clientId，类型为int，是请求方的唯一标识，用于返回请求处理结果；第二个参数requestData，类型为dict，包含HTTP请求的参数（requestBody）

	"""
	pass


def ReleasePlayerLockResult(id, success):
	# type: (int, bool) -> None
	"""
	不建议开发者使用，把释放玩家在线锁结果告知给引擎层

	Args:
		id             int            对应【ServerReleasePlayerLockEvent/ServerReleasePlayerLockOnShutDownEvent】事件传入的唯一ID
		success        bool           是否成功

	"""
	pass


def ResetServer():
	"""
	重置服务器

	"""
	pass


def ResponseOpCommandFail(clientId, code, message):
	# type: (int, int, str) -> None
	"""
	发送HTTP的失败Response，支持异步返回，返回时候指定请求传入的clientId

	Args:
		clientId       int            请求唯一id，识别HTTP请求。
		code           int            请求的失败原因code
		message        str            请求的失败原因的文本

	"""
	pass


def ResponseOpCommandSuccess(clientId, entity):
	# type: (int, dict) -> None
	"""
	发送HTTP的成功Response，支持异步返回，返回时候指定请求传入的clientId

	Args:
		clientId       int            请求唯一id，识别HTTP请求。
		entity         dict           请求中需要返回的内容，可自定义key/value的含义

	"""
	pass


def SetAutoRespawn(autoRespawn, internalSeconds, minY, x, y, z):
	# type: (bool, int, int, int, int, int) -> None
	"""
	设置是否启用自动重生逻辑

	Args:
		autoRespawn    bool           是否启用自动重生逻辑
		internalSecondsint            每隔多少秒，检查是否满足自动重生条件
		minY           int            高度低于多少，就会触发自动重生逻辑
		x              int            自动重生逻辑触发后，重生点的坐标
		y              int            自动重生逻辑触发后，重生点的坐标
		z              int            自动重生逻辑触发后，重生点的坐标

	"""
	pass


def SetCityMode(isCityMode):
	# type: (bool) -> None
	"""
	设置游戏为主城模式：包括有无法改变地形，不切换日夜，不改变天气，不刷新生物等限制

	Args:
		isCityMode     bool           是否为主城模式

	"""
	pass


def SetEnableLimitArea(limit, x, y, z, offsetX, offsetZ):
	# type: (bool, int, int, int, int, int) -> None
	"""
	设置地图最大区域，超过区域的地形不再生成

	Args:
		limit          bool           是否启用地区区域限制
		x              int            地图区域的中心点
		y              int            地图区域的中心点
		z              int            地图区域的中心点
		offsetX        int            地图区域在x方向和z方向的最大偏移
		offsetZ        int            地图区域在x方向和z方向的最大偏移

	"""
	pass


def SetForbidDragonEggTeleportField(fid, dimensionId, minPos, maxPos, priority, isForbid):
	# type: (int, int, tuple(int), tuple(int), int, bool) -> bool
	"""
	设置禁止龙蛋传送的地图区域

	Args:
		fid            int            区域的唯一ID，必须大于等于0
		dimensionId    int            区域所在的维度
		minPos         tuple(int)     长方体区域的x，y，z值最小的点，x，y，z为方块的坐标，而不是像素坐标
		maxPos         tuple(int)     长方体区域的x，y，z值最大的点，x，y，z为方块的坐标，而不是像素坐标
		priority       int            区域的优先级，缺损时默认值为0，当一个点位于多个区域包围时，最终会以优先级最高的区域为准
		isForbid       bool           是否禁止龙蛋传送，为了处理嵌套区域之间的权限冲突，只要是独立的区域都需要设置是否禁止龙蛋传送

	Returns:
		bool           是否成功设置
	"""
	pass


def SetForbidFlowField(fid, dimensionId, minPos, maxPos, priority, isForbid):
	# type: (int, int, tuple(int), tuple(int), int, bool) -> bool
	"""
	设置地图区域，不同的ID的区域边界会阻挡流体的流动

	Args:
		fid            int            区域的唯一ID，必须大于等于0
		dimensionId    int            区域所在的维度
		minPos         tuple(int)     长方体区域的x，y，z值最小的点，x，y，z为方块的坐标，而不是像素坐标
		maxPos         tuple(int)     长方体区域的x，y，z值最大的点，x，y，z为方块的坐标，而不是像素坐标
		priority       int            区域的优先级，缺损时默认值为0，当一个点位于多个区域包围时，最终会以优先级最高的区域为准
		isForbid       bool           是否禁止流体流动，为了处理嵌套区域之间的权限冲突，只要是独立的区域都需要设置是否禁止流体流动

	Returns:
		bool           是否设置成功
	"""
	pass


def SetGracefulShutdownOk():
	"""
	不建议开发者使用，设置脚本层的优雅关机逻辑已经执行完毕，引擎可以开始优雅关机了

	"""
	pass


def SetLevelGameType(mode):
	# type: (int) -> None
	"""
	强制设置游戏的玩法模式

	Args:
		mode           int            0生存模式，1创造模式，2冒险模式

	"""
	pass


def SetShowFakeSeed(fakeSeed):
	# type: (int) -> bool
	"""
	在客户端【设置】中，显示虚假的游戏地图种子

	Args:
		fakeSeed       int            想要在客户端显示的虚假的地图种子，必须为正整数，可缺损，缺损时会自动随机一个数字

	Returns:
		bool           执行结果
	"""
	pass


def SetShutdownOk():
	"""
	不建议开发者使用，设置脚本层的强制关机逻辑已经执行完毕，引擎可以开始强制关机了

	"""
	pass


def ShieldPlayerJoinText(bShield):
	# type: (bool) -> None
	"""
	是否屏蔽客户端左上角 “xxx 加入了游戏”的提示

	Args:
		bShield        bool           True，不显示提示；False，显示提示

	"""
	pass


def ShutdownServer():
	"""
	强制关机

	"""
	pass


def StartChunkProfile():
	"""
	开始启动服务端区块读写性能统计，启动后调用[StopChunkProfile](#StopChunkProfile)即可获得近期的服务端区块读写信息

	Returns:
		bool           执行结果
	"""
	pass


def StopChunkProfile():
	"""
	结束服务端区块读写性能统计，并返回近期区块读写信息，与[StartChunkProfile](#StartChunkProfile)配合使用

	Returns:
		list(dict)     每个字典都是1秒内的区块读写信息，按照时间线排序，timestamp：类型为int，统计的具体时间（秒）；saveChunks：类型为list(dict)，1秒内写chunk的坐标和维度；loadChunks：类型为list(dict)，1秒内读chunk的坐标和维度
	"""
	pass


def StopShowFakeSeed():
	"""
	在客户端【设置】中，显示真实的游戏地图种子

	Returns:
		bool           执行结果
	"""
	pass


def TransferToOtherServer(playerId, typeName, transferParam, callback):
	# type: (str, str, str, function) -> None
	"""
	玩家转移到指定类型的服务器，假如同类服务器有多个，就根据负载均衡选择一个

	Args:
		playerId       str            玩家id
		typeName       str            目标服务器的类型，对应MCStudio中配置：服务器配置->游戏配置->类型
		transferParam  str            切服传入参数，默认空字符串。当玩家跳转到目标服务器触发AddServerPlayerEvent事件时，AddServerPlayerEvent事件会携带这个参数
		callback       function       回调函数，返回转服API经过master的逻辑判定之后的结果，参数有三个，isSuc(bool), reasonCode(int), message(str)，isSuc返回是否成功；reasonCode代表失败的错误码，message为失败的理由的中文描述

	"""
	pass


def TransferToOtherServerById(playerId, serverId, transferParam, callback):
	# type: (str, str, str, function) -> None
	"""
	玩家迁移到指定服务器id的服务器

	Args:
		playerId       str            玩家id
		serverId       str            目标服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
		transferParam  str            切服传入参数，默认空字符串。当玩家跳转到目标服务器触发AddServerPlayerEvent事件时，AddServerPlayerEvent事件会携带这个参数
		callback       function       回调函数，返回转服API经过master的逻辑判定之后的结果，参数有三个，isSuc(bool), reasonCode(int), message(str)，isSuc返回是否成功；reasonCode代表失败的错误码，message为失败的理由的中文描述

	"""
	pass


def TryToKickoutPlayer(playerId, message):
	# type: (str, str) -> None
	"""
	把玩家踢下线，message中的文字会显示在客户端的断线提示中

	Args:
		playerId       str            玩家对象的entityId
		message        str            踢掉玩家的理由，默认为空

	"""
	pass


def UnRegisterOpCommand(url):
	# type: (str) -> None
	"""
	注销一个已注册的HTTP接口

	Args:
		url            str            接口url

	"""
	pass

