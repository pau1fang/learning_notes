import timeit
from DataStructures.chapter05.搜索.二分搜索 import binary_search, binary_sort, binary_search3
from DataStructures.chapter05.搜索.顺序搜索 import order_sequential_search
"""结论：
    递归版本22.8564151
    循环版本0.22093639999999937
    递归版本不用切片也很快
    递归版本二分搜索不用切片用时: 5.313207
    循环版本二分查找用时： 3.7785863
"""

a = list(range(100000))
# t1 = timeit.Timer("binary_search(a, 700)", "from __main__ import binary_search, a")
# t2 = timeit.Timer("order_sequential_search(a, 700)", "from __main__ import order_sequential_search, a")
t3 = timeit.Timer("binary_sort(a, 700)", "from __main__ import binary_sort, a")
t4 = timeit.Timer("binary_search3(a, 700)", "from __main__ import binary_search3, a")
# time1 = t1.timeit(100000)
# time2 = t2.timeit(100000)
time3 = t3.timeit(100000)
time4 = t4.timeit(100000)
# print("递归版本的二分搜索用时:     ", time1)
print("递归版本二分搜索不用切片用时:", time4)
# print(time2)
print("循环版本二分查找用时：", time3)
