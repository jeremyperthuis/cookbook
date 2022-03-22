
import unittest
from app import module_1, module_2


class Test_add(unittest.TestCase):

    def test_add(self):
        self.assertEqual(module_1.add(4,4), 8)
        self.assertEqual(module_1.add(4,3), 7)

    def test_multiply(self):
        self.assertEqual(module_2.multiply(4,4), 16)
        self.assertEqual(module_2.multiply(4, 3), 12)

    def test_add_multiply(self):
        self.assertEqual(module_2.add_multiply(4,7), 35)


if __name__ == '__main__':
    unittest.main()



