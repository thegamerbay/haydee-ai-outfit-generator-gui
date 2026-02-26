import os
import sys
import threading
import logging
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Import your library
from haydee_outfit_gen.config import settings
from haydee_outfit_gen.main import main as generate_mod
from dotenv import set_key, load_dotenv

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

        # Path to .env file next to the executable
        self.env_path = Path.cwd() / ".env"
        load_dotenv(self.env_path)

        self._build_ui()
        self._load_settings()
        self._setup_logging()

    def _setup_logging(self):
        """Redirect library logs to our text box"""
        logger = logging.getLogger("haydee_outfit_gen")
        logger.setLevel(logging.INFO)
        
        # Clear default handlers to avoid duplicates in hidden console
        if logger.hasHandlers():
            logger.handlers.clear()
            
        handler = CustomTextHandler(self.log_console)
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

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
        """Load settings from .env into GUI"""
        api_key = os.getenv("GEMINI_API_KEY", "")
        haydee_path = os.getenv("HAYDEE_PATH", "")
        res = os.getenv("IMAGE_RESOLUTION", "4K")

        self.entry_api_key.insert(0, api_key)
        self.entry_path.insert(0, haydee_path)
        self.combo_res.set(res)

    def _save_settings(self):
        """Save GUI settings to .env file"""
        api_key = self.entry_api_key.get().strip()
        haydee_path = self.entry_path.get().strip()
        res = self.combo_res.get()

        if not api_key or not haydee_path:
            messagebox.showwarning("Warning", "Please fill in both API Key and Game Path.")
            return

        set_key(self.env_path, "GEMINI_API_KEY", api_key)
        set_key(self.env_path, "HAYDEE_PATH", haydee_path)
        set_key(self.env_path, "IMAGE_RESOLUTION", res)
        
        # Dynamically update library settings in memory
        settings.gemini_api_key = api_key
        settings.haydee_path = Path(haydee_path)
        settings.image_resolution = res

        messagebox.showinfo("Success", "Settings saved successfully!")

    def _start_generation(self):
        mod_name = self.entry_mod_name.get().strip()
        style = self.textbox_style.get("1.0", "end-1c").strip()

        if not mod_name or not style:
            messagebox.showerror("Error", "Mod name and style description are required.")
            return
        
        # Save settings to memory before generation in case user forgot to click "Save"
        settings.gemini_api_key = self.entry_api_key.get().strip()
        settings.haydee_path = Path(self.entry_path.get().strip())
        settings.image_resolution = self.combo_res.get()

        if not settings.gemini_api_key or not str(settings.haydee_path):
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
            # Mock CLI arguments
            sys.argv = ["haydee-gen", "--name", mod_name, "--style", style]
            
            # Call main library function
            generate_mod()
            
            self.after(0, lambda: messagebox.showinfo("Done", f"Mod '{mod_name}' generated successfully!"))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Generation Error", str(e)))
        finally:
            # Restore UI in main thread
            self.after(0, self._restore_ui)

    def _restore_ui(self):
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.btn_generate.configure(state="normal", text="✨ Generate Outfit")
