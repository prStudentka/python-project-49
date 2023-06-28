import random as rnd


__RULE = 'Find the greatest common divisor of given numbers.'


def get_rule():
    return __RULE


def common_divisor(numbers: str):
    num1, num2 = numbers.split()
    max_num = max(int(num1), int(num2)) + 1
    min_num = min(int(num1), int(num2))
    result = 0
    if (max_num - 1) % min_num == 0:
        result = min_num
    else:
        middle = min_num // 2 + 1
        for i in range(1, middle):
            if int(num1) % i == 0 and int(num2) % i == 0:
                result = i
    return result


def check_nums(func):
    def inner():
        val = func()
        while val['num1'] == val['num2']:
            val['num1'] = get_number()
        return val
    return inner


def get_number():
    return rnd.randint(1, 120)


@check_nums
def make_example():
    return {'num1': get_number(),
            'num2': get_number()}


def get_question():
    item = make_example()
    return f"{item['num1']} {item['num2']}"


def get_answer(question):
    return common_divisor(question)


def make_QA(question, answer):
    return (question, answer)


def get_pairQA() -> list:
    question = get_question()
    answer = get_answer(question)
    pair = make_QA(question, answer)
    return pair


__all__ = ['get_pairQA']
