import threading
import logging
import tempfile
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Direct imports from the library
from haydee_outfit_gen.mod_builder import ModBuilder, MultiModBuilder
from haydee_outfit_gen.gemini_client import GeminiModClient
from haydee_outfit_gen.image_processor import ImageProcessor

from src.config_manager import ConfigManager

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
        ctk.CTkLabel(self.left_frame, text="Gemini API Key:").pack(anchor="w", padx=20)
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
        self.combo_res.pack(fill="x", padx=20, pady=(0, 20))

        # Save Button
        self.btn_save = ctk.CTkButton(self.left_frame, text="💾 Save Settings", command=self._save_settings)
        self.btn_save.pack(padx=20, pady=(0, 20))

        # === RIGHT PANEL (Workspace) ===
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nsew")
        self.right_frame.grid_rowconfigure(2, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Tabs
        self.tabview = ctk.CTkTabview(self.right_frame)
        self.tabview.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")
        
        self.tab_gen = self.tabview.add("✨ Generate Outfit")
        self.tab_group = self.tabview.add("📦 Group Mods")

        self._build_generate_tab()
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
        self.textbox_style = ctk.CTkTextbox(self.tab_gen, height=100)
        self.textbox_style.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 20))

        self.btn_generate = ctk.CTkButton(self.tab_gen, text="Start Generation", height=40, font=ctk.CTkFont(weight="bold"), command=self._start_generation)
        self.btn_generate.grid(row=4, column=0, pady=10)

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

    def _save_settings(self):
        api_key = self.entry_api_key.get().strip()
        haydee_path = self.entry_path.get().strip()
        author = self.entry_author.get().strip()
        res = self.combo_res.get()

        if not api_key or not haydee_path:
            messagebox.showwarning("Warning", "Please fill in both API Key and Game Path.")
            return

        self.config_manager.config["gemini_api_key"] = api_key
        self.config_manager.config["haydee_path"] = haydee_path
        self.config_manager.config["author_name"] = author
        self.config_manager.config["image_resolution"] = res
        self.config_manager.save()

        messagebox.showinfo("Success", "Settings saved successfully!")

    def _prepare_for_task(self):
        """Helper to save config and block UI before a task"""
        self._save_settings()
        if not self.config_manager.config["gemini_api_key"] or not self.config_manager.config["haydee_path"]:
             return False

        self.btn_generate.configure(state="disabled")
        self.btn_group.configure(state="disabled")
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

        if not mod_name or not style:
            messagebox.showerror("Error", "Mod name and style description are required.")
            return
        
        if self._prepare_for_task():
            threading.Thread(target=self._run_generator_thread, args=(mod_name, style), daemon=True).start()

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

    def _run_generator_thread(self, mod_name, style):
        try:
            api_key = self.config_manager.config["gemini_api_key"]
            haydee_path = Path(self.config_manager.config["haydee_path"])
            author = self.config_manager.config.get("author_name", "")
            res = self.config_manager.config["image_resolution"]
            
            outfits_dir = haydee_path / "Outfits"
            base_dds = outfits_dir / "Haydee" / "Suit_D.dds"

            if not base_dds.exists():
                raise FileNotFoundError(f"Base texture not found at {base_dds}. Please verify your game path.")

            builder = ModBuilder(mod_name, outfits_dir=outfits_dir, author=author if author else None)
            builder.prepare_directory()

            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                base_png = temp_path / "base_Suit_D.png"
                generated_jpg = temp_path / "generated_Suit_D.jpg"

                ImageProcessor.dds_to_png(base_dds, base_png)

                client = GeminiModClient(api_key=api_key, image_resolution=res)
                client.generate_texture(base_image_path=base_png, style=style, output_path=generated_jpg)

                final_dds_path = builder.mod_dir / "Suit_D.dds"
                ImageProcessor.img_to_dds(generated_jpg, final_dds_path, resolution=res)

            builder.generate_mtl_file()
            builder.generate_outfit_file()
            
            self.logger.info(f"Mod '{mod_name}' generated successfully! You can now test it in Haydee.")
            self.after(0, lambda: messagebox.showinfo("Done", f"Mod '{mod_name}' generated successfully!"))
            
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
        self.tabview.configure(state="normal")
