"""Abstractions related to linked lists."""


class LLNode(object):
  """Node in a linked list.

  A linked list is a collection of nodes, each containing a value and a pointer
  to the next node in the linked list.
  """

  def __init__(self, value, next_node=None):
    """Creates the `LLNode` object.

    Args:
      value: A value to be held by this node.
      next_node: An optional node this node points to. If specified, must be an
        `LLNode`.

    Raises:
      `NotLLNodeError` if `next_node` is not `None` or an `LLNode`.
    """
    self._value = value
    _validate_llnode(next_node)
    self._next_node = next_node

  @property
  def value(self):
    """Returns the value stored by this node.

    This property can be updated by direct assignment.
    """
    return self._value

  @value.setter
  def value(self, new_value):
    self._value = new_value

  @property
  def next_node(self):
    """Returns the next node in the linked list.

    This property can be updated by direct assignment.

    Returns:
      Either `None` if this node does not point to another node, or an `LLNode`
      object.
    """
    return self._next_node

  @next_node.setter
  def next_node(self, new_next_node):
    _validate_llnode(new_next_node)
    self._next_node = new_next_node


class NotLLNodeError(Exception):
  pass


def _validate_llnode(node):
  if node is not None and not isinstance(node, LLNode):
    raise NotLLNodeError()


class DLLNode(object):
  """Node in a doubly linked list.

  A doubly linked list is a collection of nodes, each containing a value and
  pointers to the next node in the list as well as to the previous node in the
  list.
  """

  def __init__(self, value, next_node=None, previous_node=None):
    """Creates the `DLLNode` object.

    Args:
      value: A value to be held by this node.
      next_node: An optional node this node points to. If specified, must be a
        `DLLNode`.

    Raises:
      `ValueError` if `next_node` is not `None` or an `DLLNode`.
    """
    self._value = value
    _validate_dllnode(next_node)
    self._next_node = next_node
    _validate_dllnode(previous_node)
    self._previous_node = previous_node

  @property
  def value(self):
    """Returns the value stored by this node.

    This property can be updated by direct assignment.
    """
    return self._value

  @value.setter
  def value(self, new_value):
    self._value = new_value

  @property
  def next_node(self):
    """Returns the next node in the doubly linked list.

    This property can be updated by direct assignment.

    Returns:
      Either `None` if this node does not point to another node, or a `DLLNode`
      object.
    """
    return self._next_node

  @next_node.setter
  def next_node(self, new_next_node):
    _validate_dllnode(new_next_node)
    self._next_node = new_next_node

  @property
  def previous_node(self):
    """Returns the previous node in the doubly linked list.

    This property can be updated by direct assignment.

    Returns:
      Either `None` if this node does not point to another node, or a `DLLNode`
      object.
    """
    return self._previous_node

  @previous_node.setter
  def previous_node(self, new_previous_node):
    _validate_dllnode(new_previous_node)
    self._previous_node = new_previous_node


class NotDLLNodeError(Exception):
  pass


def _validate_dllnode(node):
  if node is not None and not isinstance(node, DLLNode):
    raise NotDLLNodeError()
