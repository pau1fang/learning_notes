from random import randrange
from DataStructures.Stack import Stack


def flip():
    return randrange(2)


class HeaderNode:
    def __init__(self):
        self.down = None
        self.next = None

    def set_down(self, node):
        self.down = node

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_down(self):
        return self.down


class DataNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.down = None

    def get_key(self):
        return self.key

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def get_down(self):
        return self.down

    def set_val(self, val):
        self.val = val

    def set_next(self, node):
        self.next = node

    def set_down(self, node):
        self.down = node


class SkipList:
    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head
        stop = False
        found = False
        while not found and not stop:
            if current is None:
                stop = True
            else:
                if current.get_next() is None:
                    current = current.get_down()
                else:
                    if current.get_next().get_key() == key:
                        found = True
                    else:
                        if current.get_next().get_key() > key:
                            current = current.get_down()
                        else:
                            current = current.get_next()

        if found:
            return current.get_next().get_val()
        else:
            return None

    def insert(self, key, val):
        if self.head is None:
            self.head = HeaderNode()
            temp = DataNode(key, val)
            self.head.set_next(temp)
            top = temp
            while flip() == 1:
                temp = DataNode(key, val)
                new_head = HeaderNode()
                new_head.set_down(self.head)
                temp.set_down(top)
                new_head.set_next(temp)
                self.head = new_head
                top = temp
        else:
            tower_stack = Stack()
            current = self.head
            stop = False
            while not stop:
                if current is None:
                    stop = True
                else:
                    if current.get_next() is None:
                        tower_stack.push(current)
                        current = current.get_down()
                    else:
                        if current.get_next().get_key() > key:
                            tower_stack.push(current)
                            current = current.get_down()
                        else:
                            current = current.get_next()

            lowest_level = tower_stack.pop()
            temp = DataNode(key, val)
            temp.set_next(lowest_level.get_next())
            lowest_level.set_next(temp)
            top = temp
            while flip() == 1:
                if tower_stack.isEmpty():
                    new_header = HeaderNode()
                    temp = DataNode(key, val)
                    temp.set_down(top)
                    new_header.set_next(temp)
                    new_header.set_down(self.head)
                    self.head = new_header
                    top = temp
                else:
                    temp = DataNode(key, val)
                    temp.set_down(top)
                    pre_node = tower_stack.pop()
                    temp.set_next(pre_node.get_next())
                    pre_node.set_next(temp)
                    top = temp


class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def get(self, key):
        return self.collection.search(key)


def get_nodes(node):
    header_list = []
    count_node = 0
    head = node
    while head:
        header_list.append(head)
        head = head.get_down()
    for h in header_list:
        current = h.get_next()
        while current:
            count_node += 1
            current = current.get_next()
    print(header_list)
    print("header:", len(header_list), "node:", count_node)
    

if __name__ == '__main__':
    m = Map()
    m.put(1, "hello")
    print(m.get(1))
    print(m.get(2))
    m.put(2, "world")
    print(m.get(2))
    get_nodes(m.collection.head)



