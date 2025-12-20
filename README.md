<div align="center">

  # 网易我的世界 [ModSDK](https://mc.163.com/dev/index.html) 补全库修正版  
  **已更新至 3.6 版本，支持 Python2 与 Python3**

</div>

<br>

## 安装

```commandline
pip install mc-netease-sdk-nyrev
```

## 修正列表

### 接口修正

1. 移除所有接口返回值类型上的单引号。
2. 删除文档注释中多余的网址。
3. 补充`BaseUIControl.__init__()`。
4. 补充`ScreenNode.__init__()`。
5. 修复`EngineCompFactoryClient.CreateDrawing()`的返回值类型错误导致无法补全的问题。
6. 修复`EngineCompFactoryClient.CreateDimension()`的返回值类型错误导致无法补全的问题。
7. 修复`DrawingCompClient`一系列接口的返回值类型错误导致无法补全的问题。
8. 补充`mcmath`模块的类型注解。
9. 补充`mod`模块的类型注解。
10. 优化`baseSystem`模块的类型注解。
11. 补充`BlockEntityData`的类型注解。
12. 补充`CustomUIControlProxy`的类型注解。
13. 补充`CustomUIScreenProxy`的类型注解。
14. 补充缺失的`miniMapBaseScreen`模块。
15. 补充`NativeScreenManager`的类型注解。
16. 补充`ViewBinder`的类型注解。
17. 优化`BaseUIControl`的类型注解。
18. 优化`ButtonUIControl`的类型注解。
19. 优化`NeteaseComboBoxUIControl`的类型注解。
20. 优化`NeteasePaperDollUIControl`的类型注解。
21. 优化`SelectionWheelUIControl`的类型注解。
22. 优化`extraClientApi`模块的类型注解。
23. 优化`extraServerApi`模块的类型注解。
24. 优化各component类的类型注解。
25. 修复`NativeScreenManager`的补全问题。
26. 部分格式固定的字典（如物品信息字典、附魔信息字典）使用`TypedDict`表示，以支持对字典key的补全（目前仅Python3支持该功能）。
27. 用`Literal`表示枚举值参数。
28. 优化`illustratedBook`各模块的类型注解。
29. 优化了`apolloCommon`、`lobby`、`lobbyGame`、`master`、`service`各模块的类型注解。
30. 补充富文本控件实例`RichTextItem`相关补全。

### 其他修正

1. 移除`MC`文件夹（未知用途）。
2. 移除`Meta`与`Preset`文件夹（零件/预设相关模块，官方已停止维护）。

## IDE设置优化

通过对 [PyCharm](https://www.jetbrains.com/zh-cn/pycharm/) 进行设置，可在接口的文档注释中自动显示网易文档链接，点击链接即可跳转到该接口对应的网易文档。

<img src="/img/20FC8BF4C775212B968365E95DB52A0F.jpg" width="528" alt="">

设置步骤如下：  
1. 按快捷键 Ctrl+Alt+S 打开设置；
2. 找到 Python | External Documentation（外部文档）；
3. 点击加号，在 Module Name（模块名称）中输入`mod`，在 URL/Path Pattern（URL/路径模式）中输入以下网址：
   ```
   https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%8E%A5%E5%8F%A3/Api%E7%B4%A2%E5%BC%95%E8%A1%A8.html?key={function.name}&docindex=2&type=0
   ```
4. 最后点击 OK（确定）即可。
