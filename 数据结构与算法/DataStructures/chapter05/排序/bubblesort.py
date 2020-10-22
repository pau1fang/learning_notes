def bubble_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

def bubble_sort2(alist):
    """冒泡排序的改进，判断一次遍历有没有发生交换，如果没有就表明已经排序好了"""
    change = True
    length = len(alist)-1
    while (length >0) and change:
        change = False
        for i in range(0, length):
            if alist[i]>alist[i+1]:
                change = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        length -= 1

if __name__ == '__main__':
    a = [9, 8, 7, 3, 2, 1]
    print(a)
    bubble_sort2(a)
    print(a)

