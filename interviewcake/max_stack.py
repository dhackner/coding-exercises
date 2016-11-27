# https://www.interviewcake.com/question/python/largest-stack


class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        if len(self.items) == 0:
            max_beneath_inclusive = item
        else:
            max_beneath_inclusive = max(item, self.items[-1][1])
        self.items.append((item, max_beneath_inclusive))

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()[0]

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1][0]

    def max(self):
        if not self.items:
            return None
        return self.items[-1][1]

x = Stack()
x.push(2)
x.push(0)
x.push(1)
x.push(3)
assert x.peek() == 3
assert x.max() == 3
assert x.pop() == 3

assert x.max() == 2
assert x.pop() == 1
print 'OK'
