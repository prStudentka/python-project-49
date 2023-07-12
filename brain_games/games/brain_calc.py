import random as rnd
from operator import sub, mul, add


__RULE = 'What is the result of the expression?'
_MIN_NUM = 1
_MAX_NUM = 10


def get_rule():
    return __RULE


def get_pairQA():
    num1 = rnd.randint(_MIN_NUM, 2 * _MAX_NUM)
    operation = rnd.choice(['+', '-', '*'])
    num2 = rnd.randint(_MIN_NUM - 1, _MAX_NUM)
    if operation == '-' and num2 > num1:
        num1, num2 = num2, num1
    question = f'{num1} {operation} {num2}'
    dict_operation = {'+': add,
                      '-': sub,
                      '*': mul}
    answer = dict_operation.get(operation)(num1, num2)
    return (question, answer)
