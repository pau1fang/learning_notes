from DataStructures.mydeque import Deque

def palchecker(aString):
    chardeque = Deque()

    for i in aString:
        chardeque.addRear(i)

    stillEqual = True
    while chardeque.size()>1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first!=last:
            stillEqual = False
    return stillEqual

p = palchecker("aba")
print(p)