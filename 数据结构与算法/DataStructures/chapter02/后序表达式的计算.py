from DataStructures.Stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "+-*/":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        else:
            operandStack.push(int(token))
    return operandStack.pop()

# print("43" in "0123456789")
def doMath(op, op1, op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    elif op == "-":
        return op1-op2

p = postfixEval("4 5 6 * +")
print(p)
print(postfixEval("7 8 + 3 2 + /"))
