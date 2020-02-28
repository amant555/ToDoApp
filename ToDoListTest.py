import unittest
from io import StringIO
from unittest.mock import patch

from Format import Format
from ToDoList import ToDoList


class ToDoListTest(unittest.TestCase):
    @patch('builtins.input', return_value="Meet Ema at 7")
    def test_adding_single_task_in_todo_and_matching_view_output_with_expected(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Meet Ema at 7\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "Complete the assignment"])
    def test_adding_two_tasks_in_todo_and_checking_if_view_output_matches_expected(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Meet Ema at 7\n2. Complete the assignment\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7", "Complete the assignment"])
    def test_adding_two_tasks_in_two_todo_and_checking_if_output_matches_expected(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo1 = ToDoList(formatter)
        todo1.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Meet Ema at 7\n", fake_out.getvalue())

    @patch('builtins.input', return_value='')
    def test_adding_no_task(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.add_task()
            self.assertEqual("Empty Task\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7:00", 1, "Meet Ema at 8:00"])
    def test_adding_task_and_editing_there_itself(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Meet Ema at 7:00\n", fake_out.getvalue())
        todo.edit_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Meet Ema at 8:00\n", fake_out.getvalue())

    def test_empty_todo_list(self):
        formatter = Format()
        todo = ToDoList(formatter)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Your TODO list is empty!\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Have Lunch at 1:00pm", "Meet Ema at 7:00", 2, "Meet Stacy at 8:00"])
    def test_adding_two_task_and_editing_second_task(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n2. Meet Ema at 7:00\n", fake_out.getvalue())
        todo.edit_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n2. Meet Stacy at 8:00\n",
                             fake_out.getvalue())

    @patch('builtins.input', side_effect=["Have Lunch at 1:00pm", "Meet Ema at 7:00", 2])
    def test_marking_a_task_as_complete_moves_it_to_the_complete_list(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        todo.mark_completed()

        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n\nComplete Tasks:\n\n1. Meet Ema at 7:00\n",
                             fake_out.getvalue())

    @patch('builtins.input',
           side_effect=["Have Lunch at 1:00pm", "Meet Ema at 7:00", "Do your assignments", "Sleep", 2])
    def test_the_list_order_is_retained_when_a_task_from_middle_is_marked_as_complete(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.mark_completed()

        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual(
                "Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n2. Do your assignments\n3. Sleep\n\nComplete Tasks:\n\n1. Meet Ema at 7:00\n",
                fake_out.getvalue())

    @patch('builtins.input',
           side_effect=["Have Lunch at 1:00pm", "Meet Ema at 7:00", "Do your assignments", "Sleep", 7])
    def test_the_task_which_is_not_in_list_can_not_be_marked_as_completed(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.add_task()

        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual(
                "Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n2. Meet Ema at 7:00\n3. Do your assignments\n4. Sleep\nThe task you're trying to mark is not present in the list\n",
                fake_out.getvalue())

    @patch('builtins.input',
           side_effect=["Have Lunch at 1:00pm", "Meet Ema at 7:00", "Do your assignments", "Sleep", -1])
    def test_when_the_task_number_is_negative_it_can_not_be_marked_as_completed(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.add_task()

        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual(
                "Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n2. Meet Ema at 7:00\n3. Do your assignments\n4. Sleep\nThe task you're trying to mark is not present in the list\n",
                fake_out.getvalue())

    def test_when_TODO_list_is_empty_mark_as_complete_is_not_allowed(self):
        formatter = Format()
        todo = ToDoList(formatter)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.mark_completed()
            self.assertEqual("Your TODO list is empty!\n", fake_out.getvalue())

    @patch('builtins.input',
           side_effect=["Have Lunch at 1:00pm", "Send Email at 3:00", "Meeting at 4:00"])
    def test_when_saving_tasks_in_a_file(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.add_task()
        todo.add_task()
        todo.save_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with open("MyTasks.txt", "r") as file:
                content = file.readlines()
            all_tasks = ""
            for _ in content:
                all_tasks += _
            self.assertEqual("Incomplete Tasks:\n\n1. Have Lunch at 1:00pm\n2. Send Email at 3:00\n3. Meeting at 4:00",
                             all_tasks)

    @patch('builtins.input', return_value="")
    def test_when_saving_empty_tasks_in_a_file(self, mock_input):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.save_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with open("MyTasks.txt", "r") as file:
                content = file.readlines()
            all_tasks = ""
            for _ in content:
                all_tasks += _
            self.assertEqual("Your TODO list is empty!", all_tasks)

    def test_when_TODO_list_is_empty_then_no_task_to_delete(self):
        formatter = Format()
        todo = ToDoList(formatter)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.delete_task()
            self.assertEqual("Your Todo List is empty\n", fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7:00", 1, 1])
    def test_when_TODO_list_is_not_empty_then_one_task_to_delete(self, mock_list_type):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.delete_task()
            self.assertEqual("Your task has been deleted successfully\n",
                             fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Ema at 7:00", 1, 2, 1])
    def test_when_TODO_list_is_not_empty_and_list_type_is_given_then_one_task_to_delete(self, mock_list_type):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.mark_completed()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.delete_task()
            self.assertEqual("Your task has been deleted successfully\n",
                             fake_out.getvalue())

    @patch('builtins.input', side_effect=["Meet Rishabh", 1])
    def test_when_incomplete_list_is_empty_and_completed_list_has_elements(self, mock_list_type):
        formatter = Format()
        todo = ToDoList(formatter)
        todo.add_task()
        todo.mark_completed()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            todo.view_tasks()
            self.assertEqual("Complete Tasks:\n\n1. Meet Rishabh\n", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
