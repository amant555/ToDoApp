import unittest
from unittest.mock import patch
from io import StringIO
from ToDoList import ToDoList


class ToDoListTest(unittest.TestCase):
    input_string_for_first_test = "Meet Ema at 7"

    @patch('builtins.input', return_value=input_string_for_first_test)
    def test_adding_first_task_adds_the_task_to_the_list(self, mock_input):
        task = ToDoList()
        task.add()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            task.view()
            self.assertEqual("Meet Ema at 7\n", fake_out.getvalue())

    input_string_1_for_second_test = "Meet Ema at 7"
    input_string_2_for_second_test = "Complete the assignment"

    @patch('builtins.input', side_effect=[input_string_1_for_second_test, input_string_2_for_second_test])
    def test_adding_second_task_adds_the_task_to_the_list(self, mock_input):
        task = ToDoList()
        task.add()
        task.add()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            task.view()
            self.assertEqual("Meet Ema at 7\nComplete the assignment\n", fake_out.getvalue())

    input_string_for_third_test = ''

    @patch('builtins.input', return_value=input_string_for_third_test)
    def test_adding_no_task_raises_value_error(self, mock_input):
        task = ToDoList()
        with self.assertRaisesWithMessage(ValueError):
            task.add()

    # input_string_1_for_second_test = "Meet Ema at 7"
    # input_string_2_for_second_test = "Complete the assignment"
    #
    # @patch('builtins.input', side_effect=[input_string_1_for_second_test, input_string_2_for_second_test])
    # def test_marking_task_as_complete_and_seperating_it_from_pending_tasks(self, mock_input):
    #     task = ToDoList()
    #     task.add()
    #     task.add()
    #     task.complete()
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         task.view()
    #         self.assertEqual("Complete the assignment\n", fake_out.getvalue())

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
