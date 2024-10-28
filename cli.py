import modules.todo_list_logic as todo_list_logic
import time

todo_list = []
user_prompt = "Type add, show, edit, complete or exit: "
task_modify_prompt = "Enter new task: "
invalid_command_message = "Invalid command!"
invalid_task_number_message = "Invalid task number!"

def show_todo_list():
  for i, task in enumerate(todo_list):
      print(f"{i + 1}. {task}")

todo_list = todo_list_logic.read_todo_list()
now = time.strftime("%Y-%m-%d %H:%M")

print(f"It is: {now}")

while True:
    user_action = input(user_prompt).strip()
    
    if user_action.startswith("add "):
        task = user_action[4:]

        todo_list_logic.add_task(todo_list, task)
    elif user_action == "show":
        show_todo_list()
    elif user_action.startswith("edit "):
        try:
            index = int(user_action[5:]) - 1

            if index in range(len(todo_list)):
                task = todo_list[index]
                modified_task = input(task_modify_prompt)

                todo_list_logic.edit_task(todo_list, index, modified_task)
                print(f"\"{task}\" is modified to \"{modified_task}\".")
            else:
                print(invalid_task_number_message)
        except ValueError:
            print(invalid_command_message)
    elif user_action.startswith("complete "):
        try:
            index = int(user_action[9:]) - 1
            if index in range(len(todo_list)):
                todo_list_logic.complete_task(todo_list, index)
                print(f"\"{task}\" is completed.")
            else:
                print(invalid_task_number_message)
        except ValueError:
            print(invalid_command_message)
    elif user_action == "exit":
        exit("bye")
    else:
        print(f"\"{user_action}\" is an unknown action!")