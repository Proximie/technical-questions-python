import unittest
from flatten_array import execute


class TestFlattenArray(unittest.TestCase):
    def test_handles_empty_array(self):
        expected = []
        actual = execute([])
        self.assertEqual(actual, expected)

    def test_flatten_integer_array_with_one_nested_array(self):
        expected = [1, 6, 54, 8, 22, 14]
        actual = execute([1, [6, 54], 8, [22, 14]])
        self.assertEqual(actual, expected)

    def test_flatten_integer_array_with_falsy_values(self):
        expected = [23, 15, 34]
        actual = execute([23, 15, None, 34, 0, None])
        self.assertEqual(actual, expected)

    def test_flatten_integer_array_with_several_levels_of_nested_arrays(self):
        expected = [1, 6, 54, 22, 14, 3, 4, 6, 9]
        actual = execute([1, [6, 54], [[[22, 14]]], [3, None, [4, [6, 9]]], [[None]]])
        self.assertEqual(actual, expected)

    def test_flatten_string_array_with_several_levels_of_nested_arrays_and_falsy_values(self):
        expected = ['apple', 'orange', 'banana', 'pear', 'strawberry', 'lemon', 'mandarin', 'grapes', 'mango']
        actual = execute(['apple', [['orange', 'banana']], [[['pear', 'strawberry', '']]],
                          ['lemon', None, ['mandarin', ['grapes', 'mango']]], [[None]]])
        self.assertEqual(actual, expected)

    def test_flatten_object_array_with_several_levels_of_nested_arrays_and_falsy_values(self):
        expected = [{'name': 'square', 'corners': 4}, {'name': 'circle', 'corners': 0},
                    {'name': 'triangle', 'corners': 3}, {'name': 'rectangle', 'corners': 4},
                    {'name': 'ellipse', 'corners': 0}, {'name': 'hexagon', 'corners': 6},
                    {'name': 'pentagon', 'corners': 5}]
        actual = execute(
            [{'name': 'square', 'corners': 4}, [[{'name': 'circle', 'corners': 0}, {'name': 'triangle', 'corners': 3}]],
             [{'name': 'rectangle', 'corners': 4}, None, [{'name': 'ellipse', 'corners': 0},
                                                          [{'name': 'hexagon', 'corners': 6}, {},
                                                           [{'name': 'pentagon', 'corners': 5}]]]]])
        self.assertEqual(actual, expected)

    def test_flatten_mixed_types_array_with_several_levels_of_nested_arrays_and_falsy_values(self):
        expected = [{'name': 'square', 'corners': 4}, 43, {'name': 'triangle', 'corners': 3}, 'lemon', 'orange',
                    {'name': 'hexagon', 'corners': 6}, 56]
        actual = execute([{'name': 'square', 'corners': 4}, None, [[43, {'name': 'triangle', 'corners': 3}, None, 0]],
                          ['lemon', ['orange', [{'name': 'hexagon', 'corners': 6}, '', [56, {}]]]]])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
