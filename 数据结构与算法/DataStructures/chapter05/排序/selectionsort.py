def selectionsort(alist):
    for i in range(len(alist)-1, 0, -1):
        index = 0
        for j in range(i+1):
            if alist[j] > alist[index]:
                index = j
        alist[i], alist[index] = alist[index], alist[i]


if __name__ == '__main__':
    a = [9, 4, 3, 2, 1, 3]
    print(a)
    selectionsort(a)
    print(a)

