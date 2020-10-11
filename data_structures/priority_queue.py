"""Implementation of a priority queue."""

from typing import Any
import dataclasses

from data_structures import heap


class PriorityQueueEmptyError(Exception):
  pass


@dataclasses.dataclass(order=True)
class _PQElement(object):
  priority: int
  idx: int
  item: Any = dataclasses.field(compare=False)


class PriorityQueue(object):
  """Implementation of priority queue.

  Priority queue is a data structure which serves as a collection of elements
  with their relative priorities, and supports two primary operations: addition
  and removal.

  The property defining a priority queue is that removal always removes the
  element which has the highest priority among the elements in the queue. If
  multiple elements have the same highest priority, the element which has been
  in the collection for the longest time is removed.

  The implementation is realized using a heap, which is filled with elements of
  particular structure imposing the desired ordering.
  """

  def __init__(self):
    self._heap = heap.BinaryHeap()
    self._counter = 0

  def add(self, item, priority):
    """Adds `item` to the queue.

    Args:
      item: An object to be added.
      priority: The priority of `item`.
    """
    # Addition of a unique decreasing counter ensures expected ordering of
    # elements with equal priority.
    element = _PQElement(priority, self._counter, item)
    self._counter -= 1
    self._heap.add(element)

  def peek(self):
    """Returns the element from queue with the highest priority.

    Returns:
      The element from queue with the highest priority. If multiple elements
      have the same highest priority, the element which has been in the queue
      for the longest time is removed.

    Raises:
      `PriorityQueueEmptyError` if the queue is empty.
    """
    if self._heap.size() == 0:
      raise PriorityQueueEmptyError()
    return self._heap.peek().item

  def remove(self):
    """Removes the element from queue with the highest priority and returns it.

    Returns:
      The element from queue with the highest priority. If multiple elements
      have the same highest priority, the element which has been in the queue
      for the longest time is removed.

    Raises:
      `PriorityQueueEmptyError` if the queue is empty.
    """
    if self._heap.size() == 0:
      raise PriorityQueueEmptyError()
    return self._heap.remove().item

  def size(self):
    """Returns the number of elements in the queue."""
    return self._heap.size()