from postfix import *

def evaluate(pfix: str):
    stack = []
    for current in pfix.split(' '):
        if current.replace('.', '', 1).isdigit() and not float(current).is_integer():
            stack.append(float(current))
        elif current.isdigit():
            stack.append(int(current))
        elif current.startswith('-') and current[1:].isdigit():
            stack.append(int(current))
        elif current.translate(current.maketrans("-.",'11')).isdigit() and not float(current).is_integer():
            stack.append(float(current))
        elif current in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if current == '+':
                res = operand1 + operand2
                stack.append(res)
            elif current == '-':
                res = operand1 - operand2
                stack.append(res)
            elif current == '*':
                res = operand1 * operand2
                stack.append(res)
            elif current == '/':
                res = operand1/operand2
                stack.append(res)
    return stack[-1]

print(evaluate(postfix("1.2+-1.3")))