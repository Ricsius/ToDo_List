def show_todo_list():
  for i in range(len(todo_list)):
      task = todo_list[i].capitalize()
      print(f"{i + 1}. {task}")

todo_list = []
user_prompt = "Type add, show, edit or exit: "
task_prompt = "Enter a task: "
task_number_prompt = "Number of the task to the edit: "
task_modify_prompt = "Enter new task: "
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
            show_todo_list()

            number = int(input(task_number_prompt))
            index = number - 1

            if(index in range(len(todo_list))):
                modified_task = input(task_modify_prompt)
                todo_list[index] = modified_task
            else:
                print(invalid_task_number_error)
        case "exit":
            break
        case unknown_action:
            print(f"\"{unknown_action}\" is an unknown action!")

print("bye")