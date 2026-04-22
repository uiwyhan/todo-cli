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
    b = int(a)
    return b


def h(a: int) -> bool:
    return 0 <= a <= 100


def k() -> None:
    while True:
        a = input("please input your score:")
        if a == "q":
            print("it's over")
            break
        try:
            b = g(a)
        except ValueError as e:
            print(e, "Invalid input. Please enter a number.")
            continue
        if not h(b):
            print("Invalid input. please enter a number from 0 to 100.")
            continue
        c = f(b)
        print(f"score: {b},grade: {c}")


if __name__ == "__main__":
    k()
