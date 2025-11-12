# Do a to-do list app with modular functions
# that allows users to add, view,edit, delete tasks and search tasks.
# also use Json or txt file to save the tasks.

# Things to learnd: File handling (open, write, read)

# JSON basics (saving structured data)

# Separation of logic (organizing functions)

import Utilities
import json

with open("Task_Data.json", "r") as file:
    tasks = json.load(file)

Utilities.print_welcome_message()

while True:
    print(
        "\nChoose an option:\n1. Add Task\n2. View/Search Tasks\n3. Edit/Update Task\n4. Delete Task\n5. Exit"
    )
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        Utilities.add_task("Task_Data.json")
        with open("Task_Data.json", "r") as file:
            tasks = json.load(file)
    elif choice == "2":
        task_id_input = input(
            "\nEnter task ID, Name, Priority or Status to view a specific task/s or press Enter to view all tasks: "
        )
        task_id = int(task_id_input) if task_id_input else None
        Utilities.view_tasks(tasks, task_id)
    elif choice == "3":
        Utilities.edit_task("Task_Data.json")
    elif choice == "4":
        task_id_input = input("\nEnter the task ID to delete: ")
        try:
            task_id = int(task_id_input) - 1  # Adjusting for zero-based index
        except ValueError:
            task_id = task_id_input  # Keep as string if not an integer
        Utilities.delete_task("Task_Data.json", task_id)
    elif choice == "5":
        print("\nExiting the To-Do List App. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
