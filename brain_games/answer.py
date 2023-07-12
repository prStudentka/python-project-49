__ANSWER_LIST = ['yes', 'no']
__correct = ()


def has_answer(text: str) -> bool:
    try:
        if len(text.strip()) == 0:
            raise Exception
    except ValueError:
        print('raise Exception: No user answer')
    finally:
        return True


def check_answer(user_answer, brain_answer):
    if isinstance(brain_answer, str):
        return check_answer_str(user_answer)
    return check_answer_int(user_answer)


def check_answer_str(answer: str) -> list:
    if not has_answer(answer):
        return []
    user_answer = answer.lower().strip()
    __correct = (user_answer in __ANSWER_LIST,)
    return user_answer, __correct[0]


def check_answer_int(answer: str) -> list:
    if not has_answer(answer):
        return []
    __correct = (answer.isnumeric(),)
    return int(answer), __correct[0]
