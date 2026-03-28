import os


# Validate non-empty input
def input_text(message):

    while True:
        value = input(message).strip()

        if value == "":
            print("Error: input cannot be empty.")
        else:
            return value


# CREATE
def add_blocker():

    blocker = input_text("Enter your daily blocker: ")

    try:
        with open("database.txt", "a", encoding="utf-8") as file:
            file.write(blocker + "\n")

        print("Blocker saved successfully.")

    except Exception as e:
        print(f"Error saving blocker: {e}")


# READ
def fetch_blockers():

    if not os.path.exists("database.txt"):
        print("Error: database file does not exist.")
        return

    try:
        with open("database.txt", "r", encoding="utf-8") as file:

            lines = file.readlines()

            if not lines:
                print("No blockers found.")
                return

            print("\n--- TEAM BLOCKERS ---")

            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")

    except Exception as e:
        print(f"Error reading file: {e}")


# OVERWRITE (DELETE all content)
def overwrite_file():

    if not os.path.exists("database.txt"):
        print("Error: database file does not exist.")
        return

    while True:
        confirm = input("Are you sure you want to overwrite the file? (yes/no): ").lower()

        if confirm == "yes":

            try:
                with open("database.txt", "w", encoding="utf-8") as file:
                    file.write("")

                print("File has been overwritten.")
                return

            except Exception as e:
                print(f"Error overwriting file: {e}")
                return

        elif confirm == "no":
            print("Operation canceled.")
            return

        else:
            print("Invalid option. Please type 'yes' or 'no'.")


# Validate menu option
def input_option():

    while True:
        option = input("Select an option (1-4): ").strip()

        if option in ["1", "2", "3", "4"]:
            return option
        else:
            print("Invalid option. Please choose between 1 and 4.")


# MAIN
def main():

    running = True

    while running:

        print("\n--- DAILY STATUS SYSTEM ---")
        print("1. Add blocker")
        print("2. Fetch blockers")
        print("3. Overwrite file")
        print("4. Exit")

        option = input_option()

        if option == "1":
            add_blocker()

        elif option == "2":
            fetch_blockers()

        elif option == "3":
            overwrite_file()

        elif option == "4":
            print("Exiting program.")
            running = False


if __name__ == "__main__":
    main()


# -----------------------------
# ENGLISH TASKS
# -----------------------------

"""
Protocol selection:
I will reach out to the team via Slack because the issue is an immediate blocker.
I will use Email when I need to provide a detailed explanation of the problem.
I will report the issue in Jira to track the error and assign it to the responsible person.

Vocabulary integration:
This script demonstrates persistence by saving user input into a text file. 
It allows users to fetch stored data and review previous blockers. 
The overwrite feature ensures that the file can be reset when needed. 
If an issue occurs, I can reach out to the team to resolve it efficiently.
"""