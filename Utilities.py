# A module to put in utility functions such as add, view, edit, delete tasks and search tasks.
import json
import pprint


def print_welcome_message():
    print("\nWelcome to the To-Do List App!")


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
        "due_date": task_due_date,
        "priority": task_priority,
        "status": "Pending",
    }

    tasks["tasks"].append(new_task)

    with open(task, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Task added successfully!")


def delete_task(task):
    pass


def edit_task(task):
    pass


def view_task(task, task_id):
    if task_id is not None:
        pprint.pprint(
            f"Here is your task: {task["tasks"][task_id - 1]}"
        )  # Adjusting for zero-based index
    else:
        print(f"\nHere are your tasks: {task}")


def search_task(task):
    pass
