import threading
import logging
import tempfile
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Прямые импорты из библиотеки
from haydee_outfit_gen.mod_builder import ModBuilder
from haydee_outfit_gen.gemini_client import GeminiModClient
from haydee_outfit_gen.image_processor import ImageProcessor

from src.config_manager import ConfigManager

# Setup CustomTkinter appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CustomTextHandler(logging.Handler):
    """Custom log handler to redirect output to GUI text box"""
    def __init__(self, textbox):
        super().__init__()
        self.textbox = textbox

    def emit(self, record):
        msg = self.format(record)
        # Use after for thread-safe UI updates
        self.textbox.after(0, self.append_text, msg)

    def append_text(self, msg):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", msg + "\n")
        self.textbox.see("end")  # Auto-scroll down
        self.textbox.configure(state="disabled")

class HaydeeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Haydee AI Outfit Generator")
        self.geometry("900x650")
        self.minsize(800, 600)

        self.config_manager = ConfigManager()

        self._build_ui()
        self._load_settings()
        self._setup_logging()

    def _setup_logging(self):
        """Redirect library logs to our text box"""
        self.logger = logging.getLogger("haydee_outfit_gen")
        self.logger.setLevel(logging.INFO)
        
        # Clear default handlers to avoid duplicates in hidden console
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
            
        handler = CustomTextHandler(self.log_console)
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _build_ui(self):
        # Grid setup
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # === LEFT PANEL (Settings) ===
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.left_frame, text="⚙️ Settings", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 20))

        # Gemini API Key
        ctk.CTkLabel(self.left_frame, text="Gemini API Key:").pack(anchor="w", padx=20)
        self.entry_api_key = ctk.CTkEntry(self.left_frame, show="*", placeholder_text="Paste your key here...")
        self.entry_api_key.pack(fill="x", padx=20, pady=(0, 15))

        # Haydee Path
        ctk.CTkLabel(self.left_frame, text="Haydee Game Path:").pack(anchor="w", padx=20)
        self.path_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.path_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        self.entry_path = ctk.CTkEntry(self.path_frame, placeholder_text="C:\\Program Files (x86)\\Steam\\...")
        self.entry_path.pack(side="left", fill="x", expand=True)
        
        self.btn_browse = ctk.CTkButton(self.path_frame, text="📂", width=40, command=self._browse_directory)
        self.btn_browse.pack(side="right", padx=(5, 0))

        # Resolution
        ctk.CTkLabel(self.left_frame, text="Resolution:").pack(anchor="w", padx=20)
        self.combo_res = ctk.CTkComboBox(self.left_frame, values=["4K", "2K"])
        self.combo_res.pack(fill="x", padx=20, pady=(0, 20))

        # Save Button
        self.btn_save = ctk.CTkButton(self.left_frame, text="💾 Save Settings", command=self._save_settings)
        self.btn_save.pack(padx=20, pady=(0, 20))

        # === RIGHT PANEL (Generation) ===
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nsew")
        self.right_frame.grid_rowconfigure(3, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.right_frame, text="🎨 Mod Generation", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, pady=(20, 20))

        # Mod Name
        self.frame_mod_name = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.frame_mod_name.grid(row=1, column=0, sticky="ew", padx=20)
        ctk.CTkLabel(self.frame_mod_name, text="Mod Name (e.g. NeonSurge):").pack(anchor="w")
        self.entry_mod_name = ctk.CTkEntry(self.frame_mod_name)
        self.entry_mod_name.pack(fill="x", pady=(0, 15))

        # Style Prompt
        self.frame_style = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.frame_style.grid(row=2, column=0, sticky="ew", padx=20)
        ctk.CTkLabel(self.frame_style, text="Style Description (Prompt):").pack(anchor="w")
        self.textbox_style = ctk.CTkTextbox(self.frame_style, height=80)
        self.textbox_style.pack(fill="x", pady=(0, 15))

        # Generate Button & Progress
        self.btn_generate = ctk.CTkButton(self.right_frame, text="✨ Generate Outfit", height=40, font=ctk.CTkFont(weight="bold"), command=self._start_generation)
        self.btn_generate.grid(row=3, column=0, pady=10)
        
        self.progress_bar = ctk.CTkProgressBar(self.right_frame, mode="indeterminate")
        # Hide progress bar before generation
        self.progress_bar.set(0)

        # Log Console
        ctk.CTkLabel(self.right_frame, text="Execution Console:").grid(row=4, column=0, sticky="w", padx=20)
        self.log_console = ctk.CTkTextbox(self.right_frame, height=150, state="disabled", fg_color="#1E1E1E", text_color="#00FF00")
        self.log_console.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="nsew")

    def _browse_directory(self):
        dir_path = filedialog.askdirectory(title="Select Haydee Game Folder")
        if dir_path:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, dir_path)

    def _load_settings(self):
        """Load settings from ConfigManager into GUI"""
        self.entry_api_key.insert(0, self.config_manager.config.get("gemini_api_key", ""))
        self.entry_path.insert(0, self.config_manager.config.get("haydee_path", ""))
        self.combo_res.set(self.config_manager.config.get("image_resolution", "4K"))

    def _save_settings(self):
        """Save GUI settings to ConfigManager"""
        api_key = self.entry_api_key.get().strip()
        haydee_path = self.entry_path.get().strip()
        res = self.combo_res.get()

        if not api_key or not haydee_path:
            messagebox.showwarning("Warning", "Please fill in both API Key and Game Path.")
            return

        self.config_manager.config["gemini_api_key"] = api_key
        self.config_manager.config["haydee_path"] = haydee_path
        self.config_manager.config["image_resolution"] = res
        self.config_manager.save()

        messagebox.showinfo("Success", "Settings saved successfully!")

    def _start_generation(self):
        mod_name = self.entry_mod_name.get().strip()
        style = self.textbox_style.get("1.0", "end-1c").strip()

        if not mod_name or not style:
            messagebox.showerror("Error", "Mod name and style description are required.")
            return
        
        # Save settings to memory before generation
        self.config_manager.config["gemini_api_key"] = self.entry_api_key.get().strip()
        self.config_manager.config["haydee_path"] = self.entry_path.get().strip()
        self.config_manager.config["image_resolution"] = self.combo_res.get()
        self.config_manager.save()

        if not self.config_manager.config["gemini_api_key"] or not self.config_manager.config["haydee_path"]:
             messagebox.showerror("Error", "API Key or Game Path is not configured!")
             return

        # Block UI
        self.btn_generate.configure(state="disabled", text="Generating...")
        self.progress_bar.grid(row=3, column=0, sticky="s", pady=(50, 0))
        self.progress_bar.start()
        
        self.log_console.configure(state="normal")
        self.log_console.delete("1.0", "end")
        self.log_console.configure(state="disabled")

        # Start in separate thread
        threading.Thread(target=self._run_generator_thread, args=(mod_name, style), daemon=True).start()

    def _run_generator_thread(self, mod_name, style):
        try:
            # Получаем настройки
            api_key = self.config_manager.config["gemini_api_key"]
            haydee_path = Path(self.config_manager.config["haydee_path"])
            res = self.config_manager.config["image_resolution"]
            
            outfits_dir = haydee_path / "Outfits"
            base_dds = outfits_dir / "Haydee" / "Suit_D.dds"

            if not base_dds.exists():
                raise FileNotFoundError(f"Base texture not found at {base_dds}. Please verify your game path.")

            # 1. Настройка директории
            builder = ModBuilder(mod_name, outfits_dir=outfits_dir)
            builder.prepare_directory()

            # 2. Временная директория для конвертации
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                base_png = temp_path / "base_Suit_D.png"
                generated_jpg = temp_path / "generated_Suit_D.jpg"

                # 3. Конвертация исходника
                ImageProcessor.dds_to_png(base_dds, base_png)

                # 4. Генерация Gemini API
                client = GeminiModClient(api_key=api_key, image_resolution=res)
                client.generate_texture(
                    base_image_path=base_png,
                    style=style,
                    output_path=generated_jpg
                )

                # 5. Сохранение обратно в DDS
                final_dds_path = builder.mod_dir / "Suit_D.dds"
                ImageProcessor.img_to_dds(generated_jpg, final_dds_path, resolution=res)

            # 6. Генерация конфигурационных файлов игры
            builder.generate_mtl_file()
            builder.generate_outfit_file()
            
            self.logger.info(f"Mod '{mod_name}' generated successfully! You can now test it in Haydee.")
            self.after(0, lambda: messagebox.showinfo("Done", f"Mod '{mod_name}' generated successfully!"))
            
        except Exception as e:
            self.logger.error(f"Generation failed: {e}")
            self.after(0, lambda err=str(e): messagebox.showerror("Generation Error", err))
        finally:
            # Restore UI in main thread
            self.after(0, self._restore_ui)

    def _restore_ui(self):
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.btn_generate.configure(state="normal", text="✨ Generate Outfit")
