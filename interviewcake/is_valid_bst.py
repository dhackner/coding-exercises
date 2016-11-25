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

    def is_valid(self, min_compare=None, max_compare=None):
        # A node is valid if it is < any ancestors it is to the left of and >
        # any ancestors it is to the right of. So define min/max bounds for a
        # node and adjust them as moving down the tree
        return_value = True
        if min_compare:
            return_value = return_value and min_compare < self.value
        elif max_compare:
            return_value = return_value and self.value <= max_compare

        if self.left:
            return_value = return_value and self.left.is_valid(min_compare, self.value)

        if self.right:
            return_value = return_value and self.right.is_valid(self.value, max_compare)

        return return_value

root = BinaryTreeNode(3)
root.insert_left(1)
root.insert_right(4)
assert root.is_valid()
root.right.insert_left(2)  # Less than parent but not grandparent
assert not root.is_valid()

root = BinaryTreeNode(3)
root.insert_left(1)
root.insert_right(7)
root.right.insert_left(5)
root.right.insert_right(8)
assert root.is_valid()
root.right.left.insert_left(1)
assert not root.is_valid()
print 'OK'
