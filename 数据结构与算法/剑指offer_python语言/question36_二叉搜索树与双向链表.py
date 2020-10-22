class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def convert(root):
    last_node = [None]
    convert_node(root, last_node)

    head_of_list = last_node[0]

    while head_of_list is not None and head_of_list.left is not None:
        head_of_list = head_of_list.left

    return head_of_list


def convert_node(node, last_node):
    if node is None:
        return

    if node.left is not None:
        convert_node(node.left, last_node)

    node.left = last_node[0]
    if last_node[0]:
        last_node[0].right = node
    last_node[0] = node
    if node.right is not None:
        convert_node(node.right, last_node)


tree = Node(10)
tree.left = Node(6)
tree.right = Node(14)
tree.left.left = Node(4)
tree.left.right = Node(8)
tree.right.left = Node(12)
tree.right.right = Node(16)

head = convert(tree)
print()
rear = None
while head:
    print(head.val, end=' ')
    head = head.right
    if head is not None and head.right is None:
        rear = head
print()
while rear:
    print(rear.val, end=' ')
    rear = rear.left




