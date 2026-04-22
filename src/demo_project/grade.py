def f(a: int) -> str:
    if a >= 90:
        return "A"
    if a >= 80:
        return "B"
    if a >= 70:
        return "C"
    if a >= 60:
        return "D"
    return "E"


def h(a: str) -> int:
    return int(a)


def g(a: int) -> bool:
    return 0 <= a <= 100
