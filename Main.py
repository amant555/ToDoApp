from ToDoList import ToDoList

todo = ToDoList()

print("0. Exit\n1. Add task\n2. View task\n3. Edit task\n4. Mark a task as complete")


def invalid():
    print("Invalid option")


def task_options(i):
    switcher = {
        0: exit,
        1: todo.add_task,
        2: todo.view_tasks,
        3: todo.edit_task,
        4: todo.mark_completed,
        # 5: todo.save_file,
    }
    return switcher.get(i, invalid)()


while 1:
    try:
        option = int(input("Enter option to proceed: "))
        task_options(option)
    except ValueError:
        print("Invalid option")
