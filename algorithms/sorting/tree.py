"""Implementation of tree sort - using binary serach tree."""

from algorithms.sorting import utils
from data_structures import binary_search_tree


def tree_sort(array):
  utils.check_array(array)
  tree = binary_search_tree.BinarySearchTree.from_array(array)
  return tree.in_order_walk()
