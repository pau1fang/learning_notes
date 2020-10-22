class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def show(self):
        if self.head is None:
            return
        queue = [self.head]
        while len(queue)>0:
            current = queue.pop(0)
            print(current.val)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)


def solution(arr1, arr2:list):
    if len(arr1) == 1:
        return Node(arr1[0])
    elif len(arr1) == 0:
        return None
    else:
        a = arr1[0]
        index = arr2.index(a)
        left = solution(arr1[1:index+1], arr2[0:index])
        right = solution(arr1[index+1:], arr2[index+1:])
        node = Node(a)
        if left is not None:
            node.left = left
        if right is not None:
            node.right = right
        return node


print([1,2,3].index(3))

l1 = [1,2,4,7,3,5,6,8]
l2 = [4,7,2,1,5,3,8,6]

t = BinaryTree()
t.head = solution(l1, l2)
t.show()
