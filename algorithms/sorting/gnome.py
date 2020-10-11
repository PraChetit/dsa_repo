"""Implementation of gnome sort, also referred to as stupid sort."""

from algorithms.sorting import utils


def gnome_sort(array):
  utils.check_array(array)
  idx = 0
  length = len(array)
  while idx < length:
    if idx == 0 or array[idx] >= array[idx - 1]:
      idx += 1
    else:
      utils.swap(array, idx, idx - 1)
      idx -= 1
  return array
