import os #Python talk to operating system: create folders, list files, build file paths.
import shutil #handles high-level file operations like moving, copying, deleting files.

def move_jpgs(source_folder, dest_folder):
    os.makedirs(dest_folder, exist_ok=True) #create destination folder if it doesn't exist
    moved = 0
    for filename in os.listdir(source_folder): #list all files in the source folder
        if filename.lower().endswith(".jpg"): #check if the file has a .jpg extension (case-insensitive)
            src = os.path.join(source_folder, filename)
            dst = os.path.join(dest_folder, filename) # glues the folder and filename together properly for your OS
            shutil.move(src, dst)
            moved += 1
    print(f"Moved {moved} .jpg files to {dest_folder}")

# name of folders with jpg files and destination folder

move_jpgs("Wallpaper", "DestinedFloder")