import modules.todo_list_logic as todo_list_logic
import streamlit as st

TASK_INPUT_KEY = "task_input"
todo_list = []

def add_task():
    task = st.session_state[TASK_INPUT_KEY]
    todo_list_logic.add_task(todo_list, task)
    st.session_state[TASK_INPUT_KEY] = ""

todo_list = todo_list_logic.read_todo_list()


st.title("ToDo App")
st.subheader("Gather your tasks!")
st.write("Tasks")

for index, task in enumerate(todo_list):
    checkbox = st.checkbox(task, key=task)

    if(checkbox):
        del st.session_state[task]
        todo_list_logic.complete_task(todo_list, index)
        st.rerun()

st.text_input(label="Type in a task",
              placeholder="Task",
              key=TASK_INPUT_KEY,
              on_change=add_task)