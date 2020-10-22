from DataStructures.Stack import Stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber>0:
        decNumber, rem = divmod(decNumber, base)
        remstack.push(rem)
    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString


b = baseConverter(31,16)
print(b)
