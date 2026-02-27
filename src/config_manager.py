import os
import json
from pathlib import Path

class ConfigManager:
    def __init__(self):
        # Get path to AppData/Local on Windows (or ~/.local/share on Linux)
        app_data = os.getenv('LOCALAPPDATA', os.path.expanduser('~'))
        self.config_dir = Path(app_data) / "HaydeeOutfitGenerator"
        self.config_file = self.config_dir / "settings.json"
        
        # Default settings
        self.config = {
            "gemini_api_key": "",
            "haydee_path": "",
            "image_resolution": "4K"
        }
        self.load()

    def load(self):
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config.update(json.load(f))
            except Exception as e:
                print(f"Error loading config: {e}")

    def save(self):
        self.config_dir.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")
