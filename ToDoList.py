class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task: ")
        if len(task) == 0:
            raise ValueError("Empty Task")
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            task_number = 1
            for task in self.tasks:
                print(str(task_number) + ". " + task)
                task_number += 1
        else:
            print("Your TODO list is empty!")
