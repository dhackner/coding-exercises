# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

# Algorithm: On put, empty Stack 1 into Stack 2 (reversing it), insert new
# value, then empty Stack 2 back on top of Stack 1 (un-doing the reverse)

# Improved Algorithm: Don't un-do the reverse and instead only do it when
# necessary (i.e. what if they put() 5 elements in a row)

# Best Algorithm: Maintain separate stacks altogether and only do the reverse
# when the 'dequeue' is completely empty


class MyQueue(object):

    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def peek(self):
        if not len(self.dequeue):
            self.reverse()
        return self.dequeue[-1]

    def pop(self):
        if not len(self.dequeue):
            self.reverse()
        self.dequeue, pop_val = self.dequeue[:-1], self.dequeue[-1]
        return pop_val

    def put(self, value):
        self.enqueue.append(value)

    def reverse(self):
        # When you've run out of elements to dequeue, empty over into it
        for index in range(len(self.enqueue)):
            self.enqueue, pop_val = self.enqueue[:-1], self.enqueue[-1]
            self.dequeue.append(pop_val)


queue = MyQueue()
for line in open('queue_testcase1.txt'):
    values = map(int, line.split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
