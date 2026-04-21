from demo_project.main import f, g, h


def test1() -> None:
    assert f(90) == "A"


def test2() -> None:
    assert g("88") == 88


def test3() -> None:
    assert h(11) is True


def test4() -> None:
    assert h(-11) is False


def test5() -> None:
    assert h(150) is False
