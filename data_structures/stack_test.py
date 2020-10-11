from absl.testing import absltest
from absl.testing import parameterized

from data_structures import stack

_STACKS_TO_TEST = [
  ('linked_list_stack', stack.LinkedListStack,),
  ('list_stack', stack.ListStack,),
]


class BaseStackTest(parameterized.TestCase):
  """Tests for implementations of `StackInterface`."""

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_empty_at_init(self, stack_constructor):
    s = stack_constructor()
    self.assertEqual(0, s.size())

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_item_at_top(self, stack_constructor):
    s = stack_constructor()
    s.add(1)
    self.assertEqual(1, s.peek())

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_item_at_top_after_pop(self, stack_constructor):
    s = stack_constructor()
    s.add(1)
    s.add(2)
    s.remove()
    self.assertEqual(1, s.peek())

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_size_reflects_changes(self, stack_constructor):
    s = stack_constructor()
    for i in range(1, 10):
      s.add(i)
      self.assertEqual(i, s.size())
    for i in reversed(range(1, 10)):
      s.remove()
      self.assertEqual(i - 1, s.size())

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_example_behavior(self, stack_constructor):
    s = stack_constructor()
    s.add(1)
    self.assertEqual(1, s.peek())
    s.add(2)
    self.assertEqual(2, s.peek())
    self.assertEqual(2, s.remove())
    self.assertEqual(1, s.peek())
    s.add(3)
    self.assertEqual(3, s.peek())
    s.add(4)
    self.assertEqual(4, s.peek())
    self.assertEqual(4, s.remove())
    self.assertEqual(3, s.peek())
    self.assertEqual(3, s.remove())
    self.assertEqual(1, s.peek())
    self.assertEqual(1, s.remove())
    self.assertEqual(0, s.size())

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_stack_takes_anything(self, stack_constructor):
    s = stack_constructor()
    s.add(1)
    s.add(3.14)
    s.add('str')
    s.add(None)
    s.add(stack.ListStack())
    s.add(object)
    self.assertEqual(6, s.size())

  @parameterized.named_parameters(_STACKS_TO_TEST)
  def test_empty_stack_raises(self, stack_constructor):
    s = stack_constructor()
    with self.assertRaises(stack.StackEmptyError):
      s.remove()
    with self.assertRaises(stack.StackEmptyError):
      s.peek()


if __name__ == '__main__':
  absltest.main()
