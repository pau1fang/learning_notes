def solution(arr, item):
    rows = len(arr)
    col = len(arr[0]) - 1
    found = False
    row = 0
    while row < rows and col >= 0:
        if arr[row][col] == item:
            found = True
            break
        elif arr[row][col] > item:
            col -= 1
        else:
            row += 1

    return found


arr2 = [[1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]]


res = solution(arr2, 11)
print(res)
