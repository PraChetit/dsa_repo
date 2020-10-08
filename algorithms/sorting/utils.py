"""Minor utilities for sorting algorithms."""


def swap(array, i, j):
  temp = array[i]
  array[i] = array[j]
  array[j] = temp
