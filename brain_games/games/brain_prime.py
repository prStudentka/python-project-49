import random as rnd


__RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_MIN_NUM = 1
_MIN_NUM_PRIME = 2
_MAX_NUM = 120


def get_rule():
    return __RULE


def is_prime(number: int) -> bool:
    if number < _MIN_NUM_PRIME:
        return False
    end = int(number ** 0.5 + 1)
    for i in range(_MIN_NUM_PRIME, end):
        if number % i == 0:
            return False
    return True


def get_pair_QA():
    question = rnd.randint(_MIN_NUM, _MAX_NUM)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, answer)
