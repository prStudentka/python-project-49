import random as rnd


__RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_rule():
    return __RULE


def is_even(number: str) -> bool:
    return int(number) % 2 == 0


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
    return 'yes' if is_even(question) else 'no'


def make_QA(question, answer):
    return (question, answer)


def get_pairQA() -> list:
    question = get_question()
    answer = get_answer(question)
    pair = make_QA(question, answer)
    return pair


__all__ = ['get_pairQA']
