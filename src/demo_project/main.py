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


def g() -> None:
    a = input("please input your score:")
    b = int(a)
    c = f(b)
    print(c)


if __name__ == "__main__":
    g()
