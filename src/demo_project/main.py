def f(a) -> str:
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
    try:
        b = int(a)
    except ValueError as e:
        print(e)
        return
    c = f(b)
    print(f"score:{b},grade:{c}")


if __name__ == "__main__":
    g()
