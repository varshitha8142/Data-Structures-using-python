""" Python Script to convert the infix expression into postfix form. """

# Write your code from here
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
PRIORITY = {'^':1,'*':2, '/':2,'+':3, '-':3 } # dictionary having priorities 

def infix_to_postfix(expression): 
    stack = [] # initially stack empty
    output = '' # initially output empty
    for ch in expression:
        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
            output+= ch
        elif ch=='(':  # else operators should be put in stack
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output 
expression = input('Enter infix expression')
print('infix expression: ',expression)
print('postfix expression: ',infix_to_postfix(expression))