from demo_project.grade import f, g, h
from demo_project.massage import (
    MASSAGE_INVALID_INPUT,
    MASSAGE_INVALID_INPUT_RANGE,
    MASSAGE_MENE_INVALID,
    MASSAGE_NO_SCORE,
    MASSAGE_SCORES_CLEARED,
    MENU,
    PROMPT_MENU_CHOICE,
    PROMPT_MENU_SCORE,
    massage1,
    massage2,
)
from demo_project.states import get_average, get_highest, get_lowest


def add_score(a: list[int]) -> None:
    b = input(PROMPT_MENU_SCORE)
    try:
        c = h(b)
    except ValueError:
        print(MASSAGE_INVALID_INPUT)
        return
    if not g(c):
        print(MASSAGE_INVALID_INPUT_RANGE)
        return
    a.append(c)
    d = f(c)
    print(massage1(c, d))
    return


def summary_scores(a: list[int]) -> None:
    if not a:
        print(MASSAGE_NO_SCORE)
        return
    if a:
        print(
            massage2(
                count=len(a),
                average=get_average(a),
                highest=get_highest(a),
                lowest=get_lowest(a),
            )
        )
        return


def clear_scores(a: list[int]) -> None:
    a.clear()
    print(MASSAGE_SCORES_CLEARED)
    return


def k() -> None:
    a: list[int] = []
    while True:
        print(MENU)
        b = input(PROMPT_MENU_CHOICE)
        if b == "1":
            add_score(a)
        elif b == "2":
            summary_scores(a)
        elif b == "3":
            clear_scores(a)
        elif b == "4":
            break
        else:
            print(MASSAGE_MENE_INVALID)


if __name__ == "__main__":
    k()
