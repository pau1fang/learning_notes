from typing import List


def has_path_core(matrix, rows, cols, row, col, s, path_length, visited):
    if path_length == len(s):
        return True
    path = False
    if 0 <= row < rows and 0 <= col <= cols and \
            matrix[row][col] == s[path_length] and \
            not visited[row][col]:
        path_length += 1
        visited[row][col] = 1
        path = has_path_core(matrix, rows, cols, row, col - 1, s, path_length, visited) or \
               has_path_core(matrix, rows, cols, row - 1, col, s, path_length, visited) or \
               has_path_core(matrix, rows, cols, row, col + 1, s, path_length, visited) or \
               has_path_core(matrix, rows, cols, row + 1, col, s, path_length, visited)
        if not path:
            path_length -= 1
            visited[row][col] = 0
    return path


def has_path(matrix: List[List], s):
    if matrix is None or s is None:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[0 for i in range(cols)] for _ in range(rows)]
    path_length = 0
    for i in range(rows):
        for j in range(cols):
            if has_path_core(matrix, rows, cols, i, j, s, path_length, visited):
                return True
    return False


if __name__ == '__main__':
    l1 = [['a', 'b', 't', 'g'],
          ['c', 'f', 'c', 's'],
          ['j', 'd', 'e', 'h']]
    s = 'bfcf'
    print(has_path(l1, s))
