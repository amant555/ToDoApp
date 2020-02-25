class ToDoList:
    def __init__(self):
        self.incomplete_tasks = []
        self.completed_tasks = []

    def add_task(self):
        task = input("Enter the task: ").strip()
        if len(task):
            self.incomplete_tasks.append(task)
        else:
            print("Empty Task")

    def view_tasks(self):
        if len(self.incomplete_tasks) == 0 and len(self.completed_tasks) == 0:
            print("Your TODO list is empty!")

        elif len(self.incomplete_tasks) > 0 and len(self.completed_tasks) == 0:
            print("Incomplete Tasks:\n")
            task_number = 1
            for task in self.incomplete_tasks:
                print(str(task_number) + ". " + task)
                task_number += 1

        elif len(self.completed_tasks) > 0 and len(self.incomplete_tasks) == 0:
            print("Complete Tasks:\n")
            task_number = 1
            for task in self.completed_tasks:
                print(str(task_number) + ". " + task)
                task_number += 1

        elif len(self.completed_tasks) > 0 and len(self.incomplete_tasks) > 0:
            print("Incomplete Tasks:\n")
            task_number = 1
            for task in self.incomplete_tasks:
                print(str(task_number) + ". " + task)
                task_number += 1

            print("Complete Tasks: \n")
            task_number = 1
            for task in self.completed_tasks:
                print(str(task_number) + ". " + task)
                task_number += 1

    def edit_task(self):
        task_to_edit = int(input("Enter the task number to edit (like 1 for first task you added) : "))
        if task_to_edit < 1 or task_to_edit > len(self.incomplete_tasks):
            raise ValueError("Task number invalid")
        task_to_edit -= 1
        updated_task = input("Enter the updated task you want in place of previous one : ")
        self.incomplete_tasks[task_to_edit] = updated_task

    def mark_completed(self):
        self.view_tasks()
        task_number = int(input("Enter the task number of task to be marked as completed: "))
        self.completed_tasks.append(self.incomplete_tasks[task_number - 1])
        del self.incomplete_tasks[task_number - 1]

    # def delete_task(self):
    #     task_to_delete = int(input("Enter task number: "))
    #     for task in
