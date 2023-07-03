import prompt
from brain_games.games.answer import check_answer


def get_int(item: str):
    if not isinstance(item, str) or not item.isnumeric():
        return item
    return int(item)


def greetings():
    print('Welcome to the Brain Games!')


def start_game(game):
    greetings()
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    print(game.get_rule())
    for _ in range(3):
        question, brain_answer = game.get_pairQA()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        answer, correct = check_answer(user_answer, brain_answer)
        if not correct:
            print("Good joke!!! Wrong answer ;(. Let's try again")
            break
        if brain_answer == get_int(answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{brain_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
