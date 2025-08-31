<div align="center">

  # 网易我的世界ModSDK补全库修正版  
  **已更新至 3.5 版本**

</div>

<br>

## 安装

```commandline
pip install mc-netease-sdk-nyrev
```

## 修订列表

1. 移除`MC`文件夹（无用文件）、`Meta`与`Preset`文件夹（零件相关模块）。
2. 移除所有接口返回值类型上的单引号（完全多余）。
3. `class EngineCompFactoryClient():` -> `class EngineCompFactoryClient(object):`
4. 修复`EngineCompFactoryClient.CreateDrawing()`的返回值类型错误：`drawingCompClient` -> `DrawingCompClient`
5. 修复`EngineCompFactoryClient.CreateDimension()`的返回值类型错误：`dimensionCompClient` -> `DimensionCompClient`
