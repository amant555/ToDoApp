import unittest
from unittest.mock import patch
from io import StringIO
from ToDoList import ToDoList


class ToDoListTest(unittest.TestCase):
    @patch('builtins.input', return_value="Meet Ema at 7")
    def test_adding_single_task_in_todo_and_matching_view_output_with_expected_for_single_task(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Meet Ema at 7\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "Complete the assignment"])
    def test_adding_two_tasks_in_todo_and_checking_if_view_output_matches_expected(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Meet Ema at 7\nComplete the assignment\n", fake_out.getvalue())

    input_string_for_third_test = ''

    @patch('builtins.input', return_value=input_string_for_third_test)
    def test_adding_no_task_raises_value_error(self, mock_input):
        todo = ToDoList()
        with self.assertRaisesRegex(ValueError, "Empty Task"):
            todo.add_task()


if __name__ == '__main__':
    unittest.main()
