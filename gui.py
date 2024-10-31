import modules.todo_list_logic as todo_list_logic
import FreeSimpleGUI as sg
import time

CLOCK_KEY = "clock"
CLOCK_FORMAT = "%b %d, %Y %H:%M:%S"
TASK_INPUT_KEY = "task"
TASK_LIST_KEY = "task_list"
NEW_TASK_BUTTON_LABEL = "Add task"
EDIT_TASK_BUTTON_LABEL = "Edit task"
COMPLETE_TASK_BUTTON_LABEL = "Complete task"
EXIT_BUTTON_LABEL = "Exit"
FONT = ("Helvetica", 20)
EMPTY_TASK_MESSAGE = "Please type in a task first!"
NO_TASK_SELECTED_MESSAGE = "Please select a task first!"

def init_ui(todo_list):
    sg.theme("DarkTeal12")

    clock = sg.Text(time.strftime(CLOCK_FORMAT), key=CLOCK_KEY)
    add_label = sg.Text("Type in a task")
    input_box = sg.InputText(tooltip="Type in a task", key=TASK_INPUT_KEY)
    add_button = sg.Button(NEW_TASK_BUTTON_LABEL)
    list_box = sg.Listbox(values=todo_list, key=TASK_LIST_KEY, enable_events=True, size=[45,10])
    edit_button = sg.Button(EDIT_TASK_BUTTON_LABEL)
    complete_button = sg.Button(COMPLETE_TASK_BUTTON_LABEL)
    exit_button = sg.Button(EXIT_BUTTON_LABEL)

    layout = [
        [clock],
        [add_label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]
        ]
    ret = sg.Window("To-Do App", 
                    layout=layout, 
                    font=FONT)
    return ret


todo_list = todo_list_logic.read_todo_list()
window = init_ui(todo_list)

while True:
    event, values = window.read(timeout=200)

    if event == sg.WINDOW_CLOSED or event == EXIT_BUTTON_LABEL:
        break

    window[CLOCK_KEY].update(value=time.strftime(CLOCK_FORMAT))

    if event == NEW_TASK_BUTTON_LABEL:
        if not any(values[TASK_INPUT_KEY]):
            sg.popup(EMPTY_TASK_MESSAGE, font=FONT)
            continue

        todo_list_logic.add_task(todo_list, values[TASK_INPUT_KEY])
        window[TASK_LIST_KEY].update(values=todo_list)
        window[TASK_INPUT_KEY].update(value="")
    elif event == TASK_LIST_KEY:
        window[TASK_INPUT_KEY].update(value=values[TASK_LIST_KEY][0])
    elif event == EDIT_TASK_BUTTON_LABEL:
        if not any(values[TASK_LIST_KEY]):
            sg.popup(NO_TASK_SELECTED_MESSAGE, font=FONT)
            continue

        if not any(values[TASK_INPUT_KEY]):
            sg.popup(EMPTY_TASK_MESSAGE, font=FONT)
            continue

        modified_task = values[TASK_INPUT_KEY]
        index = todo_list.index(values[TASK_LIST_KEY][0])

        todo_list_logic.edit_task(todo_list, index, modified_task)
        window[TASK_LIST_KEY].update(values=todo_list)
        window[TASK_INPUT_KEY].update(value="")
    elif event == COMPLETE_TASK_BUTTON_LABEL:
        if not any(values[TASK_LIST_KEY]):
            sg.popup(NO_TASK_SELECTED_MESSAGE, font=FONT)
            continue

        index = todo_list.index(values[TASK_LIST_KEY][0])

        todo_list_logic.complete_task(todo_list, index)
        window[TASK_LIST_KEY].update(values=todo_list)
        window[TASK_INPUT_KEY].update(value="")

window.close()