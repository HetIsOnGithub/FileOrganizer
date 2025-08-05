import os
import shutil
import time
import sys
from pyfiglet import Figlet

def type_out(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


fig = Figlet(font='slant')  
ascii_banner = fig.renderText('File Organizer')
type_out(ascii_banner)
type_out('By Het\n')
print('-' * 60)


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Executables": [".exe", ".msi"],
    "Others": []
}


TARGET_DIR = input("📁 Please enter directory path: ").strip()
if not os.path.isdir(TARGET_DIR):
    print("❌ Invalid directory path.")
    sys.exit()

TARGET_DIR = os.path.normpath(TARGET_DIR)

def get_category(ext):
    for cat, exts in FILE_TYPES.items():
        if ext.lower() in exts:
            return cat
    return "Others"

def organizeFiles(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            continue
        _, ext = os.path.splitext(file)
        category = get_category(ext)
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        new_path = os.path.join(category_path, file)
        shutil.move(file_path, new_path)
        print(f"🔁 Moved: {file} → {category}/")


organizeFiles(TARGET_DIR)
print("✅ All files organized.")
