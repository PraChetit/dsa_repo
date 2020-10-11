from absl.testing import absltest
import dataclasses

from data_structures import priority_queue


class PQElementTest(absltest.TestCase):

  def test_container(self):
    e = priority_queue._PQElement(123, 0, 'test_string')
    self.assertEqual(123, e.priority)
    self.assertEqual(0, e.idx)
    self.assertEqual('test_string', e.item)
    # Assert these are all elements.
    self.assertLen(dataclasses.fields(priority_queue._PQElement), 3)

  def test_compare(self):
    e = priority_queue._PQElement(5, 1, 'a')
    self.assertEqual(priority_queue._PQElement(5, 1, 'a'), e)
    self.assertEqual(priority_queue._PQElement(5, 1, None), e)
    self.assertGreater(priority_queue._PQElement(6, 0, 'a'), e)
    self.assertGreater(priority_queue._PQElement(6, 1, 'a'), e)
    self.assertGreater(priority_queue._PQElement(5, 2, 'a'), e)
    self.assertGreater(priority_queue._PQElement(6, 2, 'a'), e)
    self.assertLess(priority_queue._PQElement(5, 0, 'a'), e)
    self.assertLess(priority_queue._PQElement(4, 0, 'a'), e)
    self.assertLess(priority_queue._PQElement(4, 1, 'a'), e)
    self.assertLess(priority_queue._PQElement(4, 2, 'a'), e)


class PriorityQueueTest(absltest.TestCase):
  """Tests for `PriorityQueue`."""

  def test_empty_at_init(self):
    q = priority_queue.PriorityQueue()
    self.assertEqual(0, q.size())

  def test_item_in_front(self):
    q = priority_queue.PriorityQueue()
    q.add('a', 1)
    self.assertEqual('a', q.peek())

  def test_item_in_front_after_pop(self):
    q = priority_queue.PriorityQueue()
    q.add('a', 1)
    q.add('b', 2)
    q.remove()
    self.assertEqual('a', q.peek())

  def test_item_with_highest_priority_popped(self):
    values = 'abcdefghij'

    # Push in increasing order.
    q = priority_queue.PriorityQueue()
    for i in range(10):
      q.add(values[i], i)
    for i in reversed(range(10)):
      self.assertEqual(values[i], q.remove())

    # Push in decreasing order.
    q = priority_queue.PriorityQueue()
    for i in reversed(range(10)):
      q.add(values[i], i)
    for i in reversed(range(10)):
      self.assertEqual(values[i], q.remove())

  def test_equal_priority_elements_in_queue_order(self):
    q = priority_queue.PriorityQueue()
    q.add('a', 1)
    q.add('b', 1)
    q.add('c', 1)
    self.assertEqual('a', q.peek())
    self.assertEqual('a', q.remove())
    self.assertEqual('b', q.peek())
    self.assertEqual('b', q.remove())
    self.assertEqual('c', q.peek())
    self.assertEqual('c', q.remove())

  def test_example_behavior(self):
    q = priority_queue.PriorityQueue()
    q.add('a', 1)
    self.assertEqual('a', q.peek())
    q.add('b', 2)
    self.assertEqual('b', q.peek())
    self.assertEqual('b', q.remove())
    self.assertEqual('a', q.peek())
    q.add('d', 3)
    self.assertEqual('d', q.peek())
    q.add('c', 3)
    self.assertEqual('d', q.peek())
    self.assertEqual('d', q.remove())
    self.assertEqual('c', q.peek())
    self.assertEqual('c', q.remove())
    self.assertEqual('a', q.peek())
    self.assertEqual('a', q.remove())
    self.assertEqual(0, q.size())

  def test_size_reflects_changes(self):
    q = priority_queue.PriorityQueue()
    for i in range(1, 10):
      q.add(None, i)
      self.assertEqual(i, q.size())
    for i in reversed(range(1, 10)):
      q.remove()
      self.assertEqual(i - 1, q.size())

  def test_queue_takes_anything(self):
    q = priority_queue.PriorityQueue()
    q.add(1, 0)
    q.add(3.14, 0)
    q.add('str', 0)
    q.add(None, 0)
    q.add(priority_queue.PriorityQueue(), 0)
    q.add(object, 0)
    self.assertEqual(6, q.size())

  def test_empty_queue_raises(self):
    q = priority_queue.PriorityQueue()
    with self.assertRaises(priority_queue.PriorityQueueEmptyError):
      q.remove()
    with self.assertRaises(priority_queue.PriorityQueueEmptyError):
      q.peek()


if __name__ == '__main__':
  absltest.main()