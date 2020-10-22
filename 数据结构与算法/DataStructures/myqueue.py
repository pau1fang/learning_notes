class Queue:
    def __init__(self):
        self.items_ = []

    def isEmpty(self):
        return self.items_ == []

    def enqueue(self, item):
        self.items_.append(item)

    def dequeue(self):
        return self.items_.pop(0)

    def size(self):
        return len(self.items_)

