import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_that_returns_true_if_list_is_empty(self):
        stack_list = []
        stack = Stack(stack_list)

        self.assertTrue(stack.is_empty())

    def test_that_returns_false_if_list_is_not_empty(self):
        stack_list = [1, 2, 3, 4, 5, 'carrot']
        stack = Stack(stack_list)

        self.assertFalse(stack.is_empty())

    def test_that_element_pushed_to_list(self):
        stack_list = []
        stack = Stack(stack_list)
        stack.push(5)
        stack.push('Hi!')

        self.assertEqual(stack.stack_list, [5, 'Hi!'])

    def test_that_returns_none_if_list_is_empty(self):
        stack_list = []
        stack = Stack(stack_list)

        self.assertEqual(stack.pop(), None)

    def test_that_last_element_removed_form_list_pop(self):
        stack_list = [1, 2, 3, 4, 5, 'carrot']
        target_list = [1, 2, 3, 4, 5]
        stack = Stack(stack_list)
        stack.pop()
        self.assertEqual(stack.stack_list, target_list)

    def test_that_returns_none_if_list_is_empty_peek(self):
        stack_list = []
        stack = Stack(stack_list)

        self.assertEqual(stack.peek(), None)

    def test_that_last_element_selected_form_list(self):
        stack_list = [1, 2, 3, 4, 5, 'carrot']
        target = 'carrot'
        stack = Stack(stack_list)
        self.assertEqual(stack.peek(), target)

if __name__ == '__main__':
    unittest.main()
