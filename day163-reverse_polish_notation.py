"""
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. 
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

OPS = ('+', '-', '/', '*')

def eval_polish_notation(expression: list):
    if len(expression) < 3:
        raise ValueError("Improper input. Must have at least 3 elements")

    stack = expression[:2]
    
    for elem in expression[2:]:
        if elem == "+":
            val = stack.pop() + stack.pop()
            stack.append(val)

        elif elem == "-":
            val = stack.pop() - stack.pop()
            stack.append(val)

        elif elem == "*":
            val = stack.pop() * stack.pop()
            stack.append(val)

        elif elem == "/":
            val = stack.pop() / stack.pop()
            stack.append(val)

        else:
            stack.append(elem)
            # must be a number

    #print(stack)
    if len(stack) != 1:
        raise ValueError("Improper input.")
    return stack[0]


# TEST CASES
assert eval_polish_notation([15, 7, 1, 1, '+', '-', '/', 
                             3, '*', 2, 1, 1, '+', '+', '-']) == 5




