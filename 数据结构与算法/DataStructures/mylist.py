class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        newnode = Node(item)
        newnode.setNext(self.head)
        self.head = newnode

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current!=None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current = self.head
        previous = None
        fount = False
        while not fount:
            if current.getData() == item:
                fount = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        pass

    def insert(self, index, item):
        pass

    def index(self,item):
        pass

    def pop(self, head_or_rear):
        pass


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(previous.getNext())
            previous.setNext(temp)

    def remove(self, item):
        pass

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                break
            else:
                current = current.getNext()

        return found

    def isEmpty(self):
        return self.head is None

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def index(self, item):
        pass

    def pop(self, pos):
        pass


u = UnorderedList()
u.add(1)
u.add(2)
print(u.length())
print(u.search(2))