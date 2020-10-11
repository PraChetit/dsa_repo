"""Implementations of a stack."""

import abc

from data_structures import linked_list


class StackEmptyError(Exception):
  pass


class StackInterface(abc.ABC):
  """Interface of a stack.

  Stack is a data structure which serves as a collection of elements with two
  primary operations: addition and removal. The property defining a stack is
  that removal always removes the most recently added element that was not yet
  removed.
  """

  @abc.abstractmethod
  def add(self, item):
    """Adds `item` to the the stack.

    Args:
      item: An object to be added.
    """

  @abc.abstractmethod
  def peek(self):
    """Returns the element at the top of the stack.

    Returns:
      The most recently added element currently in the stack.

    Raises:
      `StackEmptyError` if the stack is empty.
    """

  @abc.abstractmethod
  def remove(self):
    """Removes the element at the top of the stack and returns it.

    Returns:
      The most recently added element currently in the stack.

    Raises:
      `StackEmptyError` if the stack is empty.
    """

  @abc.abstractmethod
  def size(self):
    """Returns the number of elements in the stack."""


class LinkedListStack(StackInterface):
  """Implementation of stack using linked list.

  This implementation retains a pointer to the top of the stack, which is a
  node in a linked list, pointing to the element added to the stack previously.
  Pushing onto the stack creates a new node in the linked list and points it
  to the previous top of the stack. Popping an element out of the stack
  replaces the top of the stack with the node it points to.
  """

  def __init__(self):
    self._top = None
    self._size = 0

  def add(self, item):
    self._size += 1
    self._top = linked_list.LLNode(item, self._top)

  def peek(self):
    if self.size() == 0:
      raise StackEmptyError()
    return self._top.value

  def remove(self):
    if self.size() == 0:
      raise StackEmptyError()

    top_item = self._top.value
    self._top = self._top.next_node
    self._size -= 1
    return top_item

  def size(self):
    return self._size


class ListStack(StackInterface):
  """Implementation of stack using Python list.

  The end of the list corresponds to the top of the stack. This is relatively
  fast as manipulation with end of a list is fast in Python.
  """

  def __init__(self):
    self._stack = []
    self._size = 0

  def add(self, item):
    self._size += 1
    self._stack.append(item)

  def peek(self):
    if self.size() == 0:
      raise StackEmptyError()
    return self._stack[self._size - 1]

  def remove(self):
    if self.size() == 0:
      raise StackEmptyError()

    top_item = self._stack[self._size - 1]
    del self._stack[self._size - 1]
    self._size -= 1
    return top_item

  def size(self):
    return self._size
