import random as rnd


__RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_MIN_NUM = 1
_MAX_NUM = 120
_LIMIT_OVER_DOZEN = 11
_LIMIT = 10


def get_rule():
    return __RULE


def is_prime(number: int) -> bool:
    if number == 1 or not number:
        return False
    end = number // 2 + 1 if number <= _LIMIT else _LIMIT_OVER_DOZEN
    for i in range(2, end):
        if number % i == 0:
            return False
    return True


def get_pairQA():
    question = rnd.randint(_MIN_NUM, _MAX_NUM)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, answer)
