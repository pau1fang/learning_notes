from typing import List


def Min(numbers: List, length: int) -> int:
    if length <=0:
        raise ValueError("Invalid parameters")
    index1 = 0
    index2 = length - 1
    mid = index1
    result = numbers[index1]
    while numbers[index1] >= numbers[index2]:
        if index2 - index1 == 1:
            mid = index2
            break
        mid = (index1 + index2) // 2
        if numbers[index1] == numbers[index2] & numbers[index2] == numbers[mid]:
            for i in numbers:
                if result > i:
                    result = i
            return result
        if numbers[index1] <= numbers[mid]:
            index1 = mid
        else:
            index2 = mid
    result = numbers[mid]
    return result


if __name__ == '__main__':
    l1 = [1,2,3,4,5]
    l2 = [1,0,1,1,1]
    l3 = [4,5,1,2,3]
    l4 = []
    print(Min(l1, 5))
    print(Min(l2, 5))
    print(Min(l3, 5))
    print(Min(l4, 0))

