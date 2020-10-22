from DataStructures import Stack


def parChecker(symbolString):
    s = Stack.Stack()
    balanced = True
    index = 0
    while index<len(symbolString) and balanced:
        if symbolString[index] == "(":
            s.push("(")
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

ss = "((()))"
print(parChecker(ss))
