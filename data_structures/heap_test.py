from absl.testing import absltest
from absl.testing import parameterized

import dataclasses

from data_structures import heap


class BinaryHeapTest(parameterized.TestCase):
  """Tests for `BinaryHeap`."""

  def test_empty_heap(self):
    h = heap.BinaryHeap()
    self.assertTrue(h.size() == 0)
    self.assertListEqual([], h.as_list())

  def test_empty_heapify(self):
    h = heap.BinaryHeap.heapify([])
    self.assertIsInstance(h, heap.BinaryHeap)
    self.assertListEqual([], h.as_list())

  @parameterized.named_parameters(
    [(str(i), i) for i in [1, 2, 3, 4, 5, 6, 7, 20, 100]])
  def test_heapify(self, num_elements):
    h = heap.BinaryHeap.heapify(list(range(num_elements)))
    self._assert_list_represents_heap(h.as_list())

  def test_single_item(self):
    h = heap.BinaryHeap()
    h.add(1)
    self.assertEqual(1, h.peek())
    self.assertEqual(1, h.remove())

  def test_largest_item_popped(self):
    # Add in increasing order.
    h = heap.BinaryHeap()
    for i in range(10):
      h.add(i)
    for i in reversed(range(10)):
      self.assertEqual(i, h.remove())

    # Add in decreasing order.
    h = heap.BinaryHeap()
    for i in reversed(range(10)):
      h.add(i)
    for i in reversed(range(10)):
      self.assertEqual(i, h.remove())

  def test_example_behavior(self):
    h = heap.BinaryHeap()
    h.add(1)
    self.assertEqual(1, h.peek())
    h.add(2)
    self.assertEqual(2, h.peek())
    self.assertEqual(2, h.remove())
    self.assertEqual(1, h.peek())
    h.add(4)
    self.assertEqual(4, h.peek())
    h.add(3)
    self.assertEqual(4, h.peek())
    self.assertEqual(4, h.remove())
    self.assertEqual(3, h.peek())
    self.assertEqual(3, h.remove())
    self.assertEqual(1, h.peek())
    self.assertEqual(1, h.remove())
    self.assertEqual(0, h.size())

  def test_size_reflects_changes(self):
    h = heap.BinaryHeap()
    for i in range(1, 10):
      h.add(i)
      self.assertEqual(i, h.size())
    for i in reversed(range(1, 10)):
      h.remove()
      self.assertEqual(i - 1, h.size())

  def test_as_list_contains_correct_elements(self):
    h = heap.BinaryHeap()
    for i in range(1, 10):
      h.add(i)
      self.assertSetEqual(set(range(1, i + 1)), set(h.as_list()))
    for i in reversed(range(1, 10)):
      h.remove()
      self.assertSetEqual(set(range(1, i)), set(h.as_list()))

  def test_accepts_comparable_type(self):
    # A class of which instances compare using __eq__ and __gt__ and similar.
    value_class = dataclasses.make_dataclass('Value', ['val'], order=True)

    data = [value_class(i) for i in range(10)]
    h = heap.BinaryHeap.heapify(data)
    self._assert_list_represents_heap(h.as_list())

  def test_empty_heap_raises(self):
    h = heap.BinaryHeap()
    with self.assertRaises(heap.HeapEmptyError):
      h.remove()
    with self.assertRaises(heap.HeapEmptyError):
      h.peek()

  def test_heapify_requires_list(self):
    with self.assertRaises(TypeError):
      heap.BinaryHeap.heapify(tuple(1, 2, 3))

  def _assert_list_represents_heap(self, lst):
    """Ensures that given list represents a heap."""
    for i in range(heap._parent(len(lst))):
      self.assertGreaterEqual(lst[i], lst[heap._left(i)])
      self.assertGreaterEqual(lst[i], lst[heap._right(i)])


if __name__ == '__main__':
  absltest.main()