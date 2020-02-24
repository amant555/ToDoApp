import unittest

import ToDoList


class ToDoListTest(unittest.TestCase):
    def test_adding_first_task_adds_the_task_to_the_list(self):
        self.assertEqual("Task 1: Hi\n", ToDoList.add("Hi"))

    def test_adding_second_task_adds_the_task_to_the_list(self):
        self.assertEqual("Task 2: Hello\n", ToDoList.add("Hello"))


if __name__ == '__main__':
    unittest.main()
