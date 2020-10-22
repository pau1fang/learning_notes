def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    result = [0 for _ in range(cols)]
    # result[0] = arr[0][0]
    for i in range(rows):
        for j in range(cols):
            """
            left = 0
            up = 0
            if i>0:
                up = result[j]
            if j>0:
                left = result[j-1]
            result[j] = max(up, left) + arr[i][j]
            """
            if j == 0:
                result[j] += arr[i][j]
            else:
                if result[j - 1] > result[j]:
                    result[j] = result[j - 1] + arr[i][j]
                else:
                    result[j] += arr[i][j]
    return result[cols - 1]


tips = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
print(solution(tips))
