"""Implementation of merge sort."""


def merge_sort(array):
  length = len(array)
  if length <= 1:
    return array  # Already sorted.

  left = merge_sort(array[:(length // 2)])
  right = merge_sort(array[(length // 2):])
  return _merge(left, right)


def _merge(left, right):
  array = []
  i, j = 0, 0
  left_len = len(left)
  right_len = len(right)

  while True:
    if left[i] < right[j]:
      array.append(left[i])
      i += 1
      if i == left_len:
        array.extend(right[j:])
        break
    else:
      array.append(right[j])
      j += 1
      if j == right_len:
        array.extend(left[i:])
        break

  return array
