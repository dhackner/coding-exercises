class Node(object):

    def __init__(self, value, l=None, r=None):
        self.value = value
        self.l = l
        self.r = r

    def insert(self, value):
        if value < self.value:
            if self.l:
                self.l.insert(value)
            else:
                self.l = Node(value)
        else:
            if self.r:
                self.r.insert(value)
            else:
                self.r = Node(value)

    def to_tree(self):
        return '(%s %s %s)' % (self.l.to_tree() if self.l else None, self.value, self.r.to_tree() if self.r else None)

    def __str__(self):
        return self.value if self.value else ''
