class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def find_path(root:Node, expected_sum):
    if root is None:
        return
    stack = []
    sum_ = 0
    find_path_helper(root, stack, sum_, expected_sum)


def find_path_helper(root:Node, path:list, sum_, expected_sum):
    if root is None:
        return
    path.append(root.value)
    sum_ += root.value

    if root.left is None and root.right is None and sum_ == expected_sum:
        for i in path:
            print(i, end=' ')
        print()  

    if root.left:
        find_path_helper(root.left, path, sum_, expected_sum)
    if root.right:
        find_path_helper(root.right, path, sum_, expected_sum)
    path.pop()
    return


tree1 = Node(10)
tree1.left = Node(5)
tree1.right = Node(12)
tree1.left.left = Node(4)
tree1.left.right = Node(7)

find_path(tree1, 22)
