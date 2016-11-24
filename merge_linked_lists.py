class Node():

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge(sorted1, sorted2):
    if sorted1 is None:
        return sorted2
    if sorted2 is None:
        return sorted1
    # Learning: "Base case" initialization for iterative
    if sorted1.value <= sorted2.value:
        root = sorted1
        sorted1 = sorted1.next
    else:
        root = sorted2
        sorted2 = sorted2.next
    current = root
    while sorted1 is not None or sorted2 is not None:
        if sorted1 is not None and (sorted2 is None or sorted1.value <= sorted2.value):
            # Select value from the first list
            current.next = sorted1
            sorted1 = sorted1.next
            current = current.next
        elif sorted2 is not None and (sorted1 is None or sorted1.value > sorted2.value):
            # Select value from the second list
            current.next = sorted2
            sorted2 = sorted2.next
            current = current.next
    return root


sorted1 = Node(1, Node(2, Node(4, Node(9, Node(18)))))
sorted2 = Node(2, Node(3, Node(5)))
root = merge(sorted1, sorted2)
array = []
while root is not None:
    array.append(root.value)
    root = root.next
assert array == [1, 2, 2, 3, 4, 5, 9, 18]
assert merge(sorted1, None) == sorted1
assert merge(None, sorted2) == sorted2
print 'OK'
