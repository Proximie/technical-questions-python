import unittest
from pascals_triangle import execute

class TestPascalsTriangle(unittest.TestCase):
    def test_handles_zero_execute(self):
        self.assertEqual(execute(0), [])

    def test_handles_single_row(self):
        self.assertEqual(execute(1), [[1]])

    def test_handles_two_execute(self):
        self.assertEqual(execute(2), [[1], [1, 1]])

    def test_handles_three_execute(self):
        self.assertEqual(execute(3), [[1], [1, 1], [1, 2, 1]])

    def test_handles_four_execute(self):
        self.assertEqual(execute(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_handles_five_execute(self):
        self.assertEqual(execute(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_handles_six_execute(self):
        self.assertEqual(execute(6), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])

    def test_handles_ten_execute(self):
        self.assertEqual(execute(10), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]])

if __name__ == '__main__':
    unittest.main()
