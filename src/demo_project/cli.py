from demo_project.grade import f, g, h


def k() -> bool:
    a = input("please input your score:")
    if a == "q":
        print("it's over")
        return True
    try:
        b = h(a)
    except ValueError as e:
        print(e, "Invalid input. please enter a number.")
        return False
    if not g(b):
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
