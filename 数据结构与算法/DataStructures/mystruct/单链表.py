class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def show(self):
        # if self.head is None:
        #     return None
        # else:
        res = []
        node = self.head
        while node is not None:
            res.append(node.val)
            node = node.next
        print(res)

    def front(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert(self, i, val):
        node = self.head
        while node is not None and i > 0:
            node = node.next
            i -= 1
        new_node = Node(node.val)
        new_node.next = node.next
        node.next = new_node
        node.val = val

    def pop(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            val = self.head.val
            self.head = self.tail = None
            return val
        else:
            node = self.head
            while node.next and node.next is not self.tail:
                node = node.next
            res = self.tail.val
            self.tail = node
            self.tail.next = None
            return res


if __name__ == '__main__':
    l = List()
    l.append(1)
    l.append(2)
    l.front(3)
    l.front(4)
    l.insert(1, 10)
    l.insert(0, 0)
    print(l.pop())
    for i in range(5):
        print(l.pop())
    l.show()
