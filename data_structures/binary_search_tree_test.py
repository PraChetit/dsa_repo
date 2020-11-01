import itertools

from absl.testing import absltest
from absl.testing import parameterized

from data_structures import binary_search_tree


def test_tree():
  """Returns a tree for testing.

  The tree looks like this:
                             12
                             /\
                            /  \
                           /    \
                          /      \
                         /        \
                        /          \
                       /            \
                      /              \
                     /                \
                    /                  \
                   /                    \
                  5                      18
                 /\                      /\
                /  \                    /  \
               /    \                  /    \
              /      \                /      \
             /        \              /        \
            2          9           15          19
                                    \
                                     \
                                      17
  """
  tree = binary_search_tree.BinarySearchTree()
  for value in [12, 5, 2, 9, 18, 15, 19, 17]:
    tree.add(value)
  return tree


class TestUtilTest(parameterized.TestCase):

  def test_test_tree_as_expected(self):
    tree = test_tree()
    self.assertEqual(12, tree._root.value)
    self.assertEqual(5, tree._root.left.value)
    self.assertEqual(18, tree._root.right.value)
    self.assertEqual(2, tree._root.left.left.value)
    self.assertEqual(9, tree._root.left.right.value)
    self.assertEqual(18, tree._root.right.value)
    self.assertEqual(15, tree._root.right.left.value)
    self.assertEqual(19, tree._root.right.right.value)
    self.assertEqual(17, tree._root.right.left.right.value)
    self.assertEqual(8, tree.size())


class BinarySearchTreeTest(parameterized.TestCase):

  def test_empty_tree(self):
    tree = binary_search_tree.BinarySearchTree()
    self.assertEqual(0, tree.size())

  def test_from_array_empty(self):
    tree = binary_search_tree.BinarySearchTree.from_array([])
    self.assertEqual(0, tree.size())

  def test_in_order_walk(self):
    tree = test_tree()
    self.assertEqual([2, 5, 9, 12, 15, 17, 18, 19], tree.in_order_walk())

  @parameterized.named_parameters(
    (f'case_{i}', list(perm)) for i, perm in
    enumerate(itertools.permutations(range(4))))
  def test_creation_yields_ordered_representation(self, array):
    # Creation using `from_array` classmethod.
    tree = binary_search_tree.BinarySearchTree.from_array(array,
                                                          random_order=False)
    self.assertListEqual([0, 1, 2, 3], tree.in_order_walk())

    # Creation using manual addition.
    tree = binary_search_tree.BinarySearchTree()
    for item in array:
      tree.add(item)
    self.assertListEqual([0, 1, 2, 3], tree.in_order_walk())

  def test_search(self):
    tree = test_tree()
    for value in [2, 5, 9, 12, 15, 17, 18, 19]:
      self.assertEqual(value, tree.search(value))
    with self.assertRaises(binary_search_tree.NotInTreeError):
      tree.search(0)

  @parameterized.named_parameters(
    ('remove_1', 1), ('remove_3', 3), ('remove_10', 10), ('remove_20', 20))
  def test_search_raises(self, item_not_in_test_tree):
    tree = test_tree()
    with self.assertRaises(binary_search_tree.NotInTreeError):
      tree.search(item_not_in_test_tree)

  @parameterized.named_parameters(
    ('remove_2', 2, [5, 9, 12, 15, 17, 18, 19]),
    ('remove_5', 5, [2, 9, 12, 15, 17, 18, 19]),
    ('remove_9', 9, [2, 5, 12, 15, 17, 18, 19]),
    ('remove_12', 12, [2, 5, 9, 15, 17, 18, 19]),
    ('remove_15', 15, [2, 5, 9, 12, 17, 18, 19]),
    ('remove_17', 17, [2, 5, 9, 12, 15, 18, 19]),
    ('remove_18', 18, [2, 5, 9, 12, 15, 17, 19]),
    ('remove_19', 19, [2, 5, 9, 12, 15, 17, 18]))
  def test_remove(self, item_to_remove, expected_list):
    tree = test_tree()
    self.assertEqual(8, tree.size())
    tree.remove(item_to_remove)
    self.assertEqual(7, tree.size())
    self.assertEqual(expected_list, tree.in_order_walk())

  @parameterized.named_parameters(
    ('remove_1', 1), ('remove_3', 3), ('remove_10', 10), ('remove_20', 20))
  def test_remove_raises(self, item_not_in_test_tree):
    tree = test_tree()
    with self.assertRaises(binary_search_tree.NotInTreeError):
      tree.remove(item_not_in_test_tree)

  def test_minimum(self):
    tree = test_tree()
    self.assertEqual(2, tree.minimum())

  def test_maximum(self):
    tree = test_tree()
    self.assertEqual(19, tree.maximum())

  def test_minimum_maximum_raise_with_empty_tree(self):
    tree = binary_search_tree.BinarySearchTree()
    with self.assertRaises(binary_search_tree.TreeEmptyError):
      tree.minimum()
    with self.assertRaises(binary_search_tree.TreeEmptyError):
      tree.maximum()

  def test_from_array_requires_list(self):
    with self.assertRaises(TypeError):
      binary_search_tree.BinarySearchTree.from_array(tuple(1, 2, 3))


if __name__ == '__main__':
  absltest.main()
