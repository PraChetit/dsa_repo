"""Implementations of a heap.

NOTE: All implementations here deal with a max-heap.
"""


class HeapEmptyError(Exception):
  pass


class BinaryHeap(object):
  """Implementation of binary heap.

  A binary heap is a data structure which serves as a collection of elements
  which can be ordered and allows for a simple retrieval of the largest element
  while allowing addition and removal.

  Heap property.

  The data structure is represented as binary tree satisfying the *heap
  property*. A binary tree satisfies the heap property if:

  * It is filled on all levels except possibly the lowest, which is filled from
    the left up to a point.
  * Every node in the tree represents a value bigger than values represented
    by its children.

  Note that this does not imply that a heap is an ordered structure. It can be
  considered to be partially ordered, though. It does imply that the largest
  element is always at the root of the tree.

  For efficient access, the implementation relies on the list representation of
  binary tree. That is `k`-th level of the binary tree is in order stored at
  slice of the list indexed by `[2**(k-1) - 1, 2**k - 2]`.

  Heap operations.

  The heap property can be efficiently maintained when adding and removing an
  element:

  * Addition is realized by appending the new element to the list representing
    the tree, and repeatedly swapping it with its parent if it is larger than
    the parent.
  * Removal is realized by swapping the last element in the list with the first
    element, which is subsequently removed. The new root element is repeatedly
    swapped with its larger child, if one of the children is larger than this
    element.

  If there are `n` elements in the heap, both of these operations take
  `O(log(n))` time, as there are (approximately) `log(n)` levels in the tree.

  Heap creation.

  There are two possibilities for creation of the heap from a sequence of
  elements. The simplest is to add the elements to the heap one-by-one.

  However, there is a more efficient method, implemented as `heapify`
  classmethod. The idea is to treat the sequence as a representation of the
  binary tree not satisfying the heap property, and "fix" it. Iterating from the
  end, starting from the last non-leaf node, "fix" the subtree defined by the
  node as its root, using the same mechanism used for maintaining the heap
  property after removing an element.

  When creating a heap of `n` elements, the time complexity of the `heapify`
  method is `O(n)`, while one-by-one addition is `O(n * log(n))`.
  """

  def __init__(self):
    self._heap = []
    self._size = 0

  @classmethod
  def heapify(cls, data):
    """Efficiently constructs `BinaryHeap` containing given data.

    Args:
      data: A list of elements to be stored in the `BinaryHeap`.

    Returns:
      A `BinaryHeap`.

    Raises:
      `TypeError` if `data` is not a list.
    """
    if not isinstance(data, list):
      raise TypeError(f'Provided data must be a list, but is {type(data)}.')

    heap = cls()
    size = len(data)
    heap._heap = data
    heap._size = size
    for i in reversed(range(_parent(size) + 1)):
      heap._swap_all_down(i)
    return heap

  def add(self, item):
    """Adds `item` to the heap.

    Args:
      item: An object to be added.
    """
    self._heap.append(item)
    self._swap_all_up(self._size)
    self._size += 1

  def peek(self):
    """Returns the largest element in the heap.

    Raises:
      `HeapEmptyError` if the heap is empty.
    """
    if self._size == 0:
      raise HeapEmptyError()

    return self._heap[0]

  def remove(self):
    """Removes the largest element in the heap and returns it.

    Raises:
      `HeapEmptyError` if the heap is empty.
    """
    if self._size == 0:
      raise HeapEmptyError()

    val = self.peek()
    self._size -= 1
    self._heap[0] = self._heap[self._size]
    del self._heap[self._size]
    self._swap_all_down(0)
    return val

  # TODO: Add `replace` method more efficient than `remove` - `add` combination.

  def size(self):
    """Returns the number of elements in the heap."""
    return self._size

  def as_list(self):
    """Returns the list representation of the heap."""
    # Returns a *new* list to avoid having the user accidentally mutate the
    # internal representation of the heap.
    return [element for element in self._heap]

  def _swap_all_up(self, idx):
    """Corrects the heap property in parent path of node at location `idx`."""
    while True:
      if idx == 0:
        break
      new_idx = self._swap_up(idx)
      if new_idx == idx:
        break
      idx = new_idx

  def _swap_up(self, idx):
    """Corrects the heap property of node at location `idx` and its parent.

    If the node at location `idx` is larger than its parent, it is swapped with
    the parent.

    Returns:
      New index of the node previously at location `idx`.
    """
    parent = _parent(idx)
    if self._heap[parent] < self._heap[idx]:
      self._swap(parent, idx)
      return parent
    else:
      return idx

  def _swap_all_down(self, idx):
    """Corrects the heap property of subtree under node at location `idx`."""
    while True:
      if self._is_leaf(idx):
        break
      new_idx = self._swap_down(idx)
      if new_idx == idx:
        break
      idx = new_idx

  def _swap_down(self, idx):
    """Corrects the heap property of node at location `idx` and its children.

    If the node at location `idx` is not larger than both of its children, it is
    swapped with the larger of its children. Otherwise, nothing is changed.

    Returns:
      New index of the node previously at location `idx`.
    """
    left, right = _left(idx), _right(idx)
    if self._size > right and self._heap[left] < self._heap[right]:
      if self._heap[idx] < self._heap[right]:
        self._swap(idx, right)
        return right
    else:
      if self._heap[idx] < self._heap[left]:
        self._swap(idx, left)
        return left
    return idx

  def _swap(self, idx1, idx2):
    """Swaps nodes at locations `idx1` and `idx2`."""
    tmp = self._heap[idx1]
    self._heap[idx1] = self._heap[idx2]
    self._heap[idx2] = tmp

  def _is_leaf(self, idx):
    """Returns `True` if node at location `idx` does not have children."""
    if _left(idx) >= self._size:
      return True
    else:
      return False


# Utilities for accessing parent / child nodes in list representation of a
# binary tree.
def _parent(idx):
  return (idx - 1) // 2


def _left(idx):
  return 2 * idx + 1


def _right(idx):
  return 2 * idx + 2