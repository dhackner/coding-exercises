# Cracking the coding interview 6th Edition, p. 242
# Sorted increasing unique array, create minimal height BST


# Algorithm: Midpoint = root, create subtree on each side

from bst_node import Node


def list_to_tree(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return Node(arr[0])
    else:
        midpoint_index = len(arr) / 2
        return Node(arr[midpoint_index], list_to_tree(arr[:midpoint_index]), list_to_tree(arr[midpoint_index + 1:]))


print list_to_tree([1, 3, 4, 5, 6]).to_tree()
print list_to_tree([1, 3, 4, 5]).to_tree()
print list_to_tree([1, 3, 4, 5, 6, 7]).to_tree()
