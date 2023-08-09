import random as rnd


__RULE = 'What number is missing in the progression?'
__MIN_LENGTH = 5
__MAX_LENGTH = 11
_MIN_NUM, _MAX_NUM = 1, 16
_MIN_STEP, _MAX_STEP = 1, 11


def get_rule():
    return __RULE


def generate_progression(num, step, len):
    return [i * num + step
                for i in range(len)]


def get_str_progression(progressin, pos):
    progress_str = [str(item) if index != pos else '..'
                    for index, item in enumerate(progression)]
    return ' '.join(map(str, progress_str))


def get_pairQA():
    length = rnd.randint(__MIN_LENGTH, __MAX_LENGTH)
    num1 = rnd.randint(_MIN_NUM, __MAX_NUM)
    step = rnd.randint(_MIN_STEP, _MAX_STEP)
    pos = rnd.randint(0, length - 1)
    progression = generate_progression(num1, step, length)   
    answer = progression[pos] 
    question = get_str_progression(progression, pos)
    return (question, answer)
