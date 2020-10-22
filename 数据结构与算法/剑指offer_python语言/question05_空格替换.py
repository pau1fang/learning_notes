def solution(arr, length):
    if not isinstance(arr, list):
        return
    original_length = 0
    num_of_blank = 0
    i = 0
    while arr[i] != "\0":
        if arr[i] == " ":
            num_of_blank += 1
        original_length += 1
        i += 1

    new_length = original_length + num_of_blank * 2
    if new_length>length:
        return
    index_of_new_length = new_length
    index_of_origin = original_length

    while 0 <= index_of_origin < index_of_new_length:
        if arr[index_of_origin] == " ":
            arr[index_of_new_length] = "0"
            index_of_new_length -= 1
            arr[index_of_new_length] = "2"
            index_of_new_length -= 1
            arr[index_of_new_length] = "%"
            index_of_new_length -= 1
        else:
            arr[index_of_new_length] = arr[index_of_origin]
            index_of_new_length -= 1
        index_of_origin -= 1


char = list("hello world i am ai\0")+[None]*10
print(char)
solution(char, len(char))
print(char)
print(''.join(list([i for i in char if i is not None])))
