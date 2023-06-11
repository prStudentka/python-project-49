import prompt
from brain_games.games.rule import rule_even, rule_calc, rule_gcd, rule_progression
from brain_games.games.question import get_question_even, get_question_calc, get_question_gcd, get_question_progression
from brain_games.games.answer import check_answer_even, check_answer_calc


def get_message(num, name="gamer"):
    message = ""
    match num:
        case 1: message = f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"
        case 2: message = "Correct!"
        case 3: message = f"Congratulations, {name}!"
        case 4: message = f"Let's try again, {name}!"
        case 5: message = "is wrong answer ;(. Correct answer was"
        case _: message = "Wrong answer ;(. Let's try again"
    return message


def is_even(number: str) -> bool:
    return int(number) % 2 == 0


def common_divisor(numbers: str):
    num1, num2 = numbers.split()
    max_num = max(int(num1), int(num2)) + 1
    min_num = min(int(num1), int(num2))
    result = 0
    if (max_num - 1) % min_num == 0:
        result = min_num
    else:
        middle = min_num // 2
        for i in range(1, middle):
            if int(num1) % i == 0 and int(num2) % i == 0:
                result = i
    return result


def get_int(item: str):
    return item if not item.isnumeric() else int(item)


def find_num_progression(numbers: str):
    num_list = list(map(get_int, numbers.split()))
    diff = num_list[1] - num_list[0] if not isinstance(num_list[0] * num_list[1], str) else num_list[-1] - num_list[-2]
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
    print('Question: ', question)
    return question


def game(config: dict, func) -> list:
    question = print_question(config["question"])
    answer = prompt.string("Your answer: ")
    user_answer, correct = config["answer"](answer)
    result = [func(question), user_answer, correct]
    return result


def game_even(config: dict, name: str):
    count_success = 0
    while True or count_success <= 3:
        brain_answer, answer, correct_answer = game(config, is_even)
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


def game_calc(config: dict, name):
    count_success = 0
    while True or count_success <= 3:
        brain_answer, answer, correct_answer = game(config, eval)
        if correct_answer:
            if (brain_answer == int(answer)):
                count_success += 1
                print(get_message(2))
                if count_success == 3:
                    print(get_message(count_success, name))
                    break
            else:
                print(f"'{answer}' {get_message(5)} '{brain_answer}'.") 
                print(get_message(4, name))
                break
        else:
            print("Good joke!!! ", get_message(0))
            break


def game_gcd(config, name):
    count_success = 0
    while True or count_success <= 3:
        brain_answer, answer, correct_answer = game(config, common_divisor)
        if correct_answer:
            if (brain_answer == int(answer)):
                count_success += 1
                print(get_message(2))
                if count_success == 3:
                    print(get_message(count_success, name))
                    break
            else:
                print(f"'{answer}' {get_message(5)} '{brain_answer}'.") 
                print(get_message(4, name))
                break
        else:
            print("Good joke!!! ", get_message(0))
            break


def game_progression(config, name):
    count_success = 0
    while True or count_success <= 3:
        brain_answer, answer, correct_answer = game(config, find_num_progression)
        if correct_answer:
            if (brain_answer == int(answer)):
                count_success += 1
                print(get_message(2))
                if count_success == 3:
                    print(get_message(count_success, name))
                    break
            else:
                print(f"'{answer}' {get_message(5)} '{brain_answer}'.") 
                print(get_message(4, name))
                break
        else:
            print("Good joke!!! ", get_message(0))
            break


def welcome_and_name() -> str:
    print("\tWelcome to the Brain Games!")
    name = prompt.string("\tMay I have your name? ")
    print(f" Hello, {name}!")
    return name
 

def get_game(game_name: str):
   game_dict = {}
   if game_name == "even":
       game_dict[game_name] = game_even
       game_dict["rule"] = rule_even
       game_dict["question"] = get_question_even
       game_dict["answer"] = check_answer_even
   elif game_name == "calc":
       game_dict[game_name] = game_calc
       game_dict["rule"] = rule_calc
       game_dict["question"] = get_question_calc
       game_dict["answer"] = check_answer_calc
   elif game_name == "gcd":
       game_dict[game_name] = game_gcd
       game_dict["rule"] = rule_gcd
       game_dict["question"] = get_question_gcd
       game_dict["answer"] = check_answer_calc
   elif game_name == "progression":
       game_dict[game_name] = game_progression
       game_dict["rule"] = rule_progression
       game_dict["question"] = get_question_progression
       game_dict["answer"] = check_answer_calc
   return game_dict


def start_game(game: str):
    user_name = welcome_and_name()
    begin = get_game(game)
    begin["rule"]()
    begin[game](begin, user_name)
