# -*- coding: utf-8 -*-

"""下面是公共的接口
"""


def AddRepeatedTimer(delay, func, *args, **kwargs):
	# type: (float, func, *args, **kwargs) -> timer
	"""
	添加服务端触发的定时器，重复执行

	Args:
		delay          float          延迟时间，单位秒
		func           func           定时器触发函数
		*args          *args          变长参数，可以不设置
		**kwargs       **kwargs       字典变长参数，可以不设置

	Returns:
		timer          返回单次触发的定时器
	"""
	pass


def AddTimer(delay, func, *args, **kwargs):
	# type: (float, func, *args, **kwargs) -> timer
	"""
	添加服务端触发的定时器，非重复

	Args:
		delay          float          延迟时间，单位秒
		func           func           定时器触发函数
		*args          *args          变长参数，可以不设置
		**kwargs       **kwargs       字典变长参数，可以不设置

	Returns:
		timer          返回单次触发的定时器
	"""
	pass


def CancelTimer(timer):
	# type: (timer对象) -> None
	"""
	取消定时器

	Args:
		timer          timer对象    AddTimer和AddRepeatedTimer时返回的定时器对象

	"""
	pass


def ChangeDatabaseSlowLogLimit(db, interval):
	# type: (str, float) -> bool
	"""
	修改数据库连接池慢请求报警日志限定时间

	Args:
		db             str            数据库连接池类型，mysql/redis/mongo
		interval       float          慢请求限制时间，单个请求返回时间超过这个值就会记录慢请求日志，单位秒，mysql和mongo默认配置值为1.0秒，redis默认配置为0.1秒

	Returns:
		bool           执行结果
	"""
	pass


def CheckNameValid(name):
	# type: (str) -> int
	"""
	判定一个输入的string是否通过了命名库敏感词检查，没有敏感词返回1，存在敏感词返回0

	Args:
		name           str            需要做敏感词检查的string

	Returns:
		int            1代表没有敏感词，0代表存在敏感词
	"""
	pass


def CheckWordsValid(words):
	# type: (str) -> int
	"""
	判定一个输入的string是否通过了通用库敏感词检查，没有敏感词返回1，存在敏感词返回0

	Args:
		words          str            需要做敏感词检查的string

	Returns:
		int            1代表没有敏感词，0代表存在敏感词
	"""
	pass


def CloseAsyncTaskSlowCheck():
	"""
	停止每帧检查异步线程池中的任务

	Returns:
		bool           执行结果
	"""
	pass


def ConvertBsonToInt(input):
	# type: (dict/list/tuple/str/unicode) -> dict/list/tuple/str/unicode
	"""
	递归转换输入数据中的所有bson.int64.Int64类型的对象为int类型

	Args:
		input          dict/list/tuple/str/unicode需要转换的输入数据

	Returns:
		dict/list/tuple/str/unicode和输入数据格式相同，其中bson.int64.Int64类型的对象会被转换为int类型
	"""
	pass


def DumpAsyncTaskPool():
	"""
	打印当前异步线程池中的正在排队和执行中的任务信息

	Returns:
		bool           执行结果
	"""
	pass


def GetApolloGameId():
	"""
	获取游戏当前项目的gameId（商城查询订单时需要）

	Returns:
		int            游戏当前项目的gameId
	"""
	pass


def GetApolloGameKey():
	"""
	获取游戏当前项目的gameKey（商城查询订单时需要）

	Returns:
		int            游戏当前项目的gameKey
	"""
	pass


def GetApolloReviewStage():
	"""
	获取游戏当前审核阶段

	Returns:
		int            0 测试阶段，1 审核阶段 2 上线阶段
	"""
	pass


def GetApolloUniqueId():
	"""
	获取游戏当前项目唯一ID

	Returns:
		int            游戏当前项目唯一ID
	"""
	pass


def GetModJsonConfig(scriptRootName):
	# type: (str) -> dict
	"""
	根据脚本根目录读取mod.json配置文件。要求mod已经被加载

	Args:
		scriptRootName str            python脚本的根目录名

	Returns:
		dict           mod.json里面的内容信息
	"""
	pass


def GetModJsonConfigByName(scriptRootName, pathFile):
	# type: (str, str) -> dict
	"""
	读取基于脚本根目录的[pathFile]路径下的json格式配置文件

	Args:
		scriptRootName str            python脚本的根目录名
		pathFile       str            相对于python脚本的根目录的文件名（包括相对路径）

	Returns:
		dict           对应目录下json文件里面的内容信息
	"""
	pass


def GetModScriptRootDir(scriptRootName):
	# type: (str) -> str
	"""
	获取脚本根目录的绝对路径。要求mod已经被加载

	Args:
		scriptRootName str            python脚本的根目录名

	Returns:
		str            脚本根目录的绝对路径
	"""
	pass


def GetOnlineKey(uid):
	# type: (int/long) -> str
	"""
	输入玩家uid，返回此玩家保存在redis中的在线标识的key

	Args:
		uid            int/long       玩家的uid

	Returns:
		str            此玩家保存在redis中的在线标识的key；它是个hash表，包含两个hash key:serverid,proxyid，假如无法获取到或者只获取到proxyid获取不到serverid，说明此玩家当前不在线
	"""
	pass


def GetOnlineServerInfoOfMultiPlayers(uids, callback):
	# type: (list(int/long), function) -> None
	"""
	获取多个玩家在线信息

	Args:
		uids           list(int/long) 玩家的netease uid列表，列表不能超过100，若超过100，本api会抛出Exception
		callback       function       回调函数，该函数会被异步执行。函数只需要一个参数，是list(dict)类型。每个dict包含的键以及含义说明："uid":玩家的netease uid；      "serverId"：玩家所在lobby或game的服务器id， 若玩家不在线则为None;"proxyId"：客户端连接的proxy服务器id， 若玩家不在线则为None;     "protocolVersion"：玩家客户端协议版本号， 若玩家不在线则为None

	"""
	pass


def GetOnlineServerInfoOfPlayer(uid, callback):
	# type: (int/long, function) -> None
	"""
	获取玩家在线信息

	Args:
		uid            int/long       玩家的netease uid，玩家的唯一标识
		callback       function       回调函数，该函数会被异步执行。函数只需要一个参数，是dict类型。dict包含的键以及含义说明："uid":玩家的netease uid；  "serverId"：玩家所在lobby或game的服务器id， 若玩家不在线则为None;"proxyId"：客户端连接的proxy服务器id， 若玩家不在线则为None；   "protocolVersion"：玩家客户端协议版本号， 若玩家不在线则为None

	"""
	pass


def GetServerType():
	"""
	获取本服的服务器类型，对应MCStudio中配置：服务器配置->游戏配置->类型

	Returns:
		str            服务器类型
	"""
	pass


def GetWeekOnlineKey(uid, week):
	# type: (int/long) -> str
	"""
	输入玩家uid，返回此玩家保存在redis中的本周的在线时间

	Args:
		uid            int/long       玩家的uid

	Returns:
		str            此玩家保存在redis中的本周在线时间的key；它是个string，转化为int后就是此玩家本周在线时间的秒数
	"""
	pass


def OpenAsyncTaskSlowCheck(interval):
	# type: (float) -> bool
	"""
	启动每帧检查异步线程池中的任务，并且打印执行时间超过指定时间且尚未完成的任务，此功能消耗较大，仅建议在测试阶段和遇到线上紧急问题时启用

	Args:
		interval       float          任务限制时间，单个任务进入异步线程池排队+执行时间超过此时间还没有完成的，会以warning日志的形式输出

	Returns:
		bool           执行结果
	"""
	pass


def StartDatabaseProfile(db):
	# type: (str) -> bool
	"""
	开始记录数据库连接池请求信息统计，启动后调用[StopDatabaseMysqlProfile(db)](#StopDatabaseMysqlProfile)即可获取两个函数调用之间数据库连接池请求记录信息

	Args:
		db             str            数据库连接池类型，mysql/redis/mongo

	Returns:
		bool           执行结果
	"""
	pass


def StartYappiProfile():
	"""
	开始启动服务端脚本性能分析，启动后调用[StopYappiProfile(path)](#StopYappiProfile)即可在路径path生成函数性能火焰图

	Returns:
		bool           执行结果
	"""
	pass


def StopDatabaseMysqlProfile(db):
	# type: (str) -> list
	"""
	停止记录数据库连接池请求信息并输出统计结果，与[StartDatabaseProfile(db)](#StartDatabaseProfile)配合使用，输出结果为字典，具体见示例

	Args:
		db             str            数据库连接池类型，mysql/redis/mongo

	Returns:
		list           数据库连接池请求统计信息，具体见示例，假如没有调用过StartDatabaseProfile，则返回为None
	"""
	pass


def StopYappiProfile(fileName):
	# type: (str) -> bool
	"""
	停止服务端脚本性能分析并生成火焰图，与[StartYappiProfile()](#StartYappiProfile)配合使用

	Args:
		fileName       str            具体路径，相对于Apollo服务端启动目录的路径，默认为"flamegraph.svg"，位于Apollo服务端启动目录下，自定义路径请确保文件后缀名为".svg"

	Returns:
		bool           执行结果
	"""
	pass


def ToPcUid(uid):
	# type: (int/long) -> int/long
	"""
	将玩家的uid转换为pc平台的uid

	Args:
		uid            int/long       玩家的uid

	Returns:
		int/long       pc平台的玩家uid
	"""
	pass


def ToPeUid(uid):
	# type: (int/long) -> int/long
	"""
	将玩家的uid转换为pe平台的uid

	Args:
		uid            int/long       玩家的uid

	Returns:
		int/long       pe平台的玩家uid
	"""
	pass


def UnicodeConvert(input):
	# type: (dict/list/tuple/str/unicode) -> dict/list/tuple/str/unicode
	"""
	递归转换输入数据中的所有unicode格式的字符串为utf-8格式

	Args:
		input          dict/list/tuple/str/unicode需要转换的输入数据

	Returns:
		dict/list/tuple/str/unicode和输入数据格式相同，其中的unicode格式的字符串会被转换为utf-8格式
	"""
	pass

