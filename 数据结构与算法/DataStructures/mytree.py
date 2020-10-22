class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, new_node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, new_node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_val(self, val):
        self.key = val

    def get_root_val(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


if __name__ == '__main__':
    r = BinaryTree("a")
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left("b")
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right("c")
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val("hello")
    print(r.get_right_child().get_root_val())
    r.preorder()
