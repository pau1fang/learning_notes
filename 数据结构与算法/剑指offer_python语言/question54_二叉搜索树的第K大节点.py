class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solution(node: Node, k):
    stack = []
    stack.append(node)
    index = 0
    while stack and index < k:
        current_node = stack[-1]
        if current_node.left:
            stack.append(current_node.left)
        else:
            cur = stack.pop()
            index += 1
            if cur.right:
                stack.append(cur.right)
    print(stack.pop().val)


def solution2(node: Node, k):

    target = None

    if node.left is not None:
        target = solution2(node.left, k)

    if target is None:
        if k[0] == 1:
            target = node
        k[0] -= 1

    if target is None and node.right is not None:
        target = solution2(node.right, k)
    return target


root = Node(5)
root.left = Node(3)
root.right = Node(7)

solution(root, 2)
print(solution2(root, [2]).val)
