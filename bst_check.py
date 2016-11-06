# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

# Algorithm: True if for each subtree, the left tree is less then this node and
# the right tree is greater. i.e. recurse(left, lambda x: x < value) and
# recurse(right, lambda x: x > value). Needs to continuously check for all
# lambdas above as well for this case:
"""
        2
    1      4
      3
3 needs to be both > 1 AND < 2 in order to properly fail
"""


from bst_node import Node


def check_binary_search_tree_(root):
    return check_subtree(root, lambda x: True)


def check_subtree(root, fxn):
    if root is None:
        return True
    elif fxn(root.value):
        return check_subtree(root.l, lambda x: fxn(x) and x < root.value) and \
            check_subtree(root.r, lambda x: fxn(x) and x > root.value)
    else:
        return False

assert check_binary_search_tree_(Node(5, Node(2, Node(1), Node(3)), Node(9, Node(7), Node(10))))
assert not check_binary_search_tree_(Node(3, Node(5, Node(1), Node(4)), Node(2, Node(6), None)))
assert not check_binary_search_tree_(Node(3, Node(2, Node(1), Node(4)), Node(6, Node(5), Node(7))))
print 'OK'
