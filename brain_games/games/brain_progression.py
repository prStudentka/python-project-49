import random as rnd


__RULE = 'What number is missing in the progression?'
__MIN_LENGTH = 5


def get_rule():
    return __RULE


def get_pairQA():
    length = rnd.randint(__MIN_LENGTH, 11)
    num1 = rnd.randint(1, 15)
    diff = rnd.randint(1, 11)
    progression = [i * num1 + diff
                   for i in range(length)]
    pos = rnd.randint(0, length - 1)
    answer = progression[pos]
    question = ' '.join(map(str, progression)).replace(str(answer), '..', 1)
    return (question, answer)
