import unittest

import ToDoList


class ToDoListTest(unittest.TestCase):
    def test_adding_first_task_adds_the_task_to_the_list(self):
        self.assertEqual("Task Added Successfully", ToDoList.add("Hi"))


if __name__ == '__main__':
    unittest.main()
