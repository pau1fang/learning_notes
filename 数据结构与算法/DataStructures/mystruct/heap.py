class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i //= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        """此处有两种方法，循环和递归"""
        while (i*2)<=self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i]>self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
        # if i*2<=self.current_size:
        #     mc = self.min_child(i)
        #     if self.heap_list[i] > self.heap_list[mc]:
        #         self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
        #     self.perc_down(mc)

    def min_child(self, i):
        if i*2+1>self.current_size:
            return i*2
        else:
            if self.heap_list[i*2]<self.heap_list[2*i+1]:
                return i * 2
            else:
                return i*2+1

    def del_min(self):
        if self.current_size>0:
            ret_val = self.heap_list[1]
            self.heap_list[1] = self.heap_list[-1]
            self.current_size -= 1
            self.heap_list.pop()
            self.perc_down(1)
            return ret_val
        else:
            raise ValueError("Heap is empty")

    def build_heap(self, alist):
        i = len(alist)//2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i>0:
            self.perc_down(i)
            i -= 1

    def heap_sort(self, alist):
        self.build_heap(alist)
        blist = []
        while self.current_size>0:
            blist.append(self.del_min())
        return blist




if __name__ == '__main__':
    h = Heap()
    h.insert(1)
    h.insert(4)
    h.insert(5)
    h.insert(1)
    h.insert(1)
    print(h.heap_list)
    # for i in range(6):
    #     h.del_min()
    #     print(h.heap_list)
    a = [9,6,5,4,6,4,3,2,1]
    b = Heap().heap_sort(a)
    print(b)

