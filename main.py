import os
import sys

# Important hack: set empty environment variables BEFORE importing the library, 
# so that pydantic-settings does not raise a ValidationError if the user runs the program for the first time.
os.environ.setdefault("GEMINI_API_KEY", "")
os.environ.setdefault("HAYDEE_PATH", "")

from src.app import HaydeeGUI

if __name__ == "__main__":
    app = HaydeeGUI()
    app.mainloop()
