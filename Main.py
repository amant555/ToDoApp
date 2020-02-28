from Format import Format
from ToDoList import ToDoList

formatter = Format()
todo = ToDoList(formatter)
options = """
\n
0. Exit
1. Add task
2. View task
3. Edit task
4. Mark a task as complete
5. Save list to file
"""


def invalid():
    print("Invalid option")


def task_options(i):
    switcher = {
        0: exit,
        1: todo.add_task,
        2: todo.view_tasks,
        3: todo.edit_task,
        4: todo.mark_completed,
        5: todo.save_task,
    }
    return switcher.get(i, invalid)()


while 1:
    try:
        print(options)
        option = int(input("\nEnter option to proceed: "))
        task_options(option)
    except ValueError:
        print("Invalid option")
