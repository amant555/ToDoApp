class ToDoList:
    def __init__(self):
        self.tasks = []

    def addtask(self):
        task = input("Enter the task: ")
        if len(task) == 0:
            raise ValueError("Empty Task")
        self.tasks.append(task)

    def viewtasks(self):
        for task in self.tasks:
            print(task)
