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

def get_end_number():
    return random.randint(2, 111)

def get_question_gcd():
    num1 = get_number(1, get_end_number())
    num2 = get_number(1, get_end_number())
    question = f"{num1} {num2}"
    return question
