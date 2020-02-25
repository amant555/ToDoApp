class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self):
        task = input("Enter the task: ")
        if len(task) == 0:
            raise ValueError("Empty Task")
        self.tasks.append(task)

    def view(self):
        for task in self.tasks:
            print(task)
