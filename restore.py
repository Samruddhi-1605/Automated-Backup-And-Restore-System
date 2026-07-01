import os
import shutil

backup_root = "backups"
restore_folder = "restored_files"

try:
    backups = os.listdir(backup_root)

    if not backups:
        print("No backups found!")
        exit()

    print("\nAvailable Backups:\n")

    for i, backup in enumerate(backups):
        print(f"{i+1}. {backup}")

    choice = int(input("\nSelect Backup Number: ")) - 1

    selected_backup = os.path.join(
        backup_root,
        backups[choice]
    )

    os.makedirs(restore_folder, exist_ok=True)

    for file in os.listdir(selected_backup):
        source_file = os.path.join(selected_backup, file)
        restore_file = os.path.join(restore_folder, file)

        shutil.copy2(source_file, restore_file)

    print("\nRestore completed successfully!")

except Exception as e:
    print("Error:", e)