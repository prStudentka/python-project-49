import random as rnd


__RULE = 'What number is missing in the progression?'
__MIN_LENGTH = 5


def get_rule():
    return __RULE


def get_number(start, end):
    return rnd.randint(start, end)


def make_example():
    length = get_number(__MIN_LENGTH, 11)
    return {'num1': get_number(1, 30),
            'length': length,
            'diff': get_number(1, 11)}


def get_progression():
    item = make_example()
    return [i * item['num1'] + item['diff'] for i in range(item['length'])]


def get_pos(length):
    return get_number(0, length - 1)


def get_question(progression: list, pos) -> str:
    num = get_answer(progression, pos)
    return ' '.join(map(str, progression)).replace(str(num), '..', 1)


def get_answer(progression, pos):
    return progression[pos]


def make_QA(question, answer):
    return (question, answer)


def get_pairQA() -> list:
    progression = get_progression()
    pos = get_pos(len(progression))
    question = get_question(progression, pos)
    answer = get_answer(progression, pos)
    pair = make_QA(question, answer)
    return pair
