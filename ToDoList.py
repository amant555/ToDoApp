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
