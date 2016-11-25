class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def second_highest(node):
    if node.left is None and node.right is None:
        raise Exception

    # Find Max. If max has left subtree return max of that, otherwise return
    # parent.
    previous = None
    while node.right is not None:
        previous = node  # Node above rightmost. Track it as either the 'second to last value' or the parent of the left subtree
        node = node.right

    if node.left is None:
        # No subtree, return parent
        return previous.value
    else:
        # Has a left subtree, return max of that instead
        previous = node.left
        while previous.right is not None:
            previous = previous.right
        return previous.value


root = BinaryTreeNode(2)
root.insert_right(3)
assert second_highest(root) == 2  # 2 nodes

root = BinaryTreeNode(2)
root.insert_left(1)
assert second_highest(root) == 1  # 2 nodes
root.insert_right(6)
assert second_highest(root) == 2  # No subtree of max, return parent
root.right.insert_left(3)
assert second_highest(root) == 3  # Return max of left single-element subtree
root.right.left.insert_right(5)
assert second_highest(root) == 5  # Return max of left multi-element subtree
root.right.left.insert_left(4)
assert second_highest(root) == 5  # Add more and still use max

print 'OK'
