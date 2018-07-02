import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_that_list_is_empty(self):
        stack_list = []
        stack = Stack(stack_list)

        self.assertTrue(stack.is_empty())

    def test_that_element_pushed_to_list(self):
        stack_list = []
        stack = Stack(stack_list)
        stack.push(5)
        stack.push('Hi!')

        self.assertEqual(stack.stack_list, [5, 'Hi!'])


if __name__ == '__main__':
    unittest.main()
