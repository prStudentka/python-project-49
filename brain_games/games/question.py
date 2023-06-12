import random


def get_number(begin, end):
    num = []
    for i in range(6):
       num.append(random.randint(begin, end))
    number = random.choice(list(set(num)))
    return number


def get_question_even():
    return get_number(1, 120)


def get_question_calc():
    act = random.choice(["+", "-", "*"])
    num1 = get_number(1, 20)
    num2 = get_number(0, 11)
    if act == "-" and num1 < num2:
        num2 = get_number(0, num1)
    question = f"{num1} {act} {num2}"
    return question


def get_question_gcd():
    num1 = get_number(1, get_question_even())
    num2 = get_number(1, get_number(2, num1 + 2))
    question = f"{num1} {num2}"
    return question


def get_question_progression():
    length = get_number(5, 11)
    pos = get_number(0, length)
    diff = get_number(1, 11)
    num = get_number(0, 30)
    result = str(num) if pos > 0 else ".."
    for i in range(1, length + 1):
       num += diff
       if pos == i:
           result += " .."
       else:
           result += f" {num}"
    return result
