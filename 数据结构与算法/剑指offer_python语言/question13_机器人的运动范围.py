class Solution:
    def __init__(self, threshold, rows, cols):
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        self.visited = [[0 for _ in range(cols)] for _ in range(rows)]

    def solution(self):
        if self.threshold < 0 or self.rows <=0 or self.cols <= 0:
            return 0
        count = self.moving_count_core(0,0)
        return count

    def moving_count_core(self, row, col):
        count = 0
        if self.check(row, col):
            self.visited[row][col] = 1
            count = 1 + self.moving_count_core(row - 1, col) \
                    + self.moving_count_core(row, col - 1) \
                    + self.moving_count_core(row + 1, col) \
                    + self.moving_count_core(row, col + 1)
        return count

    def check(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols \
                and self.get_digit_sum(row) + self.get_digit_sum(col) <= self.threshold \
                and not self.visited[row][col]:
            return True
        return False

    def get_digit_sum(self, number):
        sum_ = 0
        while number > 0:
            sum_ += number % 10
            number //= 10
        return sum_


if __name__ == '__main__':
    s = Solution(10, 30, 30)
    print(s.solution())
