import os
import shutil
from datetime import datetime

source_folder = "source_data"
backup_root = "backups"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(backup_root, timestamp)

file_count = 0
total_size = 0

try:
    if not os.path.exists(source_folder):
        raise FileNotFoundError("Source folder not found")

    os.makedirs(backup_folder)

    for file in os.listdir(source_folder):

        source_file = os.path.join(source_folder, file)
        backup_file = os.path.join(backup_folder, file)

        if os.path.isfile(source_file):

            shutil.copy2(source_file, backup_file)

            file_count += 1

            total_size += os.path.getsize(source_file)

    print(f"{file_count} files backed up successfully!")
    print(f"Total Backup Size: {total_size} bytes")

    with open("backup_log.txt", "a") as log:
        log.write(
            f"Backup created at {timestamp} | "
            f"Files: {file_count} | "
            f"Size: {total_size} bytes\n"
        )

except Exception as e:
    print("Error:", e)