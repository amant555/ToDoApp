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
            self.assertEqual("1. Meet Ema at 7\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "Complete the assignment"])
    def test_adding_two_tasks_in_todo_and_checking_if_view_output_matches_expected(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("1. Meet Ema at 7\n2. Complete the assignment\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "Complete the assignment"])
    def test_adding_two_tasks_in_two_different_todo_lists_and_checking_if_view_output_matches_expected(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        todo1 = ToDoList()
        todo1.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("1. Meet Ema at 7\n", fake_out.getvalue())

    @patch('builtins.input', return_value='')
    def test_adding_no_task_raises_value_error(self, mock_input):
        todo = ToDoList()
        with self.assertRaisesRegex(ValueError, "Empty Task"):
            todo.add_task()


    @patch('builtins.input', side_effect=["Meet Ema at 7:00", 1, "Meet Ema at 8:00"])
    def test_adding_task_and_editing_there_itself(self, mock_input):
        todo = ToDoList()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("1. Meet Ema at 7:00\n", fake_out.getvalue())
        todo.edit_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("1. Meet Ema at 8:00\n", fake_out.getvalue())

    def test_empty_todo_list(self):
        todo = ToDoList()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Your TODO list is empty!\n", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
