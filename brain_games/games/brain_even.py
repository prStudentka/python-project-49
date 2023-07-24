import random as rnd


__RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
_MIN_NUM = 1
_MAX_NUM = 120


def get_rule():
    return __RULE


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_pairQA():
    question = rnd.randint(_MIN_NUM, _MAX_NUM)
    answer = 'yes' if is_even(question) else 'no'
    return (question, answer)
