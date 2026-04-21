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


def g(a: str) -> int:
    return int(a)


def h(a: int) -> bool:
    return 0 <= a <= 100


def k() -> None:
    a = input("please input your score:")
    try:
        b = g(a)
    except ValueError as e:
        print(e)
        return
    if not h(b):
        print("Invalid value.Please input from 0 to 100.")
        return
    c = f(b)
    print(f"grade:{c},score:{b}")


if __name__ == "__main__":
    k()
