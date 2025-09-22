<div align="center">

  # 网易我的世界ModSDK补全库修正版  
  **已更新至 3.5 版本，支持Python2与Python3**

</div>

<br>

## 安装

```commandline
pip install mc-netease-sdk-nyrev
```

## 修正列表

### 接口修正

1. 移除所有接口返回值类型上的单引号（完全多余）。
2. `class EngineCompFactoryClient():` -> `class EngineCompFactoryClient(object):`。
3. 修复`EngineCompFactoryClient.CreateDrawing()`的返回值类型错误导致无法补全的问题。
4. 修复`EngineCompFactoryClient.CreateDimension()`的返回值类型错误导致无法补全的问题。
5. 补充`BaseUIControl.__init__()`。
6. 补充`ScreenNode.__init__()`。
7. `CustomUIScreenProxy`的父类改为`object`。
8. 修复`DrawingCompClient`一系列接口的返回值类型错误导致无法补全的问题。

### IDE运行支持

1. 实现了`BaseUIControl`的一些方法。
2. 实现了`ScreenNode.GetBaseUIControl()`。
3. 实现了`extraClientApi`和`extraServerApi`的一些方法。

### 其他修正

1. 移除`MC`文件夹（无用文件）、`Meta`与`Preset`文件夹（零件相关模块）。
2. 移除`mod_log.py`模块。
