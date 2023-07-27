import unittest
from flatten_list import execute


class TestFlattenArray(unittest.TestCase):
    def test_handles_empty_list(self):
        expected = []
        actual = execute([])
        self.assertEqual(actual, expected)

    def test_flatten_integer_list_with_one_nested_list(self):
        expected = [1, 6, 54, 8, 22, 14]
        actual = execute([1, [6, 54], 8, [22, 14]])
        self.assertEqual(actual, expected)

    def test_flatten_integer_list_none(self):
        expected = [23, 15, 34]
        actual = execute([23, 15, None, 34, 0, None])
        self.assertEqual(actual, expected)

    def test_flatten_integer_list_with_several_levels_of_nested_lists(self):
        expected = [1, 6, 54, 22, 14, 3, 4, 6, 9]
        actual = execute([1, [6, 54], [[[22, 14]]], [3, None, [4, [6, 9]]], [[None]]])
        self.assertEqual(actual, expected)

    def test_flatten_string_list_with_several_levels_of_nested_lists_and_none(self):
        expected = ['apple', 'orange', 'banana', 'pear', 'strawberry', 'lemon', 'mandarin', 'grapes', 'mango']
        actual = execute(['apple', [['orange', 'banana']], [[['pear', 'strawberry', '']]],
                          ['lemon', None, ['mandarin', ['grapes', 'mango']]], [[None]]])
        self.assertEqual(actual, expected)

    def test_flatten_object_list_with_several_levels_of_nested_lists_and_none_and_empty_dict(self):
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

    def test_flatten_mixed_types_list_with_several_levels_of_nested_lists_and_none_and_empty_dict(self):
        expected = [{'name': 'square', 'corners': 4}, 43, {'name': 'triangle', 'corners': 3}, 'lemon', 'orange',
                    {'name': 'hexagon', 'corners': 6}, 56]
        actual = execute([{'name': 'square', 'corners': 4}, None, [[43, {'name': 'triangle', 'corners': 3}, None, 0]],
                          ['lemon', ['orange', [{'name': 'hexagon', 'corners': 6}, '', [56, {}]]]]])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
