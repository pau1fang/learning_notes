def order_sequential_search(alist, item):
    found = False
    stop = False
    pos = 0
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

