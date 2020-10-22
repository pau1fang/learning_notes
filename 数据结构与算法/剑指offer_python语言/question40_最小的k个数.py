def get_least_numbers(arr, k):
    start = 0
    end = len(arr) - 1
    index = partition(arr, 0, start, end)

    while index != k:
        if index > k:
            end = index - 1
            index = partition(arr, 0, start, end)
        else:
            start = index + 1
            index = partition(arr, 0, start, end)
    for i in range(k):
        print(arr[i], end=' ')
    print()


def partition(arr, length, start, end):
    if start >= end:
        return start
    left = start + 1
    index = start
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= arr[index]:
            left += 1
        while arr[right] >= arr[index] and left <= right:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[index], arr[right] = arr[right], arr[index]
    return right


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1.reverse()
print(l1)
get_least_numbers(l1, 3)


# print(list(reversed(l1)))
# print(l1)
# 解法二： 不修改原始数组， 基于堆或红黑树维护一个容量为k的数组池
class Heap:
    def __init__(self):
        self.container_ = [0]
        self.current_size = 0

    def prec_up(self, i):
        while i >> 1 > 0:
            if self.container_[i] > self.container_[i >> 1]:
                self.container_[i], self.container_[i >> 1] = self.container_[i >> 1], self.container_[i]
            i >>= 1

    def append(self, val):
        self.container_.append(val)
        self.current_size += 1
        self.prec_up(self.current_size)

    def max_chind(self, i):
        if 2 * i + 1 > self.current_size:
            return 2 * i
        if self.container_[2 * i] > self.container_[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1

    def prec_down(self, i):
        if 2 * i <= self.current_size:
            mc = self.max_chind(i)
            if self.container_[i] < self.container_[mc]:
                self.container_[i], self.container_[mc] = self.container_[mc], self.container_[i]
                self.prec_down(mc)

    def del_max(self):
        if self.current_size > 0:
            val = self.container_[1]
            self.container_[1] = self.container_[self.current_size]
            self.current_size -= 1
            self.prec_down(1)
            self.container_.pop()
            return val
        else:
            raise ValueError("Heap is empty")

    def build_heap(self, arr):
        length = len(arr)
        i = length >> 1
        self.container_ = [0] + arr[:]
        self.current_size = length
        while i > 0:
            self.prec_down(i)
            i -= 1

    def get_max(self):
        if self.current_size>0:
            return self.container_[1]

    def show_heap(self):
        if self.current_size>0:
            print(self.container_[1:])


heap = Heap()
heap.build_heap(l1)
# print(heap.container_)
# # for i in range(10):
# #     heap.append(i)
# # print(heap.container_)
# for i in range(9):
#     print(heap.del_max(), end=' #### ')
#     print(heap.container_)


def get_least_numbers2(arr, k):
    least_numbers = Heap()
    for i in arr:
        if least_numbers.current_size < k:
            least_numbers.append(i)
        else:
            if least_numbers.get_max() > i:
                least_numbers.del_max()
                least_numbers.append(i)
    least_numbers.show_heap()
print(l1)
get_least_numbers2(l1, 3)

