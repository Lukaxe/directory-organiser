# Use uv add when you want to add packages
import open_desktop as od
from dotenv import load_dotenv
import os

def main():
    print("Hello from desktop-organiser!")
    load_dotenv()
    folder_path = os.getenv('FOLDER_TO_BE_CLEANED')
    if folder_path:
        print("Environment variable found!")
    od.createFolders(od.sortFolder(od.openFolder(folder_path)), folder_path)

if __name__ == "__main__":
    main()