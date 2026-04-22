from demo_project.grade import f, g


def test1() -> None:
    assert f(90) == "A"


def test2() -> None:
    assert g(-11) is False
