from demo_project.models import s


def average_score(x: list[s]) -> float:
    if not x:
        print("there is no scores")
        return 0.0
    else:
        a = sum([i.b for i in x])
        b = len([i for i in x])
        return a / b


def top_student(x: list[s]) -> s | None:
    if not x:
        print("there is no student")
        return None
    else:
        a = max(x, key=lambda a: a.b)
        return a


class StudentAlreadExistError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass
