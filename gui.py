import modules.todo_list_logic as todo_list_logic
import FreeSimpleGUI as sg

task_input_key = "task"
task_list_key = "task_list"
new_task_button_label = "Add task"
edit_task_button_label = "Edit task"

def init_ui(todo_list):
    add_label = sg.Text("Type in a task")
    input_box = sg.InputText(tooltip="Type in a task", key=task_input_key)
    add_button = sg.Button(new_task_button_label)
    list_box = sg.Listbox(values=todo_list, key=task_list_key, enable_events=True, size=[45,10])
    edit_button = sg.Button(edit_task_button_label)

    layout = [
        [add_label],
        [input_box, add_button],
        [list_box, edit_button],
        ]
    ret = sg.Window("To-Do App", 
                    layout=layout, 
                    font=("Helvetica", 20))
    return ret

def refresh_task_list(window, values):
    window[task_list_key].update(values=values)

todo_list = todo_list_logic.read_todo_list()
window = init_ui(todo_list)

while True:
    event, values = window.read()
    
    if event == new_task_button_label:
        todo_list_logic.add_task(todo_list, values[task_input_key])
        refresh_task_list(window, todo_list)
        window[task_input_key].update(value="")
    elif event == task_list_key:
        window[task_input_key].update(value=values[task_list_key])
    elif event == edit_task_button_label:
        no_task_selected = len(values[task_list_key]) == 0

        if no_task_selected:
            continue

        task_to_edit = values[task_list_key][0]
        modified_task = values[task_input_key]
        index = todo_list.index(task_to_edit)

        todo_list_logic.edit_task(todo_list, index, modified_task)
        refresh_task_list(window, todo_list)
        window[task_input_key].update(value="")
    elif event == sg.WIN_CLOSED:
        break

window.close()