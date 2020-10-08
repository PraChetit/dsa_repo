"""Implementation of a stooge sort.

This sorting algorithm has time complexity of O(n^(log(3) / log(1.5))), or
approximately O(n^2.71), and is thus quite bad. But fun.
"""

import math

from algorithms.sorting import utils


def stooge_sort(array):
  _stooge_sort_impl(array, 0, len(array))  # Sorted in-place.
  return array


def _stooge_sort_impl(array, i, j):
  if (j - i) < 2:
    return array  # Already sorted.

  if array[i] > array[j - 1]:
    utils.swap(array, i, j - 1)

  if (j - i) > 2:
    gap = math.ceil(2 * (j - i) / 3)
    _stooge_sort_impl(array, i, i + gap)
    _stooge_sort_impl(array, j - gap, j)
    _stooge_sort_impl(array, i, i + gap)
