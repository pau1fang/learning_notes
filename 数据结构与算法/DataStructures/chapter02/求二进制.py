from DataStructures.Stack import Stack


def dividdeBy2(decNumber):
    s = Stack()
    while decNumber > 0:
        decNumber, m = divmod(decNumber, 2)
        s.push(m)
    # if decNumber == 1:
    #     s.push(decNumber)
    num = ''
    while not s.isEmpty():
        num += str(s.pop())
    return num


d = dividdeBy2(1024)
print(d)
