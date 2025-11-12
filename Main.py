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
        "\nChoose an option:\n1. Add Task\n2. View Tasks\n3. Edit/Update Task\n4. Delete Task\n5. Exit"
    )
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        Utilities.add_task("Task_Data.json")
        Utilities.Load_Tasks_From_File("Task_Data.json")
    elif choice == "2":
        try:
            task_id = int(input("\nEnter task ID or press Enter to view all tasks: "))
        except ValueError:
            task_id = None
        Utilities.view_tasks(tasks, task_id)
    elif choice == "3":
        task_id_input = input("\nEnter task ID to edit: ")
        try:
            task_id = int(task_id_input) - 1  # Adjusting for zero-based index
            print(
                "\nChoose what to update: \n1. Name\n2. Description\n3. Due Date\n4. Priority\n5. Status"
            )
            update_option = input("Enter your choice (1-5): ")
        except ValueError:
            print("\nInvalid task ID. Please enter a number.")
        Utilities.edit_task("Task_Data.json", task_id, update_option)
        Utilities.Load_Tasks_From_File("Task_Data.json")
    elif choice == "4":
        task_id_input = input("\nEnter the task ID to delete: ")
        try:
            task_id = int(task_id_input) - 1  # Adjusting for zero-based index
            Utilities.delete_task("Task_Data.json", task_id)
            Utilities.Load_Tasks_From_File("Task_Data.json")
        except ValueError:
            print("\nInvalid task ID. Please enter a number.")
    elif choice == "5":
        print("\nExiting the To-Do List App. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
