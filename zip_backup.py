import os
import zipfile
from datetime import datetime

source_folder = "source_data"
backup_folder = "backups"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

zip_file = os.path.join(
    backup_folder,
    f"backup_{timestamp}.zip"
)

try:

    with zipfile.ZipFile(
        zip_file,
        'w',
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for file in os.listdir(source_folder):

            file_path = os.path.join(
                source_folder,
                file
            )

            if os.path.isfile(file_path):

                zipf.write(
                    file_path,
                    arcname=file
                )

    print("\nZIP Backup Created Successfully!")
    print("Location:", zip_file)

except Exception as e:
    print("Error:", e)