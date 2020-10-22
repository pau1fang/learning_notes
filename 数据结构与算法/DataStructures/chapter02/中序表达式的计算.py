from DataStructures.Stack import Stack

"""解题思路：
    分四种情况讨论：
    1. 若是运算符，先观察运算符栈是否为空，若为空直接放入，不为空则对比优先级，若栈顶的运算符优先级不低于
    当前运算符，拿出栈顶运算符进行运算，直到栈顶运算符优先级低于当前运算符为止，压入当前运算符
    2. 若是括号左端，压入栈顶
    3. 若是括号右端，依次从运算符栈取出运算符进行运算，将运算后的数压入数据栈，直到运算符栈取出的是括号左端为止
    4. 若是数字，压入数字栈
    需要注意的一点是，计算完成后要保证运算符栈为空
"""
def solution(expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    expr = expr.split()
    print(expr)
    num_stack = Stack()
    op_stack = Stack()
    for i in expr:
        if i in "+-*/":
            while (not op_stack.isEmpty()) and (prec[op_stack.peek()] >= prec[i]):
                op = op_stack.pop()
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                res = doMath(op, num1, num2)
                num_stack.push(res)
            op_stack.push(i)
        elif i == "(":
            op_stack.push(i)
        elif i == ")":
            topToken = op_stack.pop()
            while topToken != "(":
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                res = doMath(topToken, num1, num2)
                num_stack.push(res)
                topToken = op_stack.pop()
        else:
            num_stack.push(int(i))

    while (not op_stack.isEmpty()):
        op_ = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        res = doMath(op_, num1, num2)
        num_stack.push(res)
    print(num_stack.items)

    return num_stack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2


expr = "1 + ( 2 + 5 ) * 3"

s = solution(expr)
print(s)
