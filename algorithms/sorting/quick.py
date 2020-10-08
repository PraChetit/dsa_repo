"""Implementation of quick sort."""

import random

from algorithms.sorting import utils


def quick_sort(array):
  _quick_sort_impl(array, 0, len(array))  # Sorted in-place.
  return array


def _quick_sort_impl(array, i, j):
  if (j - i) < 2:
    return  # Already sorted.
  p = _partition(array, i, j)
  _quick_sort_impl(array, i, p)
  _quick_sort_impl(array, p + 1, j)


def _partition(array, i, j):
  # Move a random element to the end of the sub-array.
  utils.swap(array, random.randrange(i, j), j - 1)

  p = i - 1
  for q in range(i, j - 1):
    if array[q] < array[j - 1]:
      p += 1
      utils.swap(array, p, q)
  if p < j - 1:
    utils.swap(array, p + 1, j - 1)
  return p + 1  # Returns the index of the pivot.
