from DataStructures.mytree import BinaryTree
from DataStructures.Stack import Stack
import operator


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree("")
    pStack.push(eTree)
    current_tree = eTree
    for i in fplist:
        if i == "(":
            current_tree.insert_left('')
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in "+-*/)":
            current_tree.set_root_val(i)
            current_tree = pStack.pop()
        elif i in "+-*/":
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = pStack.pop()
        else:
            raise ValueError("Unknown Operator:" + i)
    return eTree

def evaluate(parse_tree):
    opers = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left), evaluate(right))
    else:
        return int(parse_tree.get_root_val())

def preorder(tree):
    if tree:
        print(tree.get_root_val(), end=' ')
        preorder(tree.get_left_child())
        preorder((tree.get_right_child()))

def postorder(tree):
    if tree!=None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val(), end=' ')

def printexp(tree):
    sVal = ""
    if tree:
        if tree.get_left_child():
            sVal = "(" + printexp(tree.get_left_child())
        sVal = sVal + str(tree.get_root_val())
        if tree.get_right_child():
            sVal = sVal + printexp(tree.get_right_child()) + ")"
    return sVal

if __name__ == '__main__':
    e = build_parse_tree("( 1 + ( 2 * ( 3 + 4 ) ) )")
    print(e.key)
    print(evaluate(e))
    print("***********")
    preorder(e)
    print()
    print("*************")
    postorder(e)
    print()
    print("************")
    print(printexp(e))