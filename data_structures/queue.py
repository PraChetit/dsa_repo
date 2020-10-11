"""Implementations of a queue."""

import abc

from data_structures import linked_list
from data_structures import stack


class QueueEmptyError(Exception):
  pass


class QueueInterface(abc.ABC):
  """Interface of a queue.

  Queue is a data structure which serves as a collection of elements with two
  primary operations: addition and removal. The property defining a queue is
  that removal always removes the element which has been in the collection for
  the longest time.
  """

  @abc.abstractmethod
  def add(self, item):
    """Adds `item` to the back of the queue.

    Args:
      item: An object to be added.
    """

  @abc.abstractmethod
  def peek(self):
    """Returns the element at the front of the queue.

    Returns:
      The element which has been in the queue for the longest time.

    Raises:
      `QueueEmptyError` if the queue is empty.
    """

  @abc.abstractmethod
  def remove(self):
    """Removes the element at the front of the queue and returns it.

    Returns:
      The element which has been in the queue for the longest time.

    Raises:
      `QueueEmptyError` if the queue is empty.
    """

  @abc.abstractmethod
  def size(self):
    """Returns the number of elements in the queue."""


class LinkedListQueue(QueueInterface):
  """Implementation of a queue using linked list.

  This implementation retains pointers to the front and back of the queue, both
  of which are nodes in a linked list. Each node of the linked list points
  to the element added right after it. Adding an element to the queue creates a
  new node which becomes the new back of the queue, having previous back of the
  queue point to it. Removing an element out of the queue replaces the front of
  the queue with the node the front node points to.
  """

  def __init__(self):
    self._front = None
    self._back = None
    self._size = 0

  def add(self, item):
    new_node = linked_list.LLNode(item, next_node=None)
    if self.size() == 0:
      self._front = new_node
    else:
      self._back.next_node = new_node
    self._back = new_node
    self._size += 1

  def peek(self):
    if self.size() == 0:
      raise QueueEmptyError()
    return self._front.value

  def remove(self):
    if self.size() == 0:
      raise QueueEmptyError()

    front_of_queue = self._front.value
    self._front = self._front.next_node
    self._size -= 1
    return front_of_queue

  def size(self):
    return self._size


class ListQueue(QueueInterface):
  """Implementation of a queue using Python list.

  The queue is represented simply as a list. Adding an element to the queue
  appends the new element to the list. Removing an element from the queue
  deletes the first element of the list. Note that this operation will be slow
  for large queues, because it involves memory movements.
  """

  def __init__(self):
    self._queue = []
    self._size = 0

  def add(self, item):
    self._size += 1
    self._queue.append(item)

  def peek(self):
    if self.size() == 0:
      raise QueueEmptyError()
    return self._queue[0]

  def remove(self):
    if self.size() == 0:
      raise QueueEmptyError()

    front_of_queue = self._queue[0]
    del self._queue[0]
    self._size -= 1
    return front_of_queue

  def size(self):
    return self._size


class StackQueue(QueueInterface):
  """Implementation of a queue using two stacks.

  A fun example of how simple data structures can be used to build other data
  structures.

  The idea is that we can keep two stacks, one for adding, one for removing.
  Adding is always done onto the adding stack. When queue's `add` or `peek`
  method is invoked, we look at the removing stack. If it is not empty, simply
  use it directly. If it is empty, move elements from the adding stack one by
  one onto the removing stack. Consequently, the order of elements is reversed,
  resulting in the expected behavior of queue.

  Note that implementation of the `StackQueue` is really in terms of the
  `stack.StackInterface`, and thus the actual stacks used can be easily
  replaced by different implementations of the interface.
  """

  def __init__(self):
    self._add_stack = stack.LinkedListStack()
    self._remove_stack = stack.LinkedListStack()
    self._size = 0

  def _flip_stacks(self):
    while True:
      try:
        self._remove_stack.add(self._add_stack.remove())
      except stack.StackEmptyError:
        break

  def add(self, item):
    self._size += 1
    self._add_stack.add(item)

  def peek(self):
    if self.size() == 0:
      raise QueueEmptyError()

    if self._remove_stack.size() == 0:
      self._flip_stacks()
    return self._remove_stack.peek()

  def remove(self):
    if self.size() == 0:
      raise QueueEmptyError()

    if self._remove_stack.size() == 0:
      self._flip_stacks()
    front_of_queue = self._remove_stack.remove()
    self._size -= 1
    return front_of_queue

  def size(self):
    return self._size
