def f(x: int, y: int) -> float:
    a = x + y
    return a


def g() -> None:
    a = 11
    b = 22
    c = f(a, b)
    print(c)


if __name__ == "__main__":
    g()
