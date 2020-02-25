class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task: ")
        if len(task) == 0:
            raise ValueError("Empty Task")
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def edit_task(self):
        task_to_edit = int(input("Enter the task number to edit (like 1 for first task you added) : "))
        if task_to_edit < 1 or task_to_edit > len(self.tasks):
            raise ValueError("Task number invalid")
        task_to_edit -= 1
        updated_task = input("Enter the updated task you want in place of previous one : ")
        self.tasks[task_to_edit] = updated_task
