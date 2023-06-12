import prompt
from brain_games.games.rule import rule_even, rule_calc, rule_gcd, rule_progression, rule_prime
from brain_games.games.question import get_question_even, get_question_calc, get_question_gcd, get_question_progression
from brain_games.games.answer import check_answer_even, check_answer_calc


def get_message(num, name="gamer"):
    message = ""
    match num:
        case 1: message = "'yes' is wrong answer ;(. Correct answer was 'no'."
        case 2: message = "Correct!"
        case 3: message = f"Congratulations, {name}!"
        case 4: message = f"Let's try again, {name}!"
        case 5: message = "is wrong answer ;(. Correct answer was"
        case _: message = "Wrong answer ;(. Let's try again"
    return message


def config_game(config: dict, user_name: str):
    def inner():
        return [config, user_name]
    return inner


def is_even(number: str) -> bool:
    return int(number) % 2 == 0


def is_prime(number: str) -> bool:
    if int(number) == 1:
        return True
    else:
        length = int(number) // 2 + 1 if int(number) <= 10 else 11
        for i in range(2, length):
            if int(number) % i == 0:
                return False
    return True


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


def get_int(item: str):
    return item if not isinstance(item, str) or not item.isnumeric() else int(item)


def find_num_progression(numbers: str):
    num_list = list(map(get_int, numbers.split()))
    if not isinstance(num_list[0] * num_list[1], str):
        diff = num_list[1] - num_list[0]
    else:
        diff = num_list[-1] - num_list[-2]
    result = 0
    if not str(num_list[0]).isnumeric():
        result = num_list[1] - diff
    else:
        for i in num_list:
            if isinstance(i, str):
                break
            result = i
        result += diff
    return result


def print_question(func):
    question = func()
    print('Question:', question)
    return question


def game(request: dict) -> list:
    question = print_question(request["question"])
    answer = prompt.string("Your answer: ")
    user_answer, correct = request["answer"](answer)
    brain_answer = request["func"](question)
    result = [brain_answer, user_answer, correct]
    return result


def play_game(config):
    count_success = 0
    game_dict, user_name = config()
    answer_yes = game_dict["yes"]
    while count_success <= 3:
        brain_answer, answer, correct_answer = game(game_dict)
        if correct_answer:
            if (brain_answer == get_int(answer)):
                count_success += 1
                print(get_message(2))
                if count_success == 3:
                    print(get_message(count_success, user_name))
                    break
            else:
                if not answer_yes:
                    print(f"'{answer}' {get_message(5)} '{brain_answer}'.")
                    print(get_message(4, user_name))
                    break
                else:
                    if answer:
                        print(f"{get_message(1)}\n{get_message(4, user_name)}")
                        break
                    else:
                        print(f"'no' {get_message(5)} 'yes'.\n{get_message(4, user_name)}")
                        break
        else:
            print("Good joke!!! ", get_message(0))
            break


def greetings() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    return name


def get_game(game_name: str):
    keys = ['yes', 'rule', 'question', 'answer', 'func']
    if game_name == "even":
        values = [
                True, 
                rule_even, 
                get_question_even, 
                check_answer_even, 
                is_even
                ]
    elif game_name == "calc":
        values = [
                False, 
                rule_calc, 
                get_question_calc, 
                check_answer_calc, 
                eval
                ]
    elif game_name == "gcd":
        values = [
                False, 
                rule_gcd, 
                get_question_gcd, 
                check_answer_calc, 
                common_divisor
                ]
    elif game_name == "progression":
        values = [
                False, 
                rule_progression, 
                get_question_progression, 
                check_answer_calc, 
                find_num_progression
                ]
    else:
        values = [
                True, 
                rule_prime, 
                get_question_even, 
                check_answer_even, 
                is_prime
                ]
    return dict(zip(keys, values))


def start_game(game: str):
    user_name = greetings()
    begin = get_game(game)
    begin["rule"]()
    play_game(config_game(begin, user_name))
