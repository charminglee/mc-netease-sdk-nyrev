<div align="center">

  # 网易我的世界ModSDK补全库修正版  
  **已更新至 3.6 版本，支持Python2与Python3**

</div>

<br>

## 安装

```commandline
pip install mc-netease-sdk-nyrev
```

## 修正列表

### 接口修正

1. 移除所有接口返回值类型上的单引号（完全多余）。
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

### IDE运行支持

1. 实现了`BaseUIControl`的一些方法。
2. 实现了`ScreenNode.GetBaseUIControl()`。
3. 实现了`extraClientApi`和`extraServerApi`的一些方法。

### 其他修正

1. 移除`MC`文件夹（无用文件）、`Meta`与`Preset`文件夹（零件相关模块）。
2. 移除`mod_log`模块。
