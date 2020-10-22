class MaxHeap:
    def __init__(self):
        self._container = [0]
        self.size = 0

    def prec_up(self, i):
        while i >> 1 > 0:
            if self._container[i] > self._container[i >> 1]:
                self._container[i], self._container[i >> 1] = self._container[i >> 1], self._container[i]
            i >>= 1

    def insert(self, val):
        self._container.append(val)
        self.size += 1
        self.prec_up(self.size)

    def max_chind(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        if self._container[2 * i] > self._container[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1

    def prec_down(self, i):
        while i * 2 <= self.size:
            mc = self.max_chind(i)
            if self._container[i] < self._container[mc]:
                self._container[i], self._container[mc] = self._container[mc], self._container[i]
            i = mc

    def del_max(self):
        if self.size > 0:
            val = self._container[1]
            self._container[1] = self._container[self.size]
            self._container.pop()
            self.size -= 1
            self.prec_down(1)
            return val

    def get_max(self):
        if self.size > 0:
            return self._container[1]

    def show(self):
        print(self._container)

    def build_heap(self, arr):
        self._container = [0] + arr[:]
        self.size = len(arr)
        i = self.size >> 1
        while i > 0:
            self.prec_down(i)
            i -= 1


class MinHeap:
    def __init__(self):
        self._container = [0]
        self.size = 0

    def prec_up(self, i):
        while i >> 1 > 0:
            if self._container[i] < self._container[i >> 1]:
                self._container[i], self._container[i >> 1] = self._container[i >> 1], self._container[i]
            i >>= 1

    def insert(self, val):
        self._container.append(val)
        self.size += 1
        self.prec_up(self.size)

    def prec_down(self, i):
        while 2 * i <= self.size:
            mc = self.min_child(i)
            if self._container[i] > self._container[mc]:
                self._container[i], self._container[mc] = self._container[mc], self._container[i]
            i = mc

    def min_child(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self._container[2 * i] > self._container[2 * i + 1]:
                return 2 * i + 1
            else:
                return 2 * i

    def del_min(self):
        if self.size > 0:
            val = self._container[1]
            self._container[1] = self._container[self.size]
            self.size -= 1
            self._container.pop()
            self.prec_down(1)
            return val

    def build_heap(self, arr):
        self._container = [0] + arr[:]
        self.size = len(arr)
        i = self.size >> 1
        while i > 0:
            self.prec_down(i)
            i -= 1

    def show(self):
        print(self._container)

    def get_min(self):
        if self.size > 0:
            return self._container[1]
        else:
            raise ValueError("heap is empty")


# l1 = list(range(10))
# l2 = list(range(9, -1, -1))
# max_heap = MaxHeap()
# min_heap = MinHeap()
# max_heap.build_heap(l1)
# max_heap.show()
# min_heap.build_heap(l2)
# min_heap.show()
# for i in range(10):
#     print(max_heap.del_max(), end=' ')
#     print(min_heap.del_min())

class Solution:
    def __init__(self):
        self.min = MinHeap()
        self.max = MaxHeap()

    def insert(self, val):
        if (self.min.size + self.max.size) & 1 == 0:
            if self.max.size > 0 and val < self.max.get_max():
                self.max.insert(val)
                val = self.max.del_max()
            self.min.insert(val)
        else:
            if val > self.min.get_min():
                self.min.insert(val)
                val = self.min.del_min()
            self.max.insert(val)

    def get_median(self):
        size = (self.max.size + self.min.size)
        if size == 0:
            raise ValueError
        if size & 1 == 1:
            val = self.min.get_min()
        else:
            val = (self.max.get_max() + self.min.get_min()) >> 1

        return val


s = Solution()
for x in range(1, 10):
    s.insert(x)
    print(s.get_median())
s.max.show()
s.min.show()
