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
        "\nChoose an option:\n1. Add Task\n2. View Tasks\n3. Edit/Update Task\n4. Delete Task\n5. Search Task\n6. Exit"
    )
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        Utilities.add_task("Task_Data.json")
    elif choice == "2":
        task_id_input = input(
            "Enter task ID to view a specific task or press Enter to view all tasks: "
        )
        task_id = int(task_id_input) if task_id_input else None
        Utilities.view_tasks(tasks, task_id)
    elif choice == "3":
        Utilities.edit_task("Task_Data.json")
    elif choice == "4":
        Utilities.delete_task("Task_Data.json")
    elif choice == "5":
        Utilities.search_task("Task_Data.json")
    elif choice == "6":
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
