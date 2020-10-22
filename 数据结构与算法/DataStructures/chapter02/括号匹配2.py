from DataStructures.Stack import Stack


def parChecker(symbolString):
    balanced = True
    s = Stack()
    index = 0
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False


def matches(open, close):
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)


ss = "(){}{()}"
s = parChecker(ss)
print(s)
