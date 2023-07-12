import random as rnd


__RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_MIN_NUM = 1
_MAX_NUM = 120


def get_rule():
    return __RULE


def is_prime(number: str) -> bool:
    if int(number) == 1 or not int(number):
        return False
    length = int(number) // 2 + 1 if int(number) <= 10 else 11
    for i in range(2, length):
        if int(number) % i == 0:
            return False
    return True


def get_pairQA():
    question = rnd.randint(_MIN_NUM, _MAX_NUM)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, answer)
