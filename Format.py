class Format(object):
    def format(self, todo):
        text = ""
        if len(todo.incomplete_tasks) == 0 and len(todo.completed_tasks) == 0:
            text = "Your TODO list is empty!"
        elif len(todo.incomplete_tasks) > 0 and len(todo.completed_tasks) == 0:
            text = "Incomplete Tasks:\n"
            text += (Format.list_of_tasks(todo.incomplete_tasks))

        elif len(todo.completed_tasks) > 0 and len(todo.incomplete_tasks) == 0:
            text = "Complete Tasks:\n"
            text += (Format.list_of_tasks(todo.completed_tasks))

        elif len(todo.completed_tasks) > 0 and len(todo.incomplete_tasks) > 0:
            text = "Incomplete Tasks:\n"
            text += (Format.list_of_tasks(todo.incomplete_tasks))
            text += '\n\nComplete Tasks:\n'
            text += (Format.list_of_tasks(todo.completed_tasks))
        return text

    @staticmethod
    def list_of_tasks(task_type):
        msg = ""
        task_number = 1
        for task in task_type:
            msg += "\n" + str(task_number) + ". " + task
            task_number += 1
        return msg

