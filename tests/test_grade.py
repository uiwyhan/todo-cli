from demo_project.grade import get_grade


def test_score_grade() -> None:
    a = 90
    assert get_grade(a) == "A"
    b = 80
    assert get_grade(b) == "B"
    c = 70
    assert get_grade(c) == "C"
    d = 60
    assert get_grade(d) == "D"
    e = 11
    assert get_grade(e) == "E"
