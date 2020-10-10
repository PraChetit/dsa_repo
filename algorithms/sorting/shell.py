"""Implementation of shell sort."""

from algorithms.sorting import utils

_GAPS = [1532158938, 680959528, 302648679, 134510524, 59782455, 26569980,
         11808880, 5248391, 2332618, 1036719, 460764, 204784, 91015, 40451,
         17978, 7990, 3551, 1578, 701, 301, 132, 57, 23, 10, 4, 1]


def shell_sort(array):
  length = len(array)

  for gap in _GAPS:
    if gap >= length:
      continue

    for i in range(gap, length):
      j = i
      temp = array[j]
      while j >= gap and array[j - gap] > temp:
        array[j] = array[j - gap]
        j -= gap
      array[j] = temp

  return array
