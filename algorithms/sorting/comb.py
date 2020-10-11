"""Implementation of comb sort."""

import math

from algorithms.sorting import utils


def comb_sort(array, shrink_factor=1.3):
  """Optimized implementation of bubble sort."""
  utils.check_array(array)
  length = len(array)
  gap = length
  already_done = False

  while not already_done:
    gap = math.floor(gap // shrink_factor)
    if gap <= 1:
      gap = 1
      already_done = True

    for i in range(length - gap):
      if array[i] > array[i + 1]:
        utils.swap(array, i, i + 1)
        already_done = False

  return array
