class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class Tree:
    def __init__(self):
        self.head = None


def serialize(root, arr):
    if root is None:
        arr.append("$")
        return

    arr.append(root.val)
    serialize(root.left, arr)
    serialize(root.right, arr)


root_ = Node(1)
root_.set_left(Node(2))
root_.set_right(Node(3))
root_.get_left().set_left(Node(4))
root_.get_right().set_left(Node(5))
root_.get_right().set_right(Node(6))


ll = []
serialize(root_, ll)
print(''.join([str(x) for x in ll]))


def deserialize(arr):
    head = None
    if isinstance(arr[0], int):
        head = Node(int(arr[0]))
        arr.pop(0)
        head.left = deserialize(arr)
        head.right = deserialize(arr)
    else:
        arr.pop(0)
    return head


r = deserialize(ll)
print(ll)
stack = [r]
while stack:
    node = stack.pop(0)
    print(node.val, end=' ')
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)

