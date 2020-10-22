class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.sibling = None

    def set_next(self, node):
        self.next = node

    def set_sibling(self, node):
        self.sibling = node


class ComplexList:
    def __init__(self):
        self.head = None
        self.rear = None

    def append(self, val):
        if self.head is None:
            self.head = self.rear = Node(val)
        else:
            self.rear.next = Node(val)
            self.rear = self.rear.next

    def __getitem__(self, item):
        current_node = self.head

        while current_node is not None and item > 0:
            current_node = current_node.next
            item -= 1
        if current_node is not None and item == 0:
            return current_node.val

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.val
            current_node = current_node.next


def complex_list_clone(head: Node):
    if head is None:
        return
    current_node = head
    while current_node is not None:
        node = Node(current_node.val)
        node.next = current_node.next
        current_node.next = node
        current_node = node.next


def connect_sibling_nodes(head:Node):
    current = head
    while current is not None:
        node = current.next
        if current.sibling:
            node.sibling = current.sibling.next
        current = node.next


def reconnect_nodes(head:Node):
    if head is None:
        return None
    current = head
    new_head = head.next
    while current:
        node = current.next
        current.next = node.next
        current = current.next
    return new_head


List = ComplexList()
for i in range(10):
    List.append(i)

for i in List:
    print(i)

complex_list_clone(List.head)
for i in List:
    print(i)
connect_sibling_nodes(List.head)
new_head = reconnect_nodes(List.head)
for i in List:
    print(i)
    
while new_head:
    print(new_head.val)
    new_head = new_head.next
