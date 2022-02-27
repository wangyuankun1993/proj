import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.formatted_default = Employee('wang', 'yuankun', 1000)

    def test_give_default_raise(self):
        self.formatted_default.give_raise()
        self.assertEqual(self.formatted_default.salary, 6000)

    def test_give_custom_raise(self):
        self.formatted_default.give_raise(8000)
        self.assertEqual(self.formatted_default.salary, 9000)

unittest.main()