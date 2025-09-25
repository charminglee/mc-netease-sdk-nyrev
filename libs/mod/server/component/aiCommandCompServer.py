# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class AiCommandComponentServer(BaseComponent):
    def Enable(self):
        # type: () -> bool
        """
        启用官方魔法指令功能。需要在ClientLoadAddonsFinishServerEvent事件中调用。仅在联机大厅中生效。
        """
        pass

    def Disable(self):
        # type: () -> bool
        """
        关闭官方魔法指令功能。需要在ClientLoadAddonsFinishServerEvent事件中调用。仅在联机大厅中生效。
        """
        pass

