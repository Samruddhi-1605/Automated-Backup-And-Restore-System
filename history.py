try:

    with open(
        "backup_log.txt",
        "r"
    ) as log:

        print("\n===== BACKUP HISTORY =====\n")

        print(log.read())

except FileNotFoundError:

    print("No backup history found.")