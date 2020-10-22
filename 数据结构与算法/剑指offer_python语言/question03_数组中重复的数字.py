def solution(alist):
    if not isinstance(alist, list) or len(alist) == 0:
        return False
    count_dict = {}
    for i in alist:
        if i < 0 or i > len(alist)-1:
            return False
    for i in alist:
        if count_dict.get(i) is None:
            count_dict[i] = 1
        else:
            print(i)
            return True
    return False


def solution2(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        return False
    for i in arr:
        if not isinstance(i, int) or i<0 or i > len(arr):
            return False
    j = 0
    while True:
        if j > len(arr) - 1:
            return False
        if j == arr[j]:
            j += 1
        else:
            if arr[j] == arr[arr[j]]:
                print(arr[j])
                return True
            else:
                temp = arr[j]
                arr[j] = arr[temp]
                arr[temp] = temp


def solution3(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        return False
    for i in arr:
        if not isinstance(i, int) or i<0 or i > len(arr):
            return False
    for j in range(len(arr)):
        while j != arr[j]:
            if arr[j] == arr[arr[j]]:
                print(arr[j])
                return True
            else:
                temp = arr[j]
                arr[j] = arr[temp]
                arr[temp] = temp
    return False


ll = [1, 2, 3, 4, 23, 1, 12, 21, 121, 3, 23, 32, 1, 1, 2, 2, 21]
l2 = [1,2,3,4,5,6,0]
l3 = [0,1,2,3,4,5,1,3]
col = [ll,l2,l3,"a"]

for l in col:
    res = solution(l)
    print(res)
print("*"*10)

for a in col:
    res = solution2(a)
    print(res)
print("*"*10)


for a in col:
    res = solution3(a)
    print(res)
print("*"*10)

