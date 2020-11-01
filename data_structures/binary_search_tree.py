"""Implementation of a binary search tree."""

import random


class TreeEmptyError(Exception):
  pass


class NotInTreeError(Exception):
  pass


class _BinarySearchTreeNode(object):
  """Representation of a node in a `BinarySearchTree`."""

  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

  def minimum(self):
    if self.left is None:
      return self
    else:
      return self.left.minimum()

  def maximum(self):
    if self.right is None:
      return self
    else:
      return self.right.maximum()

  def in_order_walk(self, array):
    if self.left is not None:
      self.left.in_order_walk(array)
    array.append(self.value)
    if self.right is not None:
      self.right.in_order_walk(array)


class BinarySearchTree(object):
  """Implementation of a binary search tree.

  A binary search tree is data structure which serves as an ordered collection
  of elements, allows for addition, removal, and searching for elements, as well
  as iteration through its elements in order.

  Binary search tree property.

  The data structure is represented as binary tree satisfying the *binary search
  tree property*. A binary tree satisfies the heap property if for each node N,
  the following holds: N is greater or equal to each node in the left subtree of
  N, and N is smaller or equal to each node in the right subtree of N.

  Binary search tree operations.

  Searching for an element corresponds to walking down the tree, using the
  binary search tree property and comparison to determine whether to search in
  the left or the right subtree. Complexity of searching thus corresponds to the
  height of the tree.

  The binary search tree property can be efficiently maintained when adding and
  removing elements:

  * Addition is realized by walking down the tree and finding the leaf where the
    element to be added can be correctly placed.
  * Removal is realized by first searching for the element to be removed. The
    removal is then realized differently based on several conditions depending
    on the elements around the element to be removed.

  Binary search tree can be created form an array of elements it should contain.
  If the tree is created by adding the elements to the tree in random order, the
  expected complexity is `O(n * log(n))` and its height `O(log(n))`, but in the
  worst case, these can be `O(n^2)` and `O(n)`, respectively.
  """

  def __init__(self):
    self._root = None
    self._size = 0

  @classmethod
  def from_array(cls, array, random_order=True):
    """Constructs `BinarySearchTree` containing given data.

    Args:
      array: A list of elements to be stored in the `BinarySearchTree`.
      random_order: A boolean. Whether the order of elements added from `array`
        is random or as ordered in `array`.

    Returns:
      A `BinarySearchTree`.

    Raises:
      `TypeError` if `array` is not a list.
    """
    if not isinstance(array, list):
      raise TypeError(f'Provided data must be a list, but is {type(array)}.')

    tree = BinarySearchTree()
    if random_order:
      order = list(range(len(array)))
      random.shuffle(order)
      for i in order:
        tree.add(array[i])
    else:
      for value in array:
        tree.add(value)
    return tree

  def add(self, item):
    """Adds `item` to the tree.

    Args:
      item: An object to be added.
    """
    new_parent = None
    node = self._root

    # Walk down the tree until hitting None instead of a _BinaryTreeNode.
    # The last node visited is the new parent node.
    while node is not None:
      new_parent = node
      if item < new_parent.value:
        node = node.left
      else:
        node = node.right

    # Create a new node and place it as child of the found new parent.
    new_node = _BinarySearchTreeNode(item, parent=new_parent)
    if new_parent is None:  # The tree was empty.
      self._root = new_node
    elif item < new_parent.value:
      new_parent.left = new_node
    else:
      new_parent.right = new_node
    self._size += 1

  def remove(self, item):
    """Removes the item and returns it.

    Args:
      item: An item to be removed.

    Returns:
      The removed item.

    Raises:
      NotInTreeError: If `item` is not in the tree.
    """
    node = self._search(item)

    # The found `node` is to be deleted.
    if node.left is None:
      self._reconnect_to_parent(node.parent, node, node.right)
    elif node.right is None:
      self._reconnect_to_parent(node.parent, node, node.left)
    else:  # The found `node` has both children.
      successor = node.right.minimum()
      # NOTE: `successor.left is None`, otherwise the successor would be in its
      # left subtree.
      if successor == node.right:
        # If the successor is the right child is the easy case.
        node.right.left = node.left
        node.left.parent = node.right
        self._reconnect_to_parent(node.parent, node, node.right)
      else:
        successor.left = node.left
        node.left.parent = successor
        successor.parent.left = successor.right
        if successor.right is not None:
          successor.right.parent = successor.parent
        successor.right = node.right
        node.right.parent = successor
        self._reconnect_to_parent(node.parent, node, successor)

    self._size -= 1
    return node.value

  def search(self, item):
    """Searches for an the item and returns it.

    Args:
      item: An item to be found.

    Returns:
      The found item.

    Raises:
      NotInTreeError: If `item` is not in the tree.
    """
    return self._search(item).value

  def minimum(self):
    """Returns the smallest item in the tree."""
    if self._root is None:
      raise TreeEmptyError()
    return self._root.minimum().value

  def maximum(self):
    """Returns the largest item in the tree."""
    if self._root is None:
      raise TreeEmptyError()
    return self._root.maximum().value

  def size(self):
    """Returns the number of elements in the tree."""
    return self._size

  def in_order_walk(self):
    """Returns ordered items in the tree.

    Returns:
      A list of items in the tree in increasing order.
    """
    array = []
    if self._root is None:
      return array
    self._root.in_order_walk(array)  # Modified in-place.
    return array

  def _search(self, item):
    """Implements `search` method returning wrapping `_BinarySearchTreeNode`."""
    node = self._root
    while node is not None and item != node.value:
      if item < node.value:
        node = node.left
      else:
        node = node.right

    if node is None:
      raise NotInTreeError()
    return node

  def _reconnect_to_parent(self, parent, old_child, new_child):
    """Replaces `old_child` with `new_child` as a child of `parent`.

    This utility takes a parent node, together with a node which is one of its
    children, and another node which should replace the current child as the
    same (left or right) child of the parent.

    Args:
       parent: A `_BinarySearchTreeNode`.
       old_child: A `_BinarySearchTreeNode`.
       new_child: A `_BinarySearchTreeNode`.
    """
    if parent is None:
      self._root = new_child
      if new_child is not None:
        new_child.parent = None
    else:
      if parent.left == old_child:
        parent.left = new_child
      else:
        assert parent.right == old_child
        parent.right = new_child
      if new_child is not None:
        new_child.parent = parent
