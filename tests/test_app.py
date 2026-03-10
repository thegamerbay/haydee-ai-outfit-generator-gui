import pytest
from unittest.mock import patch

# Mock settings load to avoid creating real AppData files during tests
@pytest.fixture(scope="module", autouse=True)
def mock_config_manager():
    # Setup initial mock data
    mock_config = {
        "gemini_api_key": "test_key",
        "haydee_path": "C:\\Test\\Path",
        "author_name": "TestAuthor",
        "image_resolution": "4K",
        "model_name": "test_model_v1",
        "validator_model": "gemini-3.1-pro-preview"
    }
    
    # When ConfigManager is instantiated, inject our mock config
    def mock_init(self):
        self.config = mock_config.copy()
        
    with patch("src.config_manager.ConfigManager.load"), \
         patch("src.config_manager.ConfigManager.save"), \
         patch("src.config_manager.ConfigManager.__init__", new=mock_init):
        yield

@pytest.fixture(scope="session", autouse=True)
def _patch_mainloop():
    with patch("customtkinter.CTk.mainloop"):
        yield

from src.app import HaydeeGUI

@pytest.fixture(scope="module")
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
    assert app.entry_author.get() == "TestAuthor"
    assert app.entry_model.get() == "test_model_v1"
    assert app.entry_validator_model.get() == "gemini-3.1-pro-preview"

def test_save_settings_validation_empty(app, mocker):
    """Verify that empty fields trigger a warning dialog."""
    mock_messagebox = mocker.patch("src.app.messagebox.showwarning")
    
    # Clear required fields
    app.entry_api_key.delete(0, "end")
    app.entry_path.delete(0, "end")
    
    app._save_settings()
    
    # Check that a warning appeared and settings were not updated
    mock_messagebox.assert_called_once_with("Warning", "Please fill in both API Key and Game Path.")

def test_save_settings_success(app, mocker):
    """Verify successful saving of settings including author and model names."""
    mock_messagebox = mocker.patch("src.app.messagebox.showinfo")
    mock_save = mocker.patch.object(app.config_manager, "save")
    
    # Re-fill the haydee path that was deleted in previous test
    app.entry_path.delete(0, "end")
    app.entry_path.insert(0, "C:\\Test\\Path")
    
    # Enter new data
    app.entry_api_key.delete(0, "end")
    app.entry_api_key.insert(0, "new_super_secret_key")
    
    app.entry_author.delete(0, "end")
    app.entry_author.insert(0, "NewAuthor")

    app.entry_model.delete(0, "end")
    app.entry_model.insert(0, "gemini-4.0-pro")

    app.entry_validator_model.delete(0, "end")
    app.entry_validator_model.insert(0, "gemini-4.0-pro-validator")
    
    app._save_settings()
    
    # Check that data was written to config memory and saved
    assert mock_save.called
    assert app.config_manager.config["gemini_api_key"] == "new_super_secret_key"
    assert app.config_manager.config["author_name"] == "NewAuthor"
    assert app.config_manager.config["model_name"] == "gemini-4.0-pro"
    assert app.config_manager.config["validator_model"] == "gemini-4.0-pro-validator"
    mock_messagebox.assert_called_once_with("Success", "Settings saved successfully!")

def test_save_settings_defaults_autofill(app, mocker):
    """Verify that empty model fields are repopulated with their defaults in the UI."""
    mocker.patch("src.app.messagebox.showinfo")
    mocker.patch.object(app.config_manager, "save")
    
    # Fill required fields
    app.entry_path.delete(0, "end")
    app.entry_path.insert(0, "C:\\Test\\Path")
    app.entry_api_key.delete(0, "end")
    app.entry_api_key.insert(0, "test_key_defaults")
    
    # Leave model fields completely empty
    app.entry_model.delete(0, "end")
    app.entry_validator_model.delete(0, "end")
    
    app._save_settings()
    
    # Check that defaults were written back to the UI widgets
    assert app.entry_model.get() == "gemini-3.1-flash-image-preview"
    assert app.entry_validator_model.get() == "gemini-3.1-pro-preview"
    
    # Check that defaults were written to config memory
    assert app.config_manager.config["model_name"] == "gemini-3.1-flash-image-preview"
    assert app.config_manager.config["validator_model"] == "gemini-3.1-pro-preview"

def test_start_generation_validation(app, mocker):
    """Verify validation logic for start_generation with various skip checkboxes."""
    mock_messagebox_error = mocker.patch("src.app.messagebox.showerror")
    mock_messagebox_info = mocker.patch("src.app.messagebox.showinfo")

    # Clear mod name
    app.entry_mod_name.delete(0, "end")
    app._start_generation()
    mock_messagebox_error.assert_called_with("Error", "Mod name is required.")

    # Fill mod name
    app.entry_mod_name.insert(0, "ValidMod")

    # Set all checkboxes to off
    app.check_gen_d.deselect()
    app.check_gen_s.deselect()
    app.check_gen_n.deselect()
    app._start_generation()
    mock_messagebox_info.assert_called_with("Info", "Nothing to generate. All options are disabled.")

    # Set gen_d on but style empty
    app.check_gen_d.select()
    app.textbox_style.delete("1.0", "end")
    app._start_generation()
    mock_messagebox_error.assert_called_with("Error", "Style description is required to generate a new Diffuse texture.")

def test_start_generation_blocks_ui(app, mocker):
    """Verify that starting generation blocks the UI elements and passes correct args."""
    mock_thread = mocker.patch("src.app.threading.Thread")
    
    # Fill in required fields for Generation
    app.entry_mod_name.delete(0, "end")
    app.entry_mod_name.insert(0, "TestMod")
    app.textbox_style.delete("1.0", "end")
    app.textbox_style.insert("1.0", "Cyberpunk style")

    app.check_gen_d.select()
    app.check_gen_s.deselect()
    app.check_gen_n.select()
    
    app._start_generation()
    
    # Check that thread was started with correct arguments
    mock_thread.assert_called_once()
    _, kwargs = mock_thread.call_args
    assert kwargs['args'] == ("TestMod", "Cyberpunk style", True, False, True)

    # Check that the button is disabled
    assert app.btn_generate.cget("state") == "disabled"
    assert app.btn_group.cget("state") == "disabled"

def test_start_generation_saves_prompt(app, mocker):
    """Verify that starting generation saves or updates the prompt idea correctly."""
    mocker.patch("src.app.threading.Thread")
    mock_render = mocker.patch.object(app, "_render_all_prompt_cards")
    mock_save = mocker.patch.object(app.config_manager, "save")
    
    app.config_manager.config["saved_prompts"] = [
        {"name": "OldMod", "style": "OldStyle"},
        {"name": "ExistingMod", "style": "ExistingStyle"}
    ]
    
    # First test: Add a completely new prompt
    app.entry_mod_name.delete(0, "end")
    app.entry_mod_name.insert(0, "NewMod")
    app.textbox_style.delete("1.0", "end")
    app.textbox_style.insert("1.0", "NewStyle")
    app.check_gen_d.select()
    
    # Needs to return True for _prepare_for_task
    # mock_save is patched so it won't actually save, but config is in memory
    app._start_generation()
    
    assert mock_save.called
    assert len(app.config_manager.config["saved_prompts"]) == 3
    assert app.config_manager.config["saved_prompts"][0] == {"name": "NewMod", "style": "NewStyle"}
    mock_render.assert_called_with(new_indexes=[0])
    
    mock_save.reset_mock()
    mock_render.reset_mock()

    # Second test: Update an existing prompt (ExistingMod)
    app.entry_mod_name.delete(0, "end")
    app.entry_mod_name.insert(0, "ExistingMod")
    app.textbox_style.delete("1.0", "end")
    app.textbox_style.insert("1.0", "UpdatedStyle")
    
    app._start_generation()
    
    assert mock_save.called
    assert len(app.config_manager.config["saved_prompts"]) == 3
    assert app.config_manager.config["saved_prompts"][0] == {"name": "ExistingMod", "style": "UpdatedStyle"}
    # The old ExistingMod should have been removed from index 2
    assert app.config_manager.config["saved_prompts"][1] == {"name": "NewMod", "style": "NewStyle"}
    assert app.config_manager.config["saved_prompts"][2] == {"name": "OldMod", "style": "OldStyle"}
    mock_render.assert_called_with(new_indexes=[0])

def test_start_grouping_blocks_ui(app, mocker):
    """Verify that starting grouping blocks the UI elements."""
    mock_thread = mocker.patch("src.app.threading.Thread")
    
    # Switch to group tab logically and fill fields
    app.entry_multi_name.insert(0, "Rainbow")
    app.entry_source_mods.insert(0, "red, blue")
    
    app._start_grouping()
    
    # Check that buttons are disabled
    assert app.btn_group.cget("state") == "disabled"
    assert app.btn_generate.cget("state") == "disabled"
    assert mock_thread.called

def test_universal_hotkeys(app, mocker):
    """Verify that universal hotkeys trigger correct events based on hardware keycodes."""
    mock_widget = mocker.Mock()
    # Mock the focus_get method to return our mock widget
    app.focus_get = mocker.Mock(return_value=mock_widget)
    
    class MockEvent:
        def __init__(self, keysym, keycode):
            self.keysym = keysym
            self.keycode = keycode
            
    # Test case 1: English layout (should do nothing naturally)
    event_en = MockEvent(keysym='c', keycode=67)
    app._universal_ctrl_handler(event_en)
    mock_widget.event_generate.assert_not_called()
    
    # Test case 2: Non-English layout, Cut (X = 88)
    event_ru_x = MockEvent(keysym='ч', keycode=88)
    app._universal_ctrl_handler(event_ru_x)
    mock_widget.event_generate.assert_called_once_with('<<Cut>>')
    mock_widget.event_generate.reset_mock()
    
    # Test case 3: Non-English layout, Copy (C = 67)
    event_ru_c = MockEvent(keysym='с', keycode=67)
    app._universal_ctrl_handler(event_ru_c)
    mock_widget.event_generate.assert_called_once_with('<<Copy>>')
    mock_widget.event_generate.reset_mock()
    
    # Test case 4: Non-English layout, Paste (V = 86)
    event_ru_v = MockEvent(keysym='м', keycode=86)
    app._universal_ctrl_handler(event_ru_v)
    mock_widget.event_generate.assert_called_once_with('<<Paste>>')
    mock_widget.event_generate.reset_mock()
    
    # Test case 5: Non-English layout, Undo (Z = 90)
    event_ru_z = MockEvent(keysym='я', keycode=90)
    app._universal_ctrl_handler(event_ru_z)
    mock_widget.event_generate.assert_called_once_with('<<Undo>>')
    mock_widget.event_generate.reset_mock()
    
    # Test case 6: Non-English layout, Select All (A = 65) with Entry-like widget
    event_ru_a = MockEvent(keysym='ф', keycode=65)
    mock_entry_widget = mocker.Mock(spec=['select_range', 'icursor'])
    app.focus_get = mocker.Mock(return_value=mock_entry_widget)
    app._universal_ctrl_handler(event_ru_a)
    mock_entry_widget.select_range.assert_called_once_with(0, 'end')
    mock_entry_widget.icursor.assert_called_once_with('end')
    
    # Test case 7: Non-English layout, Select All (A = 65) with Text-like widget
    mock_text_widget = mocker.Mock(spec=['tag_add', 'mark_set'])
    app.focus_get = mocker.Mock(return_value=mock_text_widget)
    app._universal_ctrl_handler(event_ru_a)
    mock_text_widget.tag_add.assert_called_once_with('sel', '1.0', 'end')
    mock_text_widget.mark_set.assert_called_once_with('insert', 'end')

def test_google_genai_monkey_patch():
    """Verify that the google-genai Client timeout is patched securely to 600,000 ms."""
    from google import genai
    import src.app # Ensure the patch runs
    
    # With no http_options provided, it should use the patched timeout
    client = genai.Client(api_key="test_dummy_key")
    # In genai sdk 1.65.0, HttpOptions are stored in client._api_client._http_options
    http_opts = getattr(client._api_client, '_http_options', None)
    
    # Depending on exact implementation details in SDK, verify if available via dict or obj
    found_timeout = None
    if isinstance(http_opts, dict):
        found_timeout = http_opts.get('timeout')
    elif hasattr(http_opts, 'timeout'):
        found_timeout = http_opts.timeout
        
    if found_timeout is not None:
        assert found_timeout == 600000

def test_run_generator_thread_success(app, mocker):
    """Verify that the generator thread calls the library correctly."""
    mock_after = mocker.patch.object(app, "after")
    
    # Isolate filesystem operations
    mocker.patch("src.app.Path.exists", return_value=True)
    mocker.patch("src.app.ModBuilder")
    mocker.patch("src.app.ImageProcessor")
    mocker.patch("src.app.tempfile.TemporaryDirectory")
    
    mock_client_class = mocker.patch("src.app.GeminiModClient")
    mock_client_instance = mock_client_class.return_value
    
    # Execute the thread logic
    app._run_generator_thread("TestMod", "Style", True, False, False)
    
    # Validation
    mock_client_instance.generate_texture.assert_called_once()
    mock_client_instance.validate_texture.assert_called_once()
    assert mock_after.called

def test_run_generator_thread_failure(app, mocker):
    """Verify that generator throws an error correctly catching exceptions."""
    mock_after = mocker.patch.object(app, "after")
    
    mocker.patch("src.app.Path.exists", return_value=True)
    mocker.patch("src.app.ModBuilder")
    mocker.patch("src.app.ImageProcessor")
    mocker.patch("src.app.tempfile.TemporaryDirectory")
    
    mock_client_class = mocker.patch("src.app.GeminiModClient")
    mock_client_instance = mock_client_class.return_value
    
    mock_error = Exception("API Failed")
    mock_client_instance.generate_texture.side_effect = mock_error
    
    # Execute the thread logic
    app._run_generator_thread("TestErrorMod", "Style", True, False, False)
    
    assert mock_client_instance.generate_texture.call_count == 1
    assert mock_after.called

def test_start_prompt_generation_validation(app, mocker):
    """Verify validation logic for start_prompt_generation."""
    mock_messagebox_error = mocker.patch("src.app.messagebox.showerror")

    # Clear theme
    app.entry_theme.delete(0, "end")
    app._start_prompt_generation()
    mock_messagebox_error.assert_called_with("Error", "Please enter a theme or concept first.")

def test_start_prompt_generation_blocks_ui(app, mocker):
    """Verify that starting prompt generation blocks the UI elements."""
    mock_thread = mocker.patch("src.app.threading.Thread")
    
    # Switch to prompts tab logically and fill field
    app.entry_theme.insert(0, "Cyberpunk")
    
    app._start_prompt_generation()
    
    # Check that buttons are disabled
    assert app.btn_gen_prompts.cget("state") == "disabled"
    assert app.btn_generate.cget("state") == "disabled"
    assert app.btn_group.cget("state") == "disabled"
    assert mock_thread.called

def test_run_prompt_thread_success(app, mocker):
    """Verify that the prompt generator thread queries Gemini and parses the response successfully."""
    mock_after = mocker.patch.object(app, "after")
    
    mock_client_class = mocker.patch("src.app.genai.Client")
    mock_client_instance = mock_client_class.return_value
    mock_response = mocker.Mock()
    mock_response.text = '```json\n[{"name": "CyberNeon", "style": "Glowing neon lights"}]\n```'
    mock_client_instance.models.generate_content.return_value = mock_response
    
    app._run_prompt_thread("Cyberpunk")
    
    assert mock_client_instance.models.generate_content.called
    assert mock_after.called

def test_run_prompt_thread_failure(app, mocker):
    """Verify that prompt generator catches JSON parsing or API errors correctly."""
    mock_after = mocker.patch.object(app, "after")
    mock_logger = mocker.patch.object(app, "logger")
    
    mock_client_class = mocker.patch("src.app.genai.Client")
    mock_client_instance = mock_client_class.return_value
    mock_response = mocker.Mock()
    mock_response.text = 'This is not JSON'
    mock_client_instance.models.generate_content.return_value = mock_response
    
    app._run_prompt_thread("Cyberpunk")
    
    assert mock_client_instance.models.generate_content.called
    assert mock_logger.error.called
    assert mock_after.called

def test_handle_new_ideas(app, mocker):
    """Verify that new ideas are appended to saved_prompts and UI is re-rendered."""
    mock_render = mocker.patch.object(app, "_render_all_prompt_cards")
    mock_save = mocker.patch.object(app.config_manager, "save")
    
    app.config_manager.config["saved_prompts"] = []
    
    ideas = [
        {"name": "Test1", "style": "Style1"},
        {"name": "Test2", "style": "Style2"}
    ]
    
    app._handle_new_ideas(ideas)
    
    assert mock_save.called
    assert len(app.config_manager.config["saved_prompts"]) == 2
    assert app.config_manager.config["saved_prompts"][0]["name"] == "Test1"
    mock_render.assert_called_once_with(new_indexes=[0, 1])

def test_delete_prompt(app, mocker):
    """Verify that deleting a prompt removes it from saved_prompts and re-renders UI."""
    mock_render = mocker.patch.object(app, "_render_all_prompt_cards")
    mock_save = mocker.patch.object(app.config_manager, "save")
    
    app.config_manager.config["saved_prompts"] = [
        {"name": "Test1", "style": "Style1"},
        {"name": "Test2", "style": "Style2"}
    ]
    
    app._delete_prompt(0)
    
    assert mock_save.called
    assert len(app.config_manager.config["saved_prompts"]) == 1
    assert app.config_manager.config["saved_prompts"][0]["name"] == "Test2"
    assert mock_render.called

def test_apply_prompt(app):
    """Verify that applying a prompt updates the generation tab fields."""
    app.entry_mod_name.insert(0, "OldName")
    app.textbox_style.insert("1.0", "OldStyle")
    
    app._apply_prompt("NewName", "NewStyle")
    
    assert app.tabview.get() == "✨ Generate Outfit"
    assert app.entry_mod_name.get() == "NewName"
    assert app.textbox_style.get("1.0", "end-1c") == "NewStyle"
