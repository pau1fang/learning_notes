def number_of_1(num):
    n = 0
    while num:
        if num & 1:
            n += 1
        num >>= 1
    return n


# def num_of_1(num):
#
#     n = 0
#     flag = 1
#     while flag:
#         if num & flag:
#             n += 1
#         flag <<= 1
#     return n


def num_of_1(num):
    count = 0
    while num:
        count += 1
        num = num&(num-1)
    return count

print(num_of_1(int(-4)))
