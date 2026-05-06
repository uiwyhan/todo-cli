from demo_project.models import s


def f(x: list[s], y: str):
    if not y:
        raise ValueError("there can be nothing")
    a = max((i.a for i in x), default=0) + 1
    b = s(a, y)
    x.append(b)
    return b


def g(x: list[s], y: int):
    for i in x:
        if i.a == y:
            i.c = True
            return i
    raise ValueError("there is no task")


def h(x: list[s], y: int):
    for i in x:
        if i.a == y:
            x.remove(i)
            return i
    raise ValueError("there is no task")
