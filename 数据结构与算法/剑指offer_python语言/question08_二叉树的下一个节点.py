class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def is_left_child(self):
        if self.parent and self.parent.left == self:
            return True
        else:
            return False

    def has_right_child(self):
        return self.right is not None

    def is_right_child(self):
        if self.parent and self.parent.right == self:
            return True
        else:
            return False


def solution(node):
    if node is None:
        return None
    next_node = None

    if node.right is not None:
        current = node.right
        while current.left is not None:
            current = current.left
        next_node = current
    elif node.parent is not None:
        current = node
        parent = node.parent
        while parent is not None and current == parent.right:
            current = parent
            parent = parent.parent
        next_node = parent

    return next_node
