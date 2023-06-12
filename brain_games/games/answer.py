__ANSWER_LIST = ['yes', 'no']
__correct = ()


def get_transform_answer(answer: str) -> bool:
    return True if answer == __ANSWER_LIST[0] else False


def is_correct_answer(answer: str) -> bool:
    if answer in __ANSWER_LIST:
        return True
    return False


def has_answer(text: str) -> bool:
    if len(text.strip()) > 0:
        return True
    raise Exception("No user answer")
    return False


def check_answer_even(answer: str) -> list:
    if not has_answer(answer):
       return []
    user_answer = answer.lower()
    __correct = (is_correct_answer(user_answer),)
    if __correct[0]:
        user_answer = get_transform_answer(user_answer)
    return user_answer, __correct[0]


def check_answer_calc(answer: str) -> list:
    if not has_answer(answer):
       return []
    if answer.isnumeric():
        __correct = (True,)
    else:
        __correct = (False,)
    return answer, __correct[0]
