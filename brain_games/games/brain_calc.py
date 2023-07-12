import random as rnd
from operator import sub, mul, add


__RULE = 'What is the result of the expression?'


def get_rule():
    return __RULE


def get_pairQA():
    num1 = rnd.randint(1, 20)
    operation = rnd.choice(['+', '-', '*'])
    num2 = rnd.randint(0, 10)
    if operation == '-' and num2 > num1:
        num1, num2 = num2, num1
    question = f'{num1} {operation} {num2}'
    dict_operation = {'+': add,
                      '-': sub,
                      '*': mul}
    answer = dict_operation.get(operation)(num1, num2)
    return (question, answer)
