# Haydee AI Outfit Generator GUI

A modern graphical user interface for the [Haydee AI Outfit Generator](https://github.com/thegamerbay/haydee-ai-outfit-generator) library. Easily generate custom outfits for Haydee without messing with terminals or environment variables!

## ✨ Features

- **Modern Dark Interface**: Built with `CustomTkinter` for a sleek, game-themed appearance.
- **No Terminal Required**: Configures environment variables and handles logging automatically.
- **Asynchronous Generation**: The UI remains responsive while the outfit is being generated via AI.
- **Standalone Executable**: Easily package the app into a single `.exe` file that any Windows user can run out-of-the-box.

## 🚀 Quick Start (For Users)

1. Download the latest `HaydeeOutfitGenerator.exe` release.
2. Launch the application.
3. Fill in the **Settings** panel:
   - Your **Gemini API Key**.
   - Path to your **Haydee** game installation directory.
4. Click **Save Settings**.
5. In the **Mod Generation** panel, enter a unique mod name and a descriptive style prompt.
6. Click **Generate Outfit** and watch the magic happen in the built-in console window!

*(Note: The app will automatically create a `.env` file next to the `.exe` so you don't have to enter your details every time.)*

## 🛠️ Developer Setup

If you want to contribute or build the application yourself:

### Prerequisites

- Python 3.12+
- Git

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/haydee-outfit-gui.git
   cd haydee-outfit-gui
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application from source:
   ```bash
   python main.py
   ```

### Building the Executable

This project includes an automated script that uses `PyInstaller` to package the app into a standalone `.exe` without a black console window.

To build:
```bash
python build.py
```

After the build completes, your application will be available in the `dist/` folder as `HaydeeOutfitGenerator.exe`.
