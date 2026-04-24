from demo_project.grade import f, g, h
from demo_project.massage import (
    MASSAGE_GOODBYE,
    MASSAGE_INVALID_INPUT,
    MASSAGE_INVALID_INPUT_RANGE,
    PROMPT_SCORE,
    massage2,
)
from demo_project.states import average1, highest1, lowest1


def k(scores: list[int]) -> bool:
    a = input(PROMPT_SCORE)
    if a == "q":
        print(MASSAGE_GOODBYE)
        if scores:
            print(
                massage2(
                    count=len(scores),
                    average=average1(scores),
                    highest=highest1(scores),
                    lowest=lowest1(scores),
                )
            )
        return True
    try:
        b = h(a)
    except ValueError:
        print(MASSAGE_INVALID_INPUT)
        return False
    if not g(b):
        print(MASSAGE_INVALID_INPUT_RANGE)
        return False
    scores.append(b)
    c = f(b)
    print(c)
    return False


def d() -> None:
    a: list[int] = []
    while True:
        b = k(a)
        if b:
            break


if __name__ == "__main__":
    d()
