import random as rnd


__RULE = 'What is the result of the expression?'


def get_rule():
    return __RULE


def check_nums(func):
    old_act = ''

    def inner():
        nonlocal old_act
        val = func()
        while old_act == val['act']:
            val['act'] = get_act()
        old_act = val['act']
        if val['act'] == '-':
            if val['num1'] < val['num2']:
                tmp = val['num1']
                val['num1'] = val['num2']
                val['num2'] = tmp
        if val['act'] == '*':
            if val['num2'] > 10:
                val['num2'] //= 10
        return val
    return inner


def get_number():
    return rnd.randint(1, 120)


def get_act():
    return rnd.choice(['+', '-', '*'])


@check_nums
def make_example():
    return {'num1': get_number(),
            'act': get_act(),
            'num2': get_number()}


def get_question():
    item = make_example()
    return f"{item['num1']} {item['act']} {item['num2']}"


def get_answer(question):
    return int(eval(question))


def make_QA(question, answer):
    return (question, answer)


def get_pairQA() -> list:
    question = get_question()
    answer = get_answer(question)
    pair = make_QA(question, answer)
    return pair
