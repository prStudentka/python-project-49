import prompt
import random


__answer_list = ['yes', 'no']


def get_message(num, name="gamer"):
    message = ""
    match num:
        case 1: message = f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"
        case 2: message = "Correct!"
        case 3: message = f"Congratulations, {name}!"
        case _: message = "Wrong answer ;(. Let's try again"
    return message


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_transform_answer(answer: str) -> bool:
    return True if answer == __answer_list[0] else False


def is_correct_answer(answer: str) -> bool:
    if answer in __answer_list:
        return True
    return False


def game() -> list:
    question = random.randint(1, 120)
    print('Question: ', question)
    answer = prompt.string("Your answer: ")
    answer = answer.lower()
    correct = is_correct_answer(answer)
    if correct:
        answer = get_transform_answer(answer)
    return [is_even(question), answer, correct]


def start_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f" Hello, {name}!")
    print(" - " * 10)
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    print(" - " * 10)
    print()
    count_success = 0
    while True or count_success <= 3:
        brain_answer, answer, correct_answer = game()
        if correct_answer:
            if (brain_answer and answer) or (not brain_answer and not answer):
                count_success += 1
                print(get_message(2))
                if count_success == 3:
                    print(get_message(count_success, name))
                    break
            else:
                if answer:
                    print(get_message(1, name))
                    break
                else:
                    print(get_message(0))
                    break
        else:
            print("Good joke!!! ", get_message(0))
            break
