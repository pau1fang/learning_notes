class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solution(node: Node):
    high = 1
    stack = [[node, 0]]
    max_high = 0
    while stack:
        current = stack[-1]
        if current[0].left and current[1] == 0 :
            stack.append([current[0].left, 0])
            current[1] += 1
            high += 1
            if max_high < high:
                max_high = high
        elif current[0].right and current[1] == 1:
            stack.append([current[0].right, 0])
            current[1] += 1
            high += 1
            if max_high< high:
                max_high = high
        else:
            stack.pop()
            high -= 1

    return max_high


def solution2(node: Node):
    if node is None:
        return 0
    left = solution2(node.left)
    right = solution2(node.right)
    return max(left, right) + 1


def is_balanced(node:Node):
    if node is None:
        return True
    left = solution2(node.left)
    right = solution2(node.right)
    if abs(left-right) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


def is_balanced2(node:Node):
    depth = [0]
    return is_balanced_helper(node, depth)


def is_balanced_helper(node: Node, depth: list):
    if node is None:
        depth[0] = 0
        return True

    left = [0]
    right = [0]
    if is_balanced_helper(node.left, left) and is_balanced_helper(node.right, right):
        if abs(left[0]-right[0]) <= 1:
            depth[0] = max(left[0], right[0]) + 1
            return True

    return False



root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
print(solution(root))
print(solution2(root))
print(is_balanced(root))
print(is_balanced2(root))

