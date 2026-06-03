import os
import shutil

def organize_files(folder):

    file_types = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4"],
        "Music": [".mp3"]
    }

    for filename in os.listdir(folder):

        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):

            for category, extensions in file_types.items():

                if filename.lower().endswith(tuple(extensions)):

                    category_folder = os.path.join(folder, category)

                    os.makedirs(category_folder, exist_ok=True)

                    shutil.move(filepath,
                                os.path.join(category_folder, filename))

                    break
