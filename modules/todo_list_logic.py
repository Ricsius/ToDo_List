import os.path

todo_list_path = "todo_list.txt"

def process_task(task):
    return task.capitalize().strip()

def read_todo_list():
    if not os.path.isfile(todo_list_path):
        return []

    with open(todo_list_path, "r") as file:
        ret = file.readlines()
        ret = [process_task(task) for task in ret]

    return ret

def save_todo_list(todo_list):
    with open(todo_list_path, "w") as file:
        for task in todo_list:
            file.write(f"{task}\n")

def add_task(todo_list, task):
    task = process_task(task)

    todo_list.append(task)
    save_todo_list(todo_list)

def edit_task(todo_list, index, modified_task):
    modified_task = process_task(modified_task)
    todo_list[index] = modified_task

    save_todo_list(todo_list)

def complete_task(todo_list, index):
    todo_list.pop(index)
    save_todo_list(todo_list)