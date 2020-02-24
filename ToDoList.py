tasks = []
task_number = 0


def add(task):
    global task_number
    task_number += 1
    task1 = "Task " + str(task_number) + ": " + task + "\n"
    return task1
