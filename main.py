def show_todo_list():
  for i, task in enumerate(todo_list):
      task = task.capitalize()
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

todo_list = []
user_prompt = "Type add, show, edit, complete or exit: "
task_prompt = "Enter a task: "
task_edit_prompt = "Number of the task to edit: "
task_modify_prompt = "Enter new task: "
task_complete_prompt = "Number of the task to complete: "
invalid_task_number_error = "Invalid task number!"

while True:
    user_action = input(user_prompt).strip()
    
    match user_action:
        case "add":
            task = input(task_prompt)
            todo_list.append(task)
        case "show":
            show_todo_list()
        case "edit":
            index = input_task_number(task_edit_prompt)

            if(index > -1):
                modified_task = input(task_modify_prompt)
                todo_list[index] = modified_task
        case "complete":
            index = input_task_number(task_complete_prompt)

            if(index > -1):
                todo_list.pop(index)
        case "exit":
            break
        case unknown_action:
            print(f"\"{unknown_action}\" is an unknown action!")

print("bye")