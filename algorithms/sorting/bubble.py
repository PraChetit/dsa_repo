"""Implementation of bubble sort."""

from algorithms.sorting import utils


def bubble_sort(array):
  for i in reversed(range(len(array))):
    for j in range(i):
      if array[j] > array[j + 1]:
        utils.swap(array, j, j + 1)
  return array
