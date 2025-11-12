# A module to put in utility functions such as add, view, edit, delete tasks and search tasks.
import json
import pprint


def print_welcome_message():
    print("\nWelcome to the To-Do List App!")


def Load_Tasks_From_File(file_path):
    with open(file_path, "r") as file:
        tasks = json.load(file)
    return tasks


def Save_Tasks_To_File(file_path, tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task_due_date = input("Enter the task due date (YYYY-MM-DD): ")
    task_priority = input("Enter the task priority (Low, Medium, High): ")

    with open(task, "r") as file:
        tasks = json.load(file)

    new_task = {
        "task_id": len(tasks["tasks"]) + 1,
        "name": task_name,
        "description": task_description,
        "due date": task_due_date,
        "priority": task_priority,
        "status": "Pending",
    }

    tasks["tasks"].append(new_task)

    with open(task, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Task added successfully!")


def delete_task(task, task_id):
    with open(task, "r") as file:
        tasks = json.load(file)

    print(task_id)
    if task_id > len(tasks["tasks"]):
        print("\nTask ID not found.")
        return
    tasks["tasks"].pop(task_id)
    with open(task, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Task deleted successfully!")


def edit_task(task, task_id, update_option):
    with open(task, "r") as file:
        tasks = json.load(file)

    if task_id >= len(tasks["tasks"]):
        print("\nTask ID not found.")
        return
    if update_option == "1":
        new_name = input("Enter the new task name: ")
        tasks["tasks"][task_id]["name"] = new_name
    elif update_option == "2":
        new_description = input("Enter the new task description: ")
        tasks["tasks"][task_id]["description"] = new_description
    elif update_option == "3":
        new_due_date = input("Enter the new task due date (YYYY-MM-DD): ")
        tasks["tasks"][task_id]["due_date"] = new_due_date
    elif update_option == "4":
        new_priority = input("Enter the new task priority (Low, Medium, High): ")
        tasks["tasks"][task_id]["priority"] = new_priority
    elif update_option == "5":
        new_status = input(
            "Enter the new task status (Pending, In-progress, Completed): "
        )
        tasks["tasks"][task_id]["status"] = new_status
    else:
        print("Invalid update option.")
        return
    with open(task, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Task edited successfully!")


def view_tasks(task, task_id=None):
    if task_id is None or not int(task_id):
        pprint.pprint(f"Here are your tasks: {task}")
    elif task_id is not None and task_id <= len(task["tasks"]):
        pprint.pprint(
            f"Here is your task: {task["tasks"][task_id - 1]}"
        )  # Adjusting for zero-based index
    elif task_id > len(task["tasks"]):
        print("\nTask ID not found.")
