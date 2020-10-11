from absl.testing import absltest
from absl.testing import parameterized

from data_structures import queue

_QUEUES_TO_TEST = [
  ('linked_list_queue', queue.LinkedListQueue,),
  ('list_queue', queue.ListQueue,),
  ('stack_queue', queue.StackQueue,),
]


class BaseQueueTest(parameterized.TestCase):
  """Tests for implementations of `QueueInterface`."""

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_empty_at_init(self, queue_constructor):
    q = queue_constructor()
    self.assertEqual(0, q.size())

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_item_in_front(self, queue_constructor):
    q = queue_constructor()
    q.add(1)
    self.assertEqual(1, q.peek())

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_item_in_front_after_pop(self, queue_constructor):
    q = queue_constructor()
    q.add(1)
    q.add(2)
    q.remove()
    self.assertEqual(2, q.peek())

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_size_reflects_changes(self, queue_constructor):
    q = queue_constructor()
    for i in range(1, 10):
      q.add(i)
      self.assertEqual(i, q.size())
    for i in reversed(range(1, 10)):
      q.remove()
      self.assertEqual(i - 1, q.size())

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_example_behavior(self, queue_constructor):
    q = queue_constructor()
    q.add(1)
    self.assertEqual(1, q.peek())
    q.add(2)
    self.assertEqual(1, q.peek())
    self.assertEqual(1, q.remove())
    self.assertEqual(2, q.peek())
    q.add(3)
    self.assertEqual(2, q.peek())
    q.add(4)
    self.assertEqual(2, q.peek())
    self.assertEqual(2, q.remove())
    self.assertEqual(3, q.peek())
    self.assertEqual(3, q.remove())
    self.assertEqual(4, q.peek())
    self.assertEqual(4, q.remove())
    self.assertEqual(0, q.size())

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_queue_takes_anything(self, queue_constructor):
    q = queue_constructor()
    q.add(1)
    q.add(3.14)
    q.add('str')
    q.add(None)
    q.add(queue.LinkedListQueue())
    q.add(object)
    self.assertEqual(6, q.size())

  @parameterized.named_parameters(_QUEUES_TO_TEST)
  def test_empty_queue_raises(self, queue_constructor):
    q = queue_constructor()
    with self.assertRaises(queue.QueueEmptyError):
      q.remove()
    with self.assertRaises(queue.QueueEmptyError):
      q.peek()


if __name__ == '__main__':
  absltest.main()
