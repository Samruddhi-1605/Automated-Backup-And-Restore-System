import os

while True:

    print("\n")
    print("="*40)
    print(" AUTOMATED BACKUP SYSTEM ")
    print("="*40)

    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. View History")
    print("4. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        os.system("python backup.py")

    elif choice == "2":

        os.system("python restore.py")

    elif choice == "3":

        os.system("python history.py")

    elif choice == "4":

        print("Exiting...")

        break

    else:

        print("Invalid Choice")