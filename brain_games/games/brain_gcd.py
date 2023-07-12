import random as rnd
from math import gcd


__RULE = 'Find the greatest common divisor of given numbers.'
_MIN_NUM = 1
_MAX_NUM = 120


def get_rule():
    return __RULE


def check_nums(func):
    def inner():
        val = func()
        while val['num1'] == val['num2']:
            val['num1'] = get_number()
        return val
    return inner


def get_number():
    return rnd.randint(_MIN_NUM, _MAX_NUM)


@check_nums
def make_example():
    return {'num1': get_number(),
            'num2': get_number()}


def get_pairQA():
    item = make_example()
    question = f"{item['num1']} {item['num2']}"
    answer = gcd(item['num1'], item['num2'])
    return (question, answer)
