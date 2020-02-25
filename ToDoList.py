class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_number = 0

    def add(self):
        task = input("Enter the task: ")
        self.task_number += 1
        to_do = "Task " + str(self.task_number) + ": " + task
        self.tasks.append(to_do)

    def view(self):
        for task in self.tasks:
            print(task)
