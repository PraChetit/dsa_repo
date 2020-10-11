from absl.testing import absltest

from data_structures import linked_list


class LLNodeTest(absltest.TestCase):

  def test_holds_value(self):
    node = linked_list.LLNode('str')
    self.assertEqual('str', node.value)

    node2 = linked_list.LLNode(3.14, next_node=node)
    self.assertEqual(3.14, node2.value)

  def test_points_to_node(self):
    node = linked_list.LLNode('str')
    node2 = linked_list.LLNode(3.14, next_node=node)
    self.assertEqual(node, node2.next_node)

  def test_value_updated(self):
    node = linked_list.LLNode('str')
    node.value = 3.14
    self.assertEqual(3.14, node.value)

  def test_next_node_updated(self):
    node = linked_list.LLNode('str')
    node2 = linked_list.LLNode(3.14)

    node.next_node = node2
    self.assertEqual(node2, node.next_node)
    node.next_node = None
    self.assertIsNone(node.next_node)

  def test_next_node_invalid_init_raises(self):
    with self.assertRaises(linked_list.NotLLNodeError):
      linked_list.LLNode('str', next_node=3.14)

  def test_next_node_invalid_update_raises(self):
    node = linked_list.LLNode('str')
    with self.assertRaises(linked_list.NotLLNodeError):
      node.next_node = 3.14


class DLLNodeTest(absltest.TestCase):

  def test_holds_value(self):
    node = linked_list.DLLNode('str')
    self.assertEqual('str', node.value)

    node2 = linked_list.DLLNode(3.14, next_node=node, previous_node=node)
    self.assertEqual(3.14, node2.value)

  def test_points_to_node(self):
    node = linked_list.DLLNode('str')

    node2 = linked_list.DLLNode(3.14, next_node=node, previous_node=None)
    self.assertEqual(node, node2.next_node)

    node3 = linked_list.DLLNode(3.14, next_node=None, previous_node=node)
    self.assertEqual(node, node3.previous_node)

  def test_value_updated(self):
    node = linked_list.DLLNode('str')
    node.value = 3.14
    self.assertEqual(3.14, node.value)

  def test_node_updated(self):
    node = linked_list.DLLNode('str')
    node2 = linked_list.DLLNode(3.14)

    node.next_node = node2
    self.assertEqual(node2, node.next_node)
    node.next_node = None
    self.assertIsNone(node.next_node)

    node.previous_node = node2
    self.assertEqual(node2, node.previous_node)
    node.previous_node = None
    self.assertIsNone(node.previous_node)

  def test_node_invalid_init_raises(self):
    with self.assertRaises(linked_list.NotDLLNodeError):
      linked_list.DLLNode('str', next_node=3.14)
    with self.assertRaises(linked_list.NotDLLNodeError):
      linked_list.DLLNode('str', previous_node=3.14)

  def test_node_invalid_update_raises(self):
    node = linked_list.DLLNode('str')
    with self.assertRaises(linked_list.NotDLLNodeError):
      node.next_node = 3.14
    with self.assertRaises(linked_list.NotDLLNodeError):
      node.previous_node = 3.14


if __name__ == '__main__':
  absltest.main()