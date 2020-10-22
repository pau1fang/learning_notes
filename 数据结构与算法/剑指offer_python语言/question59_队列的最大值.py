# def solution(arr, n):
#     max_sum = 0
#     sum_ = 0
#     for i in range(n):
#         sum_ += arr[i]
#     if max_sum < sum_:
#         max_sum = sum_
#     start = 0
#     end = n-1
#     length = len(arr)
#     while end < length-1:
#         sum_ = sum_ + arr[end+1] - arr[start]
#         if sum_ > max_sum:
#             max_sum = sum_
#         start += 1
#         end += 1
#     return max_sum


class Stack:
    def __init__(self):
        self._container = []
        self._max = []

    def push(self, val):
        self._container.append(val)
        if not self._max:
            self._max.append(val)
        else:
            if self.max() > val:
                self._max.append(self.max())
            else:
                self._max.append(val)

    def max(self):
        if self._container:
            return self._max[-1]
        else:
            return float("-inf")

    def pop(self):
        if self._container:
            self._max.pop()
            return self._container.pop()

    def top(self):
        if self._container:
            return self._container[-1]

    def is_empty(self):
        return not self._container


class GetMaxQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push_back(self, val):
        self.stack1.push(val)

    def pop_front(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def max(self):
        if self.stack1.max() > self.stack2.max():
            return self.stack1.max()
        else:
            return self.stack2.max()


def solution(arr, k):
    queue = GetMaxQueue()
    for i in range(k):
        queue.push_back(arr[i])
    result = [queue.max()]
    for i in arr[k:]:
        queue.pop_front()
        queue.push_back(i)
        result.append(queue.max())
    return result


def solution2(arr, k):
    result = []
    index = []
    for i in range(k):
        while index and arr[i] >= arr[index[-1]]:
            index.pop()
        index.append(i)
    for i in range(k, len(arr)):
        result.append(arr[index[0]])
        while index and arr[i] >= arr[index[-1]]:
            index.pop()
        if index and i - index[0] >= k:
            index.pop(0)
        index.append(i)
    result.append(arr[index[0]])
    return result


class QueueWithMax:
    def __init__(self):
        self.data = []
        self.maximums = []
        self.current_index = 0

    def push_back(self, val):
        while self.maximums and val >= self.maximums[-1][0]:
            self.maximums.pop()
        self.data.append((val, self.current_index))
        self.maximums.append((val, self.current_index))
        self.current_index += 1

    def pop_front(self):
        if not self.maximums:
            raise ValueError("queue is empty")
        data = self.data.pop(0)
        if data[1] == self.maximums[0][1]:
            self.maximums.pop(0)
        return data[0]

    def max(self):
        if not self.maximums:
            raise ValueError("queue is empty")
        return self.maximums[0][0]


array = [2,3,4,2,6,2,5,1]
print(solution(array, 3))
print(solution2(array, 3))
q = QueueWithMax()
for x in array:
    q.push_back(x)
    print(q.max())
print("*"*20)
for x in range(len(array)):
    q.pop_front()
    print(q.max())