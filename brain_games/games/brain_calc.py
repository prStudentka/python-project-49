import random as rnd
from operator import sub, mul, add


__RULE = 'What is the result of the expression?'
_MIN_NUM = 1
_MAX_NUM = 10


def get_rule():
    return __RULE


def get_pair_QA():
    num1 = rnd.randint(_MIN_NUM, _MAX_NUM)
    operation = rnd.choice(['+', '-', '*'])
    num2 = rnd.randint(_MIN_NUM, _MAX_NUM)
    question = f'{num1} {operation} {num2}'
    dict_operation = {'+': add,
                      '-': sub,
                      '*': mul}
    answer = dict_operation.get(operation)(num1, num2)
    return (question, str(answer))
