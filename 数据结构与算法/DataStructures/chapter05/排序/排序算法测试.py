from DataStructures.chapter05.排序.bubblesort import bubble_sort2, bubble_sort
from DataStructures.chapter05.排序.selectionsort import selectionsort
from DataStructures.chapter05.排序.insectionsort import insertion_sort
from DataStructures.chapter05.排序.shellsort import shell_sort
from DataStructures.chapter05.排序.归并排序 import merge_sort
from DataStructures.chapter05.排序.quicksort import quick_sort
from timeit import Timer
import random


def random_list(n):
    return [random.randint(0, 1000) for i in range(n)]


list_ = random_list(500)
print(list_)
bubble = Timer("bubble_sort(list_[:])", "from __main__ import bubble_sort, list_")
bubble2 = Timer("bubble_sort2(list_[:])", "from __main__ import bubble_sort2, list_")
select = Timer("selectionsort(list_[:])", "from __main__ import selectionsort, list_")
insertion = Timer("insertion_sort(list_[:])", "from __main__ import insertion_sort, list_")
shell = Timer("shell_sort(list_[:])", "from __main__ import shell_sort, list_")
merge = Timer("merge_sort(list_[:])", "from __main__ import merge_sort, list_")
quick = Timer("quick_sort(list_[:])", "from __main__ import quick_sort, list_")
bubble_time = bubble.timeit(100)
bubble2_time = bubble2.timeit(100)
select_time = select.timeit(100)
insertion_time = insertion.timeit(100)
shell_time = shell.timeit(100)
merge_time = merge.timeit(100)
quick_time = quick.timeit(100)
print(list_)

print("冒泡排序用时：", bubble_time)
print("冒泡排序用时：", bubble2_time)
print("选择排序用时：", select_time)
print("插入排序用时：", insertion_time)
print("希尔排序用时：", shell_time)
print("归并排序用时：", merge_time)
print("快速排序用时：", quick_time)
print("*"*30)
print()
print("*"*30)

