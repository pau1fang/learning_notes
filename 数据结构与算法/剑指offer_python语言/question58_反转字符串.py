def solution(string):
    return ' '.join(reversed(string.split()))


print(solution("i am a student."))


def reversed_(arr, begin, end):
    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1


def solution2(string):
    string_list = list(string)
    begin = 0
    end = 0
    reversed_(string_list, 0, len(string_list)-1)
    while end < len(string_list):
        if string_list[end] == ' ':
            reversed_(string_list, begin, end-1)
            begin = end+1
        end += 1
    reversed_(string_list, begin, end-1)
    return ''.join(string_list)


print(solution2("i am a student."))


def left_rotate_string(arr, n):
    if n >= len(arr):
        return
    reversed_(arr, 0, n-1)
    reversed_(arr, n, len(arr)-1)
    reversed_(arr, 0, len(arr)-1)
    return ''.join(arr)


print(left_rotate_string(list('hello, world'), 2))
