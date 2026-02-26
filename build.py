import os
import subprocess
import sys

def build_exe():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print("Starting application build...")
    
    # PyInstaller command
    # --noconsole hides the black terminal window
    # --onefile packages everything into a single .exe
    # --name sets the output file name
    command = [
        sys.executable, "-m", "PyInstaller",
        "--noconsole",
        "--onefile",
        "--name", "HaydeeOutfitGenerator",
        "--clean",
        "main.py"
    ]
    
    try:
        subprocess.run(command, check=True)
        print("\nBuild completed successfully!")
        print(f"Executable file is located in the folder: {os.path.abspath('dist')}")
    except subprocess.CalledProcessError as e:
        print(f"\nError during build: {e}")

if __name__ == "__main__":
    build_exe()
