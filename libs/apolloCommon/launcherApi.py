# -*- coding: utf-8 -*-

"""下面获取启动器信息的接口
"""


def ApplyUserFriend(requestUID, appliedUID, message, callback):
	# type: (int, int, str, function) -> None
	"""
	**Lobby/Game接口**，申请添加为启动器中的好友

	Args:
		requestUID     int            玩家的uid
		appliedUID     int            被申请添加好友玩家的uid
		message        str            申请的好友的描述信息
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段b_success，b_success表示申请是否成功。

	"""
	pass


def GetPcGameUserLike(uid, callback):
	# type: (int/long, function) -> None
	"""
	**Master/Service/Lobby/Game接口**，获取玩家是否点赞了当前网络服（仅支持PC玩家）

	Args:
		uid            int/long       玩家的pc uid
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段is_like，值为bool，表示玩家是否点赞

	"""
	pass


def GetPeGameUserStars(uid, callback):
	# type: (int/long, function) -> None
	"""
	**Master/Service/Lobby/Game接口**，获取玩家对本游戏的评分

	Args:
		uid            int/long       玩家的uid
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段stars，表示玩家评分，评分正常范围为1-5，值为-1表示没有评分数据。

	"""
	pass


def GetUIDByNickname(nickname, callback):
	# type: (str, function) -> None
	"""
	**Master/Service/Lobby/Game接口**，根据玩家昵称获取玩家uid

	Args:
		nickname       str            玩家昵称，要求是utf8编码
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段uid，表示玩家的uid。

	"""
	pass


def GetUserAuthInfo(uid, callback):
	# type: (int/long, function) -> None
	"""
	**Master/Service/Lobby/Game接口**，获取在线玩家实名制、是否绑定信息

	Args:
		uid            int/long       玩家的uid
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含下面字段：b_real_name表示玩家是否实名制,        id_hash表示玩家身份的唯一标识，未实名时为空（多个账号可以绑定到一个身份证，可以通过这个字段判断多个账号是否绑定到一个身份），        b_bind_phone表示玩家是否绑定手机

	"""
	pass


def GetUserFriend(uid, callback):
	# type: (int/long, function) -> None
	"""
	**Master/Service/Lobby/Game接口**，获取启动器中玩家好友信息

	Args:
		uid            int/long       玩家的uid
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段friend_uids，friend_uids对应内容是个list，对应好友玩家uid列表。

	"""
	pass


def GetUserGuest(uid, callback):
	# type: (int/long, function) -> None
	"""
	**Master/Service/Lobby/Game接口**，获取启动器中玩家是否游客的信息, 此接口已废弃

	Args:
		uid            int/long       玩家的uid
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段guest，表示玩家是否游客，字段意义 0：非游客，1：游客，2：不确定。

	"""
	pass


def GetUsersVIP(uids, callback):
	# type: (list(int/long), function) -> None
	"""
	**Master/Service/Lobby/Game接口**，获取启动器中玩家会员信息

	Args:
		uids           list(int/long) 玩家的uid列表，列表长度不超过20
		callback       function       回调函数，该函数会被异步执行。函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；        "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段users_vip，users_vip对应内容是个dict，key表示玩家uid，value表示是否是vip。

	"""
	pass


def IsGameUnderMaintenance(callback):
	# type: (function) -> None
	"""
	**Master/Service/Lobby/Game接口**，游戏是否在维护中

	Args:
		callback       function       回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段b_maintain，表示玩家的是否维护中。

	"""
	pass


def ShareApolloGame(uid, message):
	# type: (int/long, str) -> bool
	"""
	**Lobby/Game接口**，在RN上拉起“网络游戏分享”的界面，界面包含游戏ICON以及描述

	Args:
		uid            int/long       玩家的uid
		message        str            分享的描述信息，不能超过20个字符，要求传入utf8字符串

	Returns:
		bool           拉起分享界面是否成功。False：存在敏感词或游戏ID为0或玩家不在线或分享信息超过20个字符
	"""
	pass

