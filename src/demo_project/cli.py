from demo_project.grade import f, g, h
from demo_project.massage import (
    MASSAGE_GOODBYE,
    MASSAGE_INVALID_INPUT,
    MASSAGE_INVALID_INPUT_RANGE,
    PROMPT_SCORE,
    massage1,
)


def k() -> bool:
    a = input(PROMPT_SCORE)
    if a == "q":
        print(MASSAGE_GOODBYE)
        return True
    try:
        b = h(a)
    except ValueError:
        print(MASSAGE_INVALID_INPUT)
        return False
    if not g(b):
        print(MASSAGE_INVALID_INPUT_RANGE)
        return False
    c = f(b)
    print(massage1(b, c))
    return False


def d() -> None:
    while True:
        a = k()
        if a:
            break
