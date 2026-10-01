from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent

def open_file(PACKAGE_DIR, file_path):
    complete_file_path = PACKAGE_DIR / file_path
    print("FILE PATH:", complete_file_path)
    with open(complete_file_path, "r", encoding="utf-8") as f:
        return f.read()
        
print (open_file(PACKAGE_DIR, "data/sample-data-sherlock.txt"))