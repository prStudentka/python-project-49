__ANSWER_LIST = ['yes', 'no']
__correct = ()


def is_correct_answer(answer: str) -> bool:
    if answer in __ANSWER_LIST:
        return True
    return False


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
    __correct = (is_correct_answer(user_answer),)
    return user_answer, __correct[0]


def check_answer_int(answer: str) -> list:
    if not has_answer(answer):
        return []
    if answer.isnumeric():
        __correct = (True,)
    else:
        __correct = (False,)
    return answer, __correct[0]


__all__ = ['check_answer']
