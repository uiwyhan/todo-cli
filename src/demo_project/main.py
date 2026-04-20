def g(a: int, b: int) -> float:
    c = a + b
    return c


def f() -> None:
    a = 11
    b = 12
    c = g(11, 222)
    print(c)


if __name__ == "__main__":
    f()
