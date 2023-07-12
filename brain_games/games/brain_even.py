import random as rnd


__RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
_MIN_NUM = 1
_MAX_NUM = 120


def get_rule():
    return __RULE


def is_even(number: str) -> bool:
    return int(number) % 2 == 0


def get_pairQA():
    question = rnd.randint(1, 120)
    answer = 'yes' if is_even(question) else 'no'
    return (question, answer)
