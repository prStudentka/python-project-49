import random as rnd
from math import gcd


__RULE = 'Find the greatest common divisor of given numbers.'
_MIN_NUM = 1
_MAX_NUM = 120


def get_rule():
    return __RULE


def get_pair_QA():    
    item1 = rnd.randint(_MIN_NUM, _MAX_NUM)
    item2 = rnd.randint(_MIN_NUM, _MAX_NUM)
    question = f"{item1} {item2}"
    answer = gcd(item1, item2)
    return (question, str(answer)))
