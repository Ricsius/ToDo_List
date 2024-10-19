import os.path

todo_list = []
todo_list_path = "todo_list.txt"
user_prompt = "Type add, show, edit, complete or exit: "
task_modify_prompt = "Enter new task: "
invalid_command_message = "Invalid command!"
invalid_task_number_message = "Invalid task number!"

def process_task(task):
    return task.capitalize().strip()

def add_task(task):
    task = process_task(task)

    todo_list.append(task)
    save_todo_list()
    print(f"{task} is added.")

def show_todo_list():
  for i, task in enumerate(todo_list):
      print(f"{i + 1}. {task}")

def edit_task(index):
    if index in range(len(todo_list)):
        modified_task = input(task_modify_prompt)
        modified_task = process_task(modified_task)
        task = todo_list[index]
        todo_list[index] = modified_task

        save_todo_list()
        print(f"\"{task}\" is modified to \"{modified_task}\".")
    else:
        print(invalid_task_number_message)

def complete_task(index):
    if index in range(len(todo_list)):
        task = todo_list.pop(index)

        save_todo_list()
        print(f"\"{task}\" is completed.")
    else:
        print(invalid_task_number_message)

def read_todo_list():
    if not os.path.isfile(todo_list_path):
        return []

    with open(todo_list_path, "r") as file:
        ret = file.readlines()
        ret = [process_task(task) for task in ret]

    return ret

def save_todo_list():
    with open(todo_list_path, "w") as file:
        for task in todo_list:
            file.write(f"{task}\n")

todo_list = read_todo_list()

while True:
    user_action = input(user_prompt).strip()
    
    if user_action.startswith("add "):
        task = user_action[4:]

        add_task(task)
    elif user_action == "show":
        show_todo_list()
    elif user_action.startswith("edit "):
        try:
            index = int(user_action[5:]) - 1

            edit_task(index)
        except ValueError:
            print(invalid_command_message)
    elif user_action.startswith("complete "):
        try:
            index = int(user_action[9:]) - 1
            
            complete_task(index)
        except ValueError:
            print(invalid_command_message)
    elif user_action == "exit":
        exit("bye")
    else:
        print(f"\"{user_action}\" is an unknown action!")