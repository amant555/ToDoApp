from ToDoList import ToDoList

todo = ToDoList()


def invalid():
    print("Invalid option")


def task_options(i):
    switcher = {
        0: exit,
        1: todo.add_task,
        2: todo.view_tasks,
        3: todo.edit_task,
        4: todo.mark_completed,
        # 5: todo.generate_file,
    }
    return switcher.get(i, invalid)()


while 1:
    option = int(input("Enter option to proceed: "))
    task_options(option)