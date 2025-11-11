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

Utilities.view_task(tasks["tasks"], None)
