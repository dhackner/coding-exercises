# Path between two nodes in a binary tree (in-order)

# Assumption: Both nodes exist and are not the same node. Can reorder so val1 < val2

"""
  a
b   c

1) In order: b->a | a->c
2) Split: b->a->c
3) Both in subtree: recurse on b | recurse on c
"""


from bst_node import Node


def search_prep(root, val1, val2):
    if val1 == val2:
        raise Exception('Distinct values only')
    elif val1 > val2:
        search(root, val2, val1)
    else:
        search(root, val1, val2)


def search(root, val1, val2):
    if root is None or val1 is None and val2 is None:
        return
    if root.value in (val1, val2):
        # Case 1
        if root.value == val1:
            print root.value
            search(root.r, None, val2)
        elif root.value == val2:
            search(root.l, val1, None)
            print root.value
    elif val1 < root.value < val2:
        # Case 2
        search(root.l, val1, None)
        print root.value
        search(root.r, None, val2)
    else:
        # Case 3
        if val1 < val2 < root.value:
            search(root.l, val1, val2)
        else:
            search(root.r, val1, val2)


root = Node(2, Node(1), Node(3))
search_prep(root, 1, 3)
search_prep(root, 1, 2)
search_prep(root, 2, 3)

root = Node(2, Node(1), Node(3, None, Node(4)))
search_prep(root, 3, 4)
search_prep(root, 4, 1)
try:
    search_prep(root, 1, 1)
except:
    print 'OK'
