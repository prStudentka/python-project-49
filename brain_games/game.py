import prompt
from brain_games.games.answer import check_answer


def get_message(num, name='User'):
    message = ''
    match num:
        case 1: message = 'is wrong answer ;(. Correct answer was'
        case 2: message = 'Correct!'
        case 3: message = f'Congratulations, {name}!'
        case 4: message = f"Let's try again, {name}!"
        case _: message = "Wrong answer ;(. Let's try again"
    return message


def get_int(item: str):
    if not isinstance(item, str) or not item.isnumeric():
        return item
    return int(item)


def get_question(pair: tuple):
    return pair[0]


def get_answer(pair: tuple):
    return pair[1]


def play_game(request: tuple) -> list:
    question = get_question(request)
    print('Question:', question)
    answer = prompt.string('Your answer: ')
    brain_answer = get_answer(request)
    user_answer, correct = check_answer(answer, brain_answer)
    result = [brain_answer, user_answer, correct]
    return result


def greetings():
    print('Welcome to the Brain Games!')


def check_name(func):
    def inner():
        name = func()
        if len(name.strip()) == 0:
            name = 'User'
        return name
    return inner


@check_name
def get_name():
    name = prompt.string('May I have your name?')
    return name


def start_game(game):
    greetings()
    user_name = get_name()
    print(f'Hello, {user_name}!')
    print(game.get_rule())
    for _ in range(3):
        qa = game.get_pairQA()
        brain, answer, correct = play_game(qa)
        if not correct:
            print('Good joke!!!', get_message(0))
            break
        if brain == get_int(answer):
            print(get_message(2))
        else:
            print(f"'{answer}' {get_message(1)} '{brain}'.")
            print(get_message(4, user_name))
            break
    else:
        print(get_message(3, user_name))
