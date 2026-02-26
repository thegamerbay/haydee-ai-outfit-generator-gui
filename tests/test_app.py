import os
import pytest
from unittest.mock import MagicMock
from pathlib import Path

# Set environment variables before importing the application
os.environ["GEMINI_API_KEY"] = "test_key"
os.environ["HAYDEE_PATH"] = "C:\\Test\\Path"

from src.app import HaydeeGUI
from haydee_outfit_gen.config import settings

from unittest.mock import patch

@pytest.fixture(scope="session", autouse=True)
def _patch_mainloop():
    with patch("customtkinter.CTk.mainloop"):
        yield

@pytest.fixture(scope="session")
def base_app():
    """Fixture to create an application instance once for all tests."""
    app_instance = HaydeeGUI()
    yield app_instance
    app_instance.destroy()

@pytest.fixture
def app(base_app, mocker):
    """Fixture to clean up and mock functionality per test."""
    mocker.patch("src.app.set_key") 
    
    # Restore base state
    base_app.entry_api_key.delete(0, "end")
    base_app.entry_api_key.insert(0, "test_key")
    base_app.entry_path.delete(0, "end")
    base_app.entry_path.insert(0, "C:\\Test\\Path")
    base_app.entry_mod_name.delete(0, "end")
    base_app.textbox_style.delete("1.0", "end")
    base_app.btn_generate.configure(state="normal")
    
    yield base_app

def test_app_initialization(app):
    """Verify that the application starts and pulls settings from the environment."""
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
    mock_set_key = mocker.patch("src.app.set_key")
    
    # Enter new data
    app.entry_api_key.delete(0, "end")
    app.entry_api_key.insert(0, "new_super_secret_key")
    
    app._save_settings()
    
    # Check that data was written to the file and updated in library memory
    assert mock_set_key.call_count == 3
    assert settings.gemini_api_key == "new_super_secret_key"
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
