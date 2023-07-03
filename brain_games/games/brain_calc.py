import random as rnd
from operator import sub, mul, add


__RULE = 'What is the result of the expression?'


def get_rule():
    return __RULE


def make_example():
    return {'num1': rnd.randint(1, 20),
            'act': rnd.choice(['+', '-', '*']),
            'num2': rnd.randint(0, 10)}


def get_pairQA():
    item = make_example()
    question = f"{item['num1']} {item['act']} {item['num2']}"
    dict_act = {'+': add,
                '-': sub,
                '*': mul}
    answer = dict_act.get(item['act'])(item['num1'], item['num2'])
    return (question, answer)
