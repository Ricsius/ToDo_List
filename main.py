import os.path

todo_list = []
todo_list_path = "todo_list.txt"
user_prompt = "Type add, show, edit, complete or exit: "
task_prompt = "Enter a task: "
task_edit_prompt = "Number of the task to edit: "
task_modify_prompt = "Enter new task: "
task_complete_prompt = "Number of the task to complete: "
invalid_task_number_error = "Invalid task number!"

def process_task(task):
    return task.capitalize().strip()

def show_todo_list():
  for i, task in enumerate(todo_list):
      print(f"{i + 1}. {task}")

def input_task_number(prompt):
    show_todo_list()

    number = int(input(prompt))
    index = number - 1

    if(index in range(len(todo_list))):
        return index
    else:
        print(invalid_task_number_error)
        return -1

def read_todo_list():
    if(not os.path.isfile(todo_list_path)):
        return []

    file = open(todo_list_path, "r")
    ret = file.readlines()
    ret = [process_task(task) for task in ret]
    file.close()

    return ret

def save_todo_list():
    file = open(todo_list_path, "w")
    
    for task in todo_list:
        file.write(f"{task}\n")
    
    file.close()

todo_list = read_todo_list()

while True:
    user_action = input(user_prompt).strip()
    
    match user_action:
        case "add":
            task = input(task_prompt)
            task = process_task(task)
            todo_list.append(task)
            save_todo_list()
        case "show":
            show_todo_list()
        case "edit":
            index = input_task_number(task_edit_prompt)

            if(index > -1):
                modified_task = input(task_modify_prompt)
                modified_task = process_task(modified_task)
                todo_list[index] = modified_task
                save_todo_list()
        case "complete":
            index = input_task_number(task_complete_prompt)

            if(index > -1):
                todo_list.pop(index)
                save_todo_list()
        case "exit":
            break
        case unknown_action:
            print(f"\"{unknown_action}\" is an unknown action!")

print("bye")