def f(x: int) -> str:
    if x >= 90:
        return "the grade of your score is A"
    if 80 <= x < 90:
        return "the grade of your score is B"
    if 70 <= x < 80:
        return "the grade of your score is C"
    if 60 <= x < 70:
        return "the grade of your score is D"
    if x < 60:
        return "the grade of your score is D"


def g() -> None:
    a = 89
    b = f(a)
    print(b)


if __name__ == "__main__":
    g()
