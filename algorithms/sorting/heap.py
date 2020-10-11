"""Implementation of heap sort."""

from algorithms.sorting import utils
from data_structures import heap


def heap_sort(array):
  utils.check_array(array)
  length = len(array)
  h = heap.BinaryHeap.heapify(array)
  sorted_array = [None for _ in range(length)]
  for i in reversed(range(length)):
    sorted_array[i] = h.remove()
  return sorted_array
