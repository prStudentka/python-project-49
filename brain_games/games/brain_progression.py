import random as rnd


__RULE = 'What number is missing in the progression?'
__MIN_LENGTH = 5
__MAX_LENGTH = 11
_MIN_NUM = 1


def get_rule():
    return __RULE


def get_pairQA():
    length = rnd.randint(__MIN_LENGTH, __MAX_LENGTH)
    num1 = rnd.randint(_MIN_NUM, __MAX_LENGTH + __MIN_LENGTH)
    diff = rnd.randint(_MIN_NUM, __MAX_LENGTH)
    progression = [i * num1 + diff
                   for i in range(length)]
    pos = rnd.randint(0, length - 1)
    answer = progression[pos]
    progress_str = [str(item) if index != pos else '...'
                    for index, item in enumerate(progression)]
    question = ' '.join(map(str, progress_str))
    return (question, answer)
