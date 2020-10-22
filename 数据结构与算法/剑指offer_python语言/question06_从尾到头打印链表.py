class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class List:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node = ListNode(val)
            current.next = new_node

    def show(self):
        current = self.head
        output = []
        while current:
            output.append(current.val)
            current = current.next
        print(output)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.val
            current = current.next


def solution1(head):
    node_list = []
    node = head
    while node is not None:
        node_list.append(node)
        node = node.next

    while len(node_list) > 0:
        node = node_list.pop()
        print(node.val, end='\t')


def solution2(node):
    if node is not None:
        if node.next is not None:
            solution2(node.next)
        print(node.val, end='\t')


arr = list(range(10))
my_list = List()
for i in arr:
    my_list.add(i)
my_list.show()
solution1(my_list.head)
print()
solution2(my_list.head)
