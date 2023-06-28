import random as rnd


__RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_rule():
    return __RULE


def is_prime(number: str) -> bool:
    if int(number) == 1:
        return False
    length = int(number) // 2 + 1 if int(number) <= 10 else 11
    for i in range(2, length):
        if int(number) % i == 0:
            return False
    return True


def check_equal(func):
    old_num = [0]

    def inner():
        nonlocal old_num
        val = list(func())
        if old_num == val:
            val[0] += 1
        old_num = val
        return val[0]
    return inner


@check_equal
def get_question():
    yield rnd.randint(1, 120)


def get_answer(question):
    return 'yes' if is_prime(question) else 'no'


def make_QA(question, answer):
    return (question, answer)


def get_pairQA() -> list:
    question = get_question()
    answer = get_answer(question)
    pair = make_QA(question, answer)
    return pair


__all__ = ['get_pairQA']
