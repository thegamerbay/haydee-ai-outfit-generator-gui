import threading
import logging
import tempfile
import json
import re
from pathlib import Path
import webbrowser
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Direct imports from the library
from haydee_outfit_gen.mod_builder import ModBuilder, MultiModBuilder
from haydee_outfit_gen.gemini_client import GeminiModClient
from haydee_outfit_gen.image_processor import ImageProcessor

from src.config_manager import ConfigManager

# Monkey-patch google-genai Client to increase the default timeout to 10 minutes (600,000 ms)
from google import genai
original_client_init = genai.Client.__init__
def new_client_init(self, *args, **kwargs):
    if 'http_options' not in kwargs:
        kwargs['http_options'] = {'timeout': 600000}
    original_client_init(self, *args, **kwargs)
genai.Client.__init__ = new_client_init

import time

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CustomTextHandler(logging.Handler):
    def __init__(self, textbox):
        super().__init__()
        self.textbox = textbox

    def emit(self, record):
        msg = self.format(record)
        self.textbox.after(0, self.append_text, msg)

    def append_text(self, msg):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", msg + "\n")
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

class HaydeeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Haydee AI Outfit Generator")
        self.geometry("950x750")
        self.minsize(850, 650)

        self.config_manager = ConfigManager()

        self._build_ui()
        self._load_settings()
        self._setup_logging()
        
        # Setup universal hotkeys fix for non-English layouts
        self._setup_universal_hotkeys()

    def _setup_universal_hotkeys(self):
        """Binds Ctrl+C/V/X/Z/A handling to physical keycodes (supports any language layout)."""
        self.bind('<Control-KeyPress>', self._universal_ctrl_handler)

    def _universal_ctrl_handler(self, event):
        # If the current layout is English, tkinter natively handles these events.
        # We interrupt execution to avoid double-copying or double-pasting.
        if event.keysym.lower() in ['c', 'v', 'x', 'z', 'a']:
            return

        # Get the currently focused widget
        widget = self.focus_get()
        if not widget:
            return

        # Check the hardware keycode for Windows:
        # 86 = V, 67 = C, 88 = X, 90 = Z, 65 = A
        if event.keycode == 86:
            widget.event_generate('<<Paste>>')
        elif event.keycode == 67:
            widget.event_generate('<<Copy>>')
        elif event.keycode == 88:
            widget.event_generate('<<Cut>>')
        elif event.keycode == 90:
            widget.event_generate('<<Undo>>')
        elif event.keycode == 65:
            # Select All: the method differs between entry widgets and text widgets
            if hasattr(widget, 'select_range'):
                widget.select_range(0, 'end')
                widget.icursor('end')
            elif hasattr(widget, 'tag_add'):
                widget.tag_add('sel', '1.0', 'end')
                widget.mark_set('insert', 'end')

    def _setup_logging(self):
        self.logger = logging.getLogger("haydee_outfit_gen")
        self.logger.setLevel(logging.INFO)
        
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
            
        handler = CustomTextHandler(self.log_console)
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # === LEFT PANEL (Settings) ===
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.left_frame, text="⚙️ Settings", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 20))

        # API Key
        self.frame_api_label = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.frame_api_label.pack(fill="x", padx=20)
        
        ctk.CTkLabel(self.frame_api_label, text="Gemini API Key:").pack(side="left")
        self.lbl_get_key = ctk.CTkLabel(self.frame_api_label, text="(Get Key Here)", text_color="#1F6AA5", font=ctk.CTkFont(underline=True), cursor="hand2")
        self.lbl_get_key.pack(side="right")
        self.lbl_get_key.bind("<Button-1>", lambda e: webbrowser.open_new("https://aistudio.google.com/"))
        
        self.entry_api_key = ctk.CTkEntry(self.left_frame, show="*", placeholder_text="Paste your key here...")
        self.entry_api_key.pack(fill="x", padx=20, pady=(0, 15))

        # Game Path
        ctk.CTkLabel(self.left_frame, text="Haydee Game Path:").pack(anchor="w", padx=20)
        self.path_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.path_frame.pack(fill="x", padx=20, pady=(0, 15))
        self.entry_path = ctk.CTkEntry(self.path_frame, placeholder_text="C:\\Program Files (x86)\\Steam\\...")
        self.entry_path.pack(side="left", fill="x", expand=True)
        self.btn_browse = ctk.CTkButton(self.path_frame, text="📂", width=40, command=self._browse_directory)
        self.btn_browse.pack(side="right", padx=(5, 0))

        # Author Name
        ctk.CTkLabel(self.left_frame, text="Author Name (Optional):").pack(anchor="w", padx=20)
        self.entry_author = ctk.CTkEntry(self.left_frame, placeholder_text="e.g. TheGamerBay")
        self.entry_author.pack(fill="x", padx=20, pady=(0, 15))

        # Resolution
        ctk.CTkLabel(self.left_frame, text="Resolution:").pack(anchor="w", padx=20)
        self.combo_res = ctk.CTkComboBox(self.left_frame, values=["4K", "2K"])
        self.combo_res.pack(fill="x", padx=20, pady=(0, 15))

        # Generation Model Name
        ctk.CTkLabel(self.left_frame, text="Generation AI Model:").pack(anchor="w", padx=20)
        self.entry_model = ctk.CTkEntry(self.left_frame, placeholder_text="gemini-3.1-flash-image-preview")
        self.entry_model.pack(fill="x", padx=20, pady=(0, 15))

        # Validation Model Name
        ctk.CTkLabel(self.left_frame, text="Validation AI Model:").pack(anchor="w", padx=20)
        self.entry_validator_model = ctk.CTkEntry(self.left_frame, placeholder_text="gemini-3.1-pro-preview")
        self.entry_validator_model.pack(fill="x", padx=20, pady=(0, 20))

        # Save Button
        self.btn_save = ctk.CTkButton(self.left_frame, text="💾 Save Settings", command=self._save_settings)
        self.btn_save.pack(padx=20, pady=(0, 20))

        # Bottom spacer & FAQ Link
        ctk.CTkFrame(self.left_frame, fg_color="transparent", height=0).pack(fill="y", expand=True)
        
        self.lbl_faq = ctk.CTkLabel(self.left_frame, text="❓ Help & FAQ", text_color="#1F6AA5", font=ctk.CTkFont(underline=True), cursor="hand2")
        self.lbl_faq.pack(side="bottom", pady=20)
        self.lbl_faq.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/thegamerbay/haydee-ai-outfit-generator-gui"))

        # === RIGHT PANEL (Workspace) ===
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nsew")
        self.right_frame.grid_rowconfigure(2, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Tabs
        self.tabview = ctk.CTkTabview(self.right_frame)
        self.tabview.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")
        
        self.tab_gen = self.tabview.add("✨ Generate Outfit")
        self.tab_prompts = self.tabview.add("💡 Prompt Ideas")
        self.tab_group = self.tabview.add("📦 Group Mods")

        self._build_generate_tab()
        self._build_prompts_tab()
        self._build_group_tab()

        # Progress bar (hidden by default)
        self.progress_bar = ctk.CTkProgressBar(self.right_frame, mode="indeterminate")
        self.progress_bar.set(0)

        # Log Console
        ctk.CTkLabel(self.right_frame, text="Execution Console:").grid(row=1, column=0, sticky="w", padx=20)
        self.log_console = ctk.CTkTextbox(self.right_frame, height=180, state="disabled", fg_color="#1E1E1E", text_color="#00FF00")
        self.log_console.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

    def _build_generate_tab(self):
        self.tab_gen.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(self.tab_gen, text="Mod Name (e.g. NeonSurge):").grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))
        self.entry_mod_name = ctk.CTkEntry(self.tab_gen)
        self.entry_mod_name.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(self.tab_gen, text="Style Description (Prompt):").grid(row=2, column=0, sticky="w", padx=20)
        self.textbox_style = ctk.CTkTextbox(self.tab_gen, height=80)
        self.textbox_style.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 15))

        self.frame_options = ctk.CTkFrame(self.tab_gen, fg_color="transparent")
        self.frame_options.grid(row=4, column=0, sticky="w", padx=20, pady=(0, 15))

        self.check_gen_d = ctk.CTkCheckBox(self.frame_options, text="Diffuse (Suit_D)")
        self.check_gen_d.grid(row=0, column=0, padx=(0, 15))
        self.check_gen_d.select()

        self.check_gen_s = ctk.CTkCheckBox(self.frame_options, text="Specular (Suit_S)")
        self.check_gen_s.grid(row=0, column=1, padx=(0, 15))
        self.check_gen_s.select()

        self.check_gen_n = ctk.CTkCheckBox(self.frame_options, text="Normal (Suit_N)")
        self.check_gen_n.grid(row=0, column=2)
        self.check_gen_n.select()

        self.btn_generate = ctk.CTkButton(self.tab_gen, text="Start Generation", height=40, font=ctk.CTkFont(weight="bold"), command=self._start_generation)
        self.btn_generate.grid(row=5, column=0, pady=10)

    def _build_prompts_tab(self):
        self.tab_prompts.grid_columnconfigure(0, weight=1)
        self.tab_prompts.grid_rowconfigure(3, weight=1)

        ctk.CTkLabel(self.tab_prompts, text="Enter a theme or concept (e.g., 'Lollipop and Strawberry'):").grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))
        
        self.entry_theme = ctk.CTkEntry(self.tab_prompts, placeholder_text="Describe your desired style...")
        self.entry_theme.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 10))

        self.btn_gen_prompts = ctk.CTkButton(self.tab_prompts, text="💡 Generate Prompt Ideas", height=32, command=self._start_prompt_generation)
        self.btn_gen_prompts.grid(row=2, column=0, pady=(0, 10))

        # Scrollable area for resulting idea cards
        self.prompts_scroll_frame = ctk.CTkScrollableFrame(self.tab_prompts, fg_color="transparent")
        self.prompts_scroll_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.prompts_scroll_frame.grid_columnconfigure(0, weight=1)

    def _render_all_prompt_cards(self, new_indexes=None):
        if new_indexes is None:
            new_indexes = []
        for widget in self.prompts_scroll_frame.winfo_children():
            widget.destroy()
        
        prompts = self.config_manager.config.get("saved_prompts", [])
        for idx, prompt_data in enumerate(prompts):
            self._create_card_widget(idx, prompt_data.get("name", "Unknown"), prompt_data.get("style", ""), is_new=(idx in new_indexes))

    def _create_card_widget(self, index, name, style, is_new=False):
        # Card Frame
        fg_color = "#2E3B4E" if is_new else "#2A2D2E"
        border_color = "#3A86FF" if is_new else "#3E3E3E"
        border_width = 2 if is_new else 1
        
        card = ctk.CTkFrame(self.prompts_scroll_frame, fg_color=fg_color, border_width=border_width, border_color=border_color, corner_radius=10)
        card.pack(fill="x", padx=5, pady=5)
        card.grid_columnconfigure(0, weight=1)

        # Header: Name + Badge New
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        
        lbl_name = ctk.CTkLabel(header_frame, text=name, font=ctk.CTkFont(size=16, weight="bold"), text_color="#A9D6E5")
        lbl_name.pack(side="left")
        
        if is_new:
            badge = ctk.CTkLabel(header_frame, text=" NEW ", font=ctk.CTkFont(size=10, weight="bold"), fg_color="#E63946", text_color="white", corner_radius=5)
            badge.pack(side="left", padx=10)
            
        btn_del = ctk.CTkButton(header_frame, text="🗑️ Delete", width=60, height=24, fg_color="transparent", hover_color="#E63946", border_width=1, border_color="#E63946", text_color="#E63946", command=lambda idx=index: self._delete_prompt(idx))
        btn_del.pack(side="right")
        
        # Style Textbox (readonly)
        tb_style = ctk.CTkTextbox(card, height=60, wrap="word", fg_color="transparent")
        tb_style.grid(row=1, column=0, sticky="ew", padx=10, pady=(5, 5))
        tb_style.insert("1.0", style)
        tb_style.configure(state="disabled")
        
        # Apply button
        btn_apply = ctk.CTkButton(card, text="✨ Apply to Generator", fg_color="#1F6AA5", hover_color="#144870", command=lambda n=name, s=style: self._apply_prompt(n, s))
        btn_apply.grid(row=2, column=0, sticky="e", padx=10, pady=(0, 10))

    def _delete_prompt(self, index):
        prompts = self.config_manager.config.get("saved_prompts", [])
        if 0 <= index < len(prompts):
            del prompts[index]
            self.config_manager.config["saved_prompts"] = prompts
            self.config_manager.save()
            self._render_all_prompt_cards()

    def _apply_prompt(self, name, style):
        self.tabview.set("✨ Generate Outfit")
        self.entry_mod_name.delete(0, "end")
        self.entry_mod_name.insert(0, name)
        self.textbox_style.delete("1.0", "end")
        self.textbox_style.insert("1.0", style)
        self.logger.info(f"Applied prompt idea '{name}' to generator.")

    def _build_group_tab(self):
        self.tab_group.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.tab_group, text="Multi-Mod Name (e.g. Rainbow):").grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))
        self.entry_multi_name = ctk.CTkEntry(self.tab_group)
        self.entry_multi_name.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(self.tab_group, text="Source Mods (comma-separated, e.g. red, green, blue):").grid(row=2, column=0, sticky="w", padx=20)
        self.entry_source_mods = ctk.CTkEntry(self.tab_group)
        self.entry_source_mods.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(self.tab_group, text="Slot Category Name (e.g. color):").grid(row=4, column=0, sticky="w", padx=20)
        self.entry_slot_category = ctk.CTkEntry(self.tab_group)
        self.entry_slot_category.insert(0, "color")
        self.entry_slot_category.grid(row=5, column=0, sticky="ew", padx=20, pady=(0, 15))

        self.check_delete_sources = ctk.CTkCheckBox(self.tab_group, text="Delete original source mods after successful grouping")
        self.check_delete_sources.grid(row=6, column=0, sticky="w", padx=20, pady=(0, 20))

        self.btn_group = ctk.CTkButton(self.tab_group, text="Group Outfits", height=40, font=ctk.CTkFont(weight="bold"), command=self._start_grouping)
        self.btn_group.grid(row=7, column=0, pady=10)

    def _browse_directory(self):
        dir_path = filedialog.askdirectory(title="Select Haydee Game Folder")
        if dir_path:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, dir_path)

    def _load_settings(self):
        self.entry_api_key.insert(0, self.config_manager.config.get("gemini_api_key", ""))
        self.entry_path.insert(0, self.config_manager.config.get("haydee_path", ""))
        self.entry_author.insert(0, self.config_manager.config.get("author_name", ""))
        self.combo_res.set(self.config_manager.config.get("image_resolution", "4K"))
        self.entry_model.insert(0, self.config_manager.config.get("model_name", "gemini-3.1-flash-image-preview"))
        self.entry_validator_model.insert(0, self.config_manager.config.get("validator_model", "gemini-3.1-pro-preview"))
        
        # Load Prompt Ideas
        self._render_all_prompt_cards()

    def _save_settings(self, show_success=True):
        api_key = self.entry_api_key.get().strip()
        haydee_path = self.entry_path.get().strip()
        author = self.entry_author.get().strip()
        res = self.combo_res.get()
        model = self.entry_model.get().strip() or "gemini-3.1-flash-image-preview"
        validator_model = self.entry_validator_model.get().strip() or "gemini-3.1-pro-preview"

        if not api_key or not haydee_path:
            messagebox.showwarning("Warning", "Please fill in both API Key and Game Path.")
            return

        # Update UI to reflect assigned defaults
        if not self.entry_model.get().strip():
            self.entry_model.delete(0, "end")
            self.entry_model.insert(0, model)
            
        if not self.entry_validator_model.get().strip():
            self.entry_validator_model.delete(0, "end")
            self.entry_validator_model.insert(0, validator_model)

        self.config_manager.config["gemini_api_key"] = api_key
        self.config_manager.config["haydee_path"] = haydee_path
        self.config_manager.config["author_name"] = author
        self.config_manager.config["image_resolution"] = res
        self.config_manager.config["model_name"] = model
        self.config_manager.config["validator_model"] = validator_model
        self.config_manager.save()

        if show_success:
            messagebox.showinfo("Success", "Settings saved successfully!")

    def _prepare_for_task(self):
        """Helper to save config and block UI before a task"""
        self._save_settings(show_success=False)
        if not self.config_manager.config["gemini_api_key"] or not self.config_manager.config["haydee_path"]:
             return False

        self.btn_generate.configure(state="disabled")
        self.btn_group.configure(state="disabled")
        if hasattr(self, 'btn_gen_prompts'):
            self.btn_gen_prompts.configure(state="disabled")
        self.tabview.configure(state="disabled")
        
        self.progress_bar.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 5))
        self.progress_bar.start()
        
        self.log_console.configure(state="normal")
        self.log_console.delete("1.0", "end")
        self.log_console.configure(state="disabled")
        return True

    def _start_generation(self):
        mod_name = self.entry_mod_name.get().strip()
        style = self.textbox_style.get("1.0", "end-1c").strip()
        
        gen_d = self.check_gen_d.get() == 1
        gen_s = self.check_gen_s.get() == 1
        gen_n = self.check_gen_n.get() == 1

        if not mod_name:
            messagebox.showerror("Error", "Mod name is required.")
            return
            
        if gen_d and not style:
            messagebox.showerror("Error", "Style description is required to generate a new Diffuse texture.")
            return
            
        if not gen_d and not gen_s and not gen_n:
            messagebox.showinfo("Info", "Nothing to generate. All options are disabled.")
            return
        
        if self._prepare_for_task():
            threading.Thread(
                target=self._run_generator_thread, 
                args=(mod_name, style, gen_d, gen_s, gen_n), 
                daemon=True
            ).start()

    def _start_prompt_generation(self):
        theme = self.entry_theme.get().strip()
        if not theme:
            messagebox.showerror("Error", "Please enter a theme or concept first.")
            return

        if self._prepare_for_task():
            threading.Thread(
                target=self._run_prompt_thread,
                args=(theme,),
                daemon=True
            ).start()

    def _run_prompt_thread(self, theme):
        try:
            api_key = self.config_manager.config.get("gemini_api_key", "")
            model_name = self.config_manager.config.get("validator_model", "gemini-3.1-pro-preview")
            
            if not api_key:
                raise ValueError("API Key is missing.")

            self.logger.info(f"Generating prompt ideas for theme: '{theme}' using {model_name}...")
            
            client = genai.Client(api_key=api_key)
            
            system_instruction = """You are an expert prompt engineer for an AI texture generator modifying a biomechanical female character named Haydee.
Her original suit features synthetic skin, mechanical joints, and glossy armor plates.
Generate 3 distinct, highly detailed, and creative outfit concepts based on the user's theme.
Focus on vivid colors, specific material textures (e.g., glossy plastic, brushed metal, matte rubber, glowing LEDs), and distinct patterns.
Return the result STRICTLY as a JSON array of objects. 
Each object must have exactly two keys: 'name' (a short PascalCase string for the mod name without spaces, e.g., 'CandyPop') and 'style' (a detailed text prompt for the AI image generator, e.g., 'bright colorful lollipop candy theme, glossy plastic armor plates...').
Do not include any other text, markdown formatting, or explanation. Just the raw JSON array."""

            prompt_text = f"{system_instruction}\n\nUser Theme: {theme}"

            response = client.models.generate_content(
                model=model_name,
                contents=prompt_text,
            )
            
            response_text = response.text
            
            # Clean up potential markdown formatting block injected by LLM
            if response_text.startswith("```"):
                response_text = re.sub(r"^```(?:json)?\n|\n```$", "", response_text.strip(), flags=re.MULTILINE)
            
            try:
                ideas = json.loads(response_text)
            except json.JSONDecodeError as e:
                self.logger.error(f"Failed to parse LLM response: {response_text}")
                raise ValueError(f"AI returned invalid JSON.")
                
            if not isinstance(ideas, list):
                raise ValueError("AI did not return a JSON array.")
                
            self.logger.info(f"Successfully generated {len(ideas)} ideas.")
            self.after(0, lambda: self._handle_new_ideas(ideas))
            
        except Exception as e:
            self.logger.error(f"Prompt generation failed: {e}")
            self.after(0, lambda err=str(e): messagebox.showerror("Generation Error", err))
        finally:
            self.after(0, self._restore_ui)

    def _handle_new_ideas(self, ideas):
        prompts = self.config_manager.config.get("saved_prompts", [])
        valid_ideas = [i for i in ideas if "name" in i and "style" in i]
        
        prompts = valid_ideas + prompts
        self.config_manager.config["saved_prompts"] = prompts
        self.config_manager.save()
        
        new_indexes = list(range(len(valid_ideas)))
        self._render_all_prompt_cards(new_indexes=new_indexes)
        self.entry_theme.delete(0, "end")

    def _start_grouping(self):
        multi_name = self.entry_multi_name.get().strip()
        source_mods = self.entry_source_mods.get().strip()
        slot_cat = self.entry_slot_category.get().strip()
        delete_sources = self.check_delete_sources.get() == 1

        if not multi_name or not source_mods or not slot_cat:
            messagebox.showerror("Error", "Multi-Mod Name, Source Mods, and Slot Category are required.")
            return
            
        if self._prepare_for_task():
            threading.Thread(target=self._run_grouping_thread, args=(multi_name, source_mods, slot_cat, delete_sources), daemon=True).start()

    def _run_generator_thread(self, mod_name, style, gen_d, gen_s, gen_n):
        try:
            api_key = self.config_manager.config["gemini_api_key"]
            haydee_path = Path(self.config_manager.config["haydee_path"])
            author = self.config_manager.config.get("author_name", "")
            res = self.config_manager.config["image_resolution"]
            model_name = self.config_manager.config.get("model_name", "gemini-3.1-flash-image-preview")
            validator_model = self.config_manager.config.get("validator_model", "gemini-3.1-pro-preview")
            
            outfits_dir = haydee_path / "Outfits"
            base_dds = outfits_dir / "Haydee" / "Suit_D.dds"

            builder = ModBuilder(mod_name, outfits_dir=outfits_dir, author=author if author else None)
            builder.prepare_directory(clear_dir=gen_d)

            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                base_png = temp_path / "base_Suit_D.png"
                generated_d_png = temp_path / "generated_Suit_D.png"
                generated_mask = temp_path / "material_mask.png"
                generated_n_png = temp_path / "generated_normal.png"

                client = GeminiModClient(api_key=api_key, image_resolution=res, model_name=model_name, validator_model=validator_model)
                final_d_dds = builder.mod_dir / "Suit_D.dds"

                if gen_d:
                    if not base_dds.exists():
                        raise FileNotFoundError(f"Base texture not found at {base_dds}. Please verify your game path.")
                    ImageProcessor.dds_to_png(base_dds, base_png)
                    
                    # --- ДОБАВЛЕННЫЙ ЦИКЛ ВАЛИДАЦИИ (QA FEEDBACK LOOP) ---
                    max_attempts = 3
                    attempt = 1
                    feedback = None
                    is_valid = False

                    while attempt <= max_attempts:
                        self.logger.info(f"Generation attempt {attempt}/{max_attempts}...")
                        
                        client.generate_texture(
                            base_image_path=base_png, 
                            style=style, 
                            output_path=generated_d_png,
                            previous_feedback=feedback
                        )

                        validation_result = client.validate_texture(
                            base_image_path=base_png,
                            generated_image_path=generated_d_png, 
                            style=style
                        )

                        if validation_result.is_valid:
                            self.logger.info("✅ Texture passed QA validation!")
                            is_valid = True
                            break
                        else:
                            self.logger.warning(f"❌ Texture validation failed: {validation_result.feedback}")
                            feedback = validation_result.feedback
                            attempt += 1

                    if not is_valid:
                        self.logger.error(f"⚠️ Max retries ({max_attempts}) reached. Proceeding with the last generated texture, but it may contain structural flaws.")
                    # -----------------------------------------------------

                    ImageProcessor.img_to_dds(generated_d_png, final_d_dds, resolution=res)
                else:
                    if not final_d_dds.exists():
                        if gen_s or gen_n:
                            raise FileNotFoundError(
                                f"Cannot generate Suit_S or Suit_N because Suit_D generation was skipped and "
                                f"'{final_d_dds.name}' does not exist in the mod folder from previous runs."
                            )
                    else:
                        if gen_s or gen_n:
                            ImageProcessor.dds_to_png(final_d_dds, generated_d_png)

                if gen_s:
                    client.generate_material_mask(diffuse_image_path=generated_d_png, output_path=generated_mask)
                    final_s_dds = builder.mod_dir / "Suit_S.dds"
                    ImageProcessor.create_specular_map(generated_mask, final_s_dds, resolution=res)

                if gen_n:
                    client.generate_normal_map(diffuse_image_path=generated_d_png, output_path=generated_n_png)
                    final_n_dds = builder.mod_dir / "Suit_N.dds"
                    ImageProcessor.create_custom_normal_map(generated_n_png, final_n_dds, resolution=res)

            builder.generate_mtl_file()
            builder.generate_outfit_file()
            
            self.logger.info(f"Mod '{mod_name}' generation completed successfully!")
            self.after(0, lambda: messagebox.showinfo("Done", f"Mod '{mod_name}' generation completed successfully!"))
            
        except Exception as e:
            self.logger.error(f"Generation failed: {e}")
            self.after(0, lambda err=str(e): messagebox.showerror("Generation Error", err))
        finally:
            self.after(0, self._restore_ui)

    def _run_grouping_thread(self, multimod_name, source_mods_str, slot_category, delete_sources):
        try:
            haydee_path = Path(self.config_manager.config["haydee_path"])
            author = self.config_manager.config.get("author_name", "")
            outfits_dir = haydee_path / "Outfits"
            
            # Разделяем строку на список модов
            source_mods = [m.strip() for m in source_mods_str.split(",") if m.strip()]
            if not source_mods:
                raise ValueError("No valid source mods provided.")
            
            self.logger.info(f"Starting to group mods: {source_mods} into '{multimod_name}'...")
            
            builder = MultiModBuilder(
                multimod_name=multimod_name,
                source_mods=source_mods,
                outfits_dir=outfits_dir,
                slot_category=slot_category,
                author=author if author else None
            )
            
            builder.validate_sources()
            builder.prepare_directory()
            builder.migrate_assets_and_generate_mtls()
            builder.generate_outfit_file()
            
            if delete_sources:
                builder.cleanup_sources()
                
            self.logger.info(f"Multi-mod '{multimod_name}' created successfully from {len(source_mods)} variants!")
            self.after(0, lambda: messagebox.showinfo("Done", f"Multi-mod '{multimod_name}' created successfully!"))
            
        except Exception as e:
            self.logger.error(f"Grouping failed: {e}")
            self.after(0, lambda err=str(e): messagebox.showerror("Grouping Error", err))
        finally:
            self.after(0, self._restore_ui)

    def _restore_ui(self):
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.btn_generate.configure(state="normal")
        self.btn_group.configure(state="normal")
        if hasattr(self, 'btn_gen_prompts'):
            self.btn_gen_prompts.configure(state="normal")
        self.tabview.configure(state="normal")
