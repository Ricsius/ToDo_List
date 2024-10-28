import FreeSimpleGUI.window
import modules.todo_list_logic as todo_list_logic
import FreeSimpleGUI as sg

add_label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Type in a task")
add_button = sg.Button("Add task")
layout = [
    [add_label],
    [input_box, add_button]
    ]
window = sg.Window("To-Do App", layout=layout)

window.read()
window.close()