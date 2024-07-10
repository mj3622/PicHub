# PicHub
PicHub 是一个基于 GitHub 的图床服务，允许用户将图片上传到 GitHub 仓库并生成对应的链接，方便在网页或应用程序中引用这些图片。

# 功能
- **上传图片：** 允许用户将本地图片上传至指定仓库
- **生成链接：** 自动为上传的图片生成可访问的链接

# 使用方法
我们共提供了两种安装方法，您可以根据自己的喜好进行选择

具体的程序使用方法可以参考[使用手册](./docs/使用手册.md)
## 1. 使用提供的exe文件（推荐）
访问 [Release](https://github.com/mj3622/PicHub/releases) 页面，找到最新版本的 `PicHub.exe`程序，下载后无需安装，可直接使用

## 2. 克隆项目
将项目克隆到本地
```sh
git clone https://github.com/mj3622/PicHub.git
cd pichub
```

安装需要的依赖
```sh
pip install -r requirements.txt
```

运行主程序
```python
python main.py
```

# 常见问题
**如何获取token？**

可参考文档[获取token的方法](./docs/获取token.md)


# 未来计划
1. 提供Web版本的服务
2. 优化桌面的的UI
3. 完善对图片的管理功能


# 贡献
欢迎贡献代码，提交 issue 或提出建议