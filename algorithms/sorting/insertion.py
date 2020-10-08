"""Implementation of insertion sort."""

from algorithms.sorting import utils


def insertion_sort(array):
  for i in range(len(array)):
    for j in reversed(range(1, i + 1)):
      if array[j] >= array[j - 1]:
        break  # Sub-array already sorted.
      utils.swap(array, j, j - 1)
  return array
