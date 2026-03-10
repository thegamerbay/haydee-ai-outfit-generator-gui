> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI 服装生成器 GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

[Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator) 库的现代化图形用户界面。轻松为 Haydee 生成自定义服装，无需再被终端或环境变量困扰！

### 📥 [在此下载最新的 HaydeeOutfitGenerator.exe](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

![GUI Generate Outfit Preview](assets/gui-generate-outfit.png)
![GUI Group Mods Preview](assets/gui-group-mods.png)

## 🖼️ 生成示例

看看你能创造什么！以下服装是使用此工具生成的，并被收录在 Steam 创意工坊的 [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) 模组中。

<p align="center">
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_berry_juice.jpg" alt="Berry Juice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_citrus_spark.jpg" alt="Citrus Spark"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_cyber_banana.jpg" alt="Cyber Banana"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_dragon_bite.jpg" alt="Dragon Bite"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_golden_pine.jpg" alt="Golden Pine"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_kiwi_slice.jpg" alt="Kiwi Slice"></a>
  <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023"><img src="assets/gen_preview_melon_crush.jpg" alt="Melon Crush"></a>
</p>

## ✨ 特性

- **现代深色界面**：基于 `CustomTkinter` 构建，拥有时尚的、契合游戏主题的外观。
- **三种独特的工作流**：在通过 AI 生成全新服装、获取款式创意灵感以及将现有模组打包为单个多合一模组（multi-mods）之间无缝切换。
- **精细的生成控制**：单独切换生成漫反射（Diffuse/颜色）、高光（Specular/材质光泽）和法线（Normal/3D 凹凸）贴图，以节省 API 请求次数或重新生成特定部分。
- **可自定义的 AI 模型**：精确选择处理您请求的 Gemini AI 模型（例如 `gemini-3.1-flash-image-preview` 或其他支持的模型）。
- **网络容错性**：内置 10 分钟 SDK 超时补丁和自动 3 次 API 重试循环，确保您的生成不会因暂时的 Google API 服务器拥堵或 `503/504 Deadline Exceeded` 错误而失败。
- **无需终端**：自动配置所有路径并处理日志记录。
- **异步处理**：在通过 AI 生成服装或打包模组时，用户界面保持响应。
- **独立可执行文件**：轻松将应用程序打包为单个 `.exe` 文件，任何 Windows 用户都能开箱即用。

## 🚀 快速入门（面向用户）

1. [下载最新的 `HaydeeOutfitGenerator.exe` 发布版本](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)。
2. 启动应用程序。
3. 填写 **设置（Settings）** 面板：
   - 您的 **Gemini API 密钥（API Key）**。
   - **Haydee** 游戏安装目录的路径。
   - 您的 **作者名称（Author Name）**（可选，将应用于所有生成或打包的模组）。
   - 您的 **AI 模型**（默认为 `gemini-3.1-flash-image-preview`）。
4. 点击 **保存设置（Save Settings）**。
5. 选择您的工作流选项卡：
   - **✨ 生成服装（Generate Outfit）**：在开始之前，输入一个独一无二的模组名称、一段描述性风格提示词，并选择您要生成的贴图（漫反射、高光或法线）。
   - ** 提示词创意（Prompt Ideas）**：没有灵感？输入一个简单的主题（如“赛博朋克”），即可获取 AI 生成的服装概念设计。一键将创意直接应用到生成器中。
   - **📦 打包模组（Group Mods）**：将多个现有模组组合成一个多合一模组。输入新的多合一模组名称、要打包的源模组（例如 `red, green, blue`），以及槽位类别（例如 `color`）。
6. 点击 **开始生成（Start Generation）**、**生成提示词创意（Generate Prompt Ideas）** 或 **打包服装（Group Outfits）**，然后在内置的控制台窗口中见证奇迹的发生！

*（注：应用程序会自动将您的设置保存在 `AppData/Local/HaydeeOutfitGenerator/settings.json` 中，这样您就不必每次都输入详细信息了。）*

### 🔑 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://aistudio.google.com/)。
2. 使用您的 Google 账号登录。
3. 点击“Create API key”（创建 API 密钥）按钮。
4. 如果出现提示，请阅读并接受服务条款。
5. 点击“Create API key in new project”（在新项目中创建 API 密钥）或使用现有项目。
6. 复制生成的密钥。您需要将其粘贴到应用程序的 **设置（Settings）** 面板中。

## 🛠️ 开发者设置

如果您想参与贡献或自行构建应用程序：

### 前置要求

- Python 3.12+
- Git

### 安装

1. 克隆此仓库：
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. 安装依赖项：
   ```bash
   pip install -r requirements.txt
   ```

3. 从源代码运行应用程序：
   ```bash
   python main.py
   ```

### 构建可执行文件

本项目包含一个自动化脚本，该脚本使用 `PyInstaller` 将应用程序打包成一个独立、无黑框控制台窗口的 `.exe` 文件。

如需构建：
```bash
python build.py
```

构建完成后，您的应用程序将出现在 `dist/` 文件夹中，文件名为 `HaydeeOutfitGenerator.exe`。

### 运行测试

本项目包含使用 `pytest` 和 `pytest-mock` 编写的自动化 GUI 测试。

1. 安装测试依赖项：
   ```bash
   pip install -r requirements-dev.txt
   ```

2. 运行测试：
   ```bash
   pytest tests/
   ```

### 运行代码检查 (Linting)

本项目使用 `flake8` 来强制执行代码风格。

1. 确保已安装测试依赖项：
   ```bash
   pip install -r requirements-dev.txt
   ```

2. 运行代码检查器：
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 许可证

本项目基于 MIT 许可证开源 - 详情请参阅 [LICENSE](LICENSE) 文件。