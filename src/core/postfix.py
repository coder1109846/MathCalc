operators = ['+','-','*','/']

def precedence(opr: str) -> int:
    if opr == '(':
        return 0
    elif opr == '+' or opr == '-':
        return 1
    elif opr == '*':
        return 2
    elif opr == '/':
        return 3

def postfix(expr:str) -> str:
    output = ""
    opr_arr = []
    modified_str = ""
    for char in range(len(expr)):
        if expr[char] == '-':
            if char == 0:
                modified_str += '~'
            elif expr[char-1] in operators:
                modified_str += '~'
            else :
                modified_str += expr[char]
        else :
            modified_str += expr[char]
    expr = modified_str
    for current in expr:
        if current.isdigit() or current == '.' or current == '~':
            if current == '~':
                output += '-'
            else:
                output += current
        elif current in operators:
            while len(opr_arr) > 0 and precedence(opr_arr[-1]) > precedence(current):
                output += opr_arr.pop()
            opr_arr.append(current)
            output += ' '
        elif current == '(':
            opr_arr.append(current)
        elif current == ')':
            while opr_arr[-1] != '(':
                output += ' ' + opr_arr.pop()
            opr_arr.pop()
    while len(opr_arr) > 0:
        output += ' ' + opr_arr.pop()
    return output