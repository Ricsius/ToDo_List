todo_list = []
user_prompt = "Enter todo: "

while True:
    task = input(user_prompt).capitalize()
    todo_list.append(task)
    
    print(todo_list)