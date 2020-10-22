from DataStructures.myqueue import Queue


class Solution:
    """比较粗糙
        有待完善
    """
    def sort(self, wait_sort_list):
        main_box = Queue()
        boxs = {}
        max_number = max(wait_sort_list)
        digs = len(str(max_number))
        for i in range(10):
            boxs[i] = Queue()
        for n in wait_sort_list:
            main_box.enqueue(n)

        for d in range(digs):
            g = 10**d
            while not main_box.isEmpty():
                num = main_box.dequeue()
                dig = num//g % 10
                boxs[dig].enqueue(num)
            for i in range(10):
                while not boxs[i].isEmpty():
                    main_box.enqueue(boxs[i].dequeue())
        print(main_box.items_)

s = Solution()
s.sort([2,3,4,1,2,7,4,7,23,32,11,1111])
print(len(str(123)))