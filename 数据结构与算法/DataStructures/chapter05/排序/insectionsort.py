def insertion_sort(alist):
    # for i in range(1, len(alist)):
    #     j = i-1
    #     temp = alist[i]
    #     while (j >=0) and (alist[j]>temp):
    #         alist[j+1] = alist[j]
    #         j -= 1
    #     # if j!=i-1:
    #     alist[j+1] = temp
    for index in range(1, len(alist)):
        position = index
        current_value = alist[index]
        while position>0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = current_value

if __name__ == '__main__':
    a = [9, 5, 4, 3, 2, 3, 1]
    print(a)
    insertion_sort(a)
    print(a)