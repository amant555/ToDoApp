import unittest
from unittest.mock import patch
from io import StringIO
from ToDoList import ToDoList

task = ToDoList()


class ToDoListTest(unittest.TestCase):
    input_string_for_first_test = "Hi"

    # ToDo - Its just sample test that is working and class has been created need to work through for further tests
    @patch('builtins.input', return_value=input_string_for_first_test)
    def test_adding_first_task_adds_the_task_to_the_list(self, mock_input):
        task.add()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            task.view()
            self.assertEqual("Task 1: Hi\n", fake_out.getvalue())

    input_string_for_second_test = "Hello"
    #
    # @patch('builtins.input', return_value=input_string_for_first_test)
    # def test_adding_second_task_adds_the_task_to_the_list(self, mock_input):
    #     ToDoList().add()
    #     self.assertEqual("Task 1: Hi\nTask 2: Hello", ToDoList().view())


if __name__ == '__main__':
    unittest.main()
