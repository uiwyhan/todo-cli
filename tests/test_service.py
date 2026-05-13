from demo_project.models import s
from demo_project.service import average_score, top_student


def test_average_and_top_score() -> None:
    a = [s("wuyihan", 99), s("wuyiqian", 88)]
    b = sum(i.b for i in a)
    c = b / len(a)
    assert average_score(a) == c
    assert top_student(a) == a[0]


def test_none_score() -> None:
    a: list[s] = []
    b = average_score(a)
    c = top_student(a)
    assert b == 0.0
    assert c is None
