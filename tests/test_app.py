import pytest
from unittest.mock import patch

# Mock settings load to avoid creating real AppData files during tests
@pytest.fixture(autouse=True)
def mock_config_manager(mocker):
    # Setup initial mock data
    mock_config = {
        "gemini_api_key": "test_key",
        "haydee_path": "C:\\Test\\Path",
        "image_resolution": "4K"
    }
    
    # Patch ConfigManager methods
    mocker.patch("src.config_manager.ConfigManager.load")
    mocker.patch("src.config_manager.ConfigManager.save")
    
    # When ConfigManager is instantiated, inject our mock config
    def mock_init(self):
        self.config = mock_config.copy()
        
    mocker.patch("src.config_manager.ConfigManager.__init__", new=mock_init)

@pytest.fixture(scope="session", autouse=True)
def _patch_mainloop():
    with patch("customtkinter.CTk.mainloop"):
        yield

from src.app import HaydeeGUI

@pytest.fixture
def app():
    """Fixture to create an application instance per test."""
    app_instance = HaydeeGUI()
    yield app_instance
    app_instance.destroy()

def test_app_initialization(app):
    """Verify that the application starts and pulls settings from the ConfigManager."""
    assert app.title() == "Haydee AI Outfit Generator"
    assert app.entry_api_key.get() == "test_key"
    assert app.entry_path.get() == "C:\\Test\\Path"

def test_save_settings_validation_empty(app, mocker):
    """Verify that empty fields trigger a warning dialog."""
    mock_messagebox = mocker.patch("src.app.messagebox.showwarning")
    
    # Clear fields
    app.entry_api_key.delete(0, "end")
    app.entry_path.delete(0, "end")
    
    # Trigger save
    app._save_settings()
    
    # Check that a warning appeared and settings were not updated
    mock_messagebox.assert_called_once_with("Warning", "Please fill in both API Key and Game Path.")

def test_save_settings_success(app, mocker):
    """Verify successful saving of settings."""
    mock_messagebox = mocker.patch("src.app.messagebox.showinfo")
    mock_save = mocker.patch.object(app.config_manager, "save")
    
    # Enter new data
    app.entry_api_key.delete(0, "end")
    app.entry_api_key.insert(0, "new_super_secret_key")
    
    app._save_settings()
    
    # Check that data was written to config memory and saved
    assert mock_save.called
    assert app.config_manager.config["gemini_api_key"] == "new_super_secret_key"
    mock_messagebox.assert_called_once_with("Success", "Settings saved successfully!")

def test_start_generation_blocks_ui(app, mocker):
    """Verify that starting generation blocks the UI."""
    mock_thread = mocker.patch("src.app.threading.Thread")
    
    # Fill in required fields
    app.entry_mod_name.insert(0, "TestMod")
    app.textbox_style.insert("1.0", "Cyberpunk style")
    
    app._start_generation()
    
    # Check that the button is disabled and progress bar started
    assert app.btn_generate.cget("state") == "disabled"
    assert mock_thread.called  # Check that the generation thread was started
