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


def get_pairQA():
    item = make_example()
    progression = [i * item['num1'] + item['diff']
                   for i in range(item['length'])]
    pos = get_number(0, item['length'] - 1)
    answer = progression[pos]
    question = ' '.join(map(str, progression)).replace(str(answer), '..', 1)
    return (question, answer)
