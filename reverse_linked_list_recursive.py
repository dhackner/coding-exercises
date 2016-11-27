class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(curr):
    if not curr.next:
        print 'NEW ROOT %s' % curr.value
        return curr, curr
    new_head, new_tail = reverse(curr.next)
    new_tail.next = curr
    curr.next = None
    return new_head, curr

x = Node(1,
         Node(2,
              Node(3,
                   Node(4,
                        Node(5)
                        )
                   )
              )
         )

a = reverse(x)[0]
while a:
    print a.value
    a = a.next
