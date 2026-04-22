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


def k() -> bool:
    a = input("please input your score:")
    if a == "q":
        print("it's over")
        return True
    try:
        b = g(a)
    except ValueError as e:
        print(e, "Invalid input.Please enter a numerber.")
        return False
    if not h(b):
        print("Invalid input. Please enter a number from 0 to 100.")
        return False
    c = f(b)
    print(f"score: {b}, grade: {c}")
    return False


def d() -> None:
    while True:
        a = k()
        if a:
            break


if __name__ == "__main__":
    d()
