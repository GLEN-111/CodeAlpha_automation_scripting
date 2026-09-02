import os
import shutil


def move_jpg_files():
    source_folder = "source_folder"
    dest_folder = "jpg_folder"


    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(dest_folder, exist_ok=True)


    count = 0 
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            src = os.path.join(source_folder, file)
            dst = os.path.join(dest_folder, file)
            shutil.move(src, dst)
            print(f"Moved: {file}")
            count += 1

    if count == 0:
        print("No .jpg files found.")
    else:
        print(f"\nDone! {count} .jpg files moved to '{dest_folder}")

move_jpg_files()