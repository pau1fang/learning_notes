from typing import Counter


def solution(string):
    c = Counter()
    for i in string:
        c[i] += 1
    for i in string:
        if c[i] == 1:
            return i
    return '\0'


print(solution('fjdjfljfdslfjdsj\n'))

"""
题目二：字符流中第一个只出现一次的字符

"""


class Solution:
    def __init__(self):
        self._container = [-1 for _ in range(256)]
        self.index = 0

    def insert(self, ch):
        if self._container[ord(ch)] == -1:
            self._container[ord(ch)] = self.index
        elif self._container[ord(ch)] >= 0:
            self._container[ord(ch)] = -2
        self.index += 1

    def first_appearing_once(self):
        ch = '\0'
        min_index = float("inf")
        for i in range(256):
            if 0 <= self._container[i] < min_index:
                min_index = self._container[i]
                ch = chr(i)
        return ch


s = Solution()

s.insert('a')
print(s.first_appearing_once())
s.insert("b")
print(s.first_appearing_once())
s.insert("a")
print(s.first_appearing_once())




