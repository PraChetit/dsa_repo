import dataclasses
import itertools

from absl.testing import absltest
from absl.testing import parameterized

from algorithms.sorting.bubble import bubble_sort
from algorithms.sorting.gnome import gnome_sort
from algorithms.sorting.insertion import insertion_sort
from algorithms.sorting.merge import merge_sort

_SORTING_ALGORITHMS = [('bubble_sort', bubble_sort),
                       ('gnome_sort', gnome_sort),
                       ('insertion_sort', insertion_sort),
                       ('merge_sort', merge_sort)]

_TEST_100_ELEM_DATA = [
  ('case_0', [63, 90, 45, 50, 81, 46, 6, 3, 41, 85, 74, 72, 19, 43, 88, 51, 0,
              69, 52, 70, 8, 89, 20, 59, 79, 18, 94, 40, 71, 93, 33, 23, 62, 26,
              48, 36, 65, 21, 37, 95, 7, 84, 75, 82, 86, 47, 66, 57, 68, 92, 80,
              24, 54, 64, 30, 91, 10, 4, 78, 60, 97, 35, 58, 44, 34, 39, 42, 29,
              32, 5, 1, 9, 96, 73, 49, 83, 87, 25, 38, 17, 76, 27, 67, 61, 2,
              11, 16, 98, 13, 12, 15, 53, 22, 56, 31, 55, 28, 14, 77, 99]),
  ('case_1', [99, 8, 79, 19, 0, 69, 88, 92, 95, 38, 84, 5, 82, 33, 28, 87, 46,
              80, 57, 11, 65, 2, 35, 52, 30, 75, 67, 40, 86, 31, 14, 62, 44, 16,
              96, 29, 85, 51, 54, 93, 22, 21, 17, 37, 48, 74, 45, 56, 26, 27,
              76, 73, 50, 3, 13, 58, 41, 91, 10, 23, 6, 24, 61, 43, 72, 68, 97,
              39, 49, 9, 94, 53, 34, 60, 4, 77, 78, 55, 36, 47, 63, 98, 71, 66,
              25, 32, 20, 90, 18, 64, 12, 70, 81, 89, 15, 59, 1, 83, 42, 7]),
  ('case_2', [11, 20, 31, 16, 69, 75, 50, 3, 79, 1, 49, 25, 39, 67, 10, 42, 37,
              80, 46, 88, 62, 83, 77, 14, 44, 86, 84, 58, 12, 40, 89, 72, 4, 8,
              68, 87, 71, 2, 93, 6, 47, 17, 64, 94, 27, 18, 66, 97, 76, 9, 48,
              61, 38, 35, 36, 7, 28, 56, 78, 26, 73, 53, 19, 99, 52, 74, 21, 5,
              13, 15, 32, 90, 54, 33, 0, 70, 81, 59, 85, 34, 55, 24, 82, 23, 45,
              29, 51, 30, 92, 91, 57, 41, 43, 22, 60, 98, 63, 95, 65, 96]),
  ('case_3', [62, 92, 58, 67, 85, 84, 93, 98, 72, 11, 32, 78, 42, 82, 8, 44, 24,
              83, 7, 17, 69, 15, 71, 20, 12, 57, 37, 76, 22, 6, 96, 55, 16, 3,
              5, 34, 68, 10, 89, 40, 81, 90, 70, 99, 18, 25, 49, 31, 87, 0, 54,
              30, 97, 91, 33, 66, 38, 80, 77, 65, 63, 50, 9, 39, 64, 59, 73, 1,
              29, 61, 23, 43, 53, 51, 46, 35, 94, 2, 86, 48, 75, 56, 47, 79, 28,
              4, 74, 27, 26, 95, 60, 88, 41, 45, 19, 21, 13, 52, 36, 14]),
  ('case_4', [25, 57, 27, 31, 63, 1, 19, 32, 56, 60, 78, 14, 20, 37, 74, 33, 40,
              61, 65, 22, 81, 54, 94, 76, 75, 80, 42, 13, 43, 3, 79, 29, 23, 62,
              53, 0, 68, 46, 49, 95, 77, 89, 58, 5, 44, 83, 98, 73, 84, 36, 52,
              4, 45, 71, 87, 67, 15, 35, 28, 66, 2, 11, 16, 93, 41, 48, 59, 88,
              9, 18, 38, 55, 86, 30, 21, 51, 24, 90, 85, 72, 97, 96, 91, 92, 69,
              7, 70, 6, 50, 34, 26, 12, 17, 10, 47, 8, 39, 99, 64, 82]),
  ('case_5', [54, 90, 7, 50, 32, 94, 65, 34, 63, 25, 11, 6, 9, 31, 96, 69, 35,
              28, 2, 16, 81, 5, 68, 64, 52, 30, 77, 45, 70, 60, 26, 8, 27, 10,
              51, 0, 83, 79, 88, 23, 84, 86, 55, 87, 18, 20, 95, 42, 66, 19, 98,
              24, 22, 48, 67, 56, 97, 71, 37, 44, 46, 74, 57, 21, 4, 59, 14, 62,
              43, 92, 40, 73, 85, 13, 41, 61, 38, 1, 15, 58, 47, 89, 72, 12, 99,
              49, 78, 75, 29, 33, 93, 82, 53, 91, 36, 39, 76, 17, 80, 3]),
  ('case_6', [98, 66, 29, 10, 47, 35, 59, 31, 38, 46, 54, 45, 34, 53, 55, 99,
              82, 87, 63, 69, 36, 26, 78, 32, 57, 65, 7, 71, 50, 83, 12, 33, 17,
              97, 88, 90, 62, 18, 22, 1, 39, 28, 91, 79, 94, 84, 75, 72, 30, 74,
              48, 23, 6, 14, 20, 52, 9, 40, 86, 89, 77, 24, 37, 49, 56, 85, 11,
              67, 15, 73, 19, 61, 3, 2, 25, 81, 5, 4, 51, 93, 27, 95, 8, 16, 60,
              96, 13, 76, 58, 44, 64, 41, 42, 80, 43, 70, 92, 68, 21, 0]),
  ('case_7', [84, 3, 20, 37, 7, 11, 9, 21, 8, 50, 22, 31, 83, 16, 90, 71, 93,
              80, 26, 67, 74, 36, 42, 69, 32, 97, 1, 5, 29, 10, 39, 12, 41, 60,
              49, 0, 85, 63, 66, 40, 81, 64, 56, 14, 98, 59, 23, 77, 65, 46, 44,
              6, 79, 68, 72, 15, 55, 54, 95, 45, 2, 70, 88, 87, 57, 86, 91, 52,
              78, 96, 99, 47, 28, 33, 34, 13, 51, 19, 18, 58, 75, 61, 4, 24, 73,
              27, 30, 43, 89, 92, 62, 94, 48, 35, 76, 25, 17, 82, 38, 53]),
  ('case_8', [87, 10, 71, 51, 12, 55, 90, 84, 57, 13, 52, 14, 79, 6, 66, 97, 81,
              80, 7, 2, 24, 49, 96, 41, 95, 76, 42, 4, 94, 29, 47, 54, 5, 62,
              63, 75, 8, 65, 50, 69, 77, 1, 34, 40, 36, 28, 20, 44, 9, 3, 22,
              67, 30, 68, 73, 16, 86, 17, 70, 74, 92, 88, 21, 37, 27, 56, 32,
              26, 85, 83, 91, 31, 19, 98, 61, 43, 48, 53, 0, 59, 38, 45, 99, 25,
              58, 93, 78, 46, 18, 35, 82, 72, 64, 23, 89, 33, 15, 39, 11, 60]),
  ('case_9', [73, 27, 19, 6, 5, 51, 41, 93, 30, 77, 3, 37, 54, 13, 20, 64, 45,
              62, 70, 56, 21, 99, 35, 81, 43, 42, 0, 84, 79, 36, 90, 44, 74, 72,
              23, 68, 34, 87, 80, 50, 22, 47, 94, 24, 69, 92, 63, 39, 59, 18,
              10, 52, 8, 60, 66, 75, 11, 40, 88, 58, 26, 71, 25, 96, 46, 55, 91,
              2, 38, 53, 98, 95, 49, 1, 33, 32, 78, 82, 29, 16, 76, 57, 86, 89,
              61, 15, 97, 7, 85, 17, 65, 4, 14, 31, 67, 48, 12, 83, 9, 28])]


class SortingTest(parameterized.TestCase):

  def _test(self, sort_alg, input_array, expected_array):
    sorted_array = sort_alg(input_array)
    self.assertListEqual(expected_array, sorted_array)

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_empty_array(self, sort_alg):
    self._test(sort_alg, [], [])

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_single_element_array(self, sort_alg):
    self._test(sort_alg, [0], [0])

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_two_element_array(self, sort_alg):
    self._test(sort_alg, [0, 1], [0, 1])
    self._test(sort_alg, [1, 0], [0, 1])

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_three_element_array(self, sort_alg):
    self._test(sort_alg, [0, 1, 2], [0, 1, 2])
    self._test(sort_alg, [0, 2, 1], [0, 1, 2])
    self._test(sort_alg, [1, 0, 2], [0, 1, 2])
    self._test(sort_alg, [1, 2, 0], [0, 1, 2])
    self._test(sort_alg, [2, 0, 1], [0, 1, 2])
    self._test(sort_alg, [2, 1, 0], [0, 1, 2])

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_sorting_comparable_class_instances(self, sort_alg):
    """Test sorting elements of complex structure implementing __ge__ etc."""

    @dataclasses.dataclass(order=True)
    class Item:
      value: int = dataclasses.field(compare=False)
      key: int

    a = Item(1, 1)
    b = Item(-1, 2)
    c = Item(4, 3)
    d = Item(0, 4)
    e = Item(1, 5)
    f = Item(1, 6)

    self._test(sort_alg, [a, b, c, d, e, f], [a, b, c, d, e, f])
    self._test(sort_alg, [f, e, d, c, b, a], [a, b, c, d, e, f])
    self._test(sort_alg, [b, c, f, e, a, d], [a, b, c, d, e, f])
    self._test(sort_alg, [e, a, b, f, d, c], [a, b, c, d, e, f])

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_sorted_array(self, sort_alg):
    array = list(range(100))
    self._test(sort_alg, array, array)

  @parameterized.named_parameters(_SORTING_ALGORITHMS)
  def test_reverse_sorted_array(self, sort_alg):
    reversed_array = list(reversed(range(100)))
    sorted_array = list(range(100))
    self._test(sort_alg, reversed_array, sorted_array)

  # Combines all algorithms and 100-element test cases. This will generate test
  # names such as `test_example_100_elem_array_bubble_sort_case_0`.
  @parameterized.named_parameters(
    [('_'.join([alg[0], case[0]]), alg[1], case[1]) for alg, case in
     itertools.product(_SORTING_ALGORITHMS, _TEST_100_ELEM_DATA)])
  def test_example_100_elem_array(self, sort_alg, test_case):
    sorted_array = list(range(100))
    self._test(sort_alg, test_case, sorted_array)


if __name__ == '__main__':
  absltest.main()
