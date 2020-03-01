from SaveListsToFiles import SaveListsToFiles


class ToDoList:
    def __init__(self, formatter):
        self.incomplete_tasks = SaveListsToFiles().incomplete_task_list()
        self.completed_tasks = SaveListsToFiles().complete_task_list()
        self.formatter = formatter

    def add_task(self):
        new_task = input("Enter the task :").strip()
        self.incomplete_tasks.append(new_task) if new_task else print("Empty Task")

    def view_tasks(self):
        print(self.formatter.format(self))

    def save_task(self):
        my_tasks = open("MyTasks.txt", "w")
        my_tasks.write(self.formatter.format(self))
        my_tasks.close()
        SaveListsToFiles().save_to_files(self)

    def edit_task(self):
        task_to_edit = int(input("Enter the task number to edit (like 1 for first task you added) : "))
        if task_to_edit < 1 or task_to_edit > len(self.incomplete_tasks):
            print("Task number invalid")
        else:
            task_to_edit -= 1
            updated_task = input("Enter the updated task you want in place of previous one : ").strip()
            if len(updated_task):
                self.incomplete_tasks[task_to_edit] = updated_task
                print("Your task has been updated successfully!")
            else:
                print("Empty task")
                print("Your task cannot be updated!")

    def mark_completed(self):
        if len(self.incomplete_tasks):
            self.view_tasks()
            task_number = int(input("Enter the task number of task to be marked as completed: "))
            if task_number < 1 or task_number > len(self.incomplete_tasks):
                print("The task you're trying to mark is not present in the list")
            else:
                self.completed_tasks.append(self.incomplete_tasks[task_number - 1])
                del self.incomplete_tasks[task_number - 1]
        else:
            print("Your TODO list is empty!")
