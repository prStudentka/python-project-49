import prompt


__ROUNDS_COUNT = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    print(game.get_rule())
    for _ in range(__ROUNDS_COUNT):
        question, brain_answer = game.get_pair_QA()
        print('Question:', question)
        answer = prompt.string('Your answer: ').lower().strip()
        if brain_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ",
                  f"Correct answer was '{brain_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
