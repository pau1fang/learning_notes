class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def perc_down(self, i):
        while self.size-1>=2*i+1:
            mc = self.min_child(i)
            if self.heap[i]>self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def min_child(self, i):
        if 2*i+2>self.size-1:
            return 2*i+1
        else:
            if self.heap[2*i+1]>self.heap[2*i+2]:
                return 2*i+2
            else:
                return 2*i+1

    def del_min(self):
        if self.size>0:
            num = self.heap[0]
            rear = self.heap[-1]
            self.heap[0] = rear
            self.heap.pop()
            self.size -= 1
            self.perc_down(0)
            return num

    def build_heap(self, alist):
        self.heap = alist
        self.size = len(alist)
        i = (self.size-1)//2
        while i>=0:
            self.perc_down(i)
            i = i-1

    def heap_sort(self, alist):
        self.build_heap(alist)
        blist = []
        while self.size>0:
            blist.append(self.del_min())
        return blist


if __name__ == '__main__':
    h = Heap()
    a = [3,2,8,7,5,4,1]
    h.build_heap(a)
    print(a)
    print(h.heap_sort(a))
