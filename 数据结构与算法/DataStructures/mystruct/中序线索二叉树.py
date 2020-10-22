class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.ltag = 0
        self.rtag = 0


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def append(self, val):
        if self.root is None:
            self.root = Node(val)
            self.size += 1
        else:
            pass


def in_thread(node: Node, pre_node):
    if node is not None:
        in_thread(node.left_child, pre_node)
        if node.left_child is None:
            node.left_child = pre_node
            node.ltag = 1
        if pre_node is not None and pre_node.right_child is None:
            pre_node.right_child = node
            pre_node.rtag = 1
        pre_node = node
        in_thread(node.right_child, pre_node)


def create_in_thread(root):
    pre = None
    if root is not None:
        in_thread(root, pre)
        pre.right_child = None
        pre.rtag = 1

