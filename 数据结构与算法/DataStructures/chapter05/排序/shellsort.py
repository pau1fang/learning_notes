def shell_sort(alist):
    step = len(alist)//2
    while step>0:
        for i in range(step):
            for index in range(i, len(alist), step):
                position = index
                current_value = alist[position]
                while position > 0 and alist[position-1]>current_value:
                    alist[position] = alist[position-step]
                    position -= step
                alist[position] = current_value
        # print("After increments of size", step, "the list is", alist)
        step //= 2


if __name__ == '__main__':
    a = [9, 5, 4, 3, 2, 3, 1]
    print(a)
    shell_sort(a)
    print(a)