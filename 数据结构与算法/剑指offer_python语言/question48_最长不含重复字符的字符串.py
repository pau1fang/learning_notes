def solution(string):
    position = [-1 for _ in range(26)]
    current_length = 0
    max_length = 0

    for i in range(len(string)):
        if current_length == 0:
            current_length = 1
        else:
            if position[ord(string[i])-ord('a')] < 0 or (i-position[ord(string[i])-ord('a')])>current_length:
                current_length += 1
            else:
                current_length = i-position[ord(string[i])-ord('a')]
        position[ord(string[i]) - ord('a')] = i
        if current_length > max_length:
            max_length = current_length

    return max_length


print(solution("arabcacfr"))
