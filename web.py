import modules.todo_list_logic as todo_list_logic
import streamlit as st

TODO_LIST_KEY = "todo_list"
TASK_INPUT_KEY = "task_input"
TASK_EDIT_INPUT_KEY = "task_edit_input"
TASK_TO_EDIT_KEY = "task_to_edit"

def add_task():
    task = st.session_state[TASK_INPUT_KEY]
    todo_list_logic.add_task(st.session_state[TODO_LIST_KEY], task)
    st.session_state[TASK_INPUT_KEY] = ""

def edit_task():
    index = int(st.session_state[TASK_TO_EDIT_KEY].split("_")[0])
    modified_task = st.session_state[TASK_EDIT_INPUT_KEY]

    if modified_task.strip() == "":
        return

    todo_list_logic.edit_task(st.session_state[TODO_LIST_KEY], index, modified_task)
    st.session_state[TASK_TO_EDIT_KEY] = ""


if TODO_LIST_KEY not in st.session_state.keys():
    st.session_state[TODO_LIST_KEY] = todo_list_logic.read_todo_list()

if TASK_TO_EDIT_KEY not in st.session_state.keys():
    st.session_state[TASK_TO_EDIT_KEY] = ""

st.title("ToDo App")
st.subheader("Gather your tasks!")
st.write("Tasks")

for index, task in enumerate(st.session_state[TODO_LIST_KEY]):
    key = f"{index}_{task}"

    if key == st.session_state[TASK_TO_EDIT_KEY]:
        st.text_input(label="Edit",
              placeholder=f"{task}",
              key=TASK_EDIT_INPUT_KEY,
              on_change=edit_task)
    else:
        col1, col2 = st.columns(2)

        with col1:
            checkbox = st.checkbox(task, key=key)

        with col2:
            edit_button = st.button("Edit", key=f"{index}_Edit")

        if checkbox:
            del st.session_state[key]
            todo_list_logic.complete_task(st.session_state[TODO_LIST_KEY], index)
            st.rerun()

        if edit_button:
            st.session_state[TASK_TO_EDIT_KEY] = key
            st.rerun()
        

st.text_input(label="Type in a task",
              placeholder="Task",
              key=TASK_INPUT_KEY,
              on_change=add_task)