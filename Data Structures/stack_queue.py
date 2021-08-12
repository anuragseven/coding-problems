# create a stack using python list
class Stack:
    def __init__(self):
        self.__values = []

    def push(self, value):
        self.__values.append(value)

    def pop(self):
        return self.__values.pop()

    def peek(self):
        return self.__values[len(self.__values) - 1]

    def size(self):
        return len(self.__values)

    def _getValueByIndex(self, index):
        return self.__values[index]

    def __iter__(self):
        return StackIterator(self)


# a stack iterator class
class StackIterator:
    def __init__(self, stack):
        self.__stack = stack
        self.__index = stack.size() - 1

    def __next__(self):
        if self.__index < 0:
            raise StopIteration
        currentIndex = self.__index
        self.__index -= 1
        return self.__stack._getValueByIndex(currentIndex)


# convert infix to postfix using stack

def infixToPostfix(expr: str):
    stack = Stack()
    precedence = {
        '*': 1,
        '/': 1,
        '%': 1,
        '+': 0,
        '-': 0

    }
    result = ''
    operands = [str(i) for i in range(10)]
    for c in expr:
        if c in operands:
            result += c
        elif c == "(":
            stack.push(c)
        elif c == ')':
            while stack.size() != 0 and stack.peek() != '(':
                result += stack.pop()
            if stack.size() != 0:
                stack.pop()
        elif c in precedence:
            if stack.size() == 0 or stack.peek() == '(':
                stack.push(c)
            elif precedence[stack.peek()] < precedence[c]:
                stack.push(c)
            else:
                result += stack.pop()
                stack.push(c)

        else:
            raise Exception("Invalid expression provided")
    while stack.size() != 0:
        result += stack.pop()

    return result


# Postfix evaluation :

def postfixEvaluation(expr: str):
    stack = Stack()
    operators = ['*', '/', '+', '-', '%']
    operands = [str(i) for i in range(10)]
    for c in expr:
        if c in operands:
            stack.push(c)
        elif c in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            result = 0
            if c is '*':
                result = float(op1) * float(op2)
            elif c is '/':
                result = float(op1) / float(op2)
            elif c is '%':
                result = float(op1) % float(op2)
            elif c is '+':
                result = float(op1) + float(op2)
            elif c is '-':
                result = float(op1) - float(op2)
            stack.push(result)
        else:
            raise Exception("Invalid expression provided")
    return stack.pop()


# parenthesis matching:

def matchParenthesis(expr: str):
    stack = Stack()
    brackets = ['{', '}', ')', '(', ']', '[']
    for c in expr:
        if c in ['(', '{', '[']:
            stack.push(c)
        elif c is ')':
            while stack.size() != 0 and stack.peek() != '(':
                top = stack.peek()
                if top in brackets:
                    return False
                stack.pop()
            stack.pop()

        elif c is '}':
            while stack.size() != 0 and stack.peek() != '{':
                top = stack.peek()
                if top in brackets:
                    return False
                stack.pop()
            stack.pop()

        elif c is ']':
            while stack.size() != 0 and stack.peek() != '[':
                top = stack.peek()
                if top in brackets:
                    return False
                stack.pop()
            stack.pop()

    return stack.size() == 0



