import streamlit as st
import function

todos = function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("Todo-App")
st.subheader("This is an todo app")

for index, todo in enumerate(todos):
    cheeckbox = st.checkbox(todo,key=todo)
    if cheeckbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input("",placeholder="Enter a todo",on_change=add_todo,key = "new_todo")