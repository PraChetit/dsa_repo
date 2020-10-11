"""Minor utilities for sorting algorithms."""


def swap(array, i, j):
  temp = array[i]
  array[i] = array[j]
  array[j] = temp


def check_array(array):
  if not isinstance(array, list):
    raise NotArrayError(
      f'The array to be sorted must a list, but found: {type(array)}.')


class NotArrayError(Exception):
  pass
