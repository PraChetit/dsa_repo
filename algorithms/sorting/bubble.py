"""Implementation of bubble sort."""

from algorithms.sorting import utils


def basic_bubble_sort(array):
  """Basic implementation of bubble sort."""
  utils.check_array(array)
  for i in reversed(range(len(array))):
    for j in range(i):
      if array[j] > array[j + 1]:
        utils.swap(array, j, j + 1)
  return array


def bubble_sort(array):
  """Optimized implementation of bubble sort.

  The worst case is the same as the basic version, but in case the array is
  sorted after several passes, this variant is able to terminate early.
  """
  utils.check_array(array)
  end = len(array)
  while True:
    new_end = 0
    for i in range(end - 1):
      if array[i] > array[i + 1]:
        utils.swap(array, i, i + 1)
        new_end = i
    if new_end == 0:
      break
  return array
