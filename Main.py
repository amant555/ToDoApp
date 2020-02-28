from ToDoList import ToDoList

todo = ToDoList()
options = """
0. Exit
1. Add task
2. View task
3. Edit task
4. Mark a task as complete
5. Save list to file
"""
print(options)


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
        option = int(input("Enter option to proceed: "))
        task_options(option)
    except ValueError:
        print("Invalid option")
