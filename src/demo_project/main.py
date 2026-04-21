def f(a: int, b: int) -> float:
    c = a + b
    return c


def g() -> None:
    a = 11
    b = 22
    c = f(a, b)
    return c


if __name__ == "__main__":
    g()
