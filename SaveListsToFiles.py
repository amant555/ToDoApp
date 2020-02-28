import os.path


class SaveListsToFiles:
    def save_to_files(self, todo):
        incomplete_str = str(todo.incomplete_tasks)[1:-1]
        complete_str = str(todo.completed_tasks)[1:-1]

        incomplete_file = "Incomplete_tasks.txt"
        complete_file = "Completed_tasks.txt"

        incomplete_tasks = open(incomplete_file, "w")
        incomplete_tasks.write(incomplete_str)
        incomplete_tasks.close()

        complete_tasks = open(complete_file, "w")
        complete_tasks.write(complete_str)
        complete_tasks.close()

    def incomplete_task_list(self):
        if os.path.isfile("Incomplete_tasks.txt"):
            file_incomplete = open("Incomplete_tasks.txt", "r")
            incomplete = file_incomplete.read()
            incomplete = incomplete.replace("'", "")
            incomplete = list(incomplete.split(","))
        else:
            incomplete = []
        return incomplete

    def complete_task_list(self):
        if os.path.isfile("Completed_tasks.txt"):
            file_complete = open("Completed_tasks.txt", "r")
            complete = file_complete.read()
            complete = complete.replace("'", "")
            complete = list(complete.split(","))
        else:
            complete = []
        return complete


    def clear(self):
        os.remove("Incomplete_tasks.txt")
        os.remove("Completed_tasks.txt")