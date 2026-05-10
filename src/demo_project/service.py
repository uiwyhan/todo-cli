from demo_project.models import s


class TaskNotFoundError(Exception):
    pass


def g(x: list, y: int) -> classmethod:
    for i in x:
        if i.a == y:
            i.c = True
            return i
        raise TaskNotFoundError("the task-id is not found")


def h(x: list, y: int) -> classmethod:
    for i in x:
        if i.a == y:
            x.remove(i)
            return i
        raise TaskNotFoundError("the task is not found")


def f(x: list, y: str) -> classmethod:
    a: int = max((i.a for i in x), default=0) + 1
    b = s(a, y)
    x.append(b)
    return b
