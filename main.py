
from datetime import datetime

def create_entry():
    try:
        entry = input("Write your diary entry: ")

        with open("diary.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n[{timestamp}]\n{entry}\n")

        print("Diary entry saved successfully!")

    except PermissionError:
        print("Error: Permission denied. Cannot save the diary.")
    except OSError as error:
        print("Error saving diary:", error)


def view_entries():
    try:
        with open("diary.txt", "r") as file:
            entries = file.read()

        if entries:
            print("\n--- Previous Diary Entries ---")
            print(entries)
        else:
            print("Your diary is empty.")

    except FileNotFoundError:
        print("No diary entries found yet.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the diary.")
    except OSError as error:
        print("Error reading diary:", error)


def main():
    while True:
        print("\n--- Personal Diary ---")
        print("1. Create a new entry")
        print("2. View previous entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    return


if __name__ == "__main__":
    main()
