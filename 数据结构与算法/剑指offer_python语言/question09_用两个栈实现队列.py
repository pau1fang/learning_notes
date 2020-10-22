class Stack:
    def __init__(self):
        self.contains = []

    def is_empty(self):
        return len(self.contains) == 0

    def push(self, item):
        self.contains.append(item)

    def pop(self):
        return self.contains.pop()

    def top(self):
        if not self.is_empty():
            return self.contains[-1]


class CQueue:
    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def append_tail(self, item):
        self._stack2.push(item)

    def delete_head(self):
        if self.is_empty():
            raise ValueError("当前队列为空")
        else:
            if self._stack1.is_empty():
                while not self._stack2.is_empty():
                    self._stack1.push(self._stack2.pop())
                return self._stack1.pop()
            else:
                return self._stack1.pop()

    def is_empty(self):
        return self._stack1.is_empty() and self._stack2.is_empty()


if __name__ == '__main__':
    q = CQueue()
    for i in range(10):
        q.append_tail(i)

    for i in range(11):
        print(q.delete_head())
