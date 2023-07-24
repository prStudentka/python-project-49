import random as rnd
from math import gcd


__RULE = 'Find the greatest common divisor of given numbers.'
_MIN_NUM = 1
_MAX_NUM = 120


def get_rule():
    return __RULE


def make_example():
    return {'num1': rnd.randint(_MIN_NUM, _MAX_NUM),
            'num2': rnd.randint(_MIN_NUM, _MAX_NUM)}


def get_pairQA():
    item = make_example()
    question = f"{item['num1']} {item['num2']}"
    answer = gcd(item['num1'], item['num2'])
    return (question, answer)
