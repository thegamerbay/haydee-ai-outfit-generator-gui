> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [中文](README.zh.md) | [Español](README.es.md) | [العربية](README.ar.md)

# Haydee AI 服装生成器 GUI

[![Build Test](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/ci.yml)
[![Build and Release EXE](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/release.yml)
[![Run Tests](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/tests.yml)
[![Lint](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml/badge.svg)](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/thegamerbay/haydee-ai-outfit-generator-gui)

[Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator) 库的现代图形用户界面。轻松为 Haydee 生成自定义服装，无需再与终端或环境变量纠缠！

### 📥 [点击此处下载最新的 HaydeeOutfitGenerator.exe](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)

<img src="assets/gui-generate-outfit.png" width="852" alt="GUI Generate Outfit Preview">
<img src="assets/gui-prompt-ideas.png" width="852" alt="GUI Prompt Ideas Preview">
<img src="assets/gui-group-mods.png" width="852" alt="GUI Group Mods Preview">

## 🖼️ 生成示例

看看你能创造出什么！以下服装是使用此工具生成的，并已收录于 Steam 创意工坊的 [Haydee: Tropical Harvest (Fruit-Themed Outfit Pack)](https://steamcommunity.com/sharedfiles/filedetails/?id=3677290023) 模组中。

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

- **现代深色界面**：使用 `CustomTkinter` 构建，拥有极具游戏风格的时尚外观。
- **两种独特的工作流**：无缝切换通过 AI 生成全新服装或将现有模组组合打包为单一的多重模组。
- **精细的生成控制**：可单独切换生成漫反射（颜色）、高光（材质/光泽）和法线（3D 凹凸）贴图，以节省 API 请求或重新生成特定部分。
- **可自定义的 AI 模型**：精确选择处理请求的 Gemini AI 模型（例如 `gemini-3.1-flash-image-preview` 或其他支持的模型）。
- **网络弹性**：内置 10 分钟 SDK 超时补丁和自动 3 次 API 重试循环，确保您的生成任务不会因临时性的 Google API 服务器拥堵或 `503/504 Deadline Exceeded` 错误而失败。
- **无需终端**：自动配置所有路径并处理日志记录。
- **异步处理**：在使用 AI 生成服装或打包模组时，用户界面始终保持响应。
- **独立可执行文件**：轻松将应用程序打包为单一的 `.exe` 文件，任何 Windows 用户皆可开箱即用。

## 🚀 快速入门（面向用户）

1. [下载最新发布的 `HaydeeOutfitGenerator.exe`](https://github.com/thegamerbay/haydee-ai-outfit-generator-gui/releases)。
2. 启动应用程序。
3. 填写 **Settings**（设置）面板：
   - 您的 **Gemini API Key**（Gemini API 密钥）。
   - 您的 **Haydee** 游戏安装目录路径。
   - 您的 **Author Name**（作者名称，可选，将应用于所有生成或打包的模组）。
   - 您选择的 **AI Model**（AI 模型，默认为 `gemini-3.1-flash-image-preview`）。
4. 点击 **Save Settings**（保存设置）。
5. 选择您的工作流选项卡：
   - **✨ Generate Outfit**（生成服装）：在开始之前，输入一个唯一的模组名称、描述性的风格提示词，并切换您希望生成的贴图（漫反射、高光或法线）。
   - **📦 Group Mods**（打包模组）：将多个现有模组组合成一个多重模组。输入新的多重模组名称、要组合的源模组（例如 `red, green, blue`）以及插槽类别（例如 `color`）。
6. 点击 **Start Generation**（开始生成）或 **Group Outfits**（打包服装），在内置的控制台窗口中见证奇迹的发生！

*(注：应用程序会自动将您的设置保存在 `AppData/Local/HaydeeOutfitGenerator/settings.json` 中，因此您无需每次都重新输入详细信息。)*

### 🔑 获取 Gemini API 密钥

1. 前往 [Google AI Studio](https://aistudio.google.com/)。
2. 使用您的 Google 账号登录。
3. 点击 "Create API key"（创建 API 密钥）按钮。
4. 如果出现提示，请阅读并接受服务条款。
5. 点击 "Create API key in new project"（在新项目中创建 API 密钥）（或使用现有项目）。
6. 复制生成的密钥。您需要将其粘贴到应用程序的 **Settings**（设置）面板中。

## 🛠️ 开发者设置

如果您想参与贡献或自行构建此应用程序：

### 前置要求

- Python 3.12+
- Git

### 安装

1. 克隆此仓库：
   ```bash
   git clone https://github.com/thegamerbay/haydee-ai-outfit-generator-gui.git
   cd haydee-ai-outfit-generator-gui
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 从源码运行应用程序：
   ```bash
   python main.py
   ```

### 构建可执行文件

本项目包含一个自动化脚本，该脚本使用 `PyInstaller` 将应用程序打包为独立的 `.exe` 文件，且不显示黑色的控制台窗口。

执行构建：
```bash
python build.py
```

构建完成后，您的应用程序将生成在 `dist/` 文件夹中，文件名为 `HaydeeOutfitGenerator.exe`。

### 运行测试

本项目包含使用 `pytest` 和 `pytest-mock` 编写的自动化 GUI 测试。

1. 安装测试依赖：
   ```bash
   pip install -r requirements-dev.txt
   ```

2. 运行测试：
   ```bash
   pytest tests/
   ```

### 运行代码检查 (Linting)

本项目使用 `flake8` 来强制规范代码风格。

1. 确保已安装测试依赖：
   ```bash
   pip install -r requirements-dev.txt
   ```

2. 运行代码检查工具：
   ```bash
   flake8 src tests main.py build.py
   ```

## 📄 许可证

本项目基于 MIT 许可证开源 - 详情请参阅 [LICENSE](LICENSE) 文件。