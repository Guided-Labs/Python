## Testing add and subtract functions

import unittest
from main import add, subtract

class TestMainFunctions(unittest.TestCase):
    """Unit test class for testing functions in main.py."""

    def test_add(self):
        """Test case for the add function."""
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 equals 5
        self.assertEqual(add(-1, 1), 0)  # Test if -1 + 1 equals 0

    def test_subtract(self):
        """Test case for the subtract function."""
        self.assertEqual(subtract(5, 3), 2)  # Test if 5 - 3 equals 2
        self.assertEqual(subtract(0, 5), -5)  # Test if 0 - 5 equals -5

if __name__ == '__main__':
    unittest.main()



## Testing a String Function

# import unittest
# from main import capitalize_word
# class TestStringFunctions(unittest.TestCase):
#     """Unit test class for testing string functions."""

#     def test_capitalize_word(self):
#         """Test case for capitalize_word function."""
#         self.assertEqual(capitalize_word('hello'), 'Hello')  # Test if 'hello' becomes 'Hello'
#         self.assertEqual(capitalize_word('python'), 'Python')  # Test if 'python' becomes 'Python'



## Testing a List Function

# import unittest
# from main import get_first_element
# class TestListFunctions(unittest.TestCase):
#     """Unit test class for testing list functions."""

#     def test_get_first_element(self):
#         """Test case for get_first_element function."""
#         self.assertEqual(get_first_element([1, 2, 3]), 1)  # Test if the first element is 1
#         self.assertEqual(get_first_element([]), None)  # Test if an empty list returns None